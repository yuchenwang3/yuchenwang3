"""Regenerate checked-in vector research artwork; no network calls."""
from pathlib import Path
from profile_art import research

target = Path(__file__).resolve().parents[1] / "assets" / "research"
for name in ("occamy", "cineflow", "prefill"):
    for dark in (False, True):
        suffix = "dark" if dark else "light"
        (target / f"{name}-{suffix}.svg").write_text(research(name, dark))
        if name == "occamy":
            (target / f"occamy-compact-{suffix}.svg").write_text(research(name, dark, compact=True))
print("Rendered 8 research assets")
