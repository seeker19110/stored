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

## Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại số sao, license, ngày push của mọi repo mục 07 trong catalog bằng GitHub search API (31/10/2026); repo search trả "không tồn tại" thì tìm theo tên để phát hiện đổi chủ. (2) Tìm repo lớn còn thiếu bằng 8 truy vấn (topic `llmops`, `llm-evaluation`, `llm-observability`; từ khoá "llm evaluation", "llm observability", "agent tracing opentelemetry", "agent evaluation benchmark", repo eval tạo sau 1/10/2025). Chọn **6 repo**, clone `--filter=blob:none` đủ lịch sử, đọc LICENSE, cấu trúc, CI, file telemetry. **Không cài, không chạy script nào.**

### Repo cũ: điều đã đổi

| Repo | Thay đổi (12/10 → 31/10/2026) | Hệ quả |
|---|---|---|
| `explodinggradients/ragas` | **Đã chuyển sang `vibrantlabsai/ragas`** (16,2k★, Apache-2.0); **commit cuối 23/2/2026**, hơn 8 tháng không commit | "Stack miễn phí gợi ý" đầu mục nên dùng DeepEval làm chính, Ragas chỉ khi cần đúng metric RAG của nó; catalog đổi trường `repo` |
| `langfuse/langfuse` · `promptfoo/promptfoo` · `confident-ai/deepeval` · `Arize-ai/phoenix` | Bảng đầu chưa có số → **36,8k · 26,7k · 19,2k · 12,1k**, đều push 29–31/10 | Bổ sung số. Langfuse và Phoenix hiện `NOASSERTION` vì MIT + `ee/` và Elastic License 2.0, đúng như bảng |
| `harbor-framework/harbor` | 6,0k → **6,7k** (+11%) | Terminal-Bench tiếp tục kéo người dùng |
| `overmind-core/overmind` | 632 → **737** (+17%) | Case study bên trên vẫn đúng |
| `EleutherAI/lm-evaluation-harness` | 14,2k → 14,4k; **push cuối vẫn 14/9/2026** | Bảy tuần đứng yên; vẫn là chuẩn chấm model |
| `traceloop/openllmetry` | Push cuối 19/10/2026 | Bình thường sau thương vụ ServiceNow |
| `OpenPipe/ART` | Catalog để trống license → GitHub: **Apache-2.0** | Catalog bổ sung license |
| `ifixai-ai/iFixAi` | Catalog xếp mục 07 (41,4k★) nhưng README mục này không có hồ sơ; đánh giá nằm ở mục 08 (sao lệch so với lượt tải PyPI) | Giữ cảnh báo của mục 08 |
| Inspect, Opik, MLflow, Laminar, OpenCompass, Lighteval, tau2-bench | Dao động 1–8% | Không đổi nhận định |

### Bảng nhanh 6 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `evidentlyai/evidently` | Eval + giám sát ML/LLM | 8,0k · Apache-2.0 | 11/9/2026 | 100+ metric, test, dashboard tự host cho dữ liệu, model và LLM | **Telemetry qua HTTP thường tới IP trần**; nhịp chậm |
| `Giskard-AI/giskard-oss` | Test + quét lỗ hổng agent | 5,9k · Apache-2.0 | 29/10/2026 | v3 viết lại: checks, scan, kịch bản nhiều lượt | v2 không còn bảo trì; cần Python 3.12+ |
| `langwatch/langwatch` | Trace + eval + gateway | 5,0k · Apache-2.0 (+ `enterprise/` riêng) | 31/10/2026 | Trace, simulation test agent, AI gateway, theo dõi coding agent | Nhịp commit cực cao, 12% có trailer Claude |
| `pydantic/logfire` | Observability (SDK) | 4,5k · MIT (SDK) | 30/10/2026 | SDK Python bọc OpenTelemetry, che secret mặc định | **Backend đóng mã** |
| `coze-dev/coze-loop` | Prompt + eval + trace | 5,8k · Apache-2.0 | 29/10/2026 | Bản mở của Coze Loop (ByteDance): playground prompt, bộ eval, trace | Mặc định dùng Volcengine Ark |
| `FailproofAI/failproofai` | Trace + chặn tool call cho harness | 7,1k · **MIT + Commons Clause** | 27/10/2026 | Hook 12 harness (Claude Code, Codex…), 40 policy dựng sẵn | Không phải OSI; telemetry bật sẵn |

