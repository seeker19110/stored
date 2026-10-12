# 07 · LLM Evaluation, Testing & Observability

| Công cụ | Repo | License | Vai trò | Ghi chú |
|---|---|---|---|---|
| **Langfuse** | langfuse/langfuse | MIT (core; `ee/` thương mại) | Tracing, prompt management, evals, metrics; self-host/cloud | Trụ cột observability mở |
| **Promptfoo** | promptfoo/promptfoo | MIT | Test prompt YAML, CLI cho CI, **red-teaming** | Gate ở PR |
| **DeepEval** | confident-ai/deepeval | Apache-2.0 (kiểm tra LICENSE) | Eval kiểu pytest: G-Eval, faithfulness, hallucination | v4.1.4 (7/2026) |
| **Ragas** | explodinggradients/ragas | Apache-2.0 | Metric cho RAG | Thường ghép Langfuse |
| **Arize Phoenix** | Arize-ai/phoenix | Elastic License 2.0 (source-available) | Tracing + eval | Không OSI |
| **OpenCompass / LightEval** | open-compass/opencompass · huggingface/lighteval | Apache-2.0 / MIT | Benchmark model | Học thuật; xem bảng bổ sung |
| **LangSmith / Braintrust** | – | Đóng | SaaS eval+trace | |

**Stack miễn phí gợi ý:** Promptfoo (CI gate) + Langfuse (trace production) + DeepEval/Ragas (chấm mẫu trace).

**Cho coding agent:** SWE-bench Pro, SWE-Touch, RoadmapBench (xem mục 01); theo dõi chi phí token & KV-cache hit rate (mục 03). **Benchmark agent tổng quát:** GAIA (trợ lý đa bước), Terminal-Bench 2 (tác vụ terminal), τ-bench / τ²-bench (tool + người dùng mô phỏng), Agent-as-a-Judge (agent chấm agent) — tên gom từ docs nội bộ X-Agents (mục 23); repo và phiên bản đã đối chiếu ở mục "Repo eval & observability nổi tiếng bổ sung" bên dưới (12/10/2026).

## Mẫu eval từ repo của chủ kho (mục 23, 2026-10-12)

- **Eval record/replay trong CI** (X-Agents `.github/workflows/eval-record.yml`): ghi lại hội thoại/tool-call thật thành fixture, CI replay không gọi model; chỉ "record" lại khi prompt đổi có chủ đích.
- **EDD (eval-driven development) với pass@k & pass^k** (`ecc-eval-harness`, vendor từ ECC trong xboss): pass@k = ít nhất 1/k lần đúng, pass^k = cả k lần đúng — agent production cần pass^k.
- **Santa Method** (`ecc-santa-method`): 2 reviewer độc lập cùng rubric, **cả hai phải pass**; **Council** (`ecc-council`): 4 giọng Architect/Skeptic/Pragmatist/Critic trước quyết định lớn.
- **Mutation test tự viết** (xboss `scripts/mutation-check.mjs`, ~150 dòng; qlkh dùng mutmut): cố ý phá bất biến, đòi test phải đỏ — kiểm "test có cắn không" mà không cần Stryker.
- **Negative control bắt buộc + claim matrix** (Hermes-Agents `ai-eval-evidence-integrity`): mỗi tuyên bố eval gắn nhãn `real-path` / `faithful-fixture` / `asserted-not-measured`; phải có ca cố ý sai để chứng minh eval phát hiện được.
- **`verified_by` do code điền** (X-Agents): kết quả "đã làm" của agent không phải bằng chứng; chỉ trường do code/CI điền mới tính.

