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

## Case study: Overmind — "trace production → model fine-tune riêng" (link người dùng, 2026-10-12)

> Đọc toàn bộ repo (clone đầy đủ, 82 commit), đối chiếu từng lời hứa trong README với code; nguồn ngoài do agent tra cứu cùng ngày.

### Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `overmind-core/overmind` · **632★**, 60 fork; Trendshift ghi +543★ từ 13/8 đến 12/10 (đỉnh +101★ ngày 4/10) |
| Định vị | "The Training Platform for Specialized Agents": biến trace production thành dataset → eval → tối ưu prompt/code → fine-tune LoRA → phục vụ qua một API tương thích OpenAI |
| License | Platform (`overbae/`, `frontend/`) **AGPL-3.0**; SDK/CLI (`overmind/`) **MIT**; có license thương mại từ Overmind Ltd |
| Tác giả | Overmind Ltd (London): Tyler Edwards (CEO), Sam Brunt; seed £2M ngày 11/2/2026 do Osney Capital dẫn. Tháng 2/2026 còn tự gọi là "supervision layer for AI agents", nay đổi thành nền tảng huấn luyện |
| Lịch sử | Mở mã **15/9/2026** bằng một commit gộp ("Open source Overmind"); 82 commit, khoảng 11 người; release v0.1.3 (7/10/2026); PyPI `overmind` 0.1.85, khoảng 2,9k lượt tải/tháng |
| Quy mô | Backend Django `overbae/` ~110k dòng Python, frontend ~128k dòng TS, test ~72k dòng, SDK ~16k dòng |
| Giá hosted | Free (US$50 credit, 2 lần training/tháng), Pro US$120/tháng, Enterprise |
| Đón nhận | Không có bài HN về repo; vài bài X ngày ~7/10/2026 (@omarsar0, @rohanpaul_ai) nhắc lại số liệu của hãng; một blog review tích cực (themenonlab, 5/10) |
| Trùng tên dễ nhầm | `DarthSim/overmind` (3,8k★, quản lý process Procfile/tmux), `cerebral/overmind` (1,6k★, state management JS), **overmind.tech** — công ty London khác, seed US$6M (9/2025); vài trang tổng hợp gộp nhầm hai công ty |

### Cách hoạt động

1. `pip install overmind`, `overmind init --ide <cursor|claude|opencode|codex>`, `overmind sync`: quét repo thành **đồ thị capability** (prompt, tool, task).
2. SDK gắn OpenTelemetry vào các LLM SDK đang dùng (`providers="auto"`); `overmind.run(...)` đánh dấu một lượt chạy, `run.deliver()` là output được chấm điểm. Có connector kéo trace từ Langfuse, LangSmith, Braintrust, Galileo.
3. Trace được LLM judge chấm khi tới, gom thành dataset có version → eval theo từng capability → optimiser thử prompt/tool/control flow ngay trong repo, **bản thắng là một git diff** → fine-tune LoRA trên Modal → backtest model mới bằng chính trace cũ.
4. Coding agent điều khiển toàn bộ qua MCP server (`/api/mcp/`, 34 tool) và plugin 9 skill (`/overmind finetune`, `/overmind optimise`, `/overmind backtest`…).

### Đọc cổng thật (README → code)

| Lời hứa trong README | Code thật | Kết luận |
|---|---|---|
| "Every tool declares what it costs to run (free, compute, llm, gpu) and none can delete anything" | `overbae/services/mcp/catalog.py`: `cost_class` là trường bắt buộc kiểu `Literal`; `ToolDefinition` từ chối khi `destructive=True` hoặc tên chứa `delete/remove/cancel/retry/undeploy` (trừ `retry_deployment`); tool nào cũng phải khai scope OAuth | **Cổng thật**, chạy lúc dựng catalog. Nhưng chặn theo *tên* và *cờ do tác giả tự khai*, không theo hành vi: `set_active_model`, `configure_connector` vẫn ghi đè trạng thái. Không thấy `.delete()` nào trong `services/mcp/` |
| "Membership is checked on every operation" | `project_context()` lọc `accessible_projects(context)` theo `project_id` ở mỗi lời gọi | Đúng |
| "Keys are written to git-ignored files only" | `config.py` chạy `git ls-files --error-unmatch`, từ chối nếu file đã được track, rồi tự thêm đường dẫn vào `.git/info/exclude` | Đúng — **mẫu đáng chép** cho CLI nào phải ghi key xuống repo |
| "The API refuses to start until every required key is set" | `settings.py` ném `ImproperlyConfigured` nếu thiếu 1 trong 9 biến; `FINETUNING_BACKEND` chỉ nhận `modal` | Đúng |
| "Self-hosting keeps traces and training data inside your own network" | API không khởi động nếu thiếu `OPENROUTER_API_KEY` (judge, eval, **chấm trace**, Data Workshop), token Modal (train + serve), AWS S3 (checkpoint), `HF_TOKEN` | **Sai một phần**: trace nằm trong Postgres của bạn, nhưng nội dung trace đi qua OpenRouter để chấm, dữ liệu huấn luyện lên Modal, checkpoint lên S3 |
| Tự host: "Sign in … with any email and password" | `LocalSessionView` (`AllowAny`) tạo tài khoản ở lần đầu với `email_verified=True`, rồi `claim_pending_invites()` biến mọi lời mời trùng email thành membership ("an email match is proof of ownership") | Đúng như mô tả nhưng **nguy hiểm nếu mở ra mạng**: ai tới được cổng API có thể đăng ký trước bằng email đã được mời và vào thẳng dự án đó. Thêm nữa: `docker-compose.yml` publish 5432/6379/8000/5173/3001 trên mọi interface, mật khẩu Postgres mặc định `overbae`, `SECRET_KEY` có giá trị mặc định cứng trong `settings.py`. Bản hosted dùng Clerk và `local_session` tự từ chối khi Clerk bật |
| Telemetry "anonymous … one `cli.invoked` event per CLI run … never prompts, trace contents, keys or dataset contents" | `analytics.py`: khi có API key, gọi `/api/auth/me/` rồi gửi `$identify` với id người dùng, plan, `project_id`, gộp lịch sử ẩn danh vào tài khoản; mỗi lần chạy gửi `cli.invoked` **và** `cli.completed`, trong đó `command` là **cả dòng lệnh** — chỉ che chuỗi giống secret, **không che đường dẫn/tên file**; key PostHog viết cứng nên CLI trỏ vào bản tự host vẫn gửi về PostHog của Overmind | **Không ẩn danh** (gắn với tài khoản). Không gửi nội dung trace/dataset, đúng. Tắt bằng `DO_NOT_TRACK=1` |

