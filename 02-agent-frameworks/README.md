# 02 · Agent Frameworks & LLM Orchestration

> Thư viện để xây agent/multi-agent và ứng dụng LLM. Số sao ước lượng 8–10/2026.

## 1. Bảng tổng hợp

| Framework | Repo | Ngôn ngữ | ★ (ước lượng) | Mô hình tư duy | Khi nào dùng |
|---|---|---|---|---|---|
| **LangChain** | langchain-ai/langchain | Py/TS | ~130k | Chuỗi, tool, retriever; hệ sinh thái lớn nhất | Prototype nhanh, nhiều tích hợp |
| **LangGraph** | langchain-ai/langgraph | Py/TS | ~40k · **34.5M tải/tháng** | Đồ thị trạng thái (state graph), checkpoint, human-in-the-loop | Agent production cần kiểm soát luồng, durable |
| **AutoGen → Microsoft Agent Framework** | microsoft/autogen · microsoft/agent-framework | Py/.NET | ~60k (AutoGen, maintenance) | Hội thoại đa agent; hợp nhất AutoGen + Semantic Kernel, GA 1.0 4/2026 | Doanh nghiệp .NET/Azure |
| **CrewAI** | crewAIInc/crewAI | Py | ~57k · 5.2M tải/tháng | Vai trò (role) + nhiệm vụ + crew | Đội agent theo vai trò, dễ lên |
| **OpenAI Agents SDK** | openai/openai-agents-python | Py/TS | ~29k · 10.3M tải/tháng | Agents, handoffs, guardrails, tracing | Dùng OpenAI/Responses API |
| **LlamaIndex** | run-llama/llama_index | Py/TS | ~48k | Data framework (RAG), workflows | RAG trên dữ liệu doanh nghiệp |
| **Semantic Kernel** | microsoft/semantic-kernel | .NET/Py/Java | ~28k | Plugins, planners | Đang hợp vào Agent Framework |
| **smolagents** | huggingface/smolagents | Py | ~26k | Code-agent tối giản (agent viết Python để hành động) | Nhẹ, HF ecosystem |
| **Haystack** | deepset-ai/haystack | Py | ~20k | Pipeline component hóa | RAG/search production |
| **PydanticAI** | pydantic/pydantic-ai | Py | ~16k | Typed, dependency injection, validation | Team ưa type-safety |
| **Google ADK** | google/adk-python | Py/Java | – | Agent Development Kit, A2A native | Gemini/Vertex |
| **Mastra** | mastra-ai/mastra | TS | – | Agent framework TS, workflows, evals | Next.js/TS stack |
| **OpenClaw** | openclaw/openclaw | TS | **~390k** | Trợ lý cá nhân tự host, nối Discord/Slack/Telegram/WhatsApp, skills module | Agent cá nhân; tác giả Peter Steinberger gia nhập OpenAI 2/2026, dự án về foundation độc lập |
| **Hermes Agent** | NousResearch/hermes-agent | Py | – | Agent mã mở chạy CLI/TUI/Electron + gateway Telegram/Discord/Slack/WhatsApp + ACP cho IDE; skills tự học, memory, `delegate_task` (≤10 con, **không lồng**), kanban, cron, webhook, plugin model-provider | Chủ kho dùng thật (mục 23 §5): provider Antigravity/`claude -p`/Codex CLI, 112 skill; docs `llms.txt` |
| **MetaGPT** | FoundationAgents/MetaGPT | Py | ~70,8k (trang GitHub 12/10/2026) | "Công ty phần mềm" đa vai trò: SOP → PRD/design/code; MGX | Khung "công ty AI" đầu tiên |
| **ChatDev** | OpenBMB/ChatDev | Py | ~34,5k (12/10/2026) | Chat-chain giữa các vai trò CEO/CTO/dev/tester | Nghiên cứu, nhỏ gọn |
| **DeerFlow** | bytedance/deer-flow | Py/TS | ~83,7k (12/10/2026) | Deep research đa agent trên LangGraph, planner + coordinator | X-Agents đối chiếu (mục 23 §3.1) |
| **AG2** (ex-AutoGen fork) | ag2ai/ag2 | Py | – | Fork cộng đồng của AutoGen 0.2 | Tách khỏi Microsoft 11/2024 |
| **CAMEL** | camel-ai/camel | Py | ~13k (nt.) | Role-playing agent, data gen, OWL | Học thuật |
| **agency-swarm** | VRSEN/agency-swarm | Py | – | Agency = agent có vai trò + luồng giao tiếp định nghĩa sẵn | Trên OpenAI Assistants/Agents SDK |
| **gpt-pilot** | Pythagora-io/gpt-pilot | Py/TS | ~33,6k (12/10/2026) | Dev AI theo bước, hỏi người khi kẹt | **Ngừng bảo trì**; cảnh báo mã độc trong `core/telemetry/` (8/2025–6/2026) **(chưa xác minh)** |
| **ruflo** (claude-flow) | ruvnet/ruflo | TS | – | Swarm orchestration cho Claude Code, hive-mind, MCP tools | Nhiều tuyên bố hiệu năng **chưa kiểm chứng** |
| **Paperclip** | paperclipai/paperclip | TS | ~100,5k (12/10/2026) | "Quản lý agent như nhân viên": org chart, budget, heartbeat; `npx paperclipai onboard` | Lớn nhất họ "công ty AI" 2026 |
| **OpenOPC** | HKUDS/OpenOPC | Py | ~1,8k (12/10/2026) | "One-person company": tự dựng org chart, uỷ việc cho Claude Code/Codex/Cursor | Mới, mỏng |
| **OpenCompany** (ex-MachinaOS) | zeenie-ai/OpenCompany | Py + TS | ~995 (12/10/2026) | App desktop/self-host: nhân viên AI = lead + specialist trên canvas, trigger email/chat/lịch, Temporal, 86 SKILL.md | Xem §4; theo dõi, chưa khuyến nghị production |

