"""Refresh selected public PR metadata and GitHub-compatible SVG previews."""
import concurrent.futures
import datetime
import html
import json
import pathlib
import subprocess
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[1]
SELECTED = [
    ("flashinfer-ai/flashinfer", 4984),
    ("vllm-project/vllm", 54699),
    ("NVIDIA-NeMo/RL", 3943),
    ("NousResearch/hermes-agent", 100693),
    ("NVIDIA-NeMo/Emerging-Optimizers", 230),
    ("NVIDIA/Megatron-LM", 5396),
    ("NVIDIA/Megatron-LM", 5463),
    ("NousResearch/hermes-agent", 102549),
]


def fetch(item):
    repo, number = item
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}/pulls/{number}"],
        capture_output=True, text=True, check=True, timeout=45,
    )
    p = json.loads(result.stdout)
    return dict(repo=repo, number=number, title=p["title"], url=p["html_url"],
                additions=p["additions"], deletions=p["deletions"], files=p["changed_files"],
                updated=p["updated_at"], head=p["head"]["sha"],
                state="merged" if p["merged_at"] else p["state"])


def render(p, dark):
    bg, ink, muted, line, blue = (
        ("#141a27", "#edf1ff", "#a6b1cb", "#303b52", "#a5b5ff") if dark else
        ("#f8faff", "#172442", "#536482", "#d5def0", "#384cc0")
    )
    esc = html.escape
    title = textwrap.wrap(p["title"], width=48)[:3]
    lines = "".join(f'<text x="28" y="{104+i*28}" font-size="20" font-weight="600">{esc(t)}</text>' for i,t in enumerate(title))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="250" viewBox="0 0 600 250" role="img" aria-label="{esc(p['repo'])} PR {p['number']}">
<rect x="1" y="1" width="598" height="248" rx="14" fill="{bg}" stroke="{line}"/>
<path d="M28 54h12m-6-6v12m12-16v20" stroke="{blue}" stroke-width="2"/>
<g fill="{ink}" font-family="Segoe UI,Arial,sans-serif">
<text x="62" y="58" fill="{blue}" font-size="20" font-weight="700">{esc(p['repo'])}</text>
{lines}
<path d="M28 190H572" stroke="{line}"/>
<text x="28" y="222" fill="{muted}" font-size="16">PR #{p['number']} · {p['files']} files</text>
<text x="340" y="222" fill="{blue}" font-size="17" font-weight="600">+{p['additions']} / −{p['deletions']}</text>
<text x="545" y="58" fill="{muted}" font-size="20">↗</text>
</g></svg>'''


def main():
    # Fail before touching the last good snapshot if any request fails.
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        prs = list(pool.map(fetch, SELECTED))
    target = ROOT / "assets" / "prs"
    target.mkdir(parents=True, exist_ok=True)
    snapshot = dict(updated=datetime.date.today().isoformat(), pull_requests=prs)
    (target / "snapshot.json").write_text(json.dumps(snapshot, indent=2)+"\n")
    for p in prs:
        slug = p['repo'].replace('/', '-') + '-' + str(p['number'])
        for dark in (False, True):
            (target / f"{slug}-{'dark' if dark else 'light'}.svg").write_text(render(p,dark)+"\n")
    cards = []
    for p in prs:
        slug = p['repo'].replace('/', '-') + '-' + str(p['number'])
        cards.append(f'''<a href="{p['url']}"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/prs/{slug}-dark.svg">
  <img width="49%" src="./assets/prs/{slug}-light.svg" alt="{html.escape(p['repo'])} #{p['number']}: {html.escape(p['title'])}">
</picture></a>''')
    readme = ROOT / 'README.md'
    before, tail = readme.read_text().split('<!-- PR-PREVIEWS:START -->', 1)
    _, after = tail.split('<!-- PR-PREVIEWS:END -->', 1)
    block = '\n\n' + '\n'.join(cards) + '\n\n[All upstream contributions](https://github.com/search?q=author%3Ayuchenwang3+is%3Apr&type=pullrequests) · Previews refresh daily.\n\n'
    readme.write_text(before + '<!-- PR-PREVIEWS:START -->' + block + '<!-- PR-PREVIEWS:END -->' + after)
    print(f"Updated {len(prs)} public PR previews")


if __name__ == '__main__':
    main()
