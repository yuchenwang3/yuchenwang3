<div align="center">

  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=22&pause=1000&color=0A66C2&center=true&vCenter=true&width=860&lines=Yuchen+Wang+%7C+Agentic+LLM+Research;Post-training+%C3%97+Systems+%C3%97+Open+Source" alt="Yuchen Wang — Agentic LLM Research" />

  <p><strong>I build foundation models that can work—not just answer.</strong></p>

  <p>
    <a href="https://huggingface.co/occamy-ai/occamy-1.0"><img src="https://img.shields.io/badge/Occamy--1.0-35B--A3B-FFD21E?style=for-the-badge&logo=huggingface&logoColor=111111" alt="Occamy-1.0" /></a>
    <a href="https://yuchenwang3.github.io"><img src="https://img.shields.io/badge/Portfolio-Research%20%26%20Systems-0A66C2?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio" /></a>
    <a href="https://scholar.google.com/citations?user=NharhG8AAAAJ"><img src="https://img.shields.io/badge/Google%20Scholar-Profile-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar" /></a>
  </p>

  <p>
    <a href="https://www.linkedin.com/in/yuchen3"><img src="https://img.shields.io/badge/LinkedIn-Yuchen%20Wang-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
    <a href="https://yuchenwang3.github.io/CV.pdf"><img src="https://img.shields.io/badge/CV-PDF-B31B1B?style=flat-square&logo=adobeacrobatreader&logoColor=white" alt="CV" /></a>
    <img src="https://img.shields.io/github/followers/yuchenwang3?style=flat-square&logo=github&label=Followers" alt="GitHub followers" />
    <img src="https://komarev.com/ghpvc/?username=wangyuchen333&style=flat-square&color=0A66C2" alt="Profile views" />
  </p>

</div>

<table>
  <tr>
    <td valign="top" width="50%">
      <h3>🔬 Now</h3>
      <p><strong>Research Scientist Intern @ Alibaba</strong><br />Agentic LLM post-training, long-horizon tool use, and evaluation infrastructure.</p>
      <p><strong>M.S. Computer Science @ UIUC</strong><br />B.S. in Intelligent Science and Technology (AI), Peking University Zhi Class.</p>
    </td>
    <td valign="top" width="50%">
      <h3>⚙️ Systems</h3>
      <p>Open-source engineering across <strong>NeMo, Megatron-LM, vLLM/Vime, SGLang, and ModelScope</strong>.</p>
      <p>Training reliability · long-context kernels · CUDA · RL infrastructure · inference serving</p>
    </td>
  </tr>
</table>

<details>
  <summary><strong>🎧 Off the clock</strong></summary>
  <br />
  <strong>11,410 tracks logged on NetEase Cloud</strong>
  · hip-hop & trap, EDM, alt-pop, ambient, and post-rock.
  <br /><br />
  <img src="https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/output/music-card.svg" alt="All-time NetEase Cloud listening snapshot: 11,410 tracks and most replayed songs" width="900" />
  <br /><br />
  <em>P.S. Trying to be more engaged with the outdoors.</em>
</details>

## 🦦 Occamy-1.0

**[Occamy-1.0](https://huggingface.co/occamy-ai/occamy-1.0)** is a 35B-A3B
co-work model continued from Qwen3.6-35B-A3B through full-parameter SFT,
uniform model soup, and GRPO/SAO reinforcement learning.

I built verifier-gated data and training infrastructure for token-exact replay,
state reconstruction, episode credit across context rewrites, immutable
provenance, and quarantine gates. On the same frozen ClawEval harness, the
resulting system raised Combined T/C Strict Pass@1/3 from
**65.16/73.87% → 77.39/85.93%** while reducing tokens per trajectory by
**38.6%**.

## 🧩 Open-source systems engineering

| Area                         | Selected contribution                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Optimizer stability          | Scale-invariant Newton–Schulz for small-norm Muon inputs in [NVIDIA NeMo Emerging Optimizers #230](https://github.com/NVIDIA-NeMo/Emerging-Optimizers/pull/230)                                                                                                                                                                                |
| Hybrid-model training        | Recompute propagation and Mamba + attention + MoE runtime fixes in [vLLM/Vime #337](https://github.com/vllm-project/vime/pull/337)                                                                                                                                                                                                             |
| Training throughput          | Order-preserving sequence packing, NCCL warmup, and Muon correctness across [ModelScope ms-swift #9598](https://github.com/modelscope/ms-swift/pull/9598), [#9602](https://github.com/modelscope/ms-swift/pull/9602), [#9599](https://github.com/modelscope/ms-swift/pull/9599), and [#9591](https://github.com/modelscope/ms-swift/pull/9591) |
| Long-context kernels         | Fused GatedDeltaNet Q/K normalization for 128K SFT in [Megatron-LM #5396](https://github.com/NVIDIA/Megatron-LM/pull/5396) and selective Mamba recompute in [#5463](https://github.com/NVIDIA/Megatron-LM/pull/5463)                                                                                                                           |
| RL and inference reliability | Non-finite rollout-logprob sanitization in [NeMo RL #2962](https://github.com/NVIDIA-NeMo/RL/pull/2962) and safer hybrid-model weight reloads in [SGLang #31621](https://github.com/sgl-project/sglang/pull/31621)                                                                                                                             |

## 📚 Papers and projects

- **[CineFlow](https://raw.githubusercontent.com/yuchenwang3/yuchenwang3.github.io/main/assets/pdf/projects/cineflow-paper.pdf)** — dependency-driven parallel video generation with semantic DAG compilation, trajectory-aware fusion, and critical-path scheduling; **1.7–5.5× speedup** and **17.3% higher visual quality**.
- **[Dynamic Prefill Optimization](https://raw.githubusercontent.com/yuchenwang3/yuchenwang3.github.io/main/assets/pdf/projects/dynamic-prefill-online-packing-report.pdf)** — AIMD control with p95 TTFT feedback and greedy/DP prompt packing; up to **20% lower TTFT** on production-style traces.
- **[FlashAttention-style CUDA Optimization](https://raw.githubusercontent.com/yuchenwang3/yuchenwang3.github.io/main/assets/pdf/projects/gpt2-processing-unit-report.pdf)** — tiled online softmax and kernel fusion for GPT-2; roughly **10× lower HBM traffic** and up to **9% end-to-end speedup**.
- **[RL for Legal Reasoning](https://raw.githubusercontent.com/yuchenwang3/yuchenwang3.github.io/main/assets/pdf/projects/legal-reasoning-thesis.pdf)** — Zero-RL → distilled-CoT SFT → GRPO, reaching **57.6% accuracy**.

## 🛠️ Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="CUDA" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=111111" alt="Hugging Face" />
  <img src="https://img.shields.io/badge/vLLM-111111?style=for-the-badge" alt="vLLM" />
  <img src="https://img.shields.io/badge/Megatron--LM-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="Megatron-LM" />
  <img src="https://img.shields.io/badge/SGLang-6C5CE7?style=for-the-badge" alt="SGLang" />
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=yuchenwang3&theme=github_dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=yuchenwang3&theme=github" />
    <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=yuchenwang3&theme=github" alt="GitHub stars, commits, pull requests, issues, and contributions" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=yuchenwang3&theme=github_dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=yuchenwang3&theme=github" />
    <img height="170" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=yuchenwang3&theme=github" alt="Top GitHub repository languages" />
  </picture>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/output/github-snake.svg" />
  <img alt="GitHub contribution grid animation" src="https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/output/github-snake.svg" />
</picture>

<p align="center"><em>To an unceasing future. 致永无止境的明天。</em></p>
