"""Compact, GitHub-native profile sections (no custom CSS or script required)."""
from html import escape
from urllib.parse import quote

from profile_art import PR_DESIGN
from status_badges import status_link


def button(label, url, color="30363D"):
    styles = {
        "Website": ("181717", "vercel"), "CV": ("455A64", "readthedocs"),
        "Scholar": ("4285F4", "googlescholar"), "LinkedIn": ("0A66C2", "linkedin"),
        "Email": ("D14836", "gmail"), "Report": ("B31B1B", "arxiv"),
        "WeChat · eangyc": ("07C160", "wechat"),
        "Paper": ("B31B1B", "arxiv"), "Demo": ("087F5B", "vercel"),
        "Model": ("FFD21E", "huggingface"), "Code": ("181717", "github"),
        "Project": ("087F5B", "vercel"), "CUDA Attention": ("537C15", "nvidia"),
        "RL for Legal Reasoning": ("6554A4", "readthedocs"),
        "All contributions ↗": ("181717", "github"),
        "Engineering notes ↗": ("455A64", "readthedocs"),
    }
    style = "flat-square"
    extra = ""
    if label in styles:
        color, logo = styles[label]
        style = "for-the-badge"
        extra = f"&amp;logo={logo}&amp;logoColor={'black' if label == 'Model' else 'white'}"
    badge = f"https://img.shields.io/badge/{quote(label, safe='')}-{color}?style={style}{extra}"
    return f'<a href="{escape(url, quote=True)}"><img src="{badge}" alt="{escape(label)}"></a>'


def research_section():
    projects = [
        ("Occamy-1.0", "occamy-mark", "svg",
         "https://accio-lab.github.io/occamy/",
         "35B-A3B agent model for long-horizon tool use.",
         "Execution-grounded data · Agentic post-training",
         [("Report", "https://arxiv.org/abs/2609.11977"),
          ("Demo", "https://accio-lab.github.io/occamy/"),
          ("Model", "https://huggingface.co/Accio-Lab/Occamy-1.0"),
          ("Code", "https://github.com/Accio-Lab/occamy")]),
        ("CineFlow", "cineflow-system", "png",
         "https://yuchenwang3.github.io/projects/cineflow/",
         "Dependency-driven parallel video generation.",
         "1.7–5.5× end-to-end speedup in the reported evaluation",
         [("Project", "https://yuchenwang3.github.io/projects/cineflow/"),
          ("Paper", "https://yuchenwang3.github.io/assets/pdf/projects/cineflow-paper.pdf")]),
        ("Dynamic Prefill", "prefill-timeline", "png",
         "https://yuchenwang3.github.io/projects/prepack/",
         "Adaptive batching and prompt packing for LLM serving.",
         "Up to 20% lower TTFT on the reported traces",
         [("Report", "https://yuchenwang3.github.io/assets/pdf/projects/dynamic-prefill-online-packing-report.pdf"),
          ("Code", "https://github.com/Winlere/prepack-workspace")]),
    ]
    rows = []
    for name, stem, ext, url, summary, detail, links in projects:
        visual = f'<img width="100%" src="./assets/research/{stem}.{ext}" alt="{escape(name)}: '+("official logo" if ext == "svg" else "figure from the paper" if name == "CineFlow" else "figure from the project report")+'">'
        if ext == "svg":
            visual = f'<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/research/{stem}-dark.svg">{visual}</picture>'
        rows.append(f'''<tr>
<td width="32%" align="center"><a href="{url}">{visual}</a></td>
<td width="68%"><h3><a href="{url}">{name}</a></h3>
<p>{summary}<br><sub>{detail}</sub></p>
<p>{" ".join(button(label, target) for label, target in links)}</p></td>
</tr>''')
    return "## Research\n\n<table>\n" + "\n".join(rows) + "\n</table>\n\n" + " ".join([
        button("CUDA Attention", "https://yuchenwang3.github.io/assets/pdf/projects/gpt2-processing-unit-report.pdf"),
        button("RL for Legal Reasoning", "https://yuchenwang3.github.io/assets/pdf/projects/legal-reasoning-thesis.pdf"),
    ]) + "\n"


PROJECTS = [
    ("modelscope/ms-swift", "ms-swift", 109945100),
    ("flashinfer-ai/flashinfer", "FlashInfer", 145061914),
    ("vllm-project/vime", "vime", 136984999),
    ("NVIDIA-NeMo/Emerging-Optimizers", "Emerging Optimizers", 213689629),
    ("NVIDIA-NeMo/Gym", "NeMo Gym", 213689629),
    ("Dao-AILab/flash-attention", "FlashAttention", 139507659),
    ("vllm-project/vllm", "vLLM", 136984999),
    ("NVIDIA/Megatron-LM", "Megatron-LM", 1728152),
    ("NVIDIA-NeMo/RL", "NeMo RL", 213689629),
    ("sgl-project/sglang", "SGLang", 147780389),
    ("verl-project/verl", "verl", 212961691),
    ("NousResearch/hermes-agent", "Hermes Agent", 134168893),
    ("huggingface/trl", "TRL", 25720743),
]

