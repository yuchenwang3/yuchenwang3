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

    def test_every_pr_is_preserved(self):
        block = contribution_section(self.prs)
        for p in self.prs:
            self.assertEqual(block.count(f'href="{p["url"]}"'), 1)
            self.assertIn(f'#{p["number"]} · {p["state"]}', block)

    def test_one_row_per_project(self):
        block = contribution_section(self.prs)
        self.assertEqual(block.count("<tr>"), len(PROJECTS))
        self.assertEqual(len(PROJECTS), len({p[0] for p in PROJECTS}))

    def test_local_images_exist(self):
        readme = render_readme(self.prs)
        for path in re.findall(r'(?:src|srcset)="(\./[^\"]+)"', readme):
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertNotIn('width="410"', readme)
        self.assertNotIn("<script", readme)

    def test_refresh_preserves_outside_block(self):
        readme = render_readme(self.prs)
        before, tail = readme.split("<!-- PR-PREVIEWS:START -->")
        _, after = tail.split("<!-- PR-PREVIEWS:END -->")
        updated = before + "<!-- PR-PREVIEWS:START -->" + contribution_section(self.prs) + "<!-- PR-PREVIEWS:END -->" + after
        self.assertEqual(updated, readme)


if __name__ == "__main__":
    unittest.main()
