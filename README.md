<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/editorial-header-dark.svg">
  <img src="./assets/editorial-header-light.svg" alt="Yuchen Ean Wang — agentic post-training, ML systems, and open-source engineering">
</picture>

<div align="center">

  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=22&pause=1000&color=3843D0&center=true&vCenter=true&width=860&lines=Yuchen+Wang+%7C+Agentic+LLM+Research;Post-training+%C3%97+Systems+%C3%97+Open+Source" alt="Yuchen Wang — Agentic LLM Research" />

  <p>
    <a href="https://huggingface.co/Accio-Lab/Occamy-1.0"><img src="https://img.shields.io/badge/Occamy--1.0-35B--A3B-FFD21E?style=for-the-badge&logo=huggingface&logoColor=111111" alt="Occamy-1.0" /></a>
    <a href="https://yuchenwang3.github.io"><img src="https://img.shields.io/badge/Portfolio-Research%20%26%20Systems-3843D0?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio" /></a>
    <a href="https://scholar.google.com/citations?user=NharhG8AAAAJ"><img src="https://img.shields.io/badge/Google%20Scholar-Profile-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar" /></a>
  </p>

  <p>
    <a href="https://www.linkedin.com/in/yuchen3"><img src="https://img.shields.io/badge/LinkedIn-Yuchen%20Wang-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
    <a href="https://yuchenwang3.github.io/CV.pdf"><img src="https://img.shields.io/badge/CV-PDF-B31B1B?style=flat-square&logo=adobeacrobatreader&logoColor=white" alt="CV" /></a>
    <img src="https://img.shields.io/github/followers/yuchenwang3?style=flat-square&logo=github&label=Followers" alt="GitHub followers" />
    <img src="https://komarev.com/ghpvc/?username=yuchenwang3&base=953&style=flat-square&color=3843D0" alt="Profile views" />
    <a href="https://gitviewsmap.onrender.com/yuchenwang3"><img src="https://img.shields.io/badge/Visitor%20Map-approximate%20locations-4B55D4?style=flat-square&logo=googlemaps&logoColor=white" alt="Approximate visitor map" /></a>
  </p>

</div>

<table>
  <tr>
    <td valign="top" width="50%">
      <h3>🔬 Now</h3>
      <p><strong>Research Intern @ Alibaba U.S. · Accio Team</strong><br />Execution-grounded data, agentic post-training, and reliable long-horizon tool use.</p>
      <p><strong>M.S. Computer Science @ UIUC</strong><br />B.S. in Intelligent Science and Technology (AI), Peking University Zhi Class.</p>
    </td>
    <td valign="top" width="50%">
      <h3>⚙️ Systems</h3>
      <p>Open-source engineering across <strong>NeMo, Megatron-LM, vLLM/Vime, SGLang, and ModelScope</strong>.</p>
      <p>Training reliability · long-context kernels · CUDA · RL infrastructure · inference serving</p>
    </td>
  </tr>
</table>

## 🦦 Occamy-1.0

**Occamy-1.0: Open Pareto-frontier 35B Intelligence for Co-work**

I contribute to **Occamy-1.0 with Alibaba's Accio Team**, working on
execution-grounded data, multi-harness trajectory collection, and post-training
infrastructure. Built from Qwen3.6-35B-A3B, the model combines a long-horizon
Marathon Expert (SFT + HDPO) and a broader Sprint Expert (SFT) through model
soup, followed by SAO reinforcement learning.

My work includes verifier-gated task admission, token-exact replay, state
reconstruction, and training traces that preserve task-level outcomes across
context rewrites. The latest report records **82.2 Claw-Eval average / 71.4
Pass³**, **49.16 WildClawBench**, and **27.6% AutomationBench strict pass rate**.
On the combined Claw-Eval T/C evaluation, Occamy uses **19.5% fewer tokens per
trajectory** and **46.4% less trace wall time** than Qwen3.6-35B-A3B under the
same protocol. These are team-level model results.

