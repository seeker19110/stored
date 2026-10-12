# 📚 Kho tham khảo: Coding · AI · Agentic · Design · UI/UX

> Tổng hợp và phân tích các dự án nổi bật (chủ yếu trên GitHub) về lập trình, AI coding agent, agent framework, agentic loop, giao thức agent, low-code LLM, UI/UX & design, đánh giá/quan sát LLM, và các "awesome list" học tập.
>
> **Ngày khảo sát:** 2026-10-12 · **Phương pháp:** tìm kiếm web + đối chiếu nhiều nguồn (blog so sánh, trang GitHub, tài liệu chính thức, bài báo học thuật). Số sao GitHub là **ước lượng tại thời điểm khảo sát** (Q3–Q4/2026) và sai lệch giữa các nguồn; xem từng mục để biết nguồn.

---

## 🗂️ Mục lục

| # | Chuyên mục | Nội dung chính |
|---|-----------|----------------|
| 01 | [AI Coding Agents](01-ai-coding-agents/README.md) | OpenCode, Claude Code, Codex CLI, Gemini CLI, Cline, Aider, DeepSeek Harness, OpenHands, SWE-agent, Cursor, Windsurf/Devin, Copilot, Jules; benchmark SWE-bench; **case study Understand-Anything** (85,9k★, codebase → knowledge graph) |
| 02 | [Agent Frameworks](02-agent-frameworks/README.md) | LangGraph, CrewAI, AutoGen → MS Agent Framework, OpenAI Agents SDK, LangChain, LlamaIndex, Semantic Kernel, smolagents, Haystack, PydanticAI, OpenClaw |
| 03 | [Agentic Patterns & Loops](03-agentic-patterns-loops/README.md) | 5 workflow của Anthropic, ReAct, Plan-Execute, Reflexion, Ralph Wiggum loop, context engineering, harness engineering, multi-agent + git worktrees; **case study ADHD** (parallel divergent ideation skill) |
| 04 | [Protocols & Standards](04-protocols-standards/README.md) | MCP, A2A, AG-UI, Agent Skills (SKILL.md), AGENTS.md, .cursorrules |
| 05 | [Low-code LLM Platforms](05-low-code-llm-platforms/README.md) | n8n, Dify, Langflow, Flowise |
| 06 | [UI/UX & Design](06-ui-ux-design/README.md) | shadcn/ui, Radix, Base UI, MUI, Mantine; Penpot, Excalidraw, tldraw, Onlook; v0, Lovable, Bolt, Stitch; Taste Skill, Refactoring UI, Laws of UX; CopilotKit, assistant-ui, Vercel AI SDK; **case study Anatomy** (skill minh họa isometric tương tác) |
| 07 | [Eval & Observability](07-eval-observability/README.md) | Langfuse, Promptfoo, DeepEval, Ragas, Arize Phoenix |
| 08 | [Awesome Lists & Learning](08-awesome-lists-learning/README.md) | build-your-own-x, freeCodeCamp, system-design-primer, developer-roadmap, awesome-llm-apps, awesome-claude-code, awesome-agent-skills, awesome-mcp-servers, awesome-design-systems… |
| 09 | [Engineering Checklists](09-engineering-checklists/README.md) | **PinoyFreeCoder/deployment-checklist** (pre-deploy web/mobile, agent.md trả GO/NO-GO) so với MarinJursic/production-readiness-checklist (10k control + scanner), OWASP ASVS/MASVS, Front-End-Checklist |
| 10 | [Local LLM, Vector DB, RAG & Memory](10-local-llm-rag-memory/README.md) | Ollama, llama.cpp, vLLM, SGLang; Milvus, Qdrant, Chroma, pgvector; GraphRAG, LightRAG; Mem0, Graphiti, Letta, cognee |
| 11 | [Browser Agents, Computer Use & Sandboxes](11-browser-computer-use-sandbox/README.md) | Browser Use, Stagehand, agent-browser, Playwright MCP; Anthropic Computer Use, OpenAI Operator; E2B, Modal, Daytona |
| 12 | [AI Security & Guardrails](12-ai-security-guardrails/README.md) | OWASP LLM / Agentic / MCP Top 10; NeMo Guardrails, LLM Guard, Guardrails AI, Promptfoo red-team; gitleaks, trufflehog; AgentDojo |
| 13 | [Dev Stack & DevOps](13-dev-stack-devops/README.md) | React, Vue, Next.js, Svelte, Astro; FastAPI, NestJS, Hono; Flutter, RN/Expo, KMP; Kubernetes, OpenTofu, Argo CD, GitHub Actions; Spec Kit, Kiro, BMAD; CodeRabbit, Greptile, Qodo |
| 14 | [Voice & Multimodal](14-voice-multimodal/README.md) | Pipecat, LiveKit Agents, TEN; Whisper, faster-whisper, Kokoro, Chatterbox; Qwen3-VL, LLaVA; ComfyUI, A1111, Fooocus |
| 15 | [AI for Data](15-ai-for-data/README.md) | DuckDB, Polars, PandasAI, Vanna, marimo, Jupyter AI, Ibis, Data Formulator, MindsDB |
| 16 | [Docs Tools & Docs-for-AI](16-docs-tools/README.md) | Docusaurus, MkDocs Material/Zensical, Starlight, Fumadocs, Mintlify; llms.txt, Context7 |
| 17 | [Prompt Engineering](17-prompt-engineering/README.md) | DAIR Prompt Engineering Guide, Anthropic prompt docs, DSPy, TextGrad, bộ sưu tập system prompt |
| 18 | [Hệ sinh thái Việt Nam](18-vietnam-community/README.md) | PhoGPT, Vistral, URA-LLaMA; underthesea, VnCoreNLP; ViGen; VinAI, VietAI, Zalo AI, hackathon 2026 |
| 19 | [Agentic Video & Media](19-agentic-video-media/README.md) | **OpenMontage** (67k★, agent là orchestrator: director skills + schema + gate + cost tracker), làn sóng video/motion skills cho Claude Code, Open-Sora, HunyuanVideo, CogVideoX, Remotion |
| 20 | [Claude Plugins Ecosystem](20-claude-plugins-ecosystem/README.md) | **anthropics/knowledge-work-plugins** (29k★, 123 plugin: 22 theo vai trò + 101 vendor), **claude-plugins-official** (37,7k★, 31 plugin nội bộ + >135 vendor, quy ước `renames`/skill-bundle), giải phẫu plugin/SKILL.md/marketplace.json, so sánh với Cursor/Copilot/OpenAI Apps |
| 21 | [Autonomous Workflows](21-autonomous-workflows/README.md) | **Harness dài hạn của Anthropic** (11/2025 & 3/2026), Claude Code Routines vs Desktop tasks vs `/loop` (jitter, 7 ngày, loop.md), GitHub Agentic Workflows (gh-aw), durable execution (Temporal, Restate, Inngest, DBOS, LangGraph), Activepieces/Kestra/Windmill/Huginn, lịch sử AutoGPT/BabyAGI, failure modes + circuit breaker, METR |
| 22 | [Motion Design & Animation](22-motion-design-animation/README.md) | **16 repo "video as code"**: HyperFrames (61k★), Remotion (63k★) + skills, GSAP skills, Motion, LottieFiles skill; skill pack launch video / hậu kỳ / hoạt hình (product-launch-motion, motion-graphics-skills, claude-motion-design, hyperframes-student-kit, Barty-Bart, animate, claude-motion, claude-remotion-skill), **motionmaxxing**; kiểm chứng từng claim của bài đăng viral |
| — | [data/projects.json](data/projects.json) · [data/projects.csv](data/projects.csv) | Catalog máy-đọc-được (tên, repo, loại, license, sao ước lượng, ghi chú) |
| — | [SOURCES.md](SOURCES.md) | Toàn bộ URL nguồn đã dùng |
| — | [TEMPLATE.md](TEMPLATE.md) | Mẫu để thêm dự án mới vào kho |
| — | [WORKFLOW.md](WORKFLOW.md) | **Quy trình khi nhận link**: nghiên cứu đa nguồn → phân tích → cập nhật kho |
| — | [.github/workflows/lint.yml](.github/workflows/lint.yml) · [scripts/check_catalog.py](scripts/check_catalog.py) | CI: markdownlint (cấu hình `.markdownlint-cli2.yaml`) + kiểm tra catalog JSON/CSV; check bắt buộc cho `main` |

