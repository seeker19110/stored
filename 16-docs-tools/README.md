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

## 2b. Repo nổi tiếng bổ sung (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **vuejs/vitepress** | 18,4k | MIT | commit 11/10/2026; v2.0.0-alpha.20 (4/9) | SSG trên Vite + Vue; dựng docs của Vite, Rollup, Pinia, Vitest, D3; docs Vue chính thức dựa trên nó | v2 vẫn alpha; theme thiên về Vue |
| **rust-lang/mdBook** | 22,2k | MPL-2.0 | commit 12/10/2026; v0.5.4 (6/7) | Dự án chính thức rust-lang, dùng dựng The Rust Book | Vẫn 0.x; dạng sách, không phải framework site docs đầy đủ |
| **sphinx-doc/sphinx** | 8,1k | BSD-2-Clause | commit 18/9/2026; 9.1.0 (31/12/2025) | Chuẩn docs Python, dựng docs.python.org; xuất HTML, LaTeX/PDF, ePub, Texinfo | Chưa có release nào trong 2026 |
| **zensical/zensical** | 5,9k | MIT | commit 12/10/2026; 0.0.69 (8/10) | SSG mới của nhóm Material for MkDocs (kế nhiệm ở §1); sửa lỗi xuất llms.txt ngày 8/10/2026 (#1019) | Trước 1.0 (0.0.x); tương thích MkDocs một phần **(chưa xác minh)** |
| **docsifyjs/docsify** | 31,5k | MIT | commit 12/10/2026; v5.0.0 (23/7) | Render Markdown ngay trên trình duyệt, không cần build; v5 ổn định sau thời gian dài RC | Render phía client bất lợi cho SEO và crawler LLM **(chưa xác minh)** |
| **yamadashy/repomix** | 28,8k | MIT | commit 11/10/2026; v1.18.1 (21/9) | Gói cả repo thành một file cho AI: đếm token từng file, quét secret bằng Secretlint mặc định, chế độ MCP server | `--compress` còn thử nghiệm; MCP server đọc mọi đường dẫn trừ khi bật `--sandbox` |
| **AsyncFuncAI/deepwiki-open** | 18,2k | MIT | commit 3/9/2026 | Tự host wiki AI cho repo GitHub/GitLab/Bitbucket; có Docker, Ollama, LiteLLM; **có README tiếng Việt** (`README.vi.md`) | README nay quảng bá bản hosted "Grok Wiki"; không có release |
| **coderamp-labs/gitingest** | 15,9k | MIT | **nhánh main đứng từ 16/8/2025** | Đổi "hub" thành "ingest" trong URL GitHub để lấy bản tóm code cho LLM | Chỉ nhánh bot Renovate còn chạy → ưu tiên repomix |

**Nhận xét:** nhóm "đưa codebase cho AI" (repomix, deepwiki-open, gitingest) bổ trợ cho llms.txt/Context7 ở §2: llms.txt dành cho docs đã xuất bản, còn repomix/DeepWiki dành cho mã nguồn chưa có docs. Khi chạy MCP của repomix, bật `--sandbox` để giới hạn thư mục được đọc. Đã cân nhắc nhưng không thêm: shuding/nextra (13,9k★, không commit từ 6/2026, không release trong 2026), mintlify/starter (1,9k★, chỉ là template của nền tảng đóng).

## 3. Nguồn

- https://www.mintlify.com/library/best-llms-txt-platforms · https://dupple.com/learn/best-documentation-tools · https://ekline.io/blog/docusaurus-alternatives · https://www.pkgpulse.com/guides/best-documentation-frameworks-2026 · https://docsalot.dev/blog/best-mintlify-alternatives · https://affine.pro/blog/best-technical-documentation-software-tools-for-developers
- https://upstash.com/blog/context7-llmtxt-cursor · https://upstash.com/blog/new-context7 · https://glama.ai/mcp/servers/upstash/context7 · https://www.npmjs.com/package/@upstash/context7-mcp · https://tooldirectory.ai/tools/context7
- https://codersera.com/blog/llms-txt-complete-guide-2026/ · https://limy.ai/blog/llms-txt-in-2026-the-full-guide · https://aisaasradar.com/article/llms-txt-adoption-data-2026 · https://seeklab.io/blog/what-is-llmstxt-the-honest-2026-guide/
- §2b (12/10/2026): https://github.com/vuejs/vitepress · https://github.com/rust-lang/mdBook · https://github.com/sphinx-doc/sphinx · https://github.com/zensical/zensical · https://github.com/docsifyjs/docsify · https://github.com/yamadashy/repomix · https://github.com/AsyncFuncAI/deepwiki-open · https://github.com/coderamp-labs/gitingest · https://github.com/shuding/nextra · https://github.com/mintlify/starter
