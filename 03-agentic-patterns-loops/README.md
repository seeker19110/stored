# 03 · Agentic Patterns, Loops & Harness/Context Engineering

> Các mẫu thiết kế vòng lặp agent, kỹ thuật vận hành agent tự trị, và cách quản lý ngữ cảnh. Đây là phần "lý thuyết + thực hành" nền cho mọi mục khác.

## 1. Định nghĩa cốt lõi (Anthropic, *Building Effective Agents*, 12/2024)
> "Agents are typically just LLMs using tools based on environmental feedback in a loop."

Phân biệt **workflow** (luồng LLM + tool được code định sẵn) và **agent** (LLM tự quyết định luồng). Khuyến nghị: bắt đầu từ mẫu đơn giản nhất, chỉ thêm tự trị khi có lợi ích đo được.

### 5 workflow pattern
| Pattern | Ý tưởng | Ví dụ |
|---|---|---|
| Prompt chaining | Chuỗi gọi LLM tuần tự, có gate kiểm tra giữa các bước | Viết outline → kiểm tra → viết bài |
| Routing | Phân loại input rồi chuyển tới prompt/model chuyên biệt | Hỗ trợ khách hàng: hoàn tiền / kỹ thuật |
| Parallelization | Sectioning (chia việc độc lập) hoặc Voting (chạy nhiều lần lấy đa số) | Review code bằng nhiều góc nhìn |
| Orchestrator–workers | Orchestrator tự chia task động, giao worker, tổng hợp | Sửa code nhiều file, tìm kiếm đa nguồn |
| Evaluator–optimizer | Một LLM sinh, một LLM chấm, lặp | Dịch văn học, tìm kiếm nhiều vòng |

## 2. Hình dạng vòng lặp agent
| Mẫu | Nguồn gốc | Cơ chế | Ưu / nhược |
|---|---|---|---|
| **ReAct** | Yao et al. 2022 (Princeton/Google) | Thought → Action → Observation lặp | Linh hoạt, dễ debug / thiếu cái nhìn toàn cục, có thể lạc đường |
| **Plan-and-Execute** | LangChain, BabyAGI | Planner lập kế hoạch, executor thực thi, planner sửa lại | Hiệu quả cho task phụ thuộc nhiều bước / tốn vòng lập kế hoạch |
| **Reflexion** | Shinn et al. 2023 | Thêm tự phê bình sau mỗi lần thử, lưu vào memory | Cải thiện qua lần thử / cần tiêu chí đánh giá rõ |
| **LATS / Tree-of-Thought** | 2023 | Tìm kiếm cây trên các bước suy luận | Mạnh với bài toán tìm kiếm / đắt |
| **Generator–Evaluator (long-running)** | Anthropic (long-running agents note) | Tách sinh & đánh giá, handoff bằng artifact, reset ngữ cảnh | Nền cho agent chạy nhiều giờ |

Khảo sát học thuật: *The Landscape of Emerging AI Agent Architectures* (arXiv 2404.11584) kết luận thành công phụ thuộc **planning + self-correction**.

## 3. Ralph Wiggum loop – vòng lặp tự trị cho coding agent
- **Tác giả:** Geoffrey Huntley (7/2025). Dạng thuần túy:
  ```bash
  while :; do cat PROMPT.md | claude ; done
  ```
- **Nguyên lý:** mỗi vòng là một session mới; "bộ nhớ" duy nhất là **file trong repo** (plan, test, progress). Agent lặp cho tới khi tiêu chí hoàn thành đạt.
- **Phiên bản Anthropic:** plugin `ralph-loop` trong repo `anthropics/claude-code` dùng **Stop hook** chặn việc kết thúc session và nạp lại prompt (giữ ngữ cảnh trong 1 session); kết thúc bằng promise string + giới hạn số vòng. Claude Code cũng có `/loop`, `/goal`, `/batch` (chưa xác minh trên docs chính thức).
- **Khi nào hội tụ:** prompt chính xác + tiêu chí **kiểm chứng được** (tests pass, lint sạch, build ok). Prompt mơ hồ → lạc.
- **Phê bình:** phù hợp greenfield; để loop tự merge/tag là rủi ro khi người khác phụ thuộc vào output (orbi.build: "passed 28 tests, then failed review").
- **Triển khai cộng đồng:** `frankbria/ralph-claude-code` (exit detection thông minh), nhiều guide tại awesomeclaude.ai, paddo.dev.

## 4. Context engineering & harness engineering
| Khái niệm | Nội dung | Nguồn |
|---|---|---|
| Context engineering (Anthropic, *Effective Context Engineering for AI Agents*) | Ngân sách ngữ cảnh là kỷ luật kỹ thuật: viết / chọn / nén / cô lập ngữ cảnh qua trajectory dài | anthropic.com, philschmid.de |
| Bài học Manus | Rebuild framework 4 lần; **KV-cache hit rate** là metric quan trọng nhất; đừng để agent tự viết lại todo.md (tốn ~30% token) → dùng planner sub-agent, inject khi cần | philschmid.de part 2, Medium |
| Harness engineering (OpenAI/Anthropic thuật ngữ) | Harness = hệ thống cho phép model hành động như agent: repo map, AGENTS.md, runtime control, sandbox | arXiv 2609.00006, 2606.20683, preprints 202603.1756 |
| MemoHarness / structured memory | Harness tự học từ kinh nghiệm | arXiv 2607.14159, 2603.13258 |