## Repo eval & observability nổi tiếng bổ sung (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **UKGovernmentBEIS/inspect_ai** | 3,0k | MIT | bản 0.3.278 (9/10/2026) | Do UK AI Security Institute và Meridian Labs làm; sandbox, agent, hơn 200 eval dựng sẵn; METR bỏ Vivaria để chuyển sang Inspect, Lighteval chọn làm backend ưu tiên | Vẫn 0.x, phát hành gần như hằng ngày; dành cho eval nghiên cứu, không phải giám sát production |
| **EleutherAI/lm-evaluation-harness** | 14,2k | MIT | v0.4.13 (31/8/2026), commit 14/9 | Backend của HF Open LLM Leaderboard; NVIDIA, Cohere, BigCode, Nous Research dùng nội bộ | Không có eval agent; task logprob không chạy được với API chat đóng |
| **harbor-framework/harbor** (Terminal-Bench) | 6,0k | Apache-2.0 | 11/10/2026 | Harness chạy agent trong sandbox, runner chính thức của Terminal-Bench từ 2.0 (nhóm Stanford và Laude Institute); xuất rollout cho RL/SFT | Cần Docker hoặc container cloud; Terminal-Bench đổi phiên bản nhanh (2.0 → 4.0 trong 2026) |
| **sierra-research/tau2-bench** | 2,2k | MIT | 7/10/2026 | τ²/τ³-bench: tác vụ tool–agent–người dùng (airline, retail, telecom, banking, voice), dual-control (arXiv 2506.07982); Anthropic gọi là benchmark phổ biến cho năng lực agentic | Cần một LLM đóng vai người dùng (vd. gpt-4.1) nên tốn thêm phí API |
| **comet-ml/opik** | 22,5k | Apache-2.0 | 12/10/2026 | Tracing, LLM-judge, dashboard cho app LLM/RAG/agent; bản tự host có đủ tracing và eval | Bản tự host không có quản lý người dùng |
| **mlflow/mlflow** | 28,4k | Apache-2.0 | 3.17.0 (7/10/2026) | Dự án Linux Foundation; tracing OTel, LLM judge, quản lý prompt, gateway; auto-trace hơn 60 framework | Nền tảng MLOps rộng, nặng hơn công cụ trace chuyên dụng |
| **traceloop/openllmetry** | 7,5k | Apache-2.0 | 12/10/2026 | Instrumentation GenAI chuẩn OpenTelemetry, đổ dữ liệu về backend nào cũng được | ServiceNow mua Traceloop (3/2026); chỉ là lớp instrument, cần backend riêng |
| **lmnr-ai/lmnr** (Laminar) | 3,4k | Apache-2.0 | 11/10/2026 | YC S24; trace, eval, replay debugger, dashboard SQL; trace sẵn Claude Agent SDK, AI SDK, Browser Use | Startup trẻ, ít người đóng góp |
| **open-compass/opencompass** | 7,5k | Apache-2.0 | 12/10/2026 | Shanghai AI Lab; hơn 100 dataset cho LLM/VLM, chạy leaderboard CompassRank; gộp VLMEvalKit (8/2026) | Dùng để benchmark model, không trace app |
| **huggingface/lighteval** | 2,6k | MIT | 6/10/2026 | Hàng nghìn task trên vLLM/SGLang/TGI/LiteLLM, đẩy kết quả lên Hub | Trùng nhiều với Inspect và lm-evaluation-harness |

**Nhận xét:**

- Chọn theo mục đích: **chấm model** → lm-evaluation-harness, OpenCompass hoặc Lighteval; **chấm agent** → Inspect (đa năng), Terminal-Bench qua Harbor (tác vụ terminal), τ²-bench (tool + người dùng); **trace production** → Langfuse, Opik hoặc MLflow, hay OpenLLMetry nếu đã có backend OTel.
- Cập nhật đoạn benchmark ở đầu mục: Terminal-Bench đã tới 4.0 (8/2026) và chạy bằng Harbor (`laude-institute/terminal-bench` nay chuyển hướng sang `harbor-framework/terminal-bench-1`, tức bản TB1 đã bị thay); repo `tau-bench` gốc ghi không còn cập nhật task, tau2-bench giờ phát hành τ³-bench dưới tên repo cũ; GAIA không có repo GitHub chính thức, dữ liệu nằm trên Hugging Face.
- Đã loại: METR/vivaria và METR/task-standard (archive 7/10/2026 vì METR chuyển sang Inspect), stanford-crfm/helm (chế độ bảo trì từ 1/6/2026), openai/evals (19,6k★ nhưng commit năm 2026 chỉ là ghim dependency, lần cuối 14/4), AgentOps (5,9k★, commit cuối 25/6/2026), wandb/weave (1,1k★).

## Nguồn

- Mục 23 §3.1, §4.3, §5 (X-Agents, xboss, Hermes-Agents; đọc 2026-10-12)
- https://futureagi.com/blog/best-open-source-eval-frameworks-2026/ · https://inference.net/content/llm-evaluation-tools-comparison/ · https://agentscamp.com/guides/evaluation/best-llm-eval-tools-2026 · https://aiml.qa/llm-evaluation-framework-benchmark-2026/ · https://genai.qa/blog/promptfoo-vs-deepeval-vs-ragas/ · https://techsy.io/en/blog/best-llm-evaluation-tools
- Bổ sung (12/10/2026): https://github.com/UKGovernmentBEIS/inspect_ai · https://inspect.aisi.org.uk/ · https://github.com/METR/vivaria · https://github.com/EleutherAI/lm-evaluation-harness · https://github.com/harbor-framework/harbor · https://github.com/harbor-framework/terminal-bench-1 · https://www.tbench.ai/news · https://github.com/sierra-research/tau2-bench · https://arxiv.org/abs/2506.07982 · https://github.com/comet-ml/opik · https://github.com/mlflow/mlflow · https://github.com/traceloop/openllmetry · https://www.calcalistech.com/ctechnews/article/sjghwiqf11e · https://github.com/lmnr-ai/lmnr · https://github.com/open-compass/opencompass · https://github.com/huggingface/lighteval · https://github.com/stanford-crfm/helm · https://github.com/openai/evals · https://github.com/AgentOps-AI/agentops · https://github.com/wandb/weave