### Hồ sơ từng repo

- **Evidently.** 2.798 commit từ 11/2020, 112 tác giả; chỉ 8 commit từ 1/5/2026 và 85 commit trong 12 tháng, bản v0.7.22 (10/9/2026) — **đang chậm lại rõ**. Phủ cả ML cổ điển (drift, data quality) lẫn LLM (descriptor, LLM judge, guardrail). Telemetry (`src/evidently/telemetry.py`, `ui/service/components/telemetry.py`) dùng `iterative_telemetry`, gửi tới **`http://35.232.253.5:8000`** (không TLS, địa chỉ IP trần), bật mặc định, tắt bằng `DO_NOT_TRACK`; README không nhắc tới telemetry ⚠️. Cài: `pip install evidently` và đặt `DO_NOT_TRACK=1`.
- **Giskard (v3).** 10.786 commit từ 3/2022, 131 tác giả. Viết lại thành 5 gói nhỏ (`giskard-checks`, `-scan`, `-agents`, `-llm`, `-core`); README ghi v2 "no longer actively maintained". Telemetry PostHog EU, key viết cứng; tắt bằng `DO_NOT_TRACK=1` hoặc `GISKARD_TELEMETRY_DISABLED=1`. README hứa "No prompts or outputs are sent": decorator trong `giskard-core` chỉ gửi tên loại exception ✅, nhưng hàm `telemetry_capture` chuyển nguyên `properties` của nơi gọi, chưa kiểm hết các nơi gọi **(chưa xác minh trọn)**. CI có `zizmor` (quét bảo mật GitHub Actions) và `.secrets.baseline`. Cài: `pip install "giskard[scan]"`.
- **LangWatch.** 7.308 commit từ 9/2023, 49 tác giả, 2.648 commit từ 1/5/2026; 12% commit có trailer Claude. Apache-2.0 cho lõi; `NOTICE` liệt kê `enterprise/` theo LangWatch Enterprise License, SDK và MCP là MIT. Ngoài trace/eval còn có **simulation test cho agent** (kể cả voice), AI gateway với virtual key và ngân sách, và mảng "AI governance" kéo dữ liệu từ Copilot Studio, compliance API của Anthropic/OpenAI. Lệnh `npx langwatch claude` gắn trace cho Claude Code; dữ liệu nào được gửi đi **chưa xác minh**. Tự host: `npx @langwatch/server` (cần Node 24). Lời "giúp quota tuần dùng lâu gấp đôi" là quảng cáo, không kiểm được.
- **Logfire.** 2.241 commit, 170 tác giả. README nói rõ: repo chỉ chứa SDK Python và docs, **"the server application… is closed source"**. Điểm đáng học: `logfire-sdk/logfire/_internal/scrubbing.py` **che giá trị nhạy cảm mặc định** theo mẫu `password`, `secret`, `auth`, `api key`, `session`, `cookie`… trước khi gửi span, có danh sách ngoại lệ cho id phiên agent và test riêng (`tests/test_secret_scrubbing.py`) ✅. Cài: `pip install logfire` rồi `logfire auth`. Chỉ dùng được với dịch vụ Pydantic hoặc bản tự host trả phí.
- **Coze Loop.** 417 commit từ 6/2025, 49 tác giả, Go + TypeScript; 13% commit có trailer Claude. Tag mới nhất v1.5.1 (20/1/2026) nhưng commit vẫn đều (sandbox eval trên Windows 29/10). Compose để mật khẩu MySQL/Redis/ClickHouse/OSS qua biến môi trường, không ghi cứng ✅; cấu hình model mẫu là Volcengine Ark. Bẫy đáng ghi: workflow `ai-cr-required.yaml` (bắt buộc bot "CozeLoop" review trước khi merge) đã **bị tắt lặng lẽ** bằng cách đổi nhánh kích hoạt thành `disabled-temporarily`; workflow vẫn nằm đó nên đọc lướt dễ tưởng cổng còn chạy.
- **FailproofAI.** 746 commit, tạo 6/4/2026 (Exosphere Host Inc), 18 tác giả, 38% commit có trailer Claude; tăng lên 7,1k★ trong ~7 tháng. LICENSE là **MIT + Commons Clause** (cấm bán dịch vụ dựa trên phần mềm), nên GitHub báo `NOASSERTION` và đây không phải mã nguồn mở theo OSI. Lời "40 built-in policies" khớp `src/hooks/policy-catalog.ts` (40 mục) ✅; "Runs locally" đúng cho phần chặn, nhưng **telemetry PostHog bật mặc định** (`lib/telemetry-enabled.ts`, key trong `src/posthog-key.ts`), tắt bằng `FAILPROOFAI_TELEMETRY_DISABLED=1`; README không nhắc tới ⚠️. Có `osv-scanner` trong CI và submodule `skills`. Cài: `npm install -g failproofai`. Liên quan mục 12 (guardrail) và mục 03 (hook).

