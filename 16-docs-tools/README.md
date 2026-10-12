# 16 · Documentation Tools & Docs-for-AI (llms.txt, Context7)

## 1. Framework tài liệu
| Công cụ | Repo | License | Định vị | llms.txt |
|---|---|---|---|---|
| **Docusaurus** (Meta) | facebook/docusaurus | MIT | React, 3.10 là bản 3.x cuối, v4 canary | plugin `docusaurus-plugin-llms` |
| **Material for MkDocs → Zensical** | squidfunk/mkdocs-material · zensical | MIT | Python docs-as-code; Zensical là kế nhiệm | `mkdocs-llmstxt` |
| **Starlight** (Astro) | withastro/starlight | MIT | Nhẹ, content-first | `starlight-llms-txt` |
| **Fumadocs** | fuma-nama/fumadocs | MIT | React: Next.js, TanStack Start, React Router | |
| **Mintlify** | (SaaS, CLI mở) | – | Hosted, tự sinh llms.txt, llms-full.txt, .md mỗi trang | Có sẵn |
| GitBook, ReadMe, Docsify, VitePress, Sphinx | – | – | | GitBook có sẵn |

## 2. Docs cho AI agent
| Thành phần | Nội dung | Trạng thái 2026 |
|---|---|---|
| **llms.txt** (Jeremy Howard, Answer.AI, 9/2024) | File markdown tại root tóm tắt site cho LLM; v2 8/2026 **(chưa xác minh)** | Vẫn là đề xuất, chưa phải chuẩn web; adoption 2–10% tùy khảo sát; Google Search & OpenAI không dùng; **giá trị thật nằm ở coding agent** (Cursor, Claude Code, Copilot, Cline). Anthropic, Stripe, Mintlify đều xuất bản |
| **Context7** (Upstash) | MCP server `resolve-library-id` + `query-docs` trả docs phiên bản mới nhất cho LLM; server MIT, backend parse đóng; v4.x 9/2026; giảm ~65% token (theo Upstash) | Trong top MCP server phổ biến nhất (mục 04) |
| **DeepWiki / GitHub Copilot docs** | Wiki tự sinh từ repo | |
| AGENTS.md / CLAUDE.md / SKILL.md | Tài liệu "cho agent" ngay trong repo | Mục 04 |

**Nhận định:** tài liệu tốt cho AI = tài liệu tốt cho người + markdown sạch + phiên bản rõ ràng + có endpoint máy đọc (llms.txt hoặc MCP).

## 3. Nguồn
- https://www.mintlify.com/library/best-llms-txt-platforms · https://dupple.com/learn/best-documentation-tools · https://ekline.io/blog/docusaurus-alternatives · https://www.pkgpulse.com/guides/best-documentation-frameworks-2026 · https://docsalot.dev/blog/best-mintlify-alternatives · https://affine.pro/blog/best-technical-documentation-software-tools-for-developers
- https://upstash.com/blog/context7-llmtxt-cursor · https://upstash.com/blog/new-context7 · https://glama.ai/mcp/servers/upstash/context7 · https://www.npmjs.com/package/@upstash/context7-mcp · https://tooldirectory.ai/tools/context7
- https://codersera.com/blog/llms-txt-complete-guide-2026/ · https://limy.ai/blog/llms-txt-in-2026-the-full-guide · https://aisaasradar.com/article/llms-txt-adoption-data-2026 · https://seeklab.io/blog/what-is-llmstxt-the-honest-2026-guide/