## 5. Multi-agent coding song song (thực hành 2026)
- **Git worktrees** cho mỗi agent (`claude --worktree`): tránh ghi đè file, tranh chấp git index, port dev-server. Không bao phủ state chia sẻ (DB, API ngoài) → serialize các bước đó.
- **Phân cấp primitive (Claude Code):** subagents (trong session) · agent teams (giữa session, thử nghiệm) · background agents · `/batch` cho thay đổi cơ học lớn.
- **Hợp đồng giao diện:** sinh OpenAPI/spec trước khi chạy song song để tránh drift (mầm của "spec-driven development").
- **Giới hạn:** thêm agent chỉ khi còn sức review; 4–5 agent → RAM; 10+ → ngân sách context mỗi agent.
- **Hướng dẫn:** `FlorianBruniaux/claude-code-ultimate-guide` (agent-teams.md), thepromptshelf.dev (6 pattern), developersdigest.tech.

## 6. Checklist thiết kế agent loop (rút ra)
1. Tiêu chí dừng **kiểm chứng được bằng máy** (test, lint, type-check, build).
2. Trạng thái bền trong **file/repo**, không trong "trí nhớ" của session.
3. Giới hạn vòng lặp + exit detection + nhật ký tiến độ.
4. Tối ưu KV-cache: prefix ổn định, chỉ append, tránh sửa đầu prompt.
5. Tách generator/evaluator; evaluator nên có công cụ độc lập.
6. Cô lập tài nguyên (worktree, sandbox) khi chạy song song.
7. Người review ở cuối vòng; không để loop tự merge vào main.

## 8. Case study: ADHD – Parallel Divergent Ideation (link từ người dùng, 2026-10-12)

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo | https://github.com/UditAkhourii/adhd · npm `adhd-agent` · docs adhd.mintlify.site · preprint adhdstack.github.io (v0.1, 25/5/2026) |
| Mô tả | "A skill for coding agents. Tree-of-thought with pruning, built on the Claude & Codex Agent SDK" |
| Tác giả | Udit Akhouri (Raj) – "Independent AI Researcher", IIT Patna; từng ở Emora Health, Malpani Ventures; 125 followers; repo liên quan: neuroarxiv (434★, check prior art trên arXiv), quicksilver, brane-code, branerail, cdaf |
| ★ / forks / commit | 4.4k ★ · ~300–314 forks · 74 commit · 2 contributor · 12 issue mở; +864★ trong 61 ngày (13/8–12/10/2026), đỉnh 19/8 (+122), đang chậm lại |
| License | MIT |
| Ngôn ngữ | TypeScript (~600 dòng core), Node 18+; cài `npx skills add UditAkhourii/adhd` hoặc `npm i -g adhd-agent` |

### Cơ chế (từ `SKILL.md` và preprint)
- **Vấn đề nhắm tới:** *premature convergence* – LLM chọn phương án hợp lý đầu tiên rồi "đánh bóng" nó.
- **Phase 1 – Diverge (không critic):** chọn 5 trong 15 "cognitive frame" (hardware engineer, regulator, 10-year-old, competitor, biology, logistics, game design, markets, inversion, $0/1h, infinite budget/10y, remove load-bearing assumption, speedrunner, ant colony, 3am on-call); spawn **5 Agent/Task call song song, cô lập** (không thấy nhau → tránh anchoring), mỗi nhánh trả JSON 6 ý tưởng ngắn. Với bài code: 4 frame code/design + 1 wild.
- **Phase 2 – Focus (critic bật):** 1 call chấm novelty/viability/fit (0–10, trọng số 0.35/0.40/0.25), gắn cờ **trap** (ý tưởng hấp dẫn nhưng chi phí ẩn); 1 call cluster theo "góc nhìn"; 3 call song song **deepen** top-3 (sketch, rủi ro chịu tải, bước đầu tiên, ý con).
- **Output cố định:** Brief → Wide set (cluster + chip `[N7 V8 F9]`) → Converge (shortlist 2–4, ★ non-obvious pick, traps riêng) → Focus → Provocation.
- **Gate tiền kiểm:** chỉ chạy khi bài **mở, rủi ro cao, cách hỏi mở**; bỏ qua với syntax/lookup/"quick/standard/one-line". ~10 call/run, 30–90 giây, **5–10× chi phí** single-shot.
- **Anti-pattern tác giả nêu:** hội tụ giả dạng phân kỳ; ý lạ mà không hội tụ; chạy "song song" tuần tự; không dám chốt.
- **Khác ToT (Yao 2023):** nhánh **cô lập** (ToT chia sẻ context), phân nhánh bằng **đổi vantage point** chứ không phải đổi bước kế tiếp, generator/critic là **2 call tách biệt** với system prompt đối lập.

