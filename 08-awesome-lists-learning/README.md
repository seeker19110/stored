# 08 · Awesome Lists, Repo học tập & Repo nổi tiếng nhất GitHub

## 1. Repo nhiều sao nhất toàn GitHub (9–10/2026, ước lượng)

| # | Repo | ★ | Nội dung |
|---|---|---|---|
| 1 | codecrafters-io/build-your-own-x | ~547–552k | Tự xây lại công nghệ từ đầu (DB, OS, compiler…) |
| 2 | sindresorhus/awesome | ~400k+ | Awesome của mọi awesome |
| 3 | public-apis/public-apis | ~380k+ | API công khai |
| 4 | freeCodeCamp/freeCodeCamp | ~455k | Chương trình học lập trình miễn phí |
| 7–8 | kamranahmedse/developer-roadmap | ~360–368k | Lộ trình nghề (frontend, backend, AI engineer…) |
| 7–8 | donnemartin/system-design-primer | ~357–372k | Thiết kế hệ thống |
| – | openclaw/openclaw | ~390k | Agent cá nhân (xem mục 02) |

Theo dõi tự động: `EvanLi/Github-Ranking` (cập nhật hằng ngày), gitstarclub.com/rankings.

## 2. Awesome list theo chủ đề của kho này

| Chủ đề | Repo | Ghi chú |
|---|---|---|
| LLM apps / agents thực hành | `Shubhamsaboo/awesome-llm-apps` (~105k★) | 100+ agent, skill, RAG app có code |
| Claude Code | `hesreallyhim/awesome-claude-code` (~37–55k★) · `rohitg00/awesome-claude-code-toolkit` | Skills, hooks, commands, agents, plugins |
| Agent skills | `VoltAgent/awesome-agent-skills` (1000+) · `spencerpauly/awesome-cursor-skills` | Tương thích Claude Code/Codex/Gemini CLI/Cursor |
| Cursor rules (legacy) | `PatrickJS/awesome-cursorrules` · cursor.directory | Chuyển dần sang skills |
| Agent frameworks | `kaushikb11/awesome-llm-agents` · `aloth/awesome-ai-agents` · `e2b-dev/awesome-ai-agents` | |
| MCP | `wong2/awesome-mcp-servers` · `punkpeye/awesome-mcp-servers` · `sadekxD/Awesome-MCP` | |
| Generative UI | `narrowin/awesome-generative-ui` | LLM sinh UI động |
| AI tools cho UI | `maxbogo/awesome-ai-tools-for-ui` | Gồm Taste Skill, Refactoring UI skill |
| Design systems | `klaufel/awesome-design-systems` | |
| Design resources | `bradtraversy/design-resources-for-developers` | |
| Prompt engineering | `dair-ai/Prompt-Engineering-Guide` · `f/awesome-chatgpt-prompts` | |
| GitHub topics | github.com/topics/agent-skills · /claude-skills · /awesome-ai · /ai-agents | Khám phá theo tag |

