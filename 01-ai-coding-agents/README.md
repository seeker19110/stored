# 01 · AI Coding Agents

> Các agent/trợ lý lập trình chạy trong terminal, IDE hoặc cloud. Số sao ước lượng tại 9–10/2026, đối chiếu từ nhiều nguồn (xem cuối trang).

## 1. Bảng tổng hợp

### 1.1 Mã nguồn mở (CLI / tự host)

| Dự án | Repo | License | ★ (ước lượng) | Điểm nổi bật | Ghi chú |
|---|---|---|---|---|---|
| **OpenCode** | github.com/sst/opencode | MIT | ~210k | CLI/TUI agent đa model, provider-agnostic, LSP tích hợp | Nhiều nguồn xếp #1 nhóm mở (9/2026) |
| **DeepSeek Harness** | github.com/deepseek-ai/deepseek-harness | MIT | ~200k (2 tuần sau 13/8/2026) | Kiến trúc "mọi thứ là plugin": UI, tool call, context injection, cả agent loop đều thay được; hỗ trợ model local | Developer preview, chưa nhận PR ngoài; số sao giữa các nguồn chênh lệch (95k→203k) |
| **OpenAI Codex CLI** | github.com/openai/codex | Apache-2.0 | ~127k | Agent terminal chính thức của OpenAI, sandbox, multi-agent orchestration | Rust rewrite |
| **Gemini CLI** | github.com/google-gemini/gemini-cli | Apache-2.0 | ~107k | Agent terminal của Google, free tier rộng, MCP | |
| **OpenHands** (cũ: OpenDevin) | github.com/OpenHands/OpenHands | MIT | ~90k | Nền tảng agent dev đầy đủ (sandbox Docker, web UI, cloud), nhiều SOTA SWE-bench | Đổi tên từ All-Hands-AI |
| **Cline** | github.com/cline/cline | Apache-2.0 | ~69k | VS Code extension agent, plan/act mode, MCP marketplace | |
| **Aider** | github.com/Aider-AI/aider | Apache-2.0 | ~49k | Pair-programming terminal, repo map, git-native | Commit cuối 5/2026 → phát triển chậm lại |
| **SWE-agent** | github.com/SWE-agent/SWE-agent | MIT | ~20.5k | Princeton; agent-computer interface, giải GitHub issue tự động | Nghiên cứu, bảo trì đều (10/2026) |
| **mini-SWE-agent** | github.com/SWE-agent/mini-swe-agent | MIT | ~8.4k | **100 dòng code**, >74% SWE-bench Verified; là harness chuẩn của Vals leaderboard | Minh chứng "harness đơn giản vẫn mạnh" |
| **Goose** | github.com/block/goose | Apache-2.0 | – | Agent desktop/CLI của Block, MCP-first | |
| **Roo Code / Kilo Code** | github.com/RooCodeInc/Roo-Code | Apache-2.0 | – | Fork Cline, nhiều mode | |

### 1.2 Thương mại / mã đóng

| Sản phẩm | Hãng | Hình thức | Giá tham khảo | Điểm nổi bật |
|---|---|---|---|---|
| **Claude Code** | Anthropic | CLI + IDE + web/cloud | theo gói Claude | Repo ~148k★ nhưng mã đóng; hooks, skills, subagents, plugins (`ralph-loop`), `/loop`, worktree |
| **Cursor** | Anysphere | VS Code fork | Pro $20 / Pro+ $60 / Ultra $200 | Mạnh nhất cho multi-file; cloud agents song song; đọc SKILL.md từ 2.4 (1/2026) |
| **Windsurf → Devin Desktop** | Cognition | IDE | ~$15–20 | Sau khi Cognition mua Windsurf, vận hành dưới tên Devin Desktop (nguồn chưa thống nhất) |
| **Devin** | Cognition | Cloud agent | $20 beta / $500 seat ent. | Agent "kỹ sư phần mềm" đầu tiên |
| **GitHub Copilot** | GitHub/MS | IDE + coding agent | $10 / $19 / $39 | Mặc định cho team GitHub; agent kém Cursor/Claude Code theo review |
| **Google Jules** | Google | Cloud async agent | free 15 task/ngày | Tốt cho test & PR trên repo Python |
| **OpenAI Codex (cloud)** | OpenAI | Cloud agent | trong ChatGPT Plus $20 / Pro $100+ | Chạy song song nhiều task trong sandbox |

## 2. Benchmark & cách đánh giá