---

## 🔭 Bức tranh tổng thể (tóm tắt phân tích)

### 1. Coding agent đã trở thành "mặt tiền" của AI cho lập trình viên

- Nhóm **CLI agent mã nguồn mở** bùng nổ: OpenCode (~210k★), DeepSeek Harness (~200k★ chỉ sau 2 tuần, 8/2026), Codex CLI (~127k★), Gemini CLI (~107k★), Cline (~69k★), OpenHands (~90k★). Claude Code (~148k★) phổ biến nhưng **không** mã nguồn mở.
- **Benchmark bão hòa**: SWE-bench Verified đạt ~97% (Claude Opus 5 + mini-SWE-agent, 9/2026) và Vals ngừng chấm model mới; chuyển sang **SWE-bench Pro** (top ~65%). Số sao ≠ chất lượng sản xuất.
- Xu hướng kiến trúc: **"harness"** (vòng lặp + công cụ + ngữ cảnh) quan trọng hơn bản thân model; DeepSeek Harness biến mọi thứ thành plugin, mini-SWE-agent chứng minh 100 dòng code đủ để >74% SWE-bench.

### 2. Framework agent: từ "framework chiến tranh" sang hợp nhất và chuẩn hóa

- LangGraph dẫn đầu về lượt tải (34.5M/tháng PyPI) dù ít sao hơn AutoGen/CrewAI; AutoGen + Semantic Kernel hợp nhất thành **Microsoft Agent Framework** (GA 4/2026).
- OpenAI Agents SDK, PydanticAI, smolagents là nhóm "nhẹ, typed, tối giản" đang lên.
- OpenClaw (~390k★, assistant cá nhân tự host) cho thấy nhu cầu "agent cá nhân chạy trên máy mình" cực lớn.