### Bằng chứng & phê bình
| Nguồn | Nội dung |
|---|---|
| EVALS.md / preprint (tự báo cáo) | 6 bài kỹ thuật (LRU cache, LLM hang CLI, rate limiter + leader election, bug 0.1%, tách monolith Rails, đặt tên feature-flag); judge = LLM "skeptical staff engineer" (không nêu model); ADHD thắng 5/6; Δ: breadth +4.17, novelty +5.17, **trap detection +7.67**, actionability +3.00, builder usefulness +0.83 |
| Hạn chế tác giả tự nhận | judge cùng họ model (familiarity bias); mẫu 6 bài; frame viết tay có thể trùng ý; actionability bị **confound** do ADHD có schema output còn baseline không; chỉ bài engineering |
| The New Stack (6/2026) | Tiêu đề: *"gave Claude Code 'ADHD'… thinks 2x better now. Outside experts want more proof."* Tác giả nói với báo: "good for brainstorming and planning, **not coding**" |
| dudarik.com (5/6, cập nhật 7/7/2026) | "2×" chưa được tái lập độc lập; testdouble/han review 8 vòng nêu câu hỏi phương pháp (issues #16–18); chi phí tăng theo N, thêm độ trễ trước khi code |
| ADOPTERS.md (16 entry, tự duy trì) | Đáng tin nhất là entry có PR merge: repowire (#313), mythify, godaudits, godplans (có **control arm** và từ chối một số tính năng), han; `multi` port đa model (mỗi frame một họ model); phần còn lại là fork/cài đặt |

### Bài học cho kho này
1. Là hiện thân gọn của **parallelization (sectioning) + evaluator-optimizer** trong 5 pattern của Anthropic (mục 1), dùng đúng cho bài *open-ended* chứ không phải thực thi.
2. **Cô lập context giữa các nhánh** là điểm thiết kế đáng tái dùng khi chạy subagent song song (mục 5): subagent không nên thấy output nhau nếu muốn đa dạng.
3. Tách generator/critic bằng call riêng + rubric số + trap list → mẫu tốt cho "design review" trước khi vào Ralph loop.
4. Rủi ro: chi phí 5–10×, bằng chứng tự báo cáo với judge cùng model; nên tự chạy A/B trên bài của mình (bench/results.json có transcript đầy đủ) và kiểm tra `han` review trước khi đưa vào quy trình team.
5. Liên hệ: mục 04 (SKILL.md), mục 07 (LLM-as-judge), mục 17 (frame = persona prompting có chủ đích "distort perspective, not supply expertise").

**Nguồn:** https://github.com/UditAkhourii/adhd (README, SKILL.md, EVALS.md, ADOPTERS.md) · https://adhdstack.github.io/ · https://github.com/UditAkhourii · https://trendshift.io/repositories/39300 · https://thenewstack.io/claude-code-adhd/ · https://dudarik.com/en/blog/adhd/ · https://explainx.ai/skills/UditAkhourii/adhd/adhd · https://futureagi.com/blog/what-is-tree-of-thoughts-prompting-2026/ · https://arxiv.org/html/2605.06040v1 (Novelty-based ToT) · https://arxiv.org/html/2605.28566v2 (ToT as heuristic search)

## 9. Nguồn (mục 1–7)
- https://www.anthropic.com/research/building-effective-agents
- https://docs.spring.io/spring-ai/reference/api/effective-agents.html (diễn giải lại 5 pattern)
- https://atlan.com/know/ai-agent/what-is-an-agent-loop/ · https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems
- https://servicesground.com/blog/agentic-reasoning-patterns/ · https://arxiv.org/pdf/2404.11584 · https://arxiv.org/pdf/2509.08646
- https://arxiv.org/pdf/2603.05344 (Building Effective AI Coding Agents for the Terminal)
- https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md · https://github.com/frankbria/ralph-claude-code
- https://www.theregister.com/2026/01/27/ralph_wiggum_claude_loops/ · https://awesomeclaude.ai/ralph-wiggum · https://paddo.dev/blog/ralph-wiggum-autonomous-loops/ · https://orbi.build/blog/ralph-loop-claude-code
- https://www.philschmid.de/context-engineering-part-2 · https://snowan.gitbook.io/study-notes/ai-blogs/how-to-build-agent-harness
- https://arxiv.org/pdf/2609.00006 · https://arxiv.org/pdf/2606.20683 · https://arxiv.org/pdf/2607.14159 · https://www.preprints.org/manuscript/202603.1756
- https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/guide/workflows/agent-teams.md · https://thepromptshelf.dev/blog/claude-code-multi-agent-orchestration-patterns-2026/ · https://www.developersdigest.tech/blog/git-worktrees-claude-code-parallel-agents-guide · https://www.aakashx.com/blog/parallel-claude-code-agents/
