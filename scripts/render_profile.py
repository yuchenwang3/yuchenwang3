"""Regenerate the layout from the last public PR snapshot; refresh separately."""
import json
from pathlib import Path
from profile_art import logo, svg
from profile_layout import render_readme

ROOT = Path(__file__).resolve().parents[1]
for dark in (False, True):
    mark = logo(100, 0, 400, "#edf0ee" if dark else "#142629", "#6ed6b6" if dark else "#137765")
    name = "occamy-mark-dark.svg" if dark else "occamy-mark.svg"
    (ROOT / "assets/research" / name).write_text(svg(600, 360, "Occamy", "Official Occamy logo geometry; colors adapted to the page theme.", mark))
snapshot = json.loads((ROOT / "assets/prs/snapshot.json").read_text())
(ROOT / "README.md").write_text(render_readme(snapshot["pull_requests"]))