### 3. Vòng lặp agentic (agentic loop) là khái niệm trung tâm

- Anthropic: *"agent = LLM dùng tool trong vòng lặp dựa trên phản hồi môi trường"*; 5 workflow: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.
- ReAct (2022) và Plan-and-Execute là 2 hình dạng vòng lặp chủ đạo; Reflexion thêm tự-phê-bình.
- **Ralph Wiggum loop** (`while :; do cat PROMPT.md | claude; done`) → được Anthropic đóng gói thành plugin `ralph-loop` dùng Stop hook; hội tụ tốt khi task **có thể kiểm chứng** (test/lint/build).
- **Context engineering / harness engineering** trở thành kỹ năng cốt lõi: KV-cache hit rate, nén/chọn/cô lập ngữ cảnh, git worktree để chạy song song nhiều agent.

### 4. Giao thức mở đang định hình "hệ điều hành agent"

- **MCP** (tool/data ↔ agent, >10k server, đã vào Agentic AI Foundation/Linux Foundation 12/2025).
- **A2A** (agent ↔ agent, v1.0 3/2026, >150 tổ chức).
- **AG-UI** (agent ↔ giao diện người dùng, CopilotKit khởi xướng, được AWS/Microsoft/Oracle tích hợp).
- **Agent Skills / SKILL.md** (10/2025, chuẩn mở 12/2025, agentskills.io) đang thay thế `.cursorrules`; `AGENTS.md` là lớp hướng dẫn chung cho nhiều tool.

