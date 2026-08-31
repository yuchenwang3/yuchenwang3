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


def get_theme(dark: bool) -> dict[str, str | list[str]]:
    return (
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
        {"q": f"author:{username} type:pr is:public", "per_page": 100, "sort": "updated", "order": "desc"},
    )
    merged_requests = github_get(
        "/search/issues",
        token,
        {"q": f"author:{username} type:pr is:merged", "per_page": 1},
    )

    owned_repos = [repo for repo in repos if not repo["fork"]]
    external_prs = [
        item
        for item in pull_requests["items"]
        if item["repository_url"].split("/")[-2].lower() != username.lower()
    ]
    external_prs.sort(key=lambda item: item["updated_at"], reverse=True)
    upstream_counts: dict[str, dict[str, int | str]] = {}
    for item in external_prs:
        repo_name = "/".join(item["repository_url"].split("/")[-2:])
        repo_stats = upstream_counts.setdefault(
            repo_name,
            {"repo": repo_name, "total": 0, "merged": 0, "open": 0, "closed": 0, "last_updated": item["updated_at"]},
        )
        repo_stats["total"] += 1
        repo_stats["last_updated"] = max(str(repo_stats["last_updated"]), item["updated_at"])
        if item["pull_request"].get("merged_at"):
            repo_stats["merged"] += 1
        else:
            repo_stats[item["state"]] += 1

    upstream = sorted(
        upstream_counts.values(),
        key=lambda item: (
            int(item["total"]),
            int(item["merged"]) + int(item["open"]),
            int(item["merged"]),
            str(item["last_updated"]),
        ),
        reverse=True,
    )
    recent_prs = []
    for item in external_prs[:6]:
        status = "merged" if item["pull_request"].get("merged_at") else item["state"]
        recent_prs.append(
            {
                "repo": "/".join(item["repository_url"].split("/")[-2:]),
                "number": item["number"],
                "title": item["title"],
                "status": status,
            }
        )

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
        "upstream_repos": len(upstream),
        "followers": user["followers"],
        "languages": languages,
        "upstream": upstream,
        "recent_prs": recent_prs,
    }


def render_svg(data: dict, dark: bool) -> str:
    theme = get_theme(dark)

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


def render_upstream_svg(data: dict, dark: bool) -> str:
    theme = get_theme(dark)
    username = html.escape(data["username"])
    upstream = data["upstream"][:8]
    positions = [
        (24, 78),
        (324, 70),
        (624, 70),
        (924, 78),
        (924, 256),
        (624, 264),
        (324, 264),
        (24, 256),
    ]
    center_x, center_y = 600, 198
    connectors = []
    nodes = []
    for index, item in enumerate(upstream):
        x, y = positions[index]
        node_center_x, node_center_y = x + 126, y + 31
        connectors.append(
            f'<path d="M{center_x} {center_y} L{node_center_x} {node_center_y}" '
            f'stroke="{theme["border"]}" stroke-width="1.5" stroke-dasharray="4 7"/>'
        )
        repo_name = str(item["repo"])
        short_name = repo_name if len(repo_name) <= 30 else f"{repo_name[:27]}…"
        short_name = html.escape(short_name)
        summary = f'{item["total"]} PR · {item["merged"]} merged · {item["open"]} open'
        nodes.append(
            f'<g transform="translate({x} {y})">'
            f'<rect width="252" height="62" rx="5" fill="{theme["panel"]}" stroke="{theme["border"]}"/>'
            f'<circle cx="18" cy="19" r="4" fill="{theme["accent"]}"/>'
            f'<text class="repo" x="30" y="23">{short_name}</text>'
            f'<text class="repo-meta" x="18" y="46">{summary}</text>'
            "</g>"
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="350" viewBox="0 0 1200 350" role="img" aria-labelledby="title desc">
  <title id="title">Upstream contribution network for {username}</title>
  <desc id="desc">Repositories receiving public pull requests authored by {username}, sized and labeled by pull request activity.</desc>
  <style>
    text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; fill: {theme['text']}; }}
    .command {{ font-size: 15px; font-weight: 650; letter-spacing: .02em; }}
    .status {{ font-size: 12px; fill: {theme['muted']}; letter-spacing: .08em; }}
    .repo {{ font-size: 12px; font-weight: 700; }}
    .repo-meta {{ font-size: 10px; fill: {theme['muted']}; letter-spacing: .03em; }}
    .center {{ font-size: 18px; font-weight: 760; }}
    .center-meta {{ font-size: 11px; fill: {theme['muted']}; letter-spacing: .08em; }}
  </style>
  <rect x="0.5" y="0.5" width="1199" height="349" rx="8" fill="{theme['background']}" stroke="{theme['border']}"/>
  <rect x="1" y="1" width="1198" height="48" rx="7" fill="{theme['panel']}"/>
  <path d="M1 41h1198v8H1z" fill="{theme['panel']}"/>
  <circle cx="25" cy="25" r="5" fill="{theme['accent']}"/>
  <text class="command" x="42" y="31">github://{username} / upstream network</text>
  <text class="status" x="1172" y="30" text-anchor="end">TOP 8 · PUBLIC PR SURFACE</text>
  {''.join(connectors)}
  <g transform="translate(465 158)">
    <rect width="270" height="80" rx="6" fill="{theme['accent']}"/>
    <text class="center" x="135" y="34" text-anchor="middle" fill="{theme['background']}" style="fill:{theme['background']}">@{username}</text>
    <text class="center-meta" x="135" y="57" text-anchor="middle" fill="{theme['background']}" style="fill:{theme['background']};opacity:.78">{data['public_prs']} PRS · {data['upstream_repos']} UPSTREAM REPOS</text>
  </g>
  {''.join(nodes)}