### Mẫu chung rút ra

1. **Eval và observability đang gộp vào một nền tảng** có thêm gateway và chính sách (LangWatch, FailproofAI, Coze Loop); khi chọn, tách rõ phần cần (trace, eval, chặn) để khỏi kéo cả nền tảng.
2. **Telemetry của chính công cụ observability ít minh bạch:** Evidently gửi qua HTTP tới IP trần, FailproofAI và Evidently không nhắc trong README, Giskard và FailproofAI viết cứng key PostHog. Đặt `DO_NOT_TRACK=1` cùng biến riêng từng công cụ trong CI.
3. **Che secret ở phía SDK trước khi gửi** (Logfire) là mặc định nên có cho mọi lớp trace, kể cả tự viết.
4. **Cổng CI có thể chết mà không ai thấy** (Coze Loop đổi nhánh kích hoạt). Cần kiểm định kỳ rằng các check bắt buộc thật sự chạy trên nhánh chính.
5. **Repo đổi chủ/đứng yên lặng lẽ:** Ragas đổi tổ chức và dừng 8 tháng mà README không báo. Rà catalog bằng API định kỳ là cách duy nhất phát hiện.

**Nguồn (31/10/2026):** GitHub search API (`repo:` cho repo cũ; `ragas in:name`; 8 truy vấn topic/từ khoá) · clone nông vibrantlabsai/ragas (log 5 commit, README.md) · clone `--filter=blob:none`: evidently (LICENSE, README.md, `src/evidently/telemetry.py`, `src/evidently/ui/service/components/telemetry.py`, `git log`), giskard-oss (README.md, LICENSE, `libs/giskard-core/src/giskard/core/telemetry/telemetry.py`, workflows), langwatch (LICENSE.md, NOTICE, README.md, `enterprise/`), logfire (README.md, LICENSE, `logfire-sdk/logfire/_internal/scrubbing.py`, `tests/test_secret_scrubbing.py`), coze-loop (README.md, LICENSE, `.github/workflows/ai-cr-required.yaml`, `release/deployment/docker-compose/docker-compose.yml`), failproofai (LICENSE, README.md, .gitmodules, `lib/telemetry-enabled.ts`, `src/posthog-key.ts`, `src/hooks/{builtin-policies,policy-catalog}.ts`)

## Nâng trần 2/11/2026: chuẩn trace GenAI, kiểm tuân thủ trace bằng máy, bộ eval có version và chọn judge có số đo (yêu cầu người dùng)

> Cách làm: grep `data/projects.json` theo `repo` để loại trùng; GitHub search API (`repo:` gộp nhiều repo một truy vấn) lấy sao, license, ngày push 2/11/2026; clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, spec/manifest, CI. **Không cài, không chạy.** Loại `prometheus-eval/prometheus-eval` (1,1k★, push cuối 25/4/2025) và `ScalerLab/JudgeBench` (133★, không có license, đứng từ 11/2024) vì đã dừng.

**Trần hiện tại:**

