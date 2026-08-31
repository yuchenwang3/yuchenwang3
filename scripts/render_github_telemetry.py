#!/usr/bin/env python3
"""Render a dependency-free GitHub profile telemetry card as light/dark SVGs."""

from __future__ import annotations

import argparse
import html
import json
import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_ROOT = "https://api.github.com"


def github_get(path: str, token: str, params: dict[str, str | int] | None = None) -> dict | list:
    query = f"?{urlencode(params)}" if params else ""
    request = Request(
        f"{API_ROOT}{path}{query}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "github-profile-telemetry",
        },
    )
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def collect_telemetry(username: str, token: str) -> dict:
    user = github_get(f"/users/{username}", token)
    repos = github_get(
        f"/users/{username}/repos",
        token,
        {"type": "owner", "sort": "updated", "per_page": 100},
    )
    pull_requests = github_get(
        "/search/issues",
        token,
        {"q": f"author:{username} type:pr is:public", "per_page": 100},
    )
    merged_requests = github_get(
        "/search/issues",
        token,
        {"q": f"author:{username} type:pr is:merged", "per_page": 1},
    )

    owned_repos = [repo for repo in repos if not repo["fork"]]
    upstream_repos = {
        "/".join(item["repository_url"].split("/")[-2:])
        for item in pull_requests["items"]
        if item["repository_url"].split("/")[-2].lower() != username.lower()
    }

    language_repos = [
        repo
        for repo in owned_repos
        if repo["name"].lower() != username.lower() and not repo["name"].lower().endswith(".github.io")
    ]
    language_bytes: dict[str, int] = {}
    for repo in language_repos:
        try:
            languages = github_get(f"/repos/{username}/{repo['name']}/languages", token)
        except Exception as error:  # Keep the scheduled card alive if one repo is unavailable.
            print(f"warning: skipped languages for {repo['name']}: {error}")
            continue
        for language, byte_count in languages.items():
            language_bytes[language] = language_bytes.get(language, 0) + byte_count

    total_language_bytes = sum(language_bytes.values()) or 1
    languages = [
        {"name": name, "bytes": byte_count, "share": byte_count / total_language_bytes}
        for name, byte_count in sorted(language_bytes.items(), key=lambda item: item[1], reverse=True)[:5]
    ]

    return {
        "username": username,
        "owned_repos": len(owned_repos),
        "public_prs": pull_requests["total_count"],
        "merged_prs": merged_requests["total_count"],
        "upstream_repos": len(upstream_repos),
        "followers": user["followers"],
        "languages": languages,
    }


def render_svg(data: dict, dark: bool) -> str:
    theme = (
        {
            "background": "#0d1117",
            "panel": "#161b22",
            "border": "#30363d",
            "text": "#f0f6fc",
            "muted": "#8b949e",
            "accent": "#ff7b72",
            "segments": ["#ff7b72", "#e05d55", "#c94c44", "#a93a34", "#6e2b28"],
        }
        if dark
        else {
            "background": "#ffffff",
            "panel": "#f6f8fa",
            "border": "#d0d7de",
            "text": "#1f2328",
            "muted": "#656d76",
            "accent": "#b42318",
            "segments": ["#b42318", "#cf4b40", "#df766d", "#eaa49e", "#f2cbc7"],
        }
    )

    metric_data = [
        (data["owned_repos"], "OWNED REPOS"),
        (data["public_prs"], "PUBLIC PRS"),
        (data["merged_prs"], "MERGED"),
        (data["upstream_repos"], "UPSTREAM REPOS"),
        (data["followers"], "FOLLOWERS"),
    ]
    metrics = []
    for index, (value, label) in enumerate(metric_data):
        x = 28 + index * 229
        metrics.append(
            f'<g transform="translate({x} 82)">'
            f'<text class="metric" y="30">{value}</text>'
            f'<text class="label" y="55">{label}</text>'
            "</g>"
        )

    bar_x, bar_y, bar_width, bar_height = 28, 190, 1144, 14
    language_segments = []
    language_labels = []
    cursor = bar_x
    label_x = 28
    for index, language in enumerate(data["languages"]):
        width = bar_width * language["share"]
        if index == len(data["languages"]) - 1:
            width = bar_x + bar_width - cursor
        color = theme["segments"][index]
        language_segments.append(
            f'<rect x="{cursor:.2f}" y="{bar_y}" width="{max(width, 2):.2f}" height="{bar_height}" fill="{color}"/>'
        )
        percentage = round(language["share"] * 100)
        name = html.escape(language["name"])
        language_labels.append(
            f'<circle cx="{label_x + 4}" cy="232" r="4" fill="{color}"/>'
            f'<text class="language" x="{label_x + 15}" y="236">{name} {percentage}%</text>'
        )
        label_x += 210
        cursor += width

    username = html.escape(data["username"])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260" viewBox="0 0 1200 260" role="img" aria-labelledby="title desc">
  <title id="title">GitHub telemetry for {username}</title>
  <desc id="desc">Live public repository, pull request, follower, and language statistics generated from the GitHub API.</desc>
  <style>
    text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; fill: {theme['text']}; }}
    .command {{ font-size: 15px; font-weight: 650; letter-spacing: .02em; }}
    .status {{ font-size: 12px; fill: {theme['muted']}; letter-spacing: .08em; }}
    .metric {{ font-size: 34px; font-weight: 760; letter-spacing: -.04em; }}
    .label {{ font-size: 11px; fill: {theme['muted']}; font-weight: 650; letter-spacing: .11em; }}
    .section {{ font-size: 11px; fill: {theme['muted']}; font-weight: 650; letter-spacing: .11em; }}
    .language {{ font-size: 12px; fill: {theme['muted']}; }}
  </style>
  <rect x="0.5" y="0.5" width="1199" height="259" rx="8" fill="{theme['background']}" stroke="{theme['border']}"/>
  <rect x="1" y="1" width="1198" height="48" rx="7" fill="{theme['panel']}"/>
  <path d="M1 41h1198v8H1z" fill="{theme['panel']}"/>
  <circle cx="25" cy="25" r="5" fill="{theme['accent']}"/>
  <text class="command" x="42" y="31">github://{username} / public telemetry</text>
  <text class="status" x="1172" y="30" text-anchor="end">AUTO-REFRESH · 24H</text>
  {''.join(metrics)}
  <line x1="28" y1="157" x2="1172" y2="157" stroke="{theme['border']}"/>
  <text class="section" x="28" y="180">PRIMARY LANGUAGES · PUBLIC CODE REPOSITORIES · BY BYTES</text>
  <rect x="{bar_x}" y="{bar_y}" width="{bar_width}" height="{bar_height}" fill="{theme['panel']}"/>
  {''.join(language_segments)}
  {''.join(language_labels)}
</svg>
'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required")

    data = collect_telemetry(args.username, token)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "github-telemetry.svg").write_text(render_svg(data, dark=False), encoding="utf-8")
    (args.output_dir / "github-telemetry-dark.svg").write_text(render_svg(data, dark=True), encoding="utf-8")

    print(
        f"rendered telemetry: {data['owned_repos']} repos, {data['public_prs']} PRs, "
        f"{data['merged_prs']} merged, {data['upstream_repos']} upstream repos"
    )


if __name__ == "__main__":
    main()