PR_LABELS = {
    ("NVIDIA-NeMo/RL", 4193): "Render evaluation prompts as complete conversations",
    ("NVIDIA-NeMo/RL", 4176): "Unify worker selection through configuration",
    ("sgl-project/sglang", 40103): "Reject developer messages silently dropped by templates",
    ("verl-project/verl", 7906): "Track response truncation across context limits",
    ("huggingface/trl", 7294): "Fix async checkpoint resume after stale rollout drops",
    ("sgl-project/sglang", 39765): "Fix Mamba cache publication under overlap scheduling",
    ("NousResearch/hermes-agent", 113511): "Control partial-stream continuation for batch evaluation",
    ("NousResearch/hermes-agent", 113538): "Clarify API retry budgets and streaming defaults",
    ("modelscope/ms-swift", 9598): "Add order-preserving packing",
    ("modelscope/ms-swift", 9602): "Warm up NCCL before training",
    ("modelscope/ms-swift", 9599): "Pass through Muon Nesterov settings",
    ("modelscope/ms-swift", 9591): "Expose Muon coefficient selection",
    ("modelscope/ms-swift", 9600): "Align MoE router configuration types",
    ("vllm-project/vime", 337): "Forward recompute flags; fix hybrid models",
    ("vllm-project/vllm", 48284): "Skip layerwise reload for unquantized models",
    ("NVIDIA/Megatron-LM", 5400): "Route GDN input projections to Adam",
    ("NVIDIA/Megatron-LM", 5431): "Exclude GDN input projections from global clipping",
    ("NVIDIA/Megatron-LM", 5395): "Skip gradient clipping for Muon",
    ("NVIDIA-NeMo/RL", 2962): "Sanitize non-finite async log probabilities",
    ("NVIDIA-NeMo/RL", 2907): "Read environment names from multi-dataset configs",
    ("sgl-project/sglang", 38063): "Explain cold MXFP4 JIT startup",
    ("sgl-project/sglang", 31621): "Honor weight-check exclusions during reset",
    ("verl-project/verl", 7597): "Validate actor FSDP strategy",
    ("NVIDIA-NeMo/Gym", 1788): "Make rollout failures recoverable",
    ("NVIDIA-NeMo/Gym", 2726): "Preserve HTTP errors across process boundaries",
    ("Dao-AILab/flash-attention", 2507): "Stabilize backward JIT keys without CPU–GPU sync",
}


# Curated technical highlights, independent of merge state. The remainder stays
# visible below, and every PR is rendered exactly once across the two groups.
HIGHLIGHTS = [
    ("vllm-project/vllm", 54699),
    ("NVIDIA-NeMo/RL", 3943),
    ("NVIDIA/Megatron-LM", 5396),
    ("NVIDIA/Megatron-LM", 5463),
    ("Dao-AILab/flash-attention", 2507),
    ("flashinfer-ai/flashinfer", 4984),
    ("sgl-project/sglang", 39765),
    ("NousResearch/hermes-agent", 100693),
]


def contribution_table(prs, project_order):
    projects = {repo: (name, avatar) for repo, name, avatar in PROJECTS}
    rows = []
    for repo in project_order:
        name, avatar = projects[repo]
        contributions = []
        for p in prs:
            if p["repo"] != repo:
                continue
            key = (repo, p["number"])
            label = PR_LABELS.get(key)
            if label is None:
                label = " ".join(PR_DESIGN[key][4]) if key in PR_DESIGN else p["title"]
            status = status_link(p)
            credit = ""
            if p.get("role") == "coauthor":
                credit = "<br><sub>Co-author</sub>"
            elif p.get("role") == "adopted_solution":
                credit = f'<br><sub><a href="{escape(p["credit_url"], quote=True)}">Solution adopted by the PR author</a></sub>'
            contributions.append(f'<p>{status} {escape(label)}{credit}</p>')
        if not contributions:
            continue
        rows.append(f'''<tr>
<td width="28%" valign="top"><a href="https://github.com/{repo}"><img src="https://avatars.githubusercontent.com/u/{avatar}?s=64&amp;v=4" width="30" height="30" alt="{repo.split('/')[0]} organization avatar"><br><strong>{name}</strong></a></td>
<td width="72%">{"".join(contributions)}</td>
</tr>''')
    return "<table>\n" + "\n".join(rows) + "\n</table>" if rows else ""


