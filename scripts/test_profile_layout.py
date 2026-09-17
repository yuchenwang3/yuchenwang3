import json
from pathlib import Path
import re
import unittest

from profile_layout import contribution_section, render_readme, PROJECTS

ROOT = Path(__file__).resolve().parents[1]


class ProfileLayoutTest(unittest.TestCase):
    def setUp(self):
        self.prs = json.loads((ROOT / "assets/prs/snapshot.json").read_text())["pull_requests"]

    def test_deterministic_readme(self):
        self.assertEqual((ROOT / "README.md").read_text(), render_readme(self.prs))

    def test_every_active_or_merged_pr_is_preserved(self):
        block = contribution_section(self.prs)
        for p in self.prs:
            if p["state"] == "closed":
                self.assertNotIn(f'href="{p["url"]}"', block)
                continue
            self.assertEqual(block.count(f'href="{p["url"]}"'), 1)
            self.assertIn(f'#{p["number"]} · {p["state"]}', block)

    def test_one_row_per_project(self):
        block = contribution_section(self.prs)
        visible_projects = {p["repo"] for p in self.prs if p["state"] in ("open", "merged")}
        self.assertEqual(block.count("<tr>"), len(visible_projects))
        self.assertEqual(len(PROJECTS), len({p[0] for p in PROJECTS}))

    def test_full_upstream_inventory(self):
        from refresh_pr_cards import SELECTED
        self.assertEqual(len(SELECTED), 29)
        self.assertEqual(len(PROJECTS), 12)
        self.assertEqual(set(SELECTED), {(p["repo"], p["number"]) for p in self.prs})
        self.assertEqual(len(SELECTED), len(set(SELECTED)))
        block = contribution_section(self.prs)
        self.assertNotIn("Closed without merge", block)
        self.assertNotIn("<details>", block)

    def test_status_transitions_update_visibility_and_counts(self):
        pr = dict(self.prs[0])
        pr["state"] = "open"
        self.assertIn("<strong>1 open</strong> · 1 projects", contribution_section([pr]))
        pr["state"] = "merged"
        self.assertIn("<strong>1 merged</strong>", contribution_section([pr]))
        pr["state"] = "closed"
        block = contribution_section([pr])
        self.assertNotIn("<tr>", block)
        self.assertNotIn(pr["url"], block)

    def test_counts_match_visible_inventory(self):
        block = contribution_section(self.prs)
        for state in ("open", "merged"):
            count = sum(p["state"] == state and (state != "merged" or p.get("role") != "adopted_solution") for p in self.prs)
            self.assertIn(f"<strong>{count} {state}</strong>", block)

    def test_attribution_is_explicit(self):
        block = contribution_section(self.prs)
        self.assertIn("<sub>Co-author</sub>", block)
        self.assertIn("Solution adopted by the PR author", block)
        self.assertIn("#issuecomment-4921776396", block)
        self.assertIn("<strong>1 adopted solution</strong>", block)
        prs = {(p["repo"], p["number"]): p for p in self.prs}
        self.assertEqual(prs[("NVIDIA-NeMo/Gym", 2726)]["role"], "coauthor")
        self.assertEqual(prs[("Dao-AILab/flash-attention", 2507)]["role"], "adopted_solution")

    def test_local_images_exist(self):
        readme = render_readme(self.prs)
        for path in re.findall(r'(?:src|srcset)="(\./[^\"]+)"', readme):
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertNotIn('width="410"', readme)
        self.assertNotIn("<script", readme)

    def test_cineflow_is_a_paper(self):
        readme = render_readme(self.prs)
        self.assertIn('badge/Paper-30363D', readme)
        self.assertIn('CineFlow: figure from the paper', readme)

    def test_latest_contributions_are_tracked(self):
        keys = {(p["repo"], p["number"]) for p in self.prs}
        for key in [("sgl-project/sglang", 39765),
                    ("NousResearch/hermes-agent", 113511),
                    ("NousResearch/hermes-agent", 113538)]:
            self.assertIn(key, keys)

    def test_refresh_preserves_outside_block(self):
        readme = render_readme(self.prs)
        before, tail = readme.split("<!-- PR-PREVIEWS:START -->")
        _, after = tail.split("<!-- PR-PREVIEWS:END -->")
        updated = before + "<!-- PR-PREVIEWS:START -->" + contribution_section(self.prs) + "<!-- PR-PREVIEWS:END -->" + after
        self.assertEqual(updated, readme)


if __name__ == "__main__":
    unittest.main()