[Project & results](https://yuchenwang3.github.io/projects/occamy-1-0/) ·
[Research website](https://occamy-research.ianwang030303.chatgpt.site/) ·
[Model](https://huggingface.co/Accio-Lab/Occamy-1.0) ·
[Code](https://github.com/Accio-Lab/occamy)

## 🧩 Open-source systems engineering

| Area                         | Selected contribution                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Optimizer stability          | Scale-invariant Newton–Schulz for small-norm Muon inputs in [NVIDIA NeMo Emerging Optimizers #230](https://github.com/NVIDIA-NeMo/Emerging-Optimizers/pull/230)                                                                                                                                                                                |
| Hybrid-model training        | Recompute propagation and Mamba + attention + MoE runtime fixes in [vLLM/Vime #337](https://github.com/vllm-project/vime/pull/337)                                                                                                                                                                                                             |
| Training throughput          | Order-preserving sequence packing, NCCL warmup, and Muon correctness across [ModelScope ms-swift #9598](https://github.com/modelscope/ms-swift/pull/9598), [#9602](https://github.com/modelscope/ms-swift/pull/9602), [#9599](https://github.com/modelscope/ms-swift/pull/9599), and [#9591](https://github.com/modelscope/ms-swift/pull/9591) |
| Large-model serving          | In-place FlashInfer BF16 MoE conversion in [vLLM #54699](https://github.com/vllm-project/vllm/pull/54699), halving TP2 peak allocation from **7.88 to 3.94 GiB** and validating real 120B load, generation, and 3/3 sleep-wake cycles on 8×B200                                                                              |
| Distributed transfer         | Controlled Ray transfer path in [NeMo RL #3943](https://github.com/NVIDIA-NeMo/RL/pull/3943), delivering **4.44–5.31× speedup** while limiting driver RSS deltas to 0.1–0.3 MB                                                                                                                                                                 |
| Long-context kernels         | Fused GatedDeltaNet Q/K normalization for 128K SFT in [Megatron-LM #5396](https://github.com/NVIDIA/Megatron-LM/pull/5396) and selective Mamba recompute in [#5463](https://github.com/NVIDIA/Megatron-LM/pull/5463)                                                                                                                           |
| RL and inference reliability | Non-finite rollout-logprob sanitization in [NeMo RL #2962](https://github.com/NVIDIA-NeMo/RL/pull/2962), GDN/Muon clipping and routing in [Megatron-LM #5395](https://github.com/NVIDIA/Megatron-LM/pull/5395), [#5400](https://github.com/NVIDIA/Megatron-LM/pull/5400), and [#5431](https://github.com/NVIDIA/Megatron-LM/pull/5431), skipped-tensor checks in [SGLang #31621](https://github.com/sgl-project/sglang/pull/31621), and authoritative FSDP strategy in [verl #7597](https://github.com/verl-project/verl/pull/7597) |

## 📚 Papers and projects

- **[CineFlow](https://raw.githubusercontent.com/yuchenwang3/yuchenwang3.github.io/main/assets/pdf/projects/cineflow-paper.pdf)** — the first dependency-driven video-diffusion inference system, evaluated across Wan2.2-5B, CogVideoX-5B, and HunyuanVideo on 8×H100; **1.7–5.5× speedup**, **1.30–2.02× lower P90 latency**, and **5.4–17.3% higher VBench overall**.
- **[Dynamic Prefill Optimization](https://raw.githubusercontent.com/yuchenwang3/yuchenwang3.github.io/main/assets/pdf/projects/dynamic-prefill-online-packing-report.pdf)** — AIMD control with p95 TTFT feedback and greedy/DP prompt packing; up to **20% lower TTFT** on production-style traces.
- **[FlashAttention-style CUDA Optimization](https://raw.githubusercontent.com/yuchenwang3/yuchenwang3.github.io/main/assets/pdf/projects/gpt2-processing-unit-report.pdf)** — tiled online softmax and kernel fusion for GPT-2; roughly **10× lower HBM traffic** and up to **9% end-to-end speedup**.
- **[RL for Legal Reasoning](https://raw.githubusercontent.com/yuchenwang3/yuchenwang3.github.io/main/assets/pdf/projects/legal-reasoning-thesis.pdf)** — advised by Prof. Yansong Feng; Zero-RL → distilled-CoT SFT → GRPO, reaching **57.6% accuracy**.

## 🛠️ Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="CUDA" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=111111" alt="Hugging Face" />
  <img src="https://img.shields.io/badge/vLLM-111111?style=for-the-badge" alt="vLLM" />
  <img src="https://img.shields.io/badge/Megatron--LM-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="Megatron-LM" />
  <img src="https://img.shields.io/badge/SGLang-4B55D4?style=for-the-badge" alt="SGLang" />
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