def contribution_section(prs):
    # Retain the full snapshot for history/refresh, but only show active or
    # merged work on the profile. Closed-only projects disappear automatically.
    visible = [p for p in prs if p["state"] in ("merged", "open")]
    merged_count = sum(p["state"] == "merged" and p.get("role") != "adopted_solution" for p in visible)
    adopted_count = sum(p["state"] == "merged" and p.get("role") == "adopted_solution" for p in visible)
    open_count = sum(p["state"] == "open" for p in visible)
    project_count = len({p["repo"] for p in visible})
    adopted_summary = f'<strong>{adopted_count} adopted solution{("s" if adopted_count != 1 else "")}</strong> · ' if adopted_count else ""
    summary = (f'<p><strong>{merged_count} merged</strong> · ' + adopted_summary +
               f'<strong>{open_count} open</strong> · {project_count} projects</p>')
    by_key = {(p["repo"], p["number"]): p for p in visible}
    featured = [by_key[key] for key in HIGHLIGHTS if key in by_key]
    remainder = [p for p in visible if (p["repo"], p["number"]) not in HIGHLIGHTS]
    featured_order = list(dict.fromkeys(p["repo"] for p in featured))
    sections = []
    if featured:
        sections.append("### Highlights\n\n" + contribution_table(featured, featured_order))
    if remainder:
        sections.append("### More contributions\n\n" + contribution_table(
            sorted(remainder, key=lambda p: {"merged": 0, "open": 1}[p["state"]]),
            [repo for repo, _, _ in PROJECTS],
        ))
    footer = " ".join([
        button("All contributions ↗", "https://github.com/search?q=author%3Ayuchenwang3+is%3Apr&type=pullrequests"),
        button("Engineering notes ↗", "https://yuchenwang3.github.io/projects/open-source-systems/"),
    ])
    return "\n\n" + summary + "\n\n" + "\n\n".join(sections) + "\n\n" + footer + "\n\n"


def snake_section():
    base = "https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/output/"
    return f'''\n## Contribution trail

<picture>
<source media="(prefers-color-scheme: dark)" srcset="{base}github-snake-dark.svg">
<img width="100%" src="{base}github-snake.svg" alt="Snake animation of my GitHub contribution history">
</picture>
'''


def render_readme(prs):
    header = '''<a id="yuchen-ean-wang"></a>
<picture>
<source media="(prefers-color-scheme: dark)" srcset="./assets/signature-dark.svg">
<img width="430" src="./assets/signature-light.svg" alt="Yuchen (Ean) Wang — handwritten typing signature">
</picture>

Agentic post-training & ML systems.<br>
M.S. CS [@illinois](https://github.com/illinois) · Research intern [@Accio-Lab](https://github.com/Accio-Lab) / [@alibaba](https://github.com/alibaba).

'''
    links = [("Website", "https://yuchenwang3.github.io/"), ("CV", "https://yuchenwang3.github.io/CV.pdf"),
             ("Scholar", "https://scholar.google.com/citations?user=NharhG8AAAAJ"),
             ("LinkedIn", "https://www.linkedin.com/in/yuchen3"), ("Email", "mailto:yuchenwang0303@gmail.com"),
             ("WeChat · eangyc", "https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/main/assets/wechat-qr.jpg")]
    return header + '<p>\n' + "\n".join(button(*link) for link in links) + "\n</p>\n\n" + widget_section() + research_section() + "\n## Open-source contributions\n\n<!-- PR-PREVIEWS:START -->" + contribution_section(prs) + "<!-- PR-PREVIEWS:END -->\n" + snake_section()


def widget_section():
    badges = '''<p>
<a href="https://github.com/yuchenwang3?tab=followers"><img src="https://img.shields.io/github/followers/yuchenwang3?label=Follow&amp;style=social" alt="Follow on GitHub"></a>
<a href="https://github.com/yuchenwang3?tab=repositories&amp;sort=stargazers"><img src="https://img.shields.io/github/stars/yuchenwang3?label=Stars&amp;style=social" alt="Stars on my repositories"></a>
<a href="https://github.com/search?q=author%3Ayuchenwang3+is%3Apr+is%3Aopen&amp;type=pullrequests"><img src="https://img.shields.io/badge/PRs-in_flight-426dab?style=flat-square&amp;logo=git&amp;logoColor=white" alt="Explore my open pull requests"></a>
</p>
'''
    widgets = []
    for kind, label, target in [
        ("activity", "GitHub contribution rhythm over 26 weeks", "https://github.com/yuchenwang3?tab=overview"),
        ("languages", "Primary languages of my public non-fork repositories", "https://github.com/yuchenwang3?tab=repositories"),
    ]:
        widgets.append(f'''<a href="{target}"><picture>
<source media="(prefers-color-scheme: dark)" srcset="./assets/widgets/{kind}-dark.svg">
<img width="390" src="./assets/widgets/{kind}-light.svg" alt="{label}">
</picture></a>''')
    return badges + '\n<p>\n' + '\n'.join(widgets) + '\n</p>\n\n'