### 5. UI/UX & design: "sở hữu mã nguồn" và chống "AI slop"

- **shadcn/ui** (~115–121k★) thắng nhờ mô hình copy-paste; từ 7/2026 mặc định dùng **Base UI** thay Radix.
- Design tool mở: Penpot (~61k★, thay Figma), Excalidraw (~134k★), tldraw (~51k★), Onlook (visual editor cho React).
- AI sinh UI: v0.app, Lovable, Bolt (đóng), Google Stitch, MagicPath; **Taste Skill** (~46k★) là skill chống giao diện "generic" cho coding agent.
- Lớp "agentic UI": CopilotKit, assistant-ui, Vercel AI SDK + AI Elements.

### 6. Eval & observability là mảnh ghép bắt buộc để lên production

- Langfuse (tracing, MIT core) + Promptfoo (CI gate, red-team) + DeepEval/Ragas (metric) là stack miễn phí phổ biến.

### 7. Hạ tầng quanh agent đang chuẩn hóa thành các lớp riêng

- **Memory** (Mem0, Graphiti, Letta), **sandbox** (E2B Firecracker, Modal gVisor), **browser** (Browser Use ~114k★, Stagehand), **guardrails** (NeMo, LLM Guard) tách khỏi framework agent; OWASP đã có Top 10 riêng cho Agentic (12/2025) và MCP (2026).
- **Spec-driven development** (Spec Kit, Kiro, BMAD) và **AI code review** (CodeRabbit, Greptile, Qodo) khép kín vòng: spec → agent code → review bot → checklist deploy.

### 8. Voice, multimodal và data agent đã đủ chín để tự host

- Pipecat/LiveKit + Whisper + Kokoro/Chatterbox cho voice agent mở; ComfyUI thắng cuộc đua UI sinh ảnh; DuckDB (40k★) + Vanna/PandasAI + marimo là stack "hỏi dữ liệu bằng ngôn ngữ tự nhiên".
- Docs-for-AI: llms.txt vẫn là đề xuất (adoption 2–10%), Context7 (MCP) mới là cách coding agent lấy docs; prompt engineering chuyển thành **context engineering + DSPy**.
- Việt Nam: PhoGPT/underthesea là nền, ViGen (dataset quốc gia) và loạt hackathon 2026 cho thấy cộng đồng chuyển từ outsourcing sang AI building.

### 9. "Skills-as-orchestrator" và "ideation-as-skill" là hai mẫu mới đáng theo dõi

- **OpenMontage** (67k★) không có orchestrator bằng code: agent đọc AGENT_GUIDE, đi qua 7 stage cố định với director skill, JSON schema, approval gate per-stage, registry runtime và decision log append-only. Đây là bản mở rộng của SKILL.md sang workflow sáng tạo nhiều provider.
- **ADHD** (4.4k★) đóng gói parallelization + evaluator thành một skill cho bài open-ended: 5 nhánh cô lập dưới các "cognitive frame", critic chấm/prune/deepen; chi phí 5–10×, bằng chứng tự báo cáo và giới chuyên gia còn đòi thêm proof.

### 10. Plugin "không code" trở thành đơn vị phân phối tri thức nghề nghiệp

- `anthropics/knowledge-work-plugins`: 123 plugin toàn markdown + JSON (skills, .mcp.json), 101 trong đó là vendor pin theo commit sha. Plugin `sales` tăng từ 9 lên 36 skill trong một tháng. Skill `call-prep` là mẫu chuẩn về tool-agnostic + guardrail chống prompt injection ("data, never instructions"). Chi phí thật của plugin là context mỗi lượt.

### 11. Skill "mang theo kit + kiểm chứng bằng máy" là thế hệ skill mới

- `wheresryan22/anatomy` (3.8k★ sau 2 ngày): skill vẽ minh họa isometric không chỉ là prompt mà kèm thư viện hình học không phụ thuộc, audit hình học, headless-Chrome screenshot, đếm line-end và bộ eval; sizing (Figure/Hero/Epic) trước khi làm để kiểm soát chi phí. Cùng tinh thần với OpenMontage (mục 19) và deployment-checklist (mục 09): agent phải **chứng minh** output.

