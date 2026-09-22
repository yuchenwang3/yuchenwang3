"""Small, self-hosted GitHub README widgets using public GitHub data."""
from collections import Counter
from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/widgets"
QUERY = '''query($cursor:String) { user(login:"yuchenwang3") {
  contributionsCollection { contributionCalendar { totalContributions weeks {
    contributionDays { date contributionCount }
  } } }
  repositories(first:100,after:$cursor,ownerAffiliations:OWNER,privacy:PUBLIC,isFork:false) {
    pageInfo { hasNextPage endCursor }
    nodes { primaryLanguage { name } }
  }
} }'''


def fetch_snapshot():
    repos, cursor = [], None
    for _ in range(20):
        cmd = ["gh", "api", "graphql", "-f", f"query={QUERY}"]
        if cursor:
            cmd += ["-f", f"cursor={cursor}"]
        result = json.loads(subprocess.check_output(cmd, text=True, timeout=45))
        if result.get("errors"):
            raise ValueError("GitHub returned GraphQL errors")
        user = result["data"]["user"]
        batch = user["repositories"]
        repos.extend(batch["nodes"])
        if not batch["pageInfo"]["hasNextPage"]:
            break
        cursor = batch["pageInfo"]["endCursor"]
    else:
        raise ValueError("Repository pagination exceeded limit")
    counts = Counter(r["primaryLanguage"]["name"] for r in repos if r["primaryLanguage"])
    return {
        "updated": datetime.now(timezone.utc).date().isoformat(),
        "calendar": user["contributionsCollection"]["contributionCalendar"],
        "languages": dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))),
        "public_nonfork_repositories": len(repos),
    }


def render_widget(data, kind, dark=False):
    bg, border, ink, muted = ("#0d1117", "#30363d", "#e6edf3", "#9da7b3") if dark else ("#ffffff", "#d8dee4", "#24292f", "#57606a")
    palette = ["#7cb7ff", "#5f8fce", "#91b0d8", "#b2c8e5", "#4d6d95"] if dark else ["#426dab", "#6589bc", "#8faad0", "#b2c5df", "#d4dfed"]
    title = "Contribution rhythm" if kind == "activity" else "Languages in my repos"
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="390" height="154" viewBox="0 0 390 154" role="img" aria-label="{title}">',
             f'<title>{title}</title><desc>GitHub data updated {data["updated"]}. Language counts are primary languages of public, non-fork repositories, not proficiency.</desc>',
             '<style>text{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif}.mono{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}</style>',
             f'<rect x=".5" y=".5" width="389" height="153" rx="8" fill="{bg}" stroke="{border}"/>']

    def text(x, y, value, size=12, color=ink, extra=""):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{escape(str(value))}</text>')

    text(18, 28, title, 14, extra='font-weight="600"')
    if kind == "activity":
        weeks = data["calendar"]["weeks"][-26:]
        totals = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in weeks]
        peak = max(totals, default=1) or 1
        for i, count in enumerate(totals):
            height = max(2, count / peak * 49)
            parts.append(f'<rect x="{18+i*13.6:.1f}" y="{94-height:.1f}" width="9" height="{height:.1f}" rx="2" fill="{palette[0] if count else border}"><title>{weeks[i]["contributionDays"][0]["date"]}: {count} contributions</title></rect>')
        text(18, 114, "26 weeks · GitHub contributions", 11, muted)
        text(18, 138, f'{data["calendar"]["totalContributions"]:,} in the past year', 12, extra='class="mono"')
    else:
        items = list(data["languages"].items())
        shown = items[:4]
        if len(items) > 4:
            shown.append(("Other", sum(n for _, n in items[4:])))
        total = sum(n for _, n in shown)
        x = 18
        for i, (name, count) in enumerate(shown):
            width = 354 * count / total if total else 0
            parts.append(f'<rect x="{x:.2f}" y="47" width="{width:.2f}" height="9" fill="{palette[i]}"><title>{escape(name)}: {count} repos</title></rect>')
            x += width
            col, row = i % 3, i // 3
            parts.append(f'<circle cx="{22+col*118}" cy="{78+row*23}" r="3" fill="{palette[i]}"/>')
            short = "Notebook" if name == "Jupyter Notebook" else name
            text(30+col*118, 82+row*23, f"{short} {count}", 11)
        text(18, 138, "Public non-forks · primary language", 11, muted)
    text(371, 28, data["updated"][5:], 10, muted, 'text-anchor="end" class="mono"')
    return "".join(parts) + "</svg>\n"


def main():
    data = fetch_snapshot()  # Fetch everything before replacing last-good assets.
    rendered = {(kind, dark): render_widget(data, kind, dark)
                for kind in ("activity", "languages") for dark in (False, True)}
    OUT.mkdir(exist_ok=True)
    for (kind, dark), svg in rendered.items():
        (OUT / f'{kind}-{"dark" if dark else "light"}.svg').write_text(svg)
    (OUT / "snapshot.json").write_text(json.dumps(data, indent=2) + "\n")
    print(f'Updated GitHub widgets: {data["updated"]}')


if __name__ == "__main__":
    main()
