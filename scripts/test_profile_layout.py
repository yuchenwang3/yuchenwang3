import json
from pathlib import Path
import re
import unittest

from profile_layout import contribution_section, render_readme, PROJECTS, HIGHLIGHTS

ROOT = Path(__file__).resolve().parents[1]


class ProfileLayoutTest(unittest.TestCase):
    def setUp(self):
        self.prs = json.loads((ROOT / "assets/prs/snapshot.json").read_text())["pull_requests"]

    def test_deterministic_readme(self):
        self.assertEqual((ROOT / "README.md").read_text(), render_readme(self.prs))

    def test_wechat_links_to_original_qr(self):
        readme = render_readme(self.prs)
        self.assertIn('alt="WeChat · eangyc"', readme)
        self.assertIn('href="https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/main/assets/wechat-qr.jpg"', readme)
        self.assertTrue((ROOT / "assets/wechat-qr.jpg").is_file())

    def test_every_active_or_merged_pr_is_preserved(self):
        block = contribution_section(self.prs)
        for p in self.prs:
            if p["state"] == "closed":
                self.assertNotIn(f'href="{p["url"]}"', block)
                continue
            self.assertEqual(block.count(f'href="{p["url"]}"'), 1)
            self.assertIn(f'#{p["number"]} · {p["state"]}', block)

    def test_one_row_per_project_in_each_group(self):
        block = contribution_section(self.prs)
        visible = [p for p in self.prs if p["state"] in ("open", "merged")]
        for heading, is_featured in [("Highlights", True), ("More contributions", False)]:
            group = block.split(f"### {heading}\n", 1)[1].split("</table>", 1)[0]
            projects = {p["repo"] for p in visible
                        if ((p["repo"], p["number"]) in HIGHLIGHTS) == is_featured}
            self.assertEqual(group.count("<tr>"), len(projects))
        self.assertEqual(len(PROJECTS), len({p[0] for p in PROJECTS}))

    def test_highlights_are_first_without_duplicates(self):
        block = contribution_section(self.prs)
        featured, remainder = block.split("### More contributions", 1)
        positions = []
        for repo, number in HIGHLIGHTS:
            url = f'https://github.com/{repo}/pull/{number}'
            positions.append(featured.index(f'href="{url}"'))
            self.assertNotIn(f'href="{url}"', remainder)
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(len(HIGHLIGHTS), len(set(HIGHLIGHTS)))

    def test_closed_highlight_is_not_displayed(self):
        pr = next(p for p in self.prs if (p['repo'], p['number']) == HIGHLIGHTS[0])
        block = contribution_section([dict(pr, state='closed')])
        self.assertNotIn('### Highlights', block)
        self.assertNotIn(pr['url'], block)

    def test_full_upstream_inventory(self):
        from refresh_pr_cards import SELECTED
        self.assertEqual(len(SELECTED), 34)
        self.assertEqual(len(PROJECTS), 13)
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
        self.assertIn('badge/Paper-B31B1B?style=for-the-badge', readme)
        self.assertIn('CineFlow: figure from the paper', readme)

    def test_status_badges_are_theme_aware_and_valid(self):
        import xml.etree.ElementTree as ET
        from status_badges import render_status, status_link
        for state in ('open', 'merged'):
            pr = dict(self.prs[0], state=state)
            self.assertIn('prefers-color-scheme: dark', status_link(pr))
            for dark in (False, True):
                svg = ET.fromstring(render_status(pr, dark))
                self.assertEqual(svg.attrib['height'], '26')
                self.assertIn(state, svg.attrib['aria-label'])
        with self.assertRaises(ValueError):
            render_status(dict(self.prs[0], state='closed'))

    def test_snake_uses_existing_daily_output(self):
        readme = render_readme(self.prs)
        self.assertIn('/output/github-snake.svg', readme)
        self.assertIn('/output/github-snake-dark.svg', readme)
        self.assertEqual(readme.count('## Contribution trail'), 1)

    def test_latest_contributions_are_tracked(self):
        keys = {(p["repo"], p["number"]) for p in self.prs}
        for key in [("NVIDIA-NeMo/RL", 4193), ("NVIDIA-NeMo/RL", 4176),
                    ("sgl-project/sglang", 40103), ("verl-project/verl", 7906),
                    ("huggingface/trl", 7294), ("sgl-project/sglang", 39765),
                    ("NousResearch/hermes-agent", 113511),
                    ("NousResearch/hermes-agent", 113538)]:
            self.assertIn(key, keys)

    def test_refresh_preserves_outside_block(self):
        readme = render_readme(self.prs)
        before, tail = readme.split("<!-- PR-PREVIEWS:START -->")
        _, after = tail.split("<!-- PR-PREVIEWS:END -->")
        updated = before + "<!-- PR-PREVIEWS:START -->" + contribution_section(self.prs) + "<!-- PR-PREVIEWS:END -->" + after
        self.assertEqual(updated, readme)

    def test_compact_header_and_clickable_widgets(self):
        readme = render_readme(self.prs)
        self.assertNotIn('editorial-header', readme)
        self.assertIn('Yuchen (Ean) Wang — handwritten typing signature', readme)
        self.assertIn('img.shields.io/github/followers/yuchenwang3', readme)
        self.assertIn('img.shields.io/github/stars/yuchenwang3', readme)
        for kind in ('activity', 'languages'):
            for theme in ('light', 'dark'):
                self.assertIn(f'./assets/widgets/{kind}-{theme}.svg', readme)

    def test_widgets_are_valid_and_honest_about_language_scope(self):
        import xml.etree.ElementTree as ET
        from profile_widgets import render_widget
        data = json.loads((ROOT / 'assets/widgets/snapshot.json').read_text())
        for kind in ('activity', 'languages'):
            for dark in (False, True):
                source = render_widget(data, kind, dark)
                svg = ET.fromstring(source)
                self.assertEqual(svg.attrib['height'], '154')
                self.assertNotIn('<script', source)
                self.assertIn('not proficiency', source)
        empty = dict(data, languages={}, calendar={'weeks': [], 'totalContributions': 0})
        ET.fromstring(render_widget(empty, 'languages'))
        ET.fromstring(render_widget(empty, 'activity'))

    def test_signature_and_affiliations(self):
        import xml.etree.ElementTree as ET
        from render_signature import signature_svg
        readme = render_readme(self.prs)
        for org in ('illinois', 'Accio-Lab', 'alibaba'):
            self.assertIn(f'[@{org}](https://github.com/{org})', readme)
        for dark in (False, True):
            svg = signature_svg(dark)
            self.assertEqual(ET.fromstring(svg).attrib['height'], '52')
            self.assertIn('prefers-reduced-motion', svg)
            self.assertIn('𝓨𝓾𝓬𝓱𝓮𝓷', svg)
            self.assertNotIn('<script', svg)


if __name__ == "__main__":
    unittest.main()
