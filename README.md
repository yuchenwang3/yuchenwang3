<a id="yuchen-ean-wang"></a>

## `>` Yuchen (Ean) Wang

Agentic post-training & ML systems · M.S. CS [@illinois](https://github.com/illinois) · Research intern [@Accio-Lab](https://github.com/Accio-Lab) / [@alibaba](https://github.com/alibaba).

<p>
<a href="https://yuchenwang3.github.io/"><img src="https://img.shields.io/badge/Website-181717?style=flat-square&amp;logo=vercel&amp;logoColor=white" alt="Website"></a>
<a href="https://scholar.google.com/citations?user=NharhG8AAAAJ"><img src="https://img.shields.io/badge/Scholar-4285F4?style=flat-square&amp;logo=googlescholar&amp;logoColor=white" alt="Scholar"></a>
<a href="https://www.linkedin.com/in/yuchen3"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&amp;logo=linkedin&amp;logoColor=white" alt="LinkedIn"></a>
<a href="mailto:yuchenwang0303@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&amp;logo=gmail&amp;logoColor=white" alt="Email"></a>
<a href="https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/main/assets/wechat-qr.jpg"><img src="https://img.shields.io/badge/WeChat%20%C2%B7%20eangyc-07C160?style=flat-square&amp;logo=wechat&amp;logoColor=white" alt="WeChat · eangyc"></a>
</p>

### [Occamy-1.0](https://accio-lab.github.io/occamy/)

35B-A3B agent model for long-horizon tool use. **Core contributor** — post-training algorithms, infrastructure & data.<br>
<a href="https://huggingface.co/collections/Accio-Lab/occamy-10" title="1,190,764 all-time downloads across 12 official quantized repositories"><strong>≈1.2M cumulative downloads</strong></a> across official quantized releases.

[Report](https://arxiv.org/abs/2609.11977) · [Demo](https://accio-lab.github.io/occamy/) · [Model](https://huggingface.co/Accio-Lab/Occamy-1.0) · [Code](https://github.com/Accio-Lab/occamy)

<a id="patches"></a>

### Selected contributions

<!-- PR-PREVIEWS:START -->

<ul>
<li><a href="https://github.com/vllm-project/vllm/pull/54699"><strong>vLLM #54699</strong></a> <code>merged</code> — Remove full-weight copies during MoE loading; conversion peak 7.88 → 3.94 GiB in the exact-shape TP2 benchmark</li>
<li><a href="https://github.com/modelscope/mcore-bridge/pull/211"><strong>mcore-bridge #211</strong></a> <code>merged</code> — Score packed QSA within each document; 2.70× faster in an 8K synthetic selector benchmark</li>
<li><a href="https://github.com/huggingface/datasets/pull/8670"><strong>HF Datasets #8670</strong></a> <code>merged</code> — Preserve source shards during streaming shuffle so four workers can share 19 shards</li>
</ul>

<details>
<summary>Full PR list · <strong>13 merged</strong> · <strong>1 adopted solution</strong> · <strong>23 open</strong> · 16 projects</summary>

<table>
<tr>
<td width="28%" valign="top"><a href="https://github.com/huggingface/datasets"><strong>HF Datasets</strong></a><br><sub><code>huggingface</code></sub></td>
<td width="72%"><p><a href="https://github.com/huggingface/datasets/pull/8670"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/huggingface-datasets-8670-dark.svg"><img height="26" src="./assets/prs/status/huggingface-datasets-8670-light.svg" alt="#8670 · merged"></picture></a> Preserve source shards during streaming shuffle so four workers can share 19 shards</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/modelscope/mcore-bridge"><strong>mcore-bridge</strong></a><br><sub><code>modelscope</code></sub></td>
<td width="72%"><p><a href="https://github.com/modelscope/mcore-bridge/pull/211"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/modelscope-mcore-bridge-211-dark.svg"><img height="26" src="./assets/prs/status/modelscope-mcore-bridge-211-light.svg" alt="#211 · merged"></picture></a> Score packed QSA within each document; 2.70× faster in an 8K synthetic selector benchmark</p><p><a href="https://github.com/modelscope/mcore-bridge/pull/212"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/modelscope-mcore-bridge-212-dark.svg"><img height="26" src="./assets/prs/status/modelscope-mcore-bridge-212-light.svg" alt="#212 · open"></picture></a> Preserve low-precision rounding in gated residual mixing</p><p><a href="https://github.com/modelscope/mcore-bridge/pull/213"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/modelscope-mcore-bridge-213-dark.svg"><img height="26" src="./assets/prs/status/modelscope-mcore-bridge-213-light.svg" alt="#213 · open"></picture></a> Bound PLE backward&#x27;s extra workspace through chunked token reductions</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/NVIDIA-NeMo/Megatron-Bridge"><strong>Megatron Bridge</strong></a><br><sub><code>NVIDIA-NeMo</code></sub></td>
<td width="72%"><p><a href="https://github.com/NVIDIA-NeMo/Megatron-Bridge/pull/6315"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-NeMo-Megatron-Bridge-6315-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-NeMo-Megatron-Bridge-6315-light.svg" alt="#6315 · open"></picture></a> Add Bridge-local Qwen4-Exp text-decoder support; GPU integration is pending</p><p><a href="https://github.com/NVIDIA-NeMo/Megatron-Bridge/pull/6312"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-NeMo-Megatron-Bridge-6312-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-NeMo-Megatron-Bridge-6312-light.svg" alt="#6312 · open"></picture></a> Make HF/Megatron comparison failures return a nonzero exit status</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/THUDM/slime"><strong>slime</strong></a><br><sub><code>THUDM</code></sub></td>
<td width="72%"><p><a href="https://github.com/THUDM/slime/pull/2412"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/THUDM-slime-2412-dark.svg"><img height="26" src="./assets/prs/status/THUDM-slime-2412-light.svg" alt="#2412 · open"></picture></a> Score fan-out rollout samples as a flat group</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/modelscope/ms-swift"><strong>ms-swift</strong></a><br><sub><code>modelscope</code></sub></td>
<td width="72%"><p><a href="https://github.com/modelscope/ms-swift/pull/9598"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/modelscope-ms-swift-9598-dark.svg"><img height="26" src="./assets/prs/status/modelscope-ms-swift-9598-light.svg" alt="#9598 · merged"></picture></a> Add order-preserving packing</p><p><a href="https://github.com/modelscope/ms-swift/pull/9602"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/modelscope-ms-swift-9602-dark.svg"><img height="26" src="./assets/prs/status/modelscope-ms-swift-9602-light.svg" alt="#9602 · merged"></picture></a> Warm up NCCL before training</p><p><a href="https://github.com/modelscope/ms-swift/pull/9599"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/modelscope-ms-swift-9599-dark.svg"><img height="26" src="./assets/prs/status/modelscope-ms-swift-9599-light.svg" alt="#9599 · merged"></picture></a> Pass through Muon Nesterov settings</p><p><a href="https://github.com/modelscope/ms-swift/pull/9591"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/modelscope-ms-swift-9591-dark.svg"><img height="26" src="./assets/prs/status/modelscope-ms-swift-9591-light.svg" alt="#9591 · merged"></picture></a> Expose Muon coefficient selection</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/flashinfer-ai/flashinfer"><strong>FlashInfer</strong></a><br><sub><code>flashinfer-ai</code></sub></td>
<td width="72%"><p><a href="https://github.com/flashinfer-ai/flashinfer/pull/4984"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/flashinfer-ai-flashinfer-4984-dark.svg"><img height="26" src="./assets/prs/status/flashinfer-ai-flashinfer-4984-light.svg" alt="#4984 · merged"></picture></a> Restore K/V calibration in FP8 KV prefill, correcting silently mis-scaled attention outputs</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/vllm-project/vime"><strong>vime</strong></a><br><sub><code>vllm-project</code></sub></td>
<td width="72%"><p><a href="https://github.com/vllm-project/vime/pull/337"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/vllm-project-vime-337-dark.svg"><img height="26" src="./assets/prs/status/vllm-project-vime-337-light.svg" alt="#337 · merged"></picture></a> Forward recompute flags; fix hybrid models</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/NVIDIA-NeMo/Emerging-Optimizers"><strong>Emerging Optimizers</strong></a><br><sub><code>NVIDIA-NeMo</code></sub></td>
<td width="72%"><p><a href="https://github.com/NVIDIA-NeMo/Emerging-Optimizers/pull/230"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-NeMo-Emerging-Optimizers-230-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-NeMo-Emerging-Optimizers-230-light.svg" alt="#230 · merged"></picture></a> Keep Muon scale-invariant</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/NVIDIA-NeMo/Gym"><strong>NeMo Gym</strong></a><br><sub><code>NVIDIA-NeMo</code></sub></td>
<td width="72%"><p><a href="https://github.com/NVIDIA-NeMo/Gym/pull/2726"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-NeMo-Gym-2726-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-NeMo-Gym-2726-light.svg" alt="#2726 · merged"></picture></a> Preserve HTTP errors across process boundaries<br><sub>Co-author</sub></p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/Dao-AILab/flash-attention"><strong>FlashAttention</strong></a><br><sub><code>Dao-AILab</code></sub></td>
<td width="72%"><p><a href="https://github.com/Dao-AILab/flash-attention/pull/2507"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/Dao-AILab-flash-attention-2507-dark.svg"><img height="26" src="./assets/prs/status/Dao-AILab-flash-attention-2507-light.svg" alt="#2507 · merged"></picture></a> Prevent redundant backward-kernel recompilation with stable cache keys, without CPU–GPU sync<br><sub><a href="https://github.com/Dao-AILab/flash-attention/pull/2507#issuecomment-4921776396">Solution adopted by the PR author</a></sub></p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/vllm-project/vllm"><strong>vLLM</strong></a><br><sub><code>vllm-project</code></sub></td>
<td width="72%"><p><a href="https://github.com/vllm-project/vllm/pull/58219"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/vllm-project-vllm-58219-dark.svg"><img height="26" src="./assets/prs/status/vllm-project-vllm-58219-light.svg" alt="#58219 · merged"></picture></a> Clarify Qwen3 parser boundary tokens in custom grammars</p><p><a href="https://github.com/vllm-project/vllm/pull/54699"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/vllm-project-vllm-54699-dark.svg"><img height="26" src="./assets/prs/status/vllm-project-vllm-54699-light.svg" alt="#54699 · merged"></picture></a> Remove full-weight copies during MoE loading; conversion peak 7.88 → 3.94 GiB in the exact-shape TP2 benchmark</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/NVIDIA/Megatron-LM"><strong>Megatron-LM</strong></a><br><sub><code>NVIDIA</code></sub></td>
<td width="72%"><p><a href="https://github.com/NVIDIA/Megatron-LM/pull/7864"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-Megatron-LM-7864-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-Megatron-LM-7864-light.svg" alt="#7864 · open"></picture></a> Preserve native Adam step counters across checkpoint restoration</p><p><a href="https://github.com/NVIDIA/Megatron-LM/pull/7881"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-Megatron-LM-7881-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-Megatron-LM-7881-light.svg" alt="#7881 · open"></picture></a> Reuse packed chunkwise CP metadata across GDN and KDA layers</p><p><a href="https://github.com/NVIDIA/Megatron-LM/pull/5396"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-Megatron-LM-5396-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-Megatron-LM-5396-light.svg" alt="#5396 · open"></picture></a> Fuse GDN Q/K normalization to remove an extra backward activation buffer</p><p><a href="https://github.com/NVIDIA/Megatron-LM/pull/5463"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-Megatron-LM-5463-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-Megatron-LM-5463-light.svg" alt="#5463 · open"></picture></a> Enable selective Mamba mixer recompute to save activation memory without full-layer recomputation</p><p><a href="https://github.com/NVIDIA/Megatron-LM/pull/5400"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-Megatron-LM-5400-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-Megatron-LM-5400-light.svg" alt="#5400 · open"></picture></a> Route GDN input projections to Adam</p><p><a href="https://github.com/NVIDIA/Megatron-LM/pull/5431"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-Megatron-LM-5431-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-Megatron-LM-5431-light.svg" alt="#5431 · open"></picture></a> Exclude GDN input projections from global clipping</p><p><a href="https://github.com/NVIDIA/Megatron-LM/pull/5395"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-Megatron-LM-5395-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-Megatron-LM-5395-light.svg" alt="#5395 · open"></picture></a> Skip gradient clipping for Muon</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/NVIDIA-NeMo/RL"><strong>NeMo RL</strong></a><br><sub><code>NVIDIA-NeMo</code></sub></td>
<td width="72%"><p><a href="https://github.com/NVIDIA-NeMo/RL/pull/4193"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-NeMo-RL-4193-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-NeMo-RL-4193-light.svg" alt="#4193 · merged"></picture></a> Render evaluation prompts as complete conversations</p><p><a href="https://github.com/NVIDIA-NeMo/RL/pull/4176"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-NeMo-RL-4176-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-NeMo-RL-4176-light.svg" alt="#4176 · open"></picture></a> Unify worker selection through configuration</p><p><a href="https://github.com/NVIDIA-NeMo/RL/pull/3943"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-NeMo-RL-3943-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-NeMo-RL-3943-light.svg" alt="#3943 · open"></picture></a> Bypass driver tensor materialization in distillation; 4.4–5.3× faster transfers in a controlled Ray benchmark</p><p><a href="https://github.com/NVIDIA-NeMo/RL/pull/2962"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NVIDIA-NeMo-RL-2962-dark.svg"><img height="26" src="./assets/prs/status/NVIDIA-NeMo-RL-2962-light.svg" alt="#2962 · open"></picture></a> Sanitize non-finite async log probabilities</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/sgl-project/sglang"><strong>SGLang</strong></a><br><sub><code>sgl-project</code></sub></td>
<td width="72%"><p><a href="https://github.com/sgl-project/sglang/pull/40103"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/sgl-project-sglang-40103-dark.svg"><img height="26" src="./assets/prs/status/sgl-project-sglang-40103-light.svg" alt="#40103 · open"></picture></a> Reject developer messages silently dropped by templates</p><p><a href="https://github.com/sgl-project/sglang/pull/39765"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/sgl-project-sglang-39765-dark.svg"><img height="26" src="./assets/prs/status/sgl-project-sglang-39765-light.svg" alt="#39765 · open"></picture></a> Publish Mamba cache updates before dependent batches capture stale KV mappings</p><p><a href="https://github.com/sgl-project/sglang/pull/38063"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/sgl-project-sglang-38063-dark.svg"><img height="26" src="./assets/prs/status/sgl-project-sglang-38063-light.svg" alt="#38063 · open"></picture></a> Explain cold MXFP4 JIT startup</p><p><a href="https://github.com/sgl-project/sglang/pull/31621"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/sgl-project-sglang-31621-dark.svg"><img height="26" src="./assets/prs/status/sgl-project-sglang-31621-light.svg" alt="#31621 · open"></picture></a> Honor weight-check exclusions during reset</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/verl-project/verl"><strong>verl</strong></a><br><sub><code>verl-project</code></sub></td>
<td width="72%"><p><a href="https://github.com/verl-project/verl/pull/7906"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/verl-project-verl-7906-dark.svg"><img height="26" src="./assets/prs/status/verl-project-verl-7906-light.svg" alt="#7906 · open"></picture></a> Track response truncation across context limits</p><p><a href="https://github.com/verl-project/verl/pull/7597"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/verl-project-verl-7597-dark.svg"><img height="26" src="./assets/prs/status/verl-project-verl-7597-light.svg" alt="#7597 · open"></picture></a> Validate actor FSDP strategy</p></td>
</tr>
<tr>
<td width="28%" valign="top"><a href="https://github.com/NousResearch/hermes-agent"><strong>Hermes Agent</strong></a><br><sub><code>NousResearch</code></sub></td>
<td width="72%"><p><a href="https://github.com/NousResearch/hermes-agent/pull/113511"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NousResearch-hermes-agent-113511-dark.svg"><img height="26" src="./assets/prs/status/NousResearch-hermes-agent-113511-light.svg" alt="#113511 · open"></picture></a> Control partial-stream continuation for batch evaluation</p><p><a href="https://github.com/NousResearch/hermes-agent/pull/113538"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/prs/status/NousResearch-hermes-agent-113538-dark.svg"><img height="26" src="./assets/prs/status/NousResearch-hermes-agent-113538-light.svg" alt="#113538 · open"></picture></a> Clarify API retry budgets and streaming defaults</p></td>
</tr>
</table>

[All authored PRs](https://github.com/search?q=author%3Ayuchenwang3+is%3Apr&type=pullrequests) · [Engineering notes](https://yuchenwang3.github.io/projects/open-source-systems/)

</details>

<!-- PR-PREVIEWS:END -->

<a id="research"></a>

### Other research

- **CineFlow** — Dependency-driven parallel video generation. Co-first author · 1.7–5.5× end-to-end speedup in the reported evaluation.
- **[Dynamic Prefill](https://yuchenwang3.github.io/projects/prepack/)** — Adaptive batching and prompt packing; up to 20% lower TTFT on the reported traces. [Report](https://yuchenwang3.github.io/assets/pdf/projects/dynamic-prefill-online-packing-report.pdf) · [Code](https://github.com/Winlere/prepack-workspace)
- **[RareDx](https://arxiv.org/abs/2609.35549)** — Graph-grounded RL for rare disease diagnosis. Co-first author.
- [CUDA Attention](https://yuchenwang3.github.io/assets/pdf/projects/gpt2-processing-unit-report.pdf) · [RL for Legal Reasoning](https://yuchenwang3.github.io/assets/pdf/projects/legal-reasoning-thesis.pdf)

Reviewer, [WSDM 2027](https://www.wsdm-conference.org/2027/).

<a id="activity"></a>

<details>
<summary>Activity</summary>

<p>
<a href="https://github.com/yuchenwang3?tab=followers"><img src="https://img.shields.io/github/followers/yuchenwang3?label=Follow&amp;style=social" alt="Follow on GitHub"></a>
<a href="https://github.com/yuchenwang3?tab=repositories&amp;sort=stargazers"><img src="https://img.shields.io/github/stars/yuchenwang3?label=Stars&amp;style=social" alt="Stars on my repositories"></a>
<a href="https://github.com/search?q=author%3Ayuchenwang3+is%3Apr+is%3Aopen&amp;type=pullrequests"><img src="https://img.shields.io/badge/PRs-in_flight-426dab?style=flat-square&amp;logo=git&amp;logoColor=white" alt="Explore my open pull requests"></a>
</p>

<p>
<a href="https://github.com/yuchenwang3?tab=overview"><picture>
<source media="(prefers-color-scheme: dark)" srcset="./assets/widgets/activity-dark.svg">
<img width="390" src="./assets/widgets/activity-light.svg" alt="GitHub contribution rhythm over 26 weeks">
</picture></a>
<a href="https://github.com/yuchenwang3?tab=repositories"><picture>
<source media="(prefers-color-scheme: dark)" srcset="./assets/widgets/languages-dark.svg">
<img width="390" src="./assets/widgets/languages-light.svg" alt="Primary languages of my public non-fork repositories">
</picture></a>
</p>


#### Contribution trail

<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/output/github-snake-dark.svg">
<img width="100%" src="https://raw.githubusercontent.com/yuchenwang3/yuchenwang3/output/github-snake.svg" alt="Snake animation of my GitHub contribution history">
</picture>

</details>