| Benchmark | Trạng thái 10/2026 | Top |
|---|---|---|
| SWE-bench Verified | **Bão hòa**: Vals ngừng chấm model mới từ 1/9/2026; OpenAI tuyên bố (2/2026) không còn đo được frontier | Claude Opus 5 (mini-SWE-agent) 97.0%, DeepSeek V4 Pro 96.4%, GPT-5.6 Sol 96.2% |
| SWE-bench Pro (Verified) | Benchmark kế nhiệm, khó hơn | Claude Opus 5.5 ~65% (6/10/2026) |
| Khác | SWE-Touch (người dùng sửa code giữa chừng), RoadmapBench (nâng cấp version dài hạn), UTBoost | Đang nổi trong giới học thuật |

**Bài học:** chọn agent theo (1) harness có kiểm soát được không, (2) license, (3) chi phí token, (4) tích hợp MCP/skills; đừng dựa vào số sao.

## 3. Xu hướng kiến trúc đáng chú ý

- **Harness > Model**: các paper 2026 ("Harness Engineering: Source-Code Study of Eleven Systems", "Inside the Scaffold") cho thấy phần lớn chất lượng đến từ vòng lặp, công cụ, quản lý ngữ cảnh.
- **Plugin hóa toàn bộ** (DeepSeek Harness) và **tối giản hóa** (mini-SWE-agent) là 2 cực cùng tồn tại.
- **Cloud/async agents** (Codex cloud, Jules, Cursor cloud agents, Claude Code web) → lập trình viên trở thành người ra đề & review.
- **Memory có cấu trúc** cho agent ("Your Code Agent Can Grow Alongside You", 2026).

## 3b. Case study: Understand-Anything – codebase thành knowledge graph (trending, 2026-10-12)

> Nguồn: ảnh bảng trending người dùng gửi ("Understand-Anything: +2.331 sao/ngày"). Nghiên cứu từ repo (README, cấu trúc, CLAUDE.md), trang org, trendshift, bài Better Stack / Augment Code, các directory skill.

### 3b.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/Egonex-AI/Understand-Anything (URL cũ `Lum1104/Understand-Anything` redirect về đây; mirror `GoodDingo/understand-anything`) |
| Tác giả | Yuxiang Lin · Infinite Universe, Inc. (dòng bản quyền); org **Egonex-AI** ("Understand anything. Understand anyone."), website egonexai.com, 1 repo public, không member public |
| Ngôn ngữ / license | TypeScript, pnpm workspaces, Tree-sitter, Vite, Vitest; **MIT** |
| Số liệu | **85,9k★**, 7,2–7,5k fork, 42 contributor, 857 commit, 117 issue mở, 200 PR mở; cập nhật 10/10/2026 |
| Trending | #1 GitHub Trending TypeScript 4 ngày (21–28/5/2026, lần đầu 23/5); trendshift +6.836★/61 ngày (13/8–12/10), đỉnh 12–14/9 (+227/+240/+241 mỗi ngày); ảnh người dùng gửi ghi +2.331★/ngày (đợt sóng mới) |
| Tagline | "Graphs that teach > graphs that impress" |

### 3b.2 Nó làm gì

- Biến code (hoặc docs, wiki kiểu "Karpathy LLM wiki") thành **knowledge graph tương tác**: node là file/hàm/class, cạnh là import/call/kế thừa; tóm tắt tiếng Anh thường, **guided tour** theo thứ tự phụ thuộc, tìm fuzzy + ngữ nghĩa, **diff impact analysis**, phân lớp (API/Service/Data/UI/Utility), view business logic (domain → flow → step), UI thích ứng persona (junior dev, PM, power user), giải thích 12 pattern ngôn ngữ trong ngữ cảnh; đầu ra đa ngôn ngữ gồm **tiếng Việt** (en, zh, zh-TW, ja, ko, ru, vi).
- Lệnh: `/understand` (lưu `.ua/knowledge-graph.json`; `--language`, `--auto-update` tạo post-commit hook), `/understand-dashboard`, `/understand-chat`, `/understand-diff`, `/understand-explain`, `/understand-onboard`, `/understand-domain`, `/understand-knowledge`.
- Cài: `/plugin marketplace add Egonex-AI/Understand-Anything` → `/plugin install understand-anything`; nền tảng khác qua `install.sh`/`install.ps1` (Codex dùng tiền tố `$`). Hỗ trợ: Claude Code (plugin gốc), Cursor, VS Code + Copilot, Copilot CLI, Codex, OpenCode, OpenClaw, Antigravity, Gemini CLI, Pi Agent, Vibe CLI, Hermes, Cline, KIMI CLI, Trae, Nanobot, Kiro.
- Chia sẻ team: commit graph (trừ `.ua/intermediate/` và `diff-overlay.json`), graph lớn dùng git-lfs; viewer read-only `npx` (Node ≥18) không cần Claude Code.