</svg>
'''


def render_activity_svg(data: dict, dark: bool) -> str:
    theme = get_theme(dark)
    username = html.escape(data["username"])
    rows = []
    for index, item in enumerate(data["recent_prs"]):
        y = 66 + index * 50
        repo_name = html.escape(str(item["repo"]))
        pr_title = str(item["title"])
        if len(pr_title) > 68:
            pr_title = f"{pr_title[:65]}…"
        pr_title = html.escape(pr_title)
        status = str(item["status"]).upper()
        pill_fill = theme["accent"] if status == "OPEN" else theme["panel"]
        pill_text = theme["background"] if status == "OPEN" else theme["muted"]
        rows.append(
            f'<g transform="translate(0 {y})">'
            f'<line x1="28" y1="42" x2="1172" y2="42" stroke="{theme["border"]}"/>'
            f'<text class="repo" x="28" y="25">{repo_name}</text>'
            f'<text class="number" x="300" y="25">#{item["number"]}</text>'
            f'<text class="title" x="382" y="25">{pr_title}</text>'
            f'<rect x="1080" y="8" width="92" height="24" rx="12" fill="{pill_fill}" stroke="{theme["border"]}"/>'
            f'<text class="pill" x="1126" y="24" text-anchor="middle" style="fill:{pill_text}">{status}</text>'
            "</g>"
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="390" viewBox="0 0 1200 390" role="img" aria-labelledby="title desc">
  <title id="title">Recent upstream pull requests by {username}</title>
  <desc id="desc">The six most recently updated public upstream pull requests authored by {username}.</desc>
  <style>
    text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; fill: {theme['text']}; }}
    .command {{ font-size: 15px; font-weight: 650; letter-spacing: .02em; }}
    .status {{ font-size: 12px; fill: {theme['muted']}; letter-spacing: .08em; }}
    .repo {{ font-size: 12px; font-weight: 700; }}
    .number {{ font-size: 12px; fill: {theme['accent']}; font-weight: 700; }}
    .title {{ font-size: 12px; fill: {theme['muted']}; }}
    .pill {{ font-size: 10px; font-weight: 760; letter-spacing: .08em; }}
    .footer {{ font-size: 11px; fill: {theme['muted']}; letter-spacing: .07em; }}
  </style>
  <rect x="0.5" y="0.5" width="1199" height="389" rx="8" fill="{theme['background']}" stroke="{theme['border']}"/>
  <rect x="1" y="1" width="1198" height="48" rx="7" fill="{theme['panel']}"/>
  <path d="M1 41h1198v8H1z" fill="{theme['panel']}"/>
  <circle cx="25" cy="25" r="5" fill="{theme['accent']}"/>
  <text class="command" x="42" y="31">github://{username} / recent upstream dispatches</text>
  <text class="status" x="1172" y="30" text-anchor="end">LIVE PR LEDGER</text>
  {''.join(rows)}
  <text class="footer" x="28" y="372">VIEW FULL LEDGER → GITHUB.COM/PULLS?Q=AUTHOR:{username}</text>
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
    (args.output_dir / "github-upstream.svg").write_text(render_upstream_svg(data, dark=False), encoding="utf-8")
    (args.output_dir / "github-upstream-dark.svg").write_text(render_upstream_svg(data, dark=True), encoding="utf-8")
    (args.output_dir / "github-activity.svg").write_text(render_activity_svg(data, dark=False), encoding="utf-8")
    (args.output_dir / "github-activity-dark.svg").write_text(render_activity_svg(data, dark=True), encoding="utf-8")

    print(
        f"rendered telemetry: {data['owned_repos']} repos, {data['public_prs']} PRs, "
        f"{data['merged_prs']} merged, {data['upstream_repos']} upstream repos"
    )


if __name__ == "__main__":
    main()