## 2b. Khoá học & repo học LLM/agent chất lượng cao (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao đáng học | Lưu ý |
|---|---|---|---|---|---|
| **microsoft/generative-ai-for-beginners** | 121,2k | MIT | 12/10/2026 | 21 bài, hơn 50 bản dịch **có tiếng Việt** (`translations/vi`) | Thiên về Azure; README báo vài bài cũ sau khi GitHub Models ngừng (chưa tự kiểm) |
| **rasbt/LLMs-from-scratch** | 106,4k | Apache-2.0 | 2/10/2026 | Code đi kèm sách Manning *Build a LLM (From Scratch)*, chương 1–7 + phụ lục; vẫn cập nhật | Phần giải thích đầy đủ nằm trong sách trả phí |
| **mlabonne/llm-course** | 83,5k | Apache-2.0 | 2/2026 | Lộ trình 3 nhánh (nền tảng, LLM Scientist, LLM Engineer) + notebook Colab | Phần lớn là link tuyển chọn; ít commit |
| **microsoft/ai-agents-for-beginners** | 77,0k | MIT | 12/10/2026 | 18 bài về agent, rất tích cực (2.067 commit), **có bản tiếng Việt** | Gắn với Microsoft Agent Framework / Foundry (mục 02) |
| **labmlai/annotated_deep_learning_paper_implementations** | 67,5k | MIT | 1/2026 | Hơn 60 paper cài bằng PyTorch, chú thích từng dòng (nn.labml.ai) | README nói thêm hằng tuần nhưng commit cuối 1/2026 |
| **karpathy/nanochat** | 58,6k | MIT | 7/2026 | Karpathy: ChatGPT tối giản toàn bộ chuỗi tokenizer → pretrain → SFT → eval → inference, ~US$48 (~2 giờ trên 8×H100) | Chạy đầy đủ cần node 8×H100. **nanoGPT (63,7k★) đã deprecated** và trỏ sang nanochat; llm.c (31,1k★) không commit từ 5/2025 |
| **huggingface/agents-course** | 33,5k | Apache-2.0 | 6/10/2026 | 4 unit có chứng chỉ, bài cuối chấm trên leaderboard; smolagents, LangGraph, LlamaIndex | Thiên về hệ sinh thái HF |
| **NirDiamant/RAG_Techniques** | 29,8k | **phi thương mại (riêng)** | 11/10/2026 | Hơn 42 notebook RAG chạy được, rộng nhất hiện có | Cấm dùng thương mại; README nhiều quảng cáo. GenAI_Agents (24,6k★) cùng tác giả cũng license phi thương mại |
| **chiphuyen/aie-book** | 17,8k | không có LICENSE | 7/2026 | Tài liệu đi kèm sách *AI Engineering* (O'Reilly): mục lục, tóm tắt, case study | Không phải nội dung sách; ít code |

Thứ tự gợi ý cho người mới: `generative-ai-for-beginners` (bản tiếng Việt) → `ai-agents-for-beginners` → `agents-course` (có bài chấm) → `LLMs-from-scratch` hoặc `nanochat` nếu muốn hiểu bên trong model.

## 3. Tài liệu nền tảng nên đọc (thứ tự gợi ý)

1. Anthropic – *Building Effective Agents* → *Effective Context Engineering for AI Agents* → *Writing tools for agents*.
2. ReAct (Yao 2022), Reflexion (Shinn 2023), *Landscape of Emerging AI Agent Architectures* (2024).
3. Manus – *Context Engineering for AI Agents: Lessons from Building Manus* (2025).
4. *Harness Engineering: Source-Code Study of Eleven Systems* (arXiv 2609.00006, 2026).
5. Geoffrey Huntley – *Ralph* (ghuntley.com/ralph) + README plugin `ralph-wiggum`.
6. agentskills.io spec · modelcontextprotocol.io spec · a2a-protocol.org spec · docs.ag-ui.com.
7. Refactoring UI · Laws of UX.
8. Alex Xu – *System Design Interview* Vol 1&2 (ghi chú 28 chương trong `seeker19110/system-design-notes`, kèm ~25 link paper gốc: Dynamo, Bigtable, Raft, Kafka…; upstream/license chưa rõ) · `ai-engineering-from-scratch` (được dhcb `2026-10-05-ai-engineering-source-inventory.md` liệt kê; chưa xác minh).

## Nguồn

- https://gitstarclub.com/rankings · https://www.countly.net/most-starred-github-repositories-june-2026 · https://www.stackscan.com/blog/github-statistics · https://github.com/EvanLi/Github-Ranking · https://www.firecrawl.dev/blog/best-github-repos
- https://github.com/Shubhamsaboo/awesome-llm-apps · https://github.com/hesreallyhim/awesome-claude-code · https://github.com/rohitg00/awesome-claude-code-toolkit · https://claudefa.st/blog/tools/resources/awesome-claude-code · https://github.com/topics/agent-skills · https://github.com/topics/claude-skills
- https://github.com/kaushikb11/awesome-llm-agents · https://github.com/aloth/awesome-ai-agents
- §2b (12/10/2026): https://github.com/microsoft/generative-ai-for-beginners · https://github.com/rasbt/LLMs-from-scratch · https://github.com/mlabonne/llm-course · https://github.com/microsoft/ai-agents-for-beginners · https://github.com/labmlai/annotated_deep_learning_paper_implementations · https://github.com/karpathy/nanochat · https://github.com/karpathy/nanoGPT · https://github.com/karpathy/llm.c · https://github.com/huggingface/agents-course · https://github.com/NirDiamant/RAG_Techniques · https://github.com/NirDiamant/GenAI_Agents · https://github.com/chiphuyen/aie-book · https://github.com/datawhalechina/happy-llm (34,3k★, tiếng Trung, CC BY-NC-SA)