**Hook cho coding agent đáng học** (`.agents/hooks/guards.py`, dùng chung cho Claude Code, Codex, Cursor): mỗi rule ghi lại sự cố đã sinh ra nó (`gh pr edit` báo thành công mà không làm gì, biome `--write` làm hỏng SVG, `makemigrations --merge` làm đỏ CI); chuỗi trong dấu nháy được xoá trước khi so khớp để lệnh `grep` cụm bị cấm không bị chặn nhầm; vì Codex vẫn chạy lệnh khi hook trả `ask`, có cờ `--deny-ask` hạ thành `deny`. Họ cũng cấm trailer `Co-authored-by` trong commit.

### Đánh giá & áp dụng

- **Điểm mạnh thật:** khép trọn vòng "trace → dataset → eval → tối ưu → fine-tune → backtest" mà các công cụ ở bảng trên chỉ làm từng đoạn (Langfuse/Opik: trace + eval; DSPy: tối ưu prompt; OpenPipe ART 10,8k★: RL cho agent). `cost_class` trên từng tool MCP và quy tắc "không có tool xoá" là thiết kế tốt cho việc để agent tự lái một nền tảng tốn tiền GPU.
- **Điểm yếu:** mới mở mã 4 tuần, vẫn 0.x; số liệu chất lượng (0,12% so với 3,36% trích dẫn bịa; ít "phantom clause" hơn 20–30 lần với Qwen3.5-9B) là số tự công bố **(chưa xác minh)**; tự host vẫn phụ thuộc OpenRouter + Modal + S3; platform AGPL.
- **Nếu dùng:** thử bản hosted với dữ liệu không nhạy cảm; nếu tự host thì chỉ chạy sau localhost/VPN, đổi `DJANGO_SECRET_KEY` và mật khẩu Postgres, bỏ publish cổng 5432/6379, không mời thành viên bằng email trên bản mở ra mạng, đặt `DO_NOT_TRACK=1` cho SDK/CLI.

## Nguồn

- Mục 23 §3.1, §4.3, §5 (X-Agents, xboss, Hermes-Agents; đọc 2026-10-12)
- https://futureagi.com/blog/best-open-source-eval-frameworks-2026/ · https://inference.net/content/llm-evaluation-tools-comparison/ · https://agentscamp.com/guides/evaluation/best-llm-eval-tools-2026 · https://aiml.qa/llm-evaluation-framework-benchmark-2026/ · https://genai.qa/blog/promptfoo-vs-deepeval-vs-ragas/ · https://techsy.io/en/blog/best-llm-evaluation-tools
- Bổ sung (12/10/2026): https://github.com/UKGovernmentBEIS/inspect_ai · https://inspect.aisi.org.uk/ · https://github.com/METR/vivaria · https://github.com/EleutherAI/lm-evaluation-harness · https://github.com/harbor-framework/harbor · https://github.com/harbor-framework/terminal-bench-1 · https://www.tbench.ai/news · https://github.com/sierra-research/tau2-bench · https://arxiv.org/abs/2506.07982 · https://github.com/comet-ml/opik · https://github.com/mlflow/mlflow · https://github.com/traceloop/openllmetry · https://www.calcalistech.com/ctechnews/article/sjghwiqf11e · https://github.com/lmnr-ai/lmnr · https://github.com/open-compass/opencompass · https://github.com/huggingface/lighteval · https://github.com/stanford-crfm/helm · https://github.com/openai/evals · https://github.com/AgentOps-AI/agentops · https://github.com/wandb/weave
- Case study Overmind (12/10/2026): https://github.com/overmind-core/overmind (clone đầy đủ: README.md, .env.example, docker-compose.yml, overbae/settings.py, overbae/api/auth_registration.py, overbae/services/project_invites.py, overbae/services/mcp/{catalog,context}.py, overmind/overmind/{analytics,config}.py, .agents/hooks/guards.py, .claude/settings.json) · https://github.com/overmind-core/overmind/releases · https://pypi.org/project/overmind/ · https://pypistats.org/packages/overmind · https://trendshift.io/repositories/274765 · https://overmindlab.ai/pricing · https://overmindlab.ai/about · https://tech.eu/2026/02/11/overmind-launches-with-2m-in-seed-funding-to-support-development-of-agentic-ai/ · https://osneycapital.com/portfolio/overmind · https://digg.com/ai/fj6px48f · https://themenonlab.blog/blog/overmind-training-platform-specialized-agents · https://www.opensourcealternatives.to/item/overmind · https://github.com/OpenPipe/ART · https://github.com/DarthSim/overmind · https://github.com/cerebral/overmind · https://github.com/overmindtech/cli · https://startupintros.com/news/2025-09-01-overmind-seed