### 12. Checklist "máy đọc được" cho agent là xu hướng DevSecOps mới

- `PinoyFreeCoder/deployment-checklist`: cùng một checklist, người tick tay hoặc agent audit repo và trả **GO/NO-GO** với bằng chứng file:dòng; minh họa evaluator pattern + nguyên tắc "evidence or it's a FAIL", report-only, con người ký cuối.

### 13. Autonomous workflow = loop có ràng buộc + harness có bộ nhớ ngoài + trigger không cần người

- Anthropic (11/2025, 3/2026): progress file + feature list JSON + git + browser test; planner/generator/evaluator; **harness có hạn sử dụng** (Opus 4.5/4.6 làm reset và sprint trở nên thừa). Claude Code tách ba tầng lập lịch: Routines (cloud, ≥1h), Desktop tasks, `/loop` (7 ngày, 50 task, jitter). gh-aw đưa "prompt-as-workflow" lên GitHub Actions với `safe-outputs`. Mọi loop tự trị cần 4 số: max vòng, ngân sách (circuit breaker 80/90/100%), timeout, ngày hết hạn. Xem mục 21.

### 14. "Hiểu codebase" trở thành plugin trending: tất định + LLM

- `Egonex-AI/Understand-Anything` (85,9k★, +2.331★/ngày): Tree-sitter cho cấu trúc (tất định, incremental) + LLM cho ngữ nghĩa, pipeline 7 agent có `graph-reviewer`, một lõi nhiều host (Claude Code, Cursor, Codex, Copilot, Gemini CLI…), output tiếng Việt. Cùng ngày `anthropics/claude-plugins-official` (+2.172★/ngày) cho thấy kênh phân phối "cài plugin" đang thắng "chép prompt". Xem mục 01 §3b, mục 20 §2b.

### 15. Motion design "video as code": engine chính thức + lớp skill có gu

- Hai engine (HyperFrames HTML thuần của HeyGen, Remotion React) và ba skill chính thức (remotion/skills, gsap-skills, LottieFiles motion-design-skill) là nền; 10 skill cộng đồng 1–3 tuần tuổi ra đời ngay sau Opus 5.5 (22/9/2026) bọc thêm "gu" + gate: storyboard duyệt trước render, timeline.json là nguồn sự thật, contact sheet 1 frame/beat, lint/LUFS bằng script, "không claim done khi chưa re-render". Bài đăng viral phóng đại (link sản phẩm, 120fps, mili-giây, "Netflix engineers"); số ★ aggregator ở mục 19 lệch ~100 lần → đã sửa. Xem mục 22.

---

## 🧭 Cách dùng kho này

1. Đọc README của chuyên mục để nắm bối cảnh và bảng so sánh.
2. Dùng `data/projects.json` khi cần lọc/tra cứu bằng script.
3. Thêm dự án mới theo [TEMPLATE.md](TEMPLATE.md); luôn ghi ngày và nguồn cho số sao.
   Khi gửi link mới, kho được cập nhật theo [WORKFLOW.md](WORKFLOW.md) (đọc nguồn gốc, tác giả, nguồn ngoài, dự án tương tự, phân tích, ghi vào kho).
4. Mọi nhận định "nổi tiếng/dẫn đầu" đều gắn mốc thời gian 10/2026 – cần cập nhật định kỳ (gợi ý: mỗi quý).

## ⚠️ Lưu ý về độ tin cậy

- Nhiều nguồn là blog so sánh/SEO; các con số đã được đối chiếu chéo nhưng vẫn là ước lượng.
- Một số sự kiện chưa xác minh độc lập được đánh dấu **(chưa xác minh)** trong từng mục (ví dụ: Flowise bị archive 8/2026, A2A chuyển vào AAIF 8/2026).