## 2. Phân tích

- **Sao ≠ dùng thật**: AutoGen nhiều sao nhất nhưng ở chế độ bảo trì; LangGraph ít sao hơn nhưng dẫn đầu mọi chỉ số adoption.
- **Hợp nhất**: Microsoft gom AutoGen + Semantic Kernel; LangChain tách phần agent sang LangGraph; OpenAI tự làm SDK → xu hướng "mỗi nhà cung cấp model có SDK agent riêng + 1–2 framework trung lập".
- **Chuẩn chung thay framework**: MCP (tool), A2A (agent-agent), AG-UI (UI) khiến việc chọn framework ít "khóa chặt" hơn trước.
- **"Công ty AI" là một họ riêng** (MetaGPT, ChatDev, gpt-pilot, agency-swarm, DeerFlow; so sánh trong `X-Agents/docs/reports/2026-10-10-doi-chieu-12-repo-co-che.md`): điểm chung là vai trò + SOP + artifact trung gian; bài học từ X-Agents (mục 23 §3.1) là **model quyết định, code hành động** — mọi trường "đã làm" do code điền, không tin lời khai của model.
- **Hermes Agent** là framework agent cá nhân gần OpenClaw nhất nhưng mở hơn về provider (plugin model-provider, CLI thuê bao làm backend) — xem mục 23 §5.
- **Tiêu chí chọn**: (1) kiểm soát luồng & durable execution (LangGraph), (2) tốc độ lên demo (CrewAI), (3) type-safety (PydanticAI), (4) hệ sinh thái cloud (ADK/Agent Framework), (5) khối lượng phụ thuộc (smolagents).

## 4. Case study: zeenie-ai/OpenCompany – "nhân viên AI" đóng gói thành sản phẩm (link từ người dùng, 2026-10-12)

### Hồ sơ nhanh

| Mục | Giá trị (đọc 2026-10-12, clone nông commit `a09c079`) |
|---|---|
| Repo | zeenie-ai/OpenCompany (tên cũ **MachinaOS**, đổi ~7/2026); npm `@zeenie-ai/opencompany` 0.2.1 (12/9/2026) |
| Tác giả | Zeenie AI (tài khoản cá nhân, 5 repo); gần như toàn bộ commit của `trohitg`, trailer `Co-Authored-By: Claude`; everydev.ai nói 1 nhân sự ở Bengaluru **(chưa xác minh)** |
| License / quy mô | MIT; 995★ · 151 fork · 1.556 commit; commit cuối 11/10/2026; ~183k dòng Python + ~91k dòng TS; 386 file test; `CLAUDE.md` 359 KB (2.835 dòng) |
| Stack | FastAPI + WebSocket, React 19 + React Flow + Tailwind 4, Electron, bun, uv/Python 3.12, SQLite mặc định, **Temporal** nhúng; 14 provider LLM (Anthropic, OpenAI, Gemini, Ollama, LM Studio…) |
| Xu hướng sao | +671/90 ngày (reporank) — ổn định, không viral; **0 thread HN/Reddit** tìm được |

### Cơ chế đáng học

