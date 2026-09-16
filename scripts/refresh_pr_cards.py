"""Refresh selected public PR metadata and GitHub-compatible SVG previews."""
import concurrent.futures
import datetime
import json
import pathlib
import subprocess
from profile_art import render_pr, PR_DESIGN
from profile_layout import contribution_section

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
    ("modelscope/ms-swift", 9598),
    ("modelscope/ms-swift", 9602),
    ("modelscope/ms-swift", 9599),
    ("modelscope/ms-swift", 9591),
    ("modelscope/ms-swift", 9600),
    ("vllm-project/vime", 337),
    ("vllm-project/vllm", 48284),
    ("NVIDIA/Megatron-LM", 5400),
    ("NVIDIA/Megatron-LM", 5431),
    ("NVIDIA/Megatron-LM", 5395),
    ("NVIDIA-NeMo/RL", 2962),
    ("NVIDIA-NeMo/RL", 2907),
    ("sgl-project/sglang", 38063),
    ("sgl-project/sglang", 31621),
    ("verl-project/verl", 7597),
    ("NVIDIA-NeMo/Gym", 1788),
]


def fetch(item):
    repo, number = item
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}/pulls/{number}"],
        capture_output=True, text=True, check=True, timeout=45,
    )
    p = json.loads(result.stdout)
    if p["user"]["login"] != "yuchenwang3" or p["base"]["repo"]["private"]:
        raise ValueError(f"Not a public contribution by yuchenwang3: {repo}#{number}")
    return dict(repo=repo, number=number, title=p["title"], url=p["html_url"],
                additions=p["additions"], deletions=p["deletions"], files=p["changed_files"],
                updated=p["updated_at"], head=p["head"]["sha"],
                state="merged" if p["merged_at"] else p["state"])


def render(p, dark):
    return render_pr(p, dark).rstrip("\n")


def main():
    # Fail before touching the last good snapshot if any request fails.
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        prs = list(pool.map(fetch, SELECTED))
    target = ROOT / "assets" / "prs"
    target.mkdir(parents=True, exist_ok=True)
    snapshot = dict(updated=datetime.date.today().isoformat(), pull_requests=prs)
    (target / "snapshot.json").write_text(json.dumps(snapshot, indent=2)+"\n")
    for p in prs:
        if (p["repo"], p["number"]) not in PR_DESIGN:
            continue
        slug = p['repo'].replace('/', '-') + '-' + str(p['number'])
        for dark in (False, True):
            (target / f"{slug}-{'dark' if dark else 'light'}.svg").write_text(render(p,dark)+"\n")
    readme = ROOT / 'README.md'
    before, tail = readme.read_text().split('<!-- PR-PREVIEWS:START -->', 1)
    _, after = tail.split('<!-- PR-PREVIEWS:END -->', 1)
    block = contribution_section(prs)
    readme.write_text(before + '<!-- PR-PREVIEWS:START -->' + block + '<!-- PR-PREVIEWS:END -->' + after)
    print(f"Updated {len(prs)} public PR previews")


if __name__ == '__main__':
    main()
