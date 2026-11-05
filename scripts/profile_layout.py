"""Compact, GitHub-native profile sections (no custom CSS or script required)."""
from html import escape
from urllib.parse import quote

from profile_art import PR_DESIGN
from render_contacts import CONTACTS
from status_badges import status_link

# Hugging Face downloadsAllTime for all 12 official quantized Occamy repos.
# Source: /api/models?author=Accio-Lab&expand[]=downloadsAllTime (2026-11-05).
QUANTIZED_DOWNLOADS = {
    "GGUF": 1176549, "APEX-GGUF": 5118, "FP8": 688, "NVFP4": 4770,
    "MLX-3bit": 833, "MLX-4bit": 1089, "MLX-5bit": 294,
    "MLX-6bit": 511, "MLX-8bit": 157, "MLX-mxfp4": 327,
    "MLX-mxfp8": 73, "MLX-nvfp4": 355,
}


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
        style = "flat-square"
        extra = f"&amp;logo={logo}&amp;logoColor={'black' if label == 'Model' else 'white'}"
    badge = f"https://img.shields.io/badge/{quote(label, safe='')}-{color}?style={style}{extra}"
    return f'<a href="{escape(url, quote=True)}"><img src="{badge}" alt="{escape(label)}"></a>'


def occamy_section():
    return f'''### [Occamy-1.0](https://accio-lab.github.io/occamy/)

35B-A3B agent model for long-horizon tool use. **Core contributor** — post-training algorithms, infrastructure & data.<br>
<a href="https://huggingface.co/collections/Accio-Lab/occamy-10" title="{sum(QUANTIZED_DOWNLOADS.values()):,} all-time downloads across 12 official quantized repositories"><strong>≈1.2M cumulative downloads</strong></a> across official quantized releases.

[Report](https://arxiv.org/abs/2609.11977) · [Demo](https://accio-lab.github.io/occamy/) · [Model](https://huggingface.co/Accio-Lab/Occamy-1.0) · [Code](https://github.com/Accio-Lab/occamy)
'''


def research_section():
    return '''<a id="research"></a>

### Other research

- **CineFlow** — Dependency-driven parallel video generation. Co-first author · 1.7–5.5× end-to-end speedup in the reported evaluation.
- **[Dynamic Prefill](https://yuchenwang3.github.io/projects/prepack/)** — Adaptive batching and prompt packing; up to 20% lower TTFT on the reported traces. [Report](https://yuchenwang3.github.io/assets/pdf/projects/dynamic-prefill-online-packing-report.pdf) · [Code](https://github.com/Winlere/prepack-workspace)
- **[RareDx](https://arxiv.org/abs/2609.35549)** — Graph-grounded RL for rare disease diagnosis. Co-first author.
- [CUDA Attention](https://yuchenwang3.github.io/assets/pdf/projects/gpt2-processing-unit-report.pdf) · [RL for Legal Reasoning](https://yuchenwang3.github.io/assets/pdf/projects/legal-reasoning-thesis.pdf)
'''


PROJECTS = [
    ("huggingface/datasets", "HF Datasets", 25720743),
    ("modelscope/mcore-bridge", "mcore-bridge", 109945100),
    ("NVIDIA-NeMo/Megatron-Bridge", "Megatron Bridge", 213689629),
    ("THUDM/slime", "slime", 48590610),
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
    ("huggingface/datasets", 8670): "Preserve source shards during streaming shuffle so four workers can share 19 shards",
    ("modelscope/mcore-bridge", 211): "Score packed QSA within each document; 2.70× faster in an 8K synthetic selector benchmark",
    ("modelscope/mcore-bridge", 212): "Preserve low-precision rounding in gated residual mixing",
    ("modelscope/mcore-bridge", 213): "Bound PLE backward's extra workspace through chunked token reductions",
    ("NVIDIA-NeMo/Megatron-Bridge", 6315): "Add Bridge-local Qwen4-Exp text-decoder support; GPU integration is pending",
    ("NVIDIA-NeMo/Megatron-Bridge", 6312): "Make HF/Megatron comparison failures return a nonzero exit status",
    ("NVIDIA/Megatron-LM", 7864): "Preserve native Adam step counters across checkpoint restoration",
    ("NVIDIA/Megatron-LM", 7881): "Reuse packed chunkwise CP metadata across GDN and KDA layers",
    ("vllm-project/vllm", 58219): "Clarify Qwen3 parser boundary tokens in custom grammars",
    ("THUDM/slime", 2412): "Score fan-out rollout samples as a flat group",
    ("vllm-project/vllm", 54699): "Remove full-weight copies during MoE loading; conversion peak 7.88 → 3.94 GiB in the exact-shape TP2 benchmark",
    ("NVIDIA-NeMo/RL", 3943): "Bypass driver tensor materialization in distillation; 4.4–5.3× faster transfers in a controlled Ray benchmark",
    ("NVIDIA/Megatron-LM", 5396): "Fuse GDN Q/K normalization to remove an extra backward activation buffer",
    ("NVIDIA/Megatron-LM", 5463): "Enable selective Mamba mixer recompute to save activation memory without full-layer recomputation",
    ("flashinfer-ai/flashinfer", 4984): "Restore K/V calibration in FP8 KV prefill, correcting silently mis-scaled attention outputs",
    ("NousResearch/hermes-agent", 100693): "Resolve local schema references so nested tool arguments reach handlers as objects, not JSON strings",
    ("NVIDIA-NeMo/RL", 4193): "Render evaluation prompts as complete conversations",
    ("NVIDIA-NeMo/RL", 4176): "Unify worker selection through configuration",
    ("sgl-project/sglang", 40103): "Reject developer messages silently dropped by templates",
    ("verl-project/verl", 7906): "Track response truncation across context limits",
    ("huggingface/trl", 7294): "Fix async checkpoint resume after stale rollout drops",
    ("sgl-project/sglang", 39765): "Publish Mamba cache updates before dependent batches capture stale KV mappings",
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
    ("Dao-AILab/flash-attention", 2507): "Prevent redundant backward-kernel recompilation with stable cache keys, without CPU–GPU sync",
}