- **Một nhân viên = một workflow**: chủ mô tả việc bằng lời → LLM soạn bản thiết lập (app, giờ làm, quy tắc hỏi trước) → "Hire" tạo workflow chạy nền với trigger Gmail/Telegram/WhatsApp/Stripe/webhook/cron.
- **Topology là ranh giới uỷ quyền** (`docs-internal/agent_teams.md`): lead (`ai_employee`/`orchestrator_agent`) chỉ giao việc cho specialist nối trực tiếp vào handle `input-teammates`, tối đa 2 tầng, không trùng loại specialist trong một đội; mỗi tool node có đúng một agent sở hữu.
- **Task Manager** gắn cố định vào lead: giao việc chỉ qua `assign_task(mission, context, acceptance_criteria, assignee)`; specialist nộp, lead review và trả lại nếu chưa đạt rồi mới báo chủ. Các tool `delegate_to_*` **bị ẩn khỏi model**, lead chỉ thấy roster một dòng/teammate.
- **Context ≠ Memory** (RFC-0002): context = hội thoại backend sở hữu, khoá `(workflow, generation, agent)`, mọi lần kích hoạt nối tiếp cùng hội thoại; memory = tool `simpleMemory` gọi tường minh, người dùng sửa được. Thiết kế journal/epoch/hash-chain trong RFC bị thay bằng store phẳng sau ~2 tháng — "đơn giản thắng".
- **Compaction** tự động ở 0,8 cửa sổ ngữ cảnh thành tóm tắt 5 phần ("lấy cảm hứng từ Claude Code") kèm đếm token và tính chi phí theo `pricing.json`.
- **Skill = SKILL.md** (chuẩn Agent Skills, 86 file/21 domain, ví dụ `employee/chase-late-payments` với 3 mức nhắc nợ, cấm đe doạ/tự giảm giá); "self-improving" = memory + sửa skill + thêm tool có duyệt, **không retrain**.
- **Plugin**: class kế thừa `ActionNode/TriggerNode/ToolNode` với `Params`/`Output` Pydantic dùng chung cho form UI + tool schema LLM + REST spec; restart là có node mới, không sửa frontend. Approval gate "ask first" cho gửi/chi tiền kèm 5 giây undo. CLI agent (Claude Code/Codex/Gemini) chạy qua subprocess — gãy khi CLI đổi flag (issue #132–134).

### Mâu thuẫn & rủi ro

- README "78 skills" nhưng đếm được **86**; "140+ tools" vs docs "110+ nodes" vs mã 171 plugin; README hứa 6 "nhân viên" nhưng chỉ ship 3 template + 4 starter; website kể 6 vai khác và dashboard "$27,342/day" không có bằng chứng; website bán gói Pro/Max trong khi README nói "No subscription".
- `.env` **commit sẵn SECRET_KEY/JWT_SECRET_KEY dev**; binary desktop chưa ký; không SECURITY.md; agent có quyền email/thanh toán/shell trên máy người dùng.
- Bus-factor 1; issue 10/10/2026: job kẹt "working" khi model local không gọi `assign_task` (#145), Gmail trigger giao mission rỗng (#143). cloudnews.tech (4/2026): "còn xa mới plug-and-play".
- Trùng tên với `tinyhumansai/opencompany` (Rust, GPL-3.0, 298★) — dự án khác, vài directory gộp nhầm.

### Bài học cho kho

- Họ "công ty AI" 2026 tách làm hai: *thư viện cho dev* (MetaGPT, ChatDev, CrewAI, agency-swarm) và *sản phẩm end-user chạy nền* (Paperclip, OpenCompany, OpenOPC). OpenCompany là mẫu hiếm có installer 3 OS + Docker 1 container, docs nội bộ 300 file và 3 RFC ở dự án một người.
- Ba pattern đưa sang mục 03: topology = ranh giới uỷ quyền, ẩn tool uỷ quyền khỏi model (chỉ đưa roster), tách context/memory. Cùng ý với X-Agents "model quyết định, code hành động" (mục 23).
- Trạng thái: **theo dõi, chưa khuyến nghị production**; nếu thử: Docker, đổi secret `.env`, dùng model cloud; xem lại sau 3–6 tháng (contributor thứ hai, SECURITY.md, bản ký số).

## 4b. Case study: Munder Difflin (HarnessMD) – "văn phòng" agent CLI có avatar (link từ người dùng, 2026-10-12)

> Nguồn: https://github.com/harnessmd/munder-difflin. Đã clone đầy đủ lịch sử (1.394 commit): README, `HIVE.md`, `TELEMETRY.md`, `SECURITY.md`, `LICENSE`/`LICENSE-ASSETS`, `src/shared/agentProvider.ts`, `src/main/analytics.ts`, `test/`. Cùng với đó là trang GitHub, trendshift và Product Hunt.

### Hồ sơ nhanh

| Mục | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | `HarnessMD/munder-difflin`, nhưng README, link release và lệnh clone vẫn trỏ `chaitanyagiri/munder-difflin` → đã chuyển sang org mới. Site harnessmd.com, munderdiffl.in. Tên nhại "Dunder Mifflin" (*The Office*), agent điều phối tên "Michael" |
| Tác giả | Chaitanya Giri: 1.053/1.394 commit (2 email); có 4 người khác góp 27–56 commit |
| Tuổi / phiên bản | Commit đầu 31/5/2026; v0.5.3 "pre-release"; badge #1 Repository of the Day trên trendshift, #5 Product of the Day trên Product Hunt |
| Quy mô | Electron + React + TypeScript + Pixi.js + xterm.js + node-pty; ~66,8k dòng TS trong `src/`; 131 file test |
| License / mô hình | Code MIT; art asset tách riêng (`LICENSE-ASSETS`). **Open-core**: bản Pro US$150/năm (giảm theo sức mua, thấp nhất ~US$100) có sidebar Tasks/Inbox/Automations, ghi âm cuộc họp "Stapler"… |
| Số liệu | **8,7k★**, 1,2k fork, 34 watcher, 114 issue + 125 PR mở |
| Lịch sử commit | **75 commit `seo-engine: day N AM/PM…`**: một agent viết bài SEO/blog theo lịch rồi commit thẳng vào repo sản phẩm (thư mục `blog/`, `seo/`) |

### Cơ chế

- **Mỗi terminal là một agent:** chạy CLI thật (`claude`, `codex`, `agy`, `grok`, `kimi`, `qwen`, `opencode`, `crush`, `pi`, `copilot`, Cursor hoặc lệnh tuỳ ý) trong PTY. Dùng subscription có sẵn, chịu giới hạn theo giờ của từng gói; hỗ trợ thêm BYOK và model local (Ollama, LM Studio, vLLM). Mỗi agent tuỳ chọn một git worktree riêng.
- **"Hive" = repo git chứa file thuần:** agent ghi vào `outbox/`, router giao vào `inbox/` của người nhận; blackboard `board.md` chỉ có một người ghi; `tasks.json` là sổ giao việc; event log chỉ ghi thêm. **Chỉ harness commit git** (single-committer), nhờ vậy tránh lỗi hỏng `index.lock` khi nhiều agent cùng ghi. Chỉ request/query/propose mới bắt buộc trả lời; có trần số bước chuyển để hai agent không đá qua đá lại mãi.
- **GOD agent (Michael):** người dùng chỉ nói chuyện với Michael; Michael phân việc, tự xử việc thường, chỉ đẩy việc "critical" (chi tiền, thao tác phá huỷ, đổi phạm vi) vào hàng chờ duyệt. Ngoài ra có **circuit breaker** steer → constrain → stop khi agent lặp, bão lỗi hoặc vượt ngân sách token; chi phí thật đọc từ transcript; span OTel.
- **Memory:** markdown của từng agent được gom thành "palace" chung có tìm kiếm ngữ nghĩa và cơ chế nén. README gọi đây là "fastest memory layer in the world" nhưng không có benchmark **(chưa xác minh)**.
- **Phụ:** dictation toàn hệ thống (Whisper chạy local), avatar trên sàn văn phòng 2D, IDE Monaco, kanban có ticket key, kích hoạt qua Slack/webhook, catalog 227 skill.

### Đọc cổng thật

| Tuyên bố | Code / docs | Nhận xét |
|---|---|---|
| "Autonomy with a leash: spend, scope and destructive operations come back to you" | `HIVE.md`: "Its escalation policy (what counts as 'critical') lives in its **system prompt** and is the primary control surface — tune the prompt, not the code" | Cổng duyệt là **phán đoán của LLM**, không phải code. Prompt injection hoặc model nhầm thì thao tác phá huỷ vẫn chạy. Khác với cổng máy (mục 23) và khác với cách OpenCompany giới hạn bằng topology (§4) |
| Chế độ auto của từng agent | `agentProvider.ts`: Claude Code và Grok chạy với `--permission-mode bypassPermissions`, Cursor với `--dangerously-skip-permissions`, Gemini với `--yolo`. Riêng **Codex đã được sửa** từ `--dangerously-bypass-approvals-and-sandbox` sang `-a never -s workspace-write` + `--add-dir` (comment giải thích, có test `auto-mode-sandbox.test.cjs`) | Ngoài Codex, ở chế độ auto **không agent nào có sandbox hay cổng hỏi**; an toàn chỉ còn dựa vào lời dặn trong prompt của Michael. Nên chạy trong VM/container (mục 11) hoặc dùng Codex |
| Telemetry "anonymous" | `TELEMETRY.md` + `analytics.ts`: PostHog, **bật sẵn (opt-out)**, allowlist sự kiện (`app_launched`, `agent_spawned`, `message_sent` chỉ đếm, không có nội dung), `$ip: null`, tôn trọng `DO_NOT_TRACK`; key chỉ chèn vào bản build chính thức | Minh bạch hơn mức trung bình: tài liệu là hợp đồng và allowlist được thực thi bằng code. Nhưng mặc định vẫn là bật |
| "Free, open source" | Lõi MIT; nhiều tính năng điều hành (sidebar Pro, Stapler) nằm trong bản Pro trả phí | Open-core, giống context-mode (mục 03 §8b) |

### Đánh giá

- **Đáng học:** (1) **hive bằng file + một người commit duy nhất**: giao tiếp giữa agent đọc được, diff được, không cần message broker; (2) chặn trả lời qua lại bằng loại thông điệp + trần số bước; (3) circuit breaker có 3 nấc thay vì kill ngay; (4) `TELEMETRY.md` là hợp đồng có allowlist trong code; (5) sửa Codex từ "bypass toàn bộ" sang "sandbox + `--add-dir`" là ví dụ đúng về giữ sandbox khi cần ghi thêm thư mục.
- **Rủi ro:** cổng "critical" là LLM; bypass permission mặc định cho các CLI ngoài Codex; pre-release (0.5.x) nhưng có tới 125 PR mở; repo vừa đổi chủ; commit SEO tự động làm loãng lịch sử; chưa có đánh giá độc lập về chất lượng phối hợp nhiều agent.
- **So sánh:** cùng họ "công ty/văn phòng AI" với OpenCompany (§4), Paperclip, OpenOPC, và cùng nhóm ADE ở mục 01 §1.3 (Personal Jarvis, T3 Code, Claude Squad). Điểm khác biệt là dồn mọi CLI về **một** agent điều phối bằng giọng nói/chat và hiển thị như một văn phòng.

## 4c. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại sao, license, trạng thái của các repo mục 02 bằng GitHub search API (31/10/2026). (2) Tìm framework lớn còn thiếu: 5 truy vấn (`agent framework`, topic `ai-agents`, `multi-agent`, `agent sdk`, `agent harness`, repo tạo sau 1/10/2025), lọc bỏ repo đã có trong `data/projects.json`. Chọn **7 repo**, clone `--filter=blob:none` (lịch sử) và `--depth 1` (đọc/grep mã): LICENSE, manifest, cấu trúc gốc, file nguồn chính, CI, grep telemetry/host mạng; đếm commit, tác giả, trailer `Co-Authored-By: Claude`. **Không cài, không chạy script nào của repo.**

### 4c.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (bảng §1 → 31/10/2026) | Hệ quả |
|---|---|---|
| `FoundationAgents/MetaGPT` | **Push cuối 21/1/2026** (hơn 9 tháng); 71,1k★ | Coi như ngừng phát triển; chỉ đọc để học mẫu SOP, không chọn cho dự án mới |
| `Pythagora-io/gpt-pilot` | Push cuối 18/6/2026; GitHub báo `NOASSERTION` | Khớp ghi chú "ngừng bảo trì" ở §1 |
| `HKUDS/OpenOPC` | **Không còn trong kết quả search API** (meta_all không có) | Có thể đã đổi tên, chuyển private hoặc xoá **(chưa xác minh)**; tạm không dùng URL cũ |
| `NousResearch/hermes-agent` | "–" → **259,2k★**, MIT | Lớn thứ hai trong bảng sau OpenClaw (393,6k) |
| `ruvnet/ruflo` | "–" → 80,4k★, MIT | Số sao lớn nhưng tuyên bố hiệu năng vẫn **chưa kiểm chứng** |
| `langchain-ai/langchain` / `langgraph` | ~130k → 148,8k★ / ~40k → 44,2k★ | |
| `deepset-ai/haystack` | ~20k → 26,9k★ | Tăng mạnh nhất nhóm RAG |
| `pydantic/pydantic-ai` | ~16k → 21k★ | |
| `google/adk-python` | "–" → 22,1k★ | Bổ sung số |
| `mastra-ai/mastra` | "–" → 29,2k★; GitHub báo `NOASSERTION` | GitHub không nhận diện được license; catalog ghi Apache-2.0, cần đọc lại LICENSE trước khi nhúng **(chưa đọc lại đợt này)** |
| `microsoft/agent-framework` | "–" → 14,4k★ | Bổ sung số |
| `microsoft/autogen` | 61,7k★; GitHub nhận **CC-BY-4.0** | Nhiều khả năng do file `LICENSE` là license tài liệu, mã theo `LICENSE-CODE` (MIT) **(chưa đọc lại đợt này)**. Catalog giữ MIT |
| `camel-ai/camel` · `ag2ai/ag2` · `VRSEN/agency-swarm` | ~13k → 18k★ · "–" → 5k★ · "–" → 4,6k★ | |
| `paperclipai/paperclip` · `bytedance/deer-flow` · `crewAIInc/crewAI` | 100,5k → 109,5k · 83,7k → 84,8k · ~57k → 60,4k★ | |

### 4c.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `HKUDS/nanobot` | Agent cá nhân | 49,7k · MIT | 31/10/2026 | Agent cá nhân tự host, WebUI/TUI/chat app, memory "Dream", cron, SDK + API kiểu OpenAI | "Siêu nhẹ" nhưng ~188k dòng Python; `restrict_to_workspace` mặc định tắt |
| `agentscope-ai/agentscope` | Framework | 35k · Apache-2.0 | 31/10/2026 | AgentScope 2.0 (Alibaba): middleware, permission engine, SOP, A2A, realtime voice | Lịch sử viết lại từ 8/2025 |
| `nanocoai/nanoclaw` | Agent cá nhân | 31,1k · MIT | 26/10/2026 | "OpenClaw thu nhỏ": mỗi agent một container, chạy trên Claude Agent SDK | **PostHog lúc setup bật sẵn**; 43% commit có trailer Claude |
| `langchain-ai/deepagents` | Agent harness | 30,8k · MIT | 31/10/2026 | Harness "đủ pin" trên LangGraph: subagent, filesystem, nén ngữ cảnh, skills, HITL | `recursion_limit` 9.999 |
| `strands-agents/harness-sdk` | Framework + harness | 9k · Apache-2.0 | 30/10/2026 | Monorepo Strands (AWS) Python/TS: SDK vòng lặp + `create_harness()` | Mặc định Bedrock Claude Sonnet 4.6 |
| `anthropics/claude-agent-sdk-python` | SDK | 8,4k · MIT (+ điều khoản thương mại) | 31/10/2026 | SDK Python chạy Claude Code CLI làm vòng lặp agent | **Wheel nhúng CLI Claude Code mã đóng** |
| `vercel/eve` | Framework | 5,8k · Apache-2.0 | 31/10/2026 | Agent "filesystem-first": `instructions.md`, `tools/`, `skills/`, `channels/`, `schedules/` | 1.0.0-rc.1; telemetry CLI bật sẵn; gắn hạ tầng Vercel |

### 4c.3 Hồ sơ từng repo

- **deepagents** (LangChain). 4.546 commit từ 27/7/2025, 177 tác giả, phiên bản `deepagents` 0.7.32. Lõi là `create_deep_agent()` trong `graph.py` ghép chuỗi middleware: subagent (đồng bộ và async), filesystem kèm quyền (`FilesystemPermission`), summarization, memory, skills, prompt caching; thư mục `middleware/` còn có `_message_eviction`, `_blob_offload` (đẩy output tool ra đĩa). ✅ README "context management: summarize + offload to disk" khớp middleware thật. Đáng học nhất là **`RubricMiddleware`** (tuỳ chọn, không nằm trong graph mặc định): khi model định dừng, một grader sub-agent chấm transcript theo rubric; `needs_revision` thì đưa phản hồi lại và lặp tiếp, dừng ở `satisfied`/`failed` hoặc `max_iterations`. Đây là mẫu evaluator–optimizer đóng gói sẵn (mục 03 §1). ⚠️ Graph đặt `recursion_limit = 9_999`, nên trần vòng lặp thật nằm ở middleware/người gọi. Mạng: thư viện chỉ gọi model; `deepagents-code` (CLI kèm theo) tự bật trace LangSmith khi lưu key qua `/auth`, tắt bằng `DEEPAGENTS_CODE_LANGSMITH_TRACING=false`. Cài: `uv add deepagents`.
- **AgentScope 2.0** (Alibaba/Tongyi). Repo tạo 1/2024 nhưng lịch sử hiện tại bắt đầu 15/8/2025 (viết lại cho 2.0), 828 commit, 191 tác giả, `__version__` 2.0.12dev, cần Python ≥ 3.11. Có `permission/` (engine + rule + decision), `sop/` (chạy việc nhiều bước theo quy trình chuẩn), `pipeline/` (`TeamPipeline` leader giao việc), `realtime/`, A2A. Tracing OpenTelemetry nằm trong middleware, không thấy endpoint thu thập mặc định. Host mặc định nghiêng về Aliyun Bailian/DashScope. Cài: `pip install agentscope`.
- **Claude Agent SDK (Python)**. 952 commit từ 11/6/2025, **26,7% có trailer Claude**, phát hành tự động (bot GitHub Actions đứng đầu). ❌ Điều README không nói ở đầu: **wheel nhúng sẵn CLI Claude Code** (`_cli_version.py` = 2.1.316) là phần mềm mã đóng; LICENSE MIT chỉ phủ phần SDK, và README §"License and terms" đặt toàn bộ việc dùng dưới **Commercial Terms** của Anthropic. ⚠️ Bẫy quyền: `allowed_tools` chỉ là danh sách **tự duyệt**, không giới hạn tool; muốn chặn phải dùng `disallowed_tools` (README tự ghi). Script build `download_cli.py` tải `install.sh` và chỉ kiểm shebang, không kiểm hash. Cài: `pip install claude-agent-sdk`.
- **Strands harness-sdk** (AWS). Repo `sdk-python` cũ (tạo 14/5/2025) nay là monorepo `harness-sdk`: `strands-py`, `strands-ts`, `harness-py`, `harness-ts`, CLI, MCP server, site docs, `team/` (tenets, quyết định). 3.187 commit, 365 tác giả, 56 workflow. ✅ README "lifecycle controls (turn limits, token budgets, cancellation)" có trong SDK. ✅ Telemetry đúng mực: `harness-py/telemetry.py` **chỉ bật exporter OTel khi đặt `OTEL_TRACES_EXPORTER`**, cố ý không theo mặc định `otlp` của spec để tránh âm thầm dựng exporter. Mặc định model `global.anthropic.claude-sonnet-4-6` trên Bedrock (cần tài khoản AWS). Cài: `pip install strands-harness` hoặc `pip install strands-agents`.
- **nanobot** (HKU Data Intelligence Lab). 5.171 commit từ 1/2/2026, 543 tác giả, v0.4.0. ⚠️ Tự gọi "ultra-lightweight" nhưng gói `nanobot/` có 445 file, ~188k dòng Python, kèm cả một bộ cập nhật tự động (~20 module `update_*`). ⚠️ `restrict_to_workspace` mặc định `False`: shell và file tool không bị giới hạn trong workspace trừ khi bật. Không thấy telemetry trong mã Python. Kênh: Telegram, Discord, Slack, WeChat, Feishu, email, Linear. Cài: `pip install nanobot-ai` (Python ≥ 3.11).
- **NanoClaw**. 3.052 commit từ 31/1/2026, 196 tác giả, **43,1% commit có trailer Claude** (cao nhất đợt). Ý tưởng: thay vì OpenClaw (~500k dòng, bảo mật ở tầng ứng dụng), mỗi agent chạy trong **container Linux riêng**, chỉ thấy thư mục được mount, khoá API đi qua Agent Vault của OneCLI (agent không giữ khoá thô). ⚠️ "Một tiến trình, vài file nguồn" không khớp: `src/` có 242 file TS, ~37,7k dòng (không tính test). ⚠️ `setup/lib/diagnostics.sh` gửi sự kiện cài đặt tới PostHog (`us.i.posthog.com`, khoá nhúng sẵn) với install-id lưu ở `data/install-id`; README có nói, tắt bằng `NANOCLAW_NO_DIAGNOSTICS=1`. Khi một bước cài lỗi, script **tự gọi Claude Code để sửa**, nên cần giám sát lần cài đầu. Cài: `git clone https://github.com/nanocoai/nanoclaw.git && cd nanoclaw && bash nanoclaw.sh`.
- **eve** (Vercel). 2.360 commit từ 16/6/2026, 77 tác giả, `eve@1.0.0-rc.1`. Agent khai báo bằng thư mục: `instructions.md` bắt buộc, `tools/*.ts`, `skills/*.md`, `channels/`, `schedules/`; gói npm kèm toàn bộ docs để coding agent đọc tại `node_modules/eve/docs`. Phụ thuộc chặt hệ Vercel (`@vercel/sandbox`, `@vercel/queue`, `@vercel/oidc`, AI Gateway). ⚠️ CLI telemetry **bật sẵn** gửi `telemetry.vercel.com/api/eve-cli/v1/events`, tắt bằng `eve telemetry disable` hoặc `EVE_TELEMETRY_DISABLED=1`; **không đọc `DO_NOT_TRACK`**. Có gói `eve-self-modification` (agent tự sửa mình), nên khoá quyền ghi khi chạy production. Cài: `npx eve@latest init my-agent`.

### 4c.4 Mẫu chung rút ra

1. **"Harness" thay chữ "framework"**: deepagents ("batteries-included agent harness"), Strands đổi tên repo thành `harness-sdk` và thêm `create_harness()`, Claude Agent SDK bọc nguyên Claude Code. Xu hướng là bán một agent đã lắp sẵn với mặc định tốt, kèm lối thoát để thay từng phần.
2. **Thư mục là giao diện viết agent**: eve (`agent/` theo quy ước), nanobot/NanoClaw (`CLAUDE.md` và memory theo từng nhóm), deepagents (skills, memory trên backend file). Hợp với hướng "trạng thái bền trong file" của mục 03 §6.
3. **Cách ly bằng container thay cho allowlist** (NanoClaw) là câu trả lời trực tiếp cho rủi ro "agent cá nhân có quyền shell" của OpenClaw/nanobot; nanobot vẫn để `restrict_to_workspace` tắt.
4. **Telemetry: Strands là mẫu tốt** (tắt đến khi người dùng bật bằng biến chuẩn OTel). eve, NanoClaw, deepagents-code bật sẵn; chỉ một phần tôn trọng `DO_NOT_TRACK`.
5. **"Nhẹ" là lời quảng cáo, không phải số đo**: nanobot ~188k dòng, NanoClaw ~38k dòng. Đếm dòng trước khi tin.

**Nguồn §4c:** GitHub search API 31/10/2026 (5 truy vấn + `user:HKUDS`) · `meta_all.json`/`status_all.json` (GitHub API 31/10/2026) · clone `--filter=blob:none` và `--depth 1` 7 repo, đọc: deepagents (README.md, LICENSE, `libs/deepagents/pyproject.toml`, `deepagents/graph.py`, `deepagents/middleware/{rubric,summarization,subagents,permissions}.py`, `libs/code/DEVELOPMENT.md`, `deepagents_code/config.py`) · agentscope (README.md, LICENSE, pyproject.toml, `src/agentscope/{_version.py, permission/, sop/, middleware/_tracing/}`) · claude-agent-sdk-python (README.md, LICENSE, pyproject.toml, `src/claude_agent_sdk/_cli_version.py`, `scripts/download_cli.py`) · harness-sdk (README.md, LICENSE.APACHE, NOTICE, `harness-py/src/strands_harness/telemetry.py`, `strands-py/src/strands/models/bedrock.py`) · nanobot (README.md, LICENSE, `nanobot/config/schema.py`, `nanobot/config/loader.py`) · nanoclaw (README.md, README_zh.md, LICENSE, nanoclaw.sh, `setup/lib/diagnostics.sh`, `src/`) · eve (README.md, LICENSE, `packages/eve/package.json`, `packages/eve/src/cli/telemetry/{index,flush,preference}.ts`) · https://github.com/HKUDS/OpenOPC (không tìm thấy qua search API)

## 5. Nguồn

- https://www.firecrawl.dev/blog/best-open-source-agent-frameworks
- https://dreaming.press/posts/ai-agent-frameworks-github-ranked-by-stars-2026.html
- https://unifiedplatforms.com/blogs/web-development/agentic-ai-frameworks-compared/
- https://the-agent-report.com/2026/07/ai-agent-frameworks-comparison-2026-langgraph-crewai-autogen/
- https://pickaxe.co/post/top-ai-agent-frameworks · https://pickaxe.co/post/crewai-vs-langgraph-vs-autogen
- https://www.langchain.com/resources/ai-agent-frameworks
- https://cordum.io/blog/langchain-vs-llamaindex-vs-semantic-kernel · https://uvik.net/blog/python-ai-agent-frameworks/
- https://github.com/NousResearch/hermes-agent · https://github.com/FoundationAgents/MetaGPT · https://github.com/OpenBMB/ChatDev · https://github.com/bytedance/deer-flow · https://github.com/ag2ai/ag2 · https://github.com/camel-ai/camel · https://github.com/VRSEN/agency-swarm · https://github.com/Pythagora-io/gpt-pilot · https://github.com/ruvnet/ruflo (đọc qua docs nội bộ của X-Agents/Hermes-Agents, 2026-10-12)
- OpenCompany (đọc 2026-10-12): https://github.com/zeenie-ai/OpenCompany (README, CONTRIBUTING, CLAUDE.md, LICENSE, releases, issues #128 #129 #132–134 #143 #145, `docs-internal/{agent_teams,employee_teams,normal_mode,memory_compaction,agent_context_flow}.md`, RFC-0001..0003, `server/nodes/README.md`, `server/skills/**/SKILL.md`, `client/src/features/home/hire/starters.json`) · https://opencompany.sh · https://docs.opencompany.sh · https://reporank.net/en/repo/zeenie-ai-opencompany.html · https://www.opensourcealternatives.to/item/opencompany · https://cloudnews.tech/machinaos-wants-to-bring-the-ai-personal-assistant-from-the-cloud-to-your-own-server/ · https://www.everydev.ai/developers/zeenie-ai (chưa xác minh) · https://github.com/paperclipai/paperclip · https://github.com/HKUDS/OpenOPC · https://github.com/tinyhumansai/opencompany (trùng tên)
- https://github.com/openclaw/openclaw · https://www.digitalocean.com/resources/articles/what-is-openclaw · https://www.freecodecamp.org/news/how-to-build-and-secure-a-personal-ai-agent-with-openclaw/
- Munder Difflin (2026-10-12): https://github.com/harnessmd/munder-difflin (clone đầy đủ; README, HIVE.md, TELEMETRY.md, src/shared/agentProvider.ts, src/main/analytics.ts) · https://github.com/chaitanyagiri/munder-difflin (URL cũ) · https://trendshift.io/repositories/46562 · https://www.producthunt.com/products/munder-difflin · https://harnessmd.com · https://munderdiffl.in
