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

## 2c. Case study: CodeFlow, bản đồ kiến trúc codebase chạy trong trình duyệt (link người dùng gửi, 2026-10-12)

> Đã clone toàn bộ repo (215 commit, HEAD `b0e82d1`, 22/9/2026), grep `index.html`, `cli/codeflow.mjs`, `card/`, workflow CI và chạy bộ test (`node --test`: 231 pass, 1 skip, 0 fail).

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/braedonsaunders/codeflow · bản host: https://codeflow-five.vercel.app/ |
| Mô tả 1 dòng | Dán URL GitHub hoặc mở thư mục local → đồ thị phụ thuộc file, blast radius, owner theo git, quét bảo mật cơ bản, điểm sức khoẻ A–F; tất cả trong một `index.html` |
| Loại | codebase-knowledge (công cụ đọc hiểu codebase, không dùng LLM) |
| License | MIT (có file LICENSE); thư viện vendor kê trong `vendor/THIRD_PARTY_NOTICES.md` |
| ★ (ngày) | ~5,4k★, 820 fork, 27 watcher, 3 PR mở (2026-10-12, trang GitHub) |
| Tác giả | Braedon Saunders (Canada, 204 follower); repo khác nhỏ hơn nhiều: homerun 203★, bidwright 63★ |
| Lịch sử | 15/12/2025 → 22/9/2026; 60 commit của "Cursor Agent", 37 commit của "Claude", 4 của cursor[bot] → ~47% commit do agent viết; vài PR của người ngoài (ví dụ #104 sửa parse `owner/repo/`) |

**Kiến trúc thật (đã grep, không theo README):**

- `index.html` ~15.500 dòng: React 18 + D3 + 3d-force-graph + Mermaid + jsPDF + JSZip, chạy bằng Babel trong trình duyệt; parse bằng acorn (JS/TS) và **tree-sitter WASM** (Python và các ngôn ngữ khác). Mọi script tải từ `vendor/` trong repo, không có CDN. Blog/skill listing cũ ghi "tải React/D3/Babel từ CDN" là đã lỗi thời.
- Host mạng duy nhất trong mã là `api.github.com` / `github.com`; không có analytics hay beacon. `localStorage` chỉ giữ tuỳ chọn giao diện; token GitHub nằm trong biến JS (`GitHub.token`), không ghi vào storage và không đưa vào link chia sẻ. Khớp với mục "Privacy First" của README.
- "Recent analyses" lưu vào IndexedDB `codeflow-recents`, nhưng `compactAnalysisForCache` xoá `content` và đoạn code trước khi lưu. Chỉ metadata (đường dẫn, tên hàm, chỉ số) ở lại trên máy.
- CLI `npx codeflow .` (Node ≥18) bind `127.0.0.1` và kiểm header `Host` thuộc loopback (chống DNS rebinding), giống mô hình bridge loopback ở mục 12 §3b.
- **CodeFlow Card** (GitHub Action `node24`, không có dependency npm): cắt khối `CODEFLOW_ANALYZER_START…END` trong `index.html` rồi chạy bằng `vm` của Node, nên web app và Action dùng chung một bộ phân tích. Action cần `contents: write` để commit SVG, và cần `pull-requests: write` nếu bật `receipts`.
- CI: chỉ `node --test` (Node 20) và CodeQL (bỏ qua `vendor/**`).

**Hạn chế / rủi ro:**

- Đồ thị phụ thuộc dựa trên import tĩnh, nên blast radius bỏ sót dynamic import, reflection, DI và route theo chuỗi. Các mục "Security Scanner", "Pattern Detection" và "Health Score" là heuristic regex/AST, không thay được Semgrep hay CodeQL (mục 12 §3d).
- Chế độ **GitHub App** yêu cầu dán *App ID + private key* vào trang để ký JWT ngay trong trình duyệt (`jsrsasign`). Trên bản host ở Vercel, khoá đó nằm trong một trang web do người khác deploy; chỉ dùng chế độ này với bản tự host đã đọc code, hoặc dùng PAT fine-grained chỉ đọc.
- Bản host không có gì chứng minh nó build từ đúng commit trên GitHub. Với code riêng tư, nên clone rồi mở `index.html` local hoặc chạy CLI.
- Tag `v1` của Action đứng ở `af3b007` (6/7/2026), sau đó còn 89 commit (8 file trong `card/` đã đổi). Ví dụ dùng `@v1` nên **ghim theo SHA**, như quy tắc ở mục 12 §3.
- Một file 15k dòng, gần nửa commit do agent viết, bus factor 1. Bộ test (232 case, có fixture theo ngôn ngữ và test hiệu năng repo lớn) là cổng máy chính.

**So sánh (★ đọc 12/10/2026):**

| Công cụ | ★ | License | Cách tiếp cận | Khác CodeFlow |
|---|---|---|---|---|
| `ahmedkhaleel2004/gitdiagram` | 18,1k | MIT | LLM sinh sơ đồ kiến trúc + video giải thích | Gửi cấu trúc repo cho server và LLM (OpenAI/OpenRouter); CodeFlow không dùng LLM và không có backend |
| `sverweij/dependency-cruiser` | 7,3k | MIT | CLI kiểm và vẽ phụ thuộc JS/TS theo **rule** | Dùng làm cổng CI được (cấm import vòng, cấm tầng gọi ngược); CodeFlow chỉ để xem |
| `MaibornWolff/codecharta` | 547 | BSD-3-Clause | Bản đồ "thành phố" 3D từ chỉ số code | Cần bước phân tích riêng; mạnh về metric, yếu về đồ thị file |
| `Understand-Anything` (mục 01 §3b) · `repomix` / `deepwiki-open` (§2b) | — | — | Đưa codebase cho agent đọc | Phục vụ LLM; CodeFlow phục vụ người đọc |

**Tích hợp:**

1. Xem nhanh repo lạ: `git clone https://github.com/braedonsaunders/codeflow && open codeflow/index.html`, hoặc `node cli/codeflow.mjs <thư mục>` để tự cập nhật khi file đổi (chỉ trên loopback).
2. Lấy dữ liệu cho script hoặc agent: nút Export → JSON (file, hàm, phụ thuộc, churn, vấn đề bảo mật, vi phạm tầng). Có thể đưa file này cho agent làm bản đồ trước khi sửa code.
3. Badge sức khoẻ: `uses: braedonsaunders/codeflow/card@<sha>` kèm `permissions: contents: write`; để `receipts: false` nếu không muốn bot bình luận trên PR. Có `show-grade: false` cho README công khai.
4. Muốn chặn kiến trúc xấu trong CI thì dùng dependency-cruiser (JS/TS) hoặc import-linter (Python), không dùng điểm A–F của CodeFlow.

## 3. Nguồn

- https://www.mintlify.com/library/best-llms-txt-platforms · https://dupple.com/learn/best-documentation-tools · https://ekline.io/blog/docusaurus-alternatives · https://www.pkgpulse.com/guides/best-documentation-frameworks-2026 · https://docsalot.dev/blog/best-mintlify-alternatives · https://affine.pro/blog/best-technical-documentation-software-tools-for-developers
- https://upstash.com/blog/context7-llmtxt-cursor · https://upstash.com/blog/new-context7 · https://glama.ai/mcp/servers/upstash/context7 · https://www.npmjs.com/package/@upstash/context7-mcp · https://tooldirectory.ai/tools/context7
- https://codersera.com/blog/llms-txt-complete-guide-2026/ · https://limy.ai/blog/llms-txt-in-2026-the-full-guide · https://aisaasradar.com/article/llms-txt-adoption-data-2026 · https://seeklab.io/blog/what-is-llmstxt-the-honest-2026-guide/
- §2b (12/10/2026): https://github.com/vuejs/vitepress · https://github.com/rust-lang/mdBook · https://github.com/sphinx-doc/sphinx · https://github.com/zensical/zensical · https://github.com/docsifyjs/docsify · https://github.com/yamadashy/repomix · https://github.com/AsyncFuncAI/deepwiki-open · https://github.com/coderamp-labs/gitingest · https://github.com/shuding/nextra · https://github.com/mintlify/starter
- §2c (12/10/2026): https://github.com/braedonsaunders/codeflow (clone đầy đủ, HEAD `b0e82d1`: README.md, index.html, cli/codeflow.mjs, card/action.yml, card/lib/analyzer.js, card/README.md, .github/workflows/, tests/) · https://codeflow-five.vercel.app/ · https://github.com/braedonsaunders · https://themenonlab.blog/blog/codeflow-github-architecture-visualizer · https://www.skills.sh/akillness/jeo-skills/codeflow · https://github.com/ahmedkhaleel2004/gitdiagram · https://github.com/sverweij/dependency-cruiser · https://github.com/MaibornWolff/codecharta