# A short front-page selection; each also appears in the complete disclosure.
HIGHLIGHTS = [
    ("vllm-project/vllm", 54699),
    ("modelscope/mcore-bridge", 211),
    ("huggingface/datasets", 8670),
]


def contribution_table(prs, project_order):
    projects = {repo: (name, avatar) for repo, name, avatar in PROJECTS}
    rows = []
    for repo in project_order:
        name, avatar = projects[repo]
        contributions = []
        def contribution_line(p):
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
            return f'<p>{status} {escape(label)}{credit}</p>'
        contributions.extend(contribution_line(p) for p in prs if p["repo"] == repo)
        if not contributions:
            continue
        rows.append(f'''<tr>
<td width="28%" valign="top"><a href="https://github.com/{repo}"><strong>{name}</strong></a><br><sub><code>{repo.split('/')[0]}</code></sub></td>
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
    summary = (f'<strong>{merged_count} merged</strong> · ' + adopted_summary +
               f'<strong>{open_count} open</strong> · {project_count} projects')
    by_key = {(p["repo"], p["number"]): p for p in visible}
    featured = [by_key[key] for key in HIGHLIGHTS if key in by_key]
    names = {repo: name for repo, name, _ in PROJECTS}
    highlights = []
    for p in featured:
        label = PR_LABELS[(p["repo"], p["number"])]
        highlights.append(
            f'<li><a href="{escape(p["url"], quote=True)}"><strong>{names[p["repo"]]} #{p["number"]}</strong></a> '
            f'<code>{p["state"]}</code> — {escape(label)}</li>'
        )
    selected = '<ul>\n' + '\n'.join(highlights) + '\n</ul>\n\n' if highlights else ''
    ordered = sorted(visible, key=lambda p: {"merged": 0, "open": 1}[p["state"]])
    full_list = contribution_table(ordered, [repo for repo, _, _ in PROJECTS])
    footer = ('[All authored PRs](https://github.com/search?q=author%3Ayuchenwang3+is%3Apr&type=pullrequests) · '
              '[Engineering notes](https://yuchenwang3.github.io/projects/open-source-systems/)')
    return ('\n\n' + selected + '<details>\n<summary>Full PR list · ' + summary + '</summary>\n\n'
            + full_list + '\n\n' + footer + '\n\n</details>\n\n')


def snake_section():
    base = "https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/output/"
    return f'''\n#### Contribution trail

<picture>
<source media="(prefers-color-scheme: dark)" srcset="{base}github-snake-dark.svg">
<img width="100%" src="{base}github-snake.svg" alt="Snake animation of my GitHub contribution history">
</picture>
'''


def render_readme(prs):
    header = '''<a id="yuchen-ean-wang"></a>

## `>` Yuchen (Ean) Wang

Agentic post-training & ML systems · M.S. CS [@illinois](https://github.com/illinois) · Research intern [@Accio-Lab](https://github.com/Accio-Lab) / [@alibaba](https://github.com/alibaba).

'''
    contacts = '<p>\n' + "\n".join(button(label, url) for label, url in CONTACTS.values()) + "\n</p>\n\n"
    return (header + contacts + occamy_section()
            + '\n<a id="patches"></a>\n\n### Selected contributions\n\n<!-- PR-PREVIEWS:START -->'
            + contribution_section(prs) + "<!-- PR-PREVIEWS:END -->\n"
            + '\n' + research_section()
            + "\nReviewer, [WSDM 2027](https://www.wsdm-conference.org/2027/).\n"
            + '\n<a id="activity"></a>\n\n<details>\n<summary>Activity</summary>\n\n'
            + widget_section() + snake_section() + '\n</details>\n')


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