- Mục đã đủ công cụ trace/eval (Langfuse, Opik, MLflow, Phoenix, Promptfoo, DeepEval, Inspect) nhưng **chưa có chuẩn dữ liệu trace**: OpenLLMetry được nhắc là "chuẩn OTel" mà không chỉ tới bản đặc tả nào, ở trạng thái nào.
- Không có **cổng máy kiểm trace đúng chuẩn**: "đổi backend dễ" chỉ là tuyên bố cho tới khi có công cụ xác minh span thật.
- LLM-as-judge được dùng khắp nơi (Opik, Overmind, Evidently) nhưng **chưa có bước chọn judge bằng số đo**; mẫu "negative control" ở phần mẫu eval (mục 23) mới dừng ở quy ước.
- Bộ eval dựng sẵn (Inspect, lm-evaluation-harness) có nhắc, nhưng chưa có **quy ước version task** để kết quả hai lần chạy so được với nhau.

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `open-telemetry/semantic-conventions-genai` | Chuẩn | 506 · Apache-2.0 | 2/11/2026 | **Chuẩn GenAI của OTel đã tách khỏi repo semconv chính**: `docs/gen-ai/README.md` ở repo cũ ghi "Moved… no longer maintained". Repo mới gồm span client/agent/MCP/A2A, metric token, event, trang riêng cho Anthropic, OpenAI, Bedrock; model YAML quản bằng Weaver. Nội dung (`gen_ai.input.messages`, `gen_ai.output.messages`, `gen_ai.system_instructions`, `gen_ai.memory.records`) là **`Opt-In`**: "SHOULD NOT capture… by default" | Mọi thuộc tính vẫn **Development**, `README.md` để "Schema URL: TODO", CHANGELOG chưa có bản phát hành: tên thuộc tính còn đổi được. Link cũ trong bài tổng hợp trỏ vào trang đã ngừng cập nhật |
| `open-telemetry/weaver` | Cổng máy | 521 · Apache-2.0 | 1/11/2026 | `weaver registry live-check` nhận luồng OTLP và chấm mức tuân thủ so với registry; có GitHub Action `weaver-live-check-start/stop` đặt **ngưỡng severity làm CI fail**. Repo GenAI dùng nó để chạy `reference/`: 30 kịch bản (anthropic, openai, claude-agent-sdk, langchain, crewai, deepeval…) trên mock server tất định, sinh bảng ai hỗ trợ thuộc tính nào | Bản 0.x; live-check cần app phát trace thật trong CI |
| `Arize-ai/openinference` | Chuẩn (thứ hai) | 1,3k · Apache-2.0 | 2/11/2026 | Đặc tả trong `spec/` (LLM, embedding, tool calling, retrieval, annotation) và gói instrument cho khoảng 38 thư viện Python, 15 gói JS; là định dạng gốc của Phoenix (bảng đầu mục). `spec/configuration.md` định nghĩa biến `OPENINFERENCE_HIDE_INPUTS/OUTPUTS/…` để che nội dung | **Mặc định ghi nội dung** (mọi biến HIDE mặc định `False`), ngược với Opt-In của OTel GenAI. Gói `openinference-genai` chỉ chuyển "best effort" một phần thuộc tính OTel GenAI, README tự ghi theo định nghĩa 10/2025 |
| `openlit/openlit` | Đầu bảng (OTel-native) | 2,9k · Apache-2.0 | 22/10/2026 | SDK + nền tảng tự host phát thẳng `gen_ai.*` của OTel, đổ về Collector hay backend OTel bất kỳ; thêm eval, guardrail, giá, GPU collector, trace coding agent | `openlit.init(capture_message_content=True)` **ghi nội dung mặc định**, trái khuyến nghị Opt-In; `docker-compose.yml` đặt `TELEMETRY_ENABLED: "true"`, client có PostHog (`src/client/src/constants/posthog.ts`) |
| `UKGovernmentBEIS/inspect_evals` | Cổng máy (bộ eval) | 732 · MIT | 2/11/2026 | Hơn 200 task cho Inspect (đã có ở bảng bổ sung). Đáng chép: `TASK_VERSIONING.md` buộc mỗi task có version `N-X` (N tăng khi kết quả **không còn so được**, X khi đổi giao diện); `EVALUATION_CHECKLIST.md` đòi `VALIDITY_REPORT.md` (tên, dữ liệu, cách chấm có hợp lệ) và phân tích trajectory trước khi nhận eval | README: nay do **Generality Labs** (nonprofit London) bảo trì, chỉ nhận PR từ người được duyệt trước; thêm eval mới chuyển sang "Inspect Evals Register" từ 5/2026 |
| `allenai/reward-bench` | Cổng máy (chọn judge) | 748 · Apache-2.0 | 14/10/2026 | RewardBench 2 (arXiv 2506.01937): chấm reward model **và judge sinh văn bản** (`pip install rewardbench[generative]`, `scripts/run_generative_v2.py`, chế độ xếp hạng 4 câu hoặc chấm điểm từng câu). Dùng để chọn model judge bằng độ chính xác đo được thay vì theo cảm tính | Đo năng lực judge chung (factuality, focus, math, safety, ties), không thay việc hiệu chỉnh judge trên nhãn người của chính dự án |

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. **Ghim chuẩn trace:** instrument theo `gen_ai.*` của semantic-conventions-genai (qua OpenLLMetry, OpenLIT hoặc SDK của backend), ghi rõ commit đặc tả đang theo vì vẫn ở Development. Nội dung prompt/output **tắt mặc định**; nếu dùng OpenInference hay OpenLIT thì đặt `OPENINFERENCE_HIDE_INPUTS/OUTPUTS=true` hoặc `capture_message_content=False`, rồi che secret như Logfire (§ Nâng cấp 31/10).
2. **Cổng tuân thủ trace trong CI:** chạy test tích hợp với mock model tất định, bật `weaver registry live-check` (Action start/stop, fail theo severity). Đây là bằng chứng máy cho lời "đổi backend Langfuse ↔ Phoenix ↔ MLflow được".
3. **Eval tất định trước, judge sau:** assertion tất định của Promptfoo/DeepEval (khớp schema, regex, tool call đúng tên/tham số) chạy ở mọi PR; LLM-judge chỉ cho tiêu chí mềm, kèm record/replay và negative control (phần mẫu eval mục 23).
4. **Hiệu chỉnh judge:** chọn model judge theo RewardBench 2; rồi gán nhãn người cho 50–200 mẫu của chính dự án, đo mức đồng thuận judge–người (vd. Cohen's kappa) và chỉ cho judge làm cổng khi đạt ngưỡng; lặp lại khi đổi model judge hay prompt chấm. Cỡ mẫu và ngưỡng là đề xuất của kho **(chưa xác minh bằng nguồn chuẩn)**.
5. **Version task eval:** áp quy ước `N-X` của inspect_evals cho bộ eval nội bộ; chỉ so điểm giữa các lần chạy có cùng `N`.

**Nguồn §Nâng trần 2/11/2026:** GitHub search API 2/11/2026 (`repo:` gộp) · `data/projects.json` (grep `repo`) · clone `--depth 1 --filter=blob:none`: open-telemetry/semantic-conventions (HEAD fb30ca1, 1/11/2026; `docs/gen-ai/README.md`), open-telemetry/semantic-conventions-genai (HEAD 16f3130, 2/11/2026; README.md, CHANGELOG.md, versions.env, `docs/gen-ai/{gen-ai-spans,gen-ai-agent-spans,mcp}.md`, `reference/README.md`, `reference/scenarios/`), open-telemetry/weaver (HEAD 8ed44ad, 1/11/2026; README.md, `docs/usage.md`), Arize-ai/openinference (HEAD 5c68f3a, 1/11/2026; LICENSE, README.md, `spec/configuration.md`, `python/instrumentation/`, `js/packages/openinference-genai/README.md`), openlit/openlit (HEAD 1ed8bb7, 22/10/2026; LICENSE, README.md, docker-compose.yml, `sdk/python/src/openlit/__init__.py`), UKGovernmentBEIS/inspect_evals (HEAD ca99b73, 2/11/2026; LICENSE, README.md, EVALUATION_CHECKLIST.md, TASK_VERSIONING.md, `.github/workflows/`), allenai/reward-bench (HEAD 59f6ff7, 14/10/2026; LICENSE, README.md, `scripts/`), prometheus-eval/prometheus-eval (HEAD dcfb442, 24/4/2025; loại) · https://github.com/open-telemetry/semantic-conventions-genai · https://github.com/open-telemetry/weaver · https://github.com/Arize-ai/openinference · https://github.com/openlit/openlit · https://github.com/UKGovernmentBEIS/inspect_evals · https://github.com/allenai/reward-bench · https://arxiv.org/abs/2506.01937

<a id="core-eval-validity"></a>

## Nâng trần 2/11/2026: đơn vị đo, lặp độc lập và hiệu lực của kết luận (mở rộng cùng ngày)

> Mở rộng chiều sâu trong cùng đợt 2/11/2026, không phải công bố các repo vừa ra mắt. Hai repo dưới đã có trong catalog: đọc lại LICENSE, CI và nhánh mặc định bằng clone chỉ đọc; SHA đối chiếu GitHub API. Mức bằng chứng **code-read**; không chạy/build repo ngoài, hiệu năng và hành vi thực tế **(chưa xác minh)**. Số sao/trạng thái đọc 2026-11-02; ngày commit tính theo UTC, tách khỏi `pushed_at`.

| Repo đã có | ★ · license (2026-11-02) | HEAD nhánh mặc định | Vai trò đọc sâu |
|---|---|---|---|
| `UKGovernmentBEIS/inspect_ai` | 3.153 · MIT | 2026-11-01 · `1f1a0039` | Epoch. cache và uncertainty theo đúng đơn vị mẫu |
| `promptfoo/promptfoo` | 26.736 · MIT | 2026-11-02 · `bfb96e2e` | Cache namespace cho repeat. assertion và hồi quy CI |

**Trần còn thiếu:** phần nâng trần trước đã có task version, judge calibration và trace conformance. Bước tiếp theo là chống kết luận sai từ **điểm trung bình, lần gọi đã cache, nhiều câu cùng hội thoại** hoặc chọn prompt bằng chính tập test.

### Inspect AI: số dòng kết quả không bằng số mẫu độc lập

- [`CachePolicy.per_epoch=True`](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/model/_cache.py#L109) tách cache theo epoch; epoch là thành phần cache key khi policy này bật. Nếu chủ ý bỏ epoch khỏi cache, phải ghi rõ: không được diễn giải việc dùng lại cùng output là nhiều lần sinh độc lập.
- [`std.py`](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/scorer/_metrics/std.py) có `stderr`, bootstrap, `ci` kiểu t/bootstrap và clustering theo metadata. Khi nhiều câu thuộc một tài liệu/hội thoại/user, cluster theo đơn vị đó thay vì giả định mỗi dòng độc lập. Với quá ít cluster, khoảng ước lượng không đủ để xếp hạng đáng tin; ghi số cluster và kiểm phân phối.
- Task/epoch reduction thay đổi mẫu mà metric nhận; phải ghi rõ đo theo **attempt, sample hay episode**, cách gộp epoch và cách xử lý unscored/error. CI kiểm framework không kiểm tính đúng đắn khoa học của một scorer tự viết. Mức tăng 1–2 điểm cần khoảng bất định và phân tích lỗi, không tự gán ý nghĩa thống kê.

### Promptfoo: repeat có namespace, nhưng chạy lại vẫn có thể dùng cache

- [`getRepeatCacheNamespace`](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/src/evaluator.ts#L474) tách `repeat:N`; [test repeat cache](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/test/evaluator/repeatCache.test.ts) chứng minh hai repeat được phân biệt nhưng **lần eval tiếp theo vẫn lấy lại output đã cache**. Đây là tính năng tái lập, không phải bug. Khi cần đo biến thiên mới, dùng `--no-cache` và kiểm provider/custom wrapper có thực sự gọi mới.
- Tách assertion tất định (schema/tool/regex/ground truth) khỏi judge. Giữ cùng input và cấu hình khi so baseline/candidate; lần chạy dùng cache là cổng hồi quy, lần sinh mới là thí nghiệm độ ổn định. Ghi model ID, seed/temperature nếu hỗ trợ, cache policy, repeat, lỗi và giá.
- [`telemetry.ts`](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/src/telemetry.ts#L22) có đường tắt `PROMPTFOO_DISABLE_TELEMETRY=1`; tắt telemetry không tự tắt provider call/remote grader. [CI](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/.github/workflows/main.yml) gồm ma trận Node/OS và test evaluator; chưa chạy các job đó trong đợt đọc này.

**Ma trận thiết kế phép đo**

| Câu hỏi | Đơn vị và cổng nên dùng | Sai lệch cần kiểm |
|---|---|---|
| Prompt mới có làm hỏng ca cũ? | Tập regression cố định + assertion; cache cho replay | Grader/model/version thay mà baseline giữ nguyên |
| Model có ổn định khi sinh mới? | Repeat/epoch tách cache; báo phân phối | Tính cùng output cache như lần thử độc lập |
| Tốt hơn trên dữ liệu thật? | Holdout theo user/tài liệu/thời gian; so cặp cùng mẫu | Train–test leakage, nhiều câu cùng episode |
| Judge có đáng tin? | Nhãn người, negative control, đo đồng thuận | Judge cùng model hoặc thấy tên phương án |
| Tăng chất lượng có đáng chi phí? | Chất lượng kèm token/$/p95 và lỗi | Chỉ báo điểm của những run thành công |

**Cách ghép:** (1) khoá dataset/task/scorer/model version và đơn vị mẫu; (2) tách development/validation/final test, chia theo nguồn để giảm rò rỉ; (3) chạy baseline/candidate trên cùng mẫu, assertion trước judge; (4) một run replay cho CI và một run sinh mới khi cần đo độ ổn định; (5) báo điểm, uncertainty/cluster, error/unscored, chi phí và nhóm ca thua. Không diễn giải hai CI giao nhau/không giao nhau như một phép kiểm so sánh cặp đầy đủ; muốn kết luận khác biệt cần phương pháp phù hợp và cỡ mẫu đã xác định. Đây là thiết kế đề xuất, chưa có số benchmark mới trong kho.

**Nguồn phần mở rộng:** [1](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/LICENSE) · [2](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/model/_cache.py) · [3](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/scorer/_metrics/std.py) · [4](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/src/inspect_ai/scorer/_metrics/aggregate.py) · [5](https://github.com/UKGovernmentBEIS/inspect_ai/blob/1f1a0039d49c628a41898a7a7ba4843c5bbbc91b/.github/workflows/pr-gate.yml) · [6](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/LICENSE) · [7](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/src/evaluator.ts) · [8](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/test/evaluator/repeatCache.test.ts) · [9](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/src/telemetry.ts) · [10](https://github.com/promptfoo/promptfoo/blob/bfb96e2ee2304ec87a7a32054a4907ea39f5c920/.github/workflows/main.yml) · [11](https://inspect.aisi.org.uk/metrics.html) · [12](https://inspect.aisi.org.uk/caching.html) · [13](https://www.promptfoo.dev/docs/usage/command-line/)

## Nguồn

- Mục 23 §3.1, §4.3, §5 (X-Agents, xboss, Hermes-Agents; đọc 2026-10-12)
- https://futureagi.com/blog/best-open-source-eval-frameworks-2026/ · https://inference.net/content/llm-evaluation-tools-comparison/ · https://agentscamp.com/guides/evaluation/best-llm-eval-tools-2026 · https://aiml.qa/llm-evaluation-framework-benchmark-2026/ · https://genai.qa/blog/promptfoo-vs-deepeval-vs-ragas/ · https://techsy.io/en/blog/best-llm-evaluation-tools
- Bổ sung (12/10/2026): https://github.com/UKGovernmentBEIS/inspect_ai · https://inspect.aisi.org.uk/ · https://github.com/METR/vivaria · https://github.com/EleutherAI/lm-evaluation-harness · https://github.com/harbor-framework/harbor · https://github.com/harbor-framework/terminal-bench-1 · https://www.tbench.ai/news · https://github.com/sierra-research/tau2-bench · https://arxiv.org/abs/2506.07982 · https://github.com/comet-ml/opik · https://github.com/mlflow/mlflow · https://github.com/traceloop/openllmetry · https://www.calcalistech.com/ctechnews/article/sjghwiqf11e · https://github.com/lmnr-ai/lmnr · https://github.com/open-compass/opencompass · https://github.com/huggingface/lighteval · https://github.com/stanford-crfm/helm · https://github.com/openai/evals · https://github.com/AgentOps-AI/agentops · https://github.com/wandb/weave
- Case study Overmind (12/10/2026): https://github.com/overmind-core/overmind (clone đầy đủ: README.md, .env.example, docker-compose.yml, overbae/settings.py, overbae/api/auth_registration.py, overbae/services/project_invites.py, overbae/services/mcp/{catalog,context}.py, overmind/overmind/{analytics,config}.py, .agents/hooks/guards.py, .claude/settings.json) · https://github.com/overmind-core/overmind/releases · https://pypi.org/project/overmind/ · https://pypistats.org/packages/overmind · https://trendshift.io/repositories/274765 · https://overmindlab.ai/pricing · https://overmindlab.ai/about · https://tech.eu/2026/02/11/overmind-launches-with-2m-in-seed-funding-to-support-development-of-agentic-ai/ · https://osneycapital.com/portfolio/overmind · https://digg.com/ai/fj6px48f · https://themenonlab.blog/blog/overmind-training-platform-specialized-agents · https://www.opensourcealternatives.to/item/overmind · https://github.com/OpenPipe/ART · https://github.com/DarthSim/overmind · https://github.com/cerebral/overmind · https://github.com/overmindtech/cli · https://startupintros.com/news/2025-09-01-overmind-seed
