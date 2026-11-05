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
        full_list = block.split('<details>', 1)[1]
        for p in self.prs:
            if p["state"] == "closed":
                self.assertNotIn(f'href="{p["url"]}"', block)
                continue
            self.assertEqual(full_list.count(f'href="{p["url"]}"'), 1)
            self.assertIn(f'#{p["number"]} · {p["state"]}', full_list)

    def test_one_row_per_project_in_full_list(self):
        block = contribution_section(self.prs)
        visible = [p for p in self.prs if p["state"] in ("open", "merged")]
        self.assertEqual(block.count("<tr>"), len({p["repo"] for p in visible}))
        self.assertEqual(len(PROJECTS), len({p[0] for p in PROJECTS}))

    def test_highlights_precede_and_remain_in_full_list(self):
        block = contribution_section(self.prs)
        featured, full_list = block.split("<details>", 1)
        positions = []
        visible = {(p["repo"], p["number"]) for p in self.prs if p["state"] in ("open", "merged")}
        for repo, number in HIGHLIGHTS:
            if (repo, number) not in visible:
                continue
            url = f'https://github.com/{repo}/pull/{number}'
            positions.append(featured.index(f'href="{url}"'))
            self.assertEqual(full_list.count(f'href="{url}"'), 1)
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(len(HIGHLIGHTS), 3)
        self.assertEqual(featured.count('<li>'), len(positions))
        self.assertEqual(len(HIGHLIGHTS), len(set(HIGHLIGHTS)))

    def test_closed_highlight_is_not_displayed(self):
        pr = next(p for p in self.prs if (p['repo'], p['number']) == HIGHLIGHTS[0])
        block = contribution_section([dict(pr, state='closed')])
        self.assertNotIn('<li>', block.split('<details>', 1)[0])
        self.assertNotIn(pr['url'], block)

    def test_full_upstream_inventory(self):
        from refresh_pr_cards import SELECTED
        self.assertEqual(len(SELECTED), 44)
        self.assertEqual(len(PROJECTS), 17)
        self.assertEqual(set(SELECTED), {(p["repo"], p["number"]) for p in self.prs})
        self.assertEqual(len(SELECTED), len(set(SELECTED)))
        block = contribution_section(self.prs)
        self.assertNotIn("Closed without merge", block)
        self.assertIn("<details>", block)

    def test_full_list_is_one_collapsed_group(self):
        block = contribution_section(self.prs)
        self.assertEqual(block.count('<details>'), 1)
        self.assertEqual(block.count('</details>'), 1)
        self.assertNotIn('<details open', block)
        full_list = block.split('<details>', 1)[1]
        self.assertIn('<summary>Full PR list', full_list)
        repos = {p['repo'] for p in self.prs if p['state'] in ('merged', 'open')}
        self.assertEqual(full_list.count('<tr>'), len(repos))

    def test_highlight_metrics_keep_benchmark_scope(self):
        block = contribution_section(self.prs)
        self.assertIn('7.88 → 3.94 GiB in the exact-shape TP2 benchmark', block)
        self.assertIn('4.4–5.3× faster transfers in a controlled Ray benchmark', block)
        self.assertNotIn('faster training', block)

    def test_research_and_contributions_precede_widgets(self):
        readme = render_readme(self.prs)
        sections = ['### [Occamy-1.0]', '### Selected contributions', '### Other research', '<summary>Activity</summary>', '#### Contribution trail']
        positions = [readme.index(section) for section in sections]
        self.assertEqual(positions, sorted(positions))

    def test_contact_assets_have_equal_size_and_theme_support(self):
        import xml.etree.ElementTree as ET
        from render_contacts import CONTACTS, contact_svg, contact_button
        self.assertEqual(len(CONTACTS), 5)
        for key in CONTACTS:
            self.assertIn('prefers-color-scheme: dark', contact_button(key))
            for dark in (False, True):
                source = contact_svg(key, dark)
                svg = ET.fromstring(source)
                self.assertEqual((svg.attrib['width'], svg.attrib['height']), ('104', '30'))
                path = ROOT / f'assets/contacts/{key}-{"dark" if dark else "light"}.svg'
                self.assertEqual(path.read_text(), source)
                self.assertNotIn('<script', source)

    def test_visible_contact_buttons_keep_compact_brand_styles(self):
        from profile_layout import button
        from render_contacts import CONTACTS
        readme = render_readme(self.prs)
        for label, url in CONTACTS.values():
            self.assertIn(button(label, url), readme)
        self.assertIn('badge/Email-D14836?style=flat-square', readme)
        self.assertIn('badge/LinkedIn-0A66C2?style=flat-square', readme)
        self.assertIn('badge/WeChat%20%C2%B7%20eangyc-07C160?style=flat-square', readme)
        self.assertNotIn('./assets/contacts/', readme)

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

    def test_only_selected_prs_are_expanded(self):
        block = contribution_section(self.prs)
        featured, full_list = block.split("<details>", 1)
        visible = {(p["repo"], p["number"]) for p in self.prs if p["state"] in ("open", "merged")}
        for p in self.prs:
            url = f'href="{p["url"]}"'
            if (p["repo"], p["number"]) in HIGHLIGHTS and (p["repo"], p["number"]) in visible:
                self.assertEqual(featured.count(url), 1)
                self.assertIn(f'<code>{p["state"]}</code>', featured)
            else:
                self.assertNotIn(url, featured)
        self.assertNotIn('<table>', featured)
        self.assertIn('<table>', full_list)

    def test_profile_does_not_claim_visitor_identity_or_inflated_views(self):
        readme = render_readme(self.prs)
        self.assertNotIn("komarev.com", readme)
        self.assertNotIn("Profile views", readme)

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
        self.assertNotIn('https://yuchenwang3.github.io/projects/cineflow/', readme)
        self.assertNotIn('https://yuchenwang3.github.io/assets/pdf/projects/cineflow-paper.pdf', readme)
        self.assertIn('**CineFlow**', readme)
        self.assertIn('Co-first author · 1.7–5.5× end-to-end speedup in the reported evaluation', readme)

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
        self.assertEqual(readme.count('#### Contribution trail'), 1)
        activity = readme.split('<summary>Activity</summary>', 1)[1]
        self.assertIn('/output/github-snake.svg', activity)
        self.assertTrue(activity.rstrip().endswith('</details>'))

    def test_latest_contributions_are_tracked(self):
        keys = {(p["repo"], p["number"]) for p in self.prs}
        for key in [("NVIDIA-NeMo/RL", 4193), ("NVIDIA-NeMo/RL", 4176),
                    ("huggingface/datasets", 8670), ("modelscope/mcore-bridge", 211),
                    ("NVIDIA-NeMo/Megatron-Bridge", 6315), ("NVIDIA/Megatron-LM", 7864),
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
        self.assertNotIn('./assets/terminal-', readme)
        self.assertIn('## `>` Yuchen (Ean) Wang', readme)
        activity = readme.split('<summary>Activity</summary>', 1)[1]
        self.assertIn('img.shields.io/github/followers/yuchenwang3', readme)
        self.assertIn('img.shields.io/github/stars/yuchenwang3', readme)
        for kind in ('activity', 'languages'):
            for theme in ('light', 'dark'):
                self.assertIn(f'./assets/widgets/{kind}-{theme}.svg', activity)

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

    def test_occamy_scope_and_affiliations(self):
        from profile_layout import QUANTIZED_DOWNLOADS
        readme = render_readme(self.prs)
        for org in ('illinois', 'Accio-Lab', 'alibaba'):
            self.assertIn(f'[@{org}](https://github.com/{org})', readme)
        self.assertIn('**Core contributor** — post-training algorithms, infrastructure & data', readme)
        self.assertIn('≈1.2M cumulative downloads', readme)
        self.assertIn('across official quantized releases', readme)
        self.assertIn(f'{sum(QUANTIZED_DOWNLOADS.values()):,} all-time downloads across 12 official quantized repositories', readme)


if __name__ == "__main__":
    unittest.main()
