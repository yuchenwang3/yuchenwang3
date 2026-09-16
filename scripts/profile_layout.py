"""Compact, GitHub-native profile sections (no custom CSS or script required)."""
from html import escape
from urllib.parse import quote

from profile_art import PR_DESIGN


def button(label, url, color="30363D"):
    badge = f"https://img.shields.io/badge/{quote(label, safe='')}-{color}?style=flat-square"
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
          ("Report", "https://yuchenwang3.github.io/assets/pdf/projects/cineflow-paper.pdf")]),
        ("Dynamic Prefill", "prefill-timeline", "png",
         "https://yuchenwang3.github.io/projects/prepack/",
         "Adaptive batching and prompt packing for LLM serving.",
         "Up to 20% lower TTFT on the reported traces",
         [("Report", "https://yuchenwang3.github.io/assets/pdf/projects/dynamic-prefill-online-packing-report.pdf"),
          ("Code", "https://github.com/Winlere/prepack-workspace")]),
    ]
    rows = []
    for name, stem, ext, url, summary, detail, links in projects:
        visual = f'<img width="100%" src="./assets/research/{stem}.{ext}" alt="{escape(name)}: '+("official logo" if ext == "svg" else "figure from the project report")+'">'
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
    ("flashinfer-ai/flashinfer", "FlashInfer", 145061914),
    ("vllm-project/vllm", "vLLM", 136984999),
    ("NVIDIA/Megatron-LM", "Megatron-LM", 1728152),
    ("NVIDIA-NeMo/RL", "NeMo RL", 213689629),
    ("NVIDIA-NeMo/Emerging-Optimizers", "Emerging Optimizers", 213689629),
    ("NousResearch/hermes-agent", "Hermes Agent", 134168893),
]


def contribution_section(prs):
    rows = []
    for repo, name, avatar in PROJECTS:
        contributions = []
        for p in prs:
            if p["repo"] != repo:
                continue
            design = PR_DESIGN[(repo, p["number"])]
            label = " ".join(design[4])
            # One status per PR: never imply an open proposal has merged.
            color = {"merged": "8250df", "open": "1a7f37", "closed": "656d76"}[p["state"]]
            status = button(f'#{p["number"]} · {p["state"]}', p["url"], color)
            contributions.append(f'<p>{escape(label)}<br>{status}</p>')
        if not contributions:
            continue
        rows.append(f'''<tr>
<td width="28%"><a href="https://github.com/{repo}"><img src="https://avatars.githubusercontent.com/u/{avatar}?s=64&amp;v=4" width="30" height="30" alt="{repo.split('/')[0]} organization avatar"><br><strong>{name}</strong></a></td>
<td width="72%">{"".join(contributions)}</td>
</tr>''')
    footer = " ".join([
        button("All contributions ↗", "https://github.com/search?q=author%3Ayuchenwang3+is%3Apr&type=pullrequests"),
        button("Engineering notes ↗", "https://yuchenwang3.github.io/projects/open-source-systems/"),
    ])
    return "\n\n<table>\n" + "\n".join(rows) + "\n</table>\n\n" + footer + "\n\n"


def render_readme(prs):
    header = '''<picture>
<source media="(prefers-color-scheme: dark)" srcset="./assets/editorial-header-dark.svg">
<img width="100%" src="./assets/editorial-header-light.svg" alt="Yuchen (Ean) Wang — agentic post-training and ML systems">
</picture>

Agentic post-training & ML systems. M.S. CS @ UIUC · Research intern @ Alibaba Accio · PKU Zhi Class.

'''
    links = [("Website", "https://yuchenwang3.github.io/"), ("CV", "https://yuchenwang3.github.io/CV.pdf"),
             ("Scholar", "https://scholar.google.com/citations?user=NharhG8AAAAJ"),
             ("LinkedIn", "https://www.linkedin.com/in/yuchen3"), ("Email", "mailto:yuchenwang0303@gmail.com")]
    return header + " ".join(button(*link) for link in links) + "\n\n" + research_section() + "\n## Open-source contributions\n\n<!-- PR-PREVIEWS:START -->" + contribution_section(prs) + "<!-- PR-PREVIEWS:END -->\n"