### 3b.3 Cách hoạt động (điểm đáng học)

| Lớp | Cơ chế | Vì sao quan trọng |
|---|---|---|
| **Tất định** | Tree-sitter trích import/export/định nghĩa/call site/kế thừa; cùng input → cùng output; cũng là cơ sở **incremental** (chỉ phân tích file đổi) | Giảm hallucination cấu trúc, giảm token lần sau |
| **Ngữ nghĩa** | LLM sinh summary, tag, layer, domain mapping, tour, concept callout | Phần "dạy" người đọc |
| **Pipeline đa agent** | project-scanner → file-analyzer (song song tối đa 5 worker, 20–30 file/batch) → architecture-analyzer → tour-builder → graph-reviewer; thêm domain-analyzer, article-analyzer | Chia việc theo vai trò + có **reviewer** kiểm graph (evaluator pattern, mục 03) |
| **Đóng gói** | Cùng một lõi, nhiều thư mục plugin (`.claude-plugin`, `.copilot-plugin`, `.cursor-plugin`) + installer | Mẫu "một skill, nhiều host" (mục 04/20) |

README tự cảnh báo: lần chạy đầu trên codebase lớn **tốn nhiều token**; gợi ý gói subscription hoặc model local (Ollama, mục 10).

### 3b.4 Đánh giá

- **Điểm mạnh:** lai tất định + LLM đúng chỗ; incremental; output kiểm tra được (JSON trong repo); viewer không cần agent; đa host; đa ngôn ngữ (có vi).
- **Rủi ro / lưu ý:** phần lớn bài viết bên ngoài là aggregator/khuyến mãi, chưa có đánh giá độc lập về độ chính xác graph; một trang trending (trendingrepo.com) gắn cờ "có thể star-farming" cho bản owner cũ — **chưa xác minh**, nhưng tốc độ +2k★/ngày sau 5 tháng ra mắt là bất thường và đáng theo dõi (so sánh ADHD, Anatomy, OpenMontage ở mục 03/06/19 đều có đợt sóng tương tự). Chi phí token lần đầu; graph lớn cần lfs; 200 PR mở cho thấy maintainer quá tải.
- **Vị trí trong kho:** công cụ "đọc hiểu codebase" cho coding agent, cùng nhóm với Context7/llms.txt (mục 16) và memory có cấu trúc (mục 10). Đáng thử cho onboarding dự án lạ và review tác động diff trước khi vào Ralph loop (mục 03).

## 4. Nguồn

- https://pinggy.io/blog/best_open_source_cli_coding_agents/
- https://www.morphllm.com/best-ai-coding-agents-2026
- https://www.openhands.dev/blog/open-source-ai-coding-agents
- https://stoneforge.ai/blog/open-source-ai-coding-agents/
- https://andrew.ooo/answers/best-open-source-ai-coding-agent-2026-ranked-guide/
- https://thenewstack.io/deepseek-harness-open-source-plugins/
- https://www.mindstudio.ai/blog/deepseek-harness-coding-agent
- https://github.com/OpenHands/OpenHands · https://github.com/SWE-agent/mini-swe-agent · https://github.com/SWE-agent
- https://arxiv.org/html/2604.03515v2 (Inside the Scaffold) · https://arxiv.org/pdf/2609.00006 (Harness Engineering)
- Understand-Anything: https://github.com/Egonex-AI/Understand-Anything · https://github.com/Egonex-AI · https://trendshift.io/repositories/23482 · https://betterstack.com/community/guides/ai/understand-anything/ · https://www.augmentcode.com/learn/understand-anything-71k-stars · https://mcpmarket.com/tools/skills/understand-anything-code-graph · https://github.com/GoodDingo/understand-anything · understand-anything.com
- https://www.vals.ai/benchmarks/swebench · https://arxiv.org/pdf/2609.08149 (SWE-Bench Pro Verified)
- https://codeant.ai/blogs/best-ai-code-editor-cursor-vs-windsurf-vs-copilot · https://www.developersdigest.tech/blog/ai-coding-tools-pricing-2026 · https://levelop.dev/blog/the-best-ai-coding-agents-in-2026-a-practical-ranking-for-working-developers
