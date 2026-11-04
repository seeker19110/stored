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
| **Context7** (Upstash) | MCP `resolve-library-id` + `query-docs`, CLI/SDK lấy docs theo thư viện/version; **phải kiểm phiên bản thực được trả**, vì version chưa index có thể fallback (§2i). Mã client/MCP MIT, mặc định gọi API Context7 | Truy vấn được gửi tới API; chạy MCP local không đồng nghĩa có toàn bộ index local (§2i) |
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

## 2d. Cụm "Code Knowledge Graph cho agent" (ảnh "Top Code Knowledge Graph Tools", 2026-10-12)

> Ảnh người dùng gửi xếp 3 tool: Graphify (125k+★), Understand-Anything (85k+★), codegraph (73k+★). **Số sao đều thật** (kiểm bằng shields `github/stars`: 126k / 86k / 74k, 12/10/2026) — khác với cảnh báo "aggregator phóng sao" ở mục 19; ở đây sao thật nhưng khung "Top 3" là marketing (các trang dẫn ảnh là betterstack/augmentcode/mindstudio kiểu quảng cáo). Đã clone cả ba, đọc README + license + telemetry + installer. Ba tool cùng ý tưởng: tree-sitter AST → đồ thị tri thức tất định, local, truy vấn thay cho grep; đều ~6–9 tháng tuổi, Trendshift, đều có bản cloud thương mại đi kèm.

| Tool | Repo | ★ (12/10) | License | Ngôn ngữ / cài | Dạng |
|---|---|---|---|---|---|
| **Graphify** | `Graphify-Labs/graphify` | 126k★, 388 contributor, 2.324 commit từ 3/4/2026 | Apache-2.0 (relicense từ MIT) | Python; `uv tool install graphifyy` (PyPI, có provenance) | CLI + skill `/graphify`, xuất `graph.html`/`GRAPH_REPORT.md`/`graph.json` |
| **Understand-Anything** (đã có §3b mục 01) | `Egonex-AI/Understand-Anything` | 86k★ | — | TS; plugin marketplace | Knowledge graph tương tác + guided tour, đa ngôn ngữ (có vi) |
| **codegraph** | `colbymchenry/codegraph` | 74k★, ~1.296/1.428 commit của một tác giả, từ 18/1/2026 | MIT | Rust kernel + TS; `curl \| sh` hoặc npm `@colbymchenry/codegraph` | MCP server, graph SQLite `.codegraph/` + FTS, auto-sync theo file-watch |

**Khác nhau thật (đã đọc code, không theo ảnh):**

- **Graphify**: code parse bằng tree-sitter **không dùng LLM, không rời máy**; mỗi cạnh gắn nhãn `EXTRACTED` (có thật trong source) vs `INFERRED` (do tool suy ra) — minh bạch đáng học. Không vector store, là graph duyệt được (`query`/`path`/`explain`). Docs/PDF/ảnh/video mới gọi model cho lượt ngữ nghĩa. Công ty YC S26, có Graphify Cloud (app.graphify.com, trial 14 ngày, "cắt 80% token"). Benchmark tự công bố (LOCOMO, LongMemEval vs mem0/supermemory/BM25) chạy trên harness của chính họ → **(chưa xác minh độc lập)**. 388 "contributor" phần lớn là PR dịch README (30+ ngôn ngữ) và 812 PR mở — sao/PR cao một phần do chiến dịch dịch thuật.
- **codegraph**: kernel Rust, index **100% local** vào SQLite, auto-sync bằng OS file-watch trong MCP server — điểm khác biệt chính so với hai tool kia (incremental tự động). Release có **npm provenance + ký/attest** (tốt), nhưng installer vẫn là `curl … | sh` không kiểm checksum tại chỗ (mẫu cần tránh ở mục 12 §3 — dựa vào provenance npm thay vì checksum trong script). **Telemetry mặc định BẬT** (opt-out qua `codegraph telemetry off` / `CODEGRAPH_TELEMETRY=0` / `DO_NOT_TRACK=1`); ẩn danh, endpoint ingest là code công khai kiểm được, nhưng default-on là điểm trừ. Gần như một tác giả (bus factor 1). Có waitlist sản phẩm host (getcodegraph.com).
- **Understand-Anything**: xem hồ sơ đầy đủ ở mục 01 §3b (pipeline đa agent có reviewer, output đa ngôn ngữ gồm vi, viewer read-only không cần agent).

**Phân biệt với các tool đã có trong kho:**

- Khác **CodeFlow** (§2c): CodeFlow là *viewer kiến trúc* chạy trong trình duyệt cho người đọc; cụm này sinh *đồ thị truy vấn được* cho **agent** đọc (MCP/skill, xuất JSON).
- Khác **repomix / deepwiki-open / gitingest** (§2b): nhóm kia *gói/dump* codebase thành văn bản cho LLM; cụm này giữ **quan hệ graph** (call/import/kế thừa) để truy vấn theo đường đi, không nhồi cả repo vào context.

**Cách dùng / tích hợp:**

1. Agent cần "bản đồ quan hệ truy vấn được, chạy local": chọn **Graphify** (Apache-2.0, nhãn EXTRACTED/INFERRED minh bạch, cài qua PyPI có provenance) hoặc **codegraph** (auto-sync incremental) tuỳ cần cập nhật liên tục hay không.
2. Với **codegraph**, tắt telemetry ngay (`DO_NOT_TRACK=1` hoặc `codegraph telemetry off`) cho máy có mã khách hàng, và ưu tiên cài qua npm (có provenance) thay vì `curl | sh`; nếu buộc dùng script thì ghim tag `CODEGRAPH_VERSION` và kiểm attestation.
3. Mọi số benchmark/★ coi là tuyên bố marketing cho tới khi có bên thứ ba tái lập; "Top 3" trong ảnh không phải xếp hạng độc lập.
4. Ba tool trùng vai; đừng cài cả ba — chọn một theo tiêu chí license (Graphify Apache-2.0 > codegraph MIT), mô hình cập nhật và chính sách telemetry.

## 2e. Hồ sơ `Graphify-Labs/graphify`: codebase → knowledge graph tất định cho agent (yêu cầu người dùng, clone 2026-10-31)

> §2d chỉ có một đoạn so sánh. Đây là hồ sơ đầy đủ. Đã clone đủ lịch sử (blob:none), đọc README, SECURITY.md, NOTICE/LICENSE/LICENSE-MIT, `pyproject.toml`, `graphify/querylog.py`, CHANGELOG, workflow CI. **Không cài, không chạy.**

### 2e.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/Graphify-Labs/graphify (tên cũ `safishamsi/graphify`, cùng HEAD — mục 20 §3k.2) · **140k★, 13k fork** (shields) · **Apache-2.0 từ 22/7/2026** (trước MIT; `NOTICE` + `LICENSE-MIT` giữ điều khoản cho phần đóng góp cũ) · v0.9.99; commit cuối 30/10/2026 |
| Lịch sử | **2.675 commit** từ 3/4/2026, 408 tác giả; Safi Shamsi ~1.245 commit (2 tên), `ayushcodes10` 191; 1.314 dòng trailer `Co-Authored-By: Claude`; 295 commit từ 14/10 |
| Tồn đọng | **722 issue + 920 PR mở** — lớn nhất trong các repo kho theo dõi; phần lớn PR là dịch README/đóng góp lẻ (§2d) |
| Công ty | Graphify Labs (YC S26); **Graphify Cloud** (app.graphify.com) bán bản luôn-bật: monorepo/cross-repo, code review, "formal verification", connector Sentry/Jira, quảng cáo "cắt 80% token" |
| Cài | `uv tool install graphifyy` (**tên PyPI hai chữ y** — `graphify` đã có người dùng; gõ thiếu một chữ là cài nhầm gói khác) → `graphify install` tự nhận agent; hoặc `graphify claude install` / `codex install` … (20+ host) |
| Kiểm thử | 484 file test; 5 workflow (ci, publish, release-graph, pr-management, welcome); action **ghim theo tag** (`actions/checkout@v6`, `setup-uv@v8.1.0`), không ghim SHA |

### 2e.2 Nó làm gì (đọc mã)

- **Code → graph không cần LLM:** tree-sitter AST cho ~40 ngôn ngữ, giải quyết `calls`/`imports`/`inherits`/`mixes_in` xuyên file; chia cộng đồng bằng Leiden với nhãn không cần LLM; tìm "god node". Mỗi cạnh gắn **`EXTRACTED`** (có trong source) hoặc **`INFERRED`** (tool tự suy) — điểm đáng học nhất.
- **Ngoài code:** docs, PDF, ảnh, video/audio đi qua lượt ngữ nghĩa bằng **model của chính agent** hoặc API key cấu hình; comment `# NOTE:`/`# WHY:` và trích dẫn ADR/RFC thành node nối với code. Có ingest SCIP, introspect Postgres/Cargo, Google Workspace, PR.
- **Đầu ra:** `graphify-out/graph.html` (xem trong trình duyệt), `GRAPH_REPORT.md`, `graph.json` (có `schema_version`); truy vấn `graphify query/path/explain`; MCP server stdio (HTTP chỉ khi `--transport http`, mặc định bind `127.0.0.1`); `export callflow-html` (Mermaid, tự sinh lại sau commit nếu cài git hook).
- **Hook "always-on":** trên Claude Code/Gemini CLI, hook PreToolUse chạy trước lệnh tìm kiếm và trước Read/Glob từng file để **đẩy agent sang truy vấn graph**; host khác dùng file chỉ dẫn (`AGENTS.md`, `.cursor/rules/`…).

### 2e.3 Dữ liệu và rủi ro

- **Không telemetry** (grep `posthog|telemetry|analytics` 31/10/2026 chỉ thấy `querylog.py`). Query log **tắt mặc định** từ #1797 — comment trong mã giải thích: ghi mọi câu hỏi vào `~/.cache` ngoài `.gitignore` là trái tư thế "on-device, no-telemetry". Mạng chỉ khi: lượt ngữ nghĩa docs/media (gửi nội dung tới model cấu hình), `ingest <url>` do người dùng đưa.
- **Benchmark tự công bố** (README): LOCOMO recall@10 0,497 (mem0 0,048, supermemory 0,149) nhưng QA accuracy 45,3% **thua** supermemory 49,7%; LongMemEval-S n=50 hòa dense RAG; ERPNext n=6 phủ 82% so với grep/read 70,8%. Mẫu nhỏ, harness của chính họ → **(chưa xác minh độc lập)**. Đáng ghi: README tự để lộ chỗ thua.
- **Hook đổi hành vi agent:** chặn/nhắc trước Read/Glob có thể khiến agent tin graph cũ khi code đã đổi; nên bật auto-update (git hook) hoặc dựng lại graph trước phiên lớn.
- **Tồn đọng PR/issue rất cao** và nhịp ~16 commit/ngày → API, schema `graph.json` đổi nhanh; ghim phiên bản.

### 2e.4 So sánh và dùng thế nào

| Tool | ★ (31/10) | License | Khác Graphify |
|---|---|---|---|
| `Graphify-Labs/graphify` | 140k | Apache-2.0 | CLI Python, nhãn EXTRACTED/INFERRED, đa phương tiện, không telemetry |
| `Egonex-AI/Understand-Anything` (mục 01 §3b) | 89k (30/10) | MIT | Pipeline 10 agent dùng LLM cho ngữ nghĩa + guided tour cho **người học**; tốn token hơn |
| `colbymchenry/codegraph` (§2d) | 74k (12/10) | MIT | MCP server Rust, auto-sync theo file-watch; telemetry bật mặc định |
| CodeFlow (§2c) | – | – | Viewer cho người, không cho agent |

- **Chọn Graphify khi** cần graph tất định, chạy local, license Apache-2.0, không telemetry; hợp repo lớn mà agent hay grep lan man.
- **Cài an toàn:** gõ đúng `graphifyy`, ghim phiên bản (`uv tool install graphifyy==0.9.99`); với code nhạy cảm, đừng chạy lượt ngữ nghĩa trên docs nội bộ trừ khi model là local; kiểm hook được ghi vào `.claude/settings.json` sau `graphify claude install`.
- Không cài chồng với Understand-Anything/codegraph (§2d, "Cách dùng" điểm 4).

**Nguồn §2e:** clone github.com/Graphify-Labs/graphify 31/10/2026 (blob:none, 2.675 commit, HEAD a0946f9 30/10/2026; README.md (What it does, Benchmarks, always-on), SECURITY.md (Security Model, Optional network calls), NOTICE, LICENSE, LICENSE-MIT, pyproject.toml, graphify/querylog.py, CHANGELOG.md, .github/workflows/*; git log "relicense from MIT to Apache-2.0" 22/7/2026; git shortlog) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/Graphify-Labs/graphify.json (31/10/2026) · app.graphify.com · docs.graphify.com

### 2e.5 Kiểm ảnh "Give Claude a map of your code: graphify in 5 steps" (ảnh người dùng gửi, đọc lại mã 3/11/2026)

> Ảnh là infographic 5 bước (cài tool → thêm skill → map dự án → mở 3 file → hỏi graph), không có tác giả hay link. Đối chiếu với clone `--filter=blob:none` HEAD `8e6a6d2129d4aeffc7a0e9ed79b153f7f057f42b` (2/11/2026, tag v0.9.101, 2.775 commit, 100 commit sau lần đọc §2e). **Không cài, không chạy.**

| Bước trong ảnh | Kết quả | Đối chiếu |
|---|---|---|
| 1. "Note the double y in the name. You need Python 3.10 or newer", lệnh `uv tool instal` | ⚠️ | Python `>=3.10` và tên PyPI `graphifyy` đúng (`pyproject.toml`). Nhưng ô lệnh trong ảnh bị cắt đúng chỗ tên gói, nên chính phần "hai chữ y" mà ảnh dặn lại không hiện ra. Lệnh đủ là `uv tool install graphifyy` (README:53). Gõ `graphify` một chữ y là cài nhầm gói khác (§2e.1) |
| 2. "Registers graphify with your AI assistant" | ✅ (ô lệnh trống) | `graphify install` tự nhận agent; `--project` để cài theo dự án, `--platform <host>` cho 20+ host (README:202–230) |
| 3. "Type it inside Claude Code. Your code is mapped on your machine, with no AI" | ⚠️ đúng một phần | `/graphify .` (README:60). "No AI" chỉ đúng với **code** (tree-sitter AST). Docs, PDF, ảnh, video trong cùng thư mục đi qua lượt ngữ nghĩa bằng model của agent hoặc API key (README:36, :123). Với repo có tài liệu nội bộ, đây là dữ liệu rời máy |
| 4. "Open the 3 files: a map you can click, the key ideas Claude reads first, and the full graph" | ✅ | `graphify-out/graph.html`, `GRAPH_REPORT.md`, `graph.json` (README:67–69) |
| 5. "Ask the graph: shows how two parts of your code connect, without reading every file" | ✅ (ô lệnh trống) | `graphify path A B` trả đường đi và độ tin cậy của chặng yếu nhất; `graphify query "<câu hỏi>"` trả subgraph (README:102–107). Lưu ý cạnh `INFERRED` là do tool suy ra, không phải đọc trực tiếp từ source |

**Đã đổi từ §2e (31/10 → 3/11/2026):** v0.9.99 → **v0.9.101**. Schema cache AST tăng từ 32 lên **36** chỉ trong 3 ngày (sửa extractor PHP, Scala/Terraform, Go/Python, Rust, C++). Vẫn Apache-2.0 (`pyproject.toml` khai `license-files` gồm LICENSE, LICENSE-MIT, NOTICE). Vẫn không có telemetry; query log vẫn tắt mặc định (`graphify/querylog.py:17–23`). 141.191★, 13.496 fork, 1.622 issue+PR mở (GitHub search API 3/11/2026; 31/10 là 722 issue + 920 PR).

**Bổ sung cho §2e.4:** nhịp đổi schema cao xác nhận lời khuyên ghim phiên bản (`uv tool install graphifyy==0.9.101`) và dựng lại graph sau mỗi lần nâng. Ảnh hướng dẫn bỏ qua cả hai việc này, cũng như việc `graphify install` ghi hook PreToolUse vào cấu hình agent (§2e.2).

**Nguồn §2e.5:** ảnh infographic người dùng gửi 3/11/2026 · clone https://github.com/Graphify-Labs/graphify HEAD `8e6a6d2129d4aeffc7a0e9ed79b153f7f057f42b` (README.md:34–123, :190–230; pyproject.toml; LICENSE; graphify/querylog.py; `git log a0946f9..HEAD`; `git tag`) · GitHub search API `repo:Graphify-Labs/graphify` 3/11/2026.

## 2f. Hồ sơ `colbymchenry/codegraph`: code graph cho agent qua MCP, chạy cục bộ (yêu cầu người dùng, clone 2026-10-31)

> §2d chỉ có một đoạn so sánh (12/10/2026). Đã clone đủ lịch sử (blob:none), đọc README, `TELEMETRY.md`, `install.sh`, `telemetry-worker/`, cấu trúc `codegraph-kernel/`, workflow CI. **Không cài, không chạy.**

### 2f.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 31/10/2026) |
|---|---|
| Repo | github.com/colbymchenry/codegraph · **76k★, 5k fork** (12/10: 74k) · **MIT** · v1.6.2 · 161 issue / 46 PR mở · site colbymchenry.github.io/codegraph, getcodegraph.com |
| Lịch sử | **1.802 commit** từ 18/1/2026, 57 tác giả; Colby McHenry **1.593 commit** (2 tên, ~88%) — bus factor 1; **1.708 trailer Claude**; 379 commit từ 12/10 (~20/ngày) |
| Kiến trúc | Kernel **Rust** (`codegraph-kernel/`, grammar tree-sitter) + CLI/MCP TypeScript; index **100% cục bộ** vào SQLite + FTS trong `.codegraph/`, tự đồng bộ theo file-watch qua daemon nền |
| 8 tool MCP | `codegraph_explore` (trả lời "X hoạt động thế nào / X đi tới Y ra sao" trong một lần gọi), `codegraph_search`, `codegraph_node`, `codegraph_callers`, `codegraph_callees`, `codegraph_impact` (blast radius), `codegraph_files`, `codegraph_status` |
| Ngôn ngữ / host | 20+ ngôn ngữ, route theo framework, cầu nối iOS/React Native/Expo; 8+ agent (Claude Code, Cursor, Codex, OpenCode, Hermes, Gemini, Antigravity, Kiro, Copilot) |
| Đo độ phủ | README công bố **"fair coverage"** (tỉ lệ file có ít nhất một phụ thuộc chéo đã giải được) trên repo mẫu: TS/JS 95,8% (chính repo này), Python 100% (psf/requests), Go 96,6% (gin), Rust 86,7% (ripgrep) — tự đo, nhưng cách đo được công bố |
| Thương mại | "The CodeGraph platform is coming" — waitlist getcodegraph.com cho bản phân tích PR (cái gì cần test, cái gì có thể vỡ) |

### 2f.2 Cổng thật và rủi ro

- **Không có CI chạy test:** chỉ 2 workflow (`release`, `deploy-site`); `npm test` (vitest, **1.006 file test** trong `__tests__/`, có `test:eval`) chạy tay. Phát hành thì có bảo chứng: npm **trusted publishing (OIDC) + provenance**, artifact build trong workflow công khai ("never from a laptop").
- **Installer `curl … | sh` không kiểm checksum:** `install.sh` (151 dòng) lấy release mới nhất từ GitHub rồi tải về, không thấy bước sha256/attestation trong script (grep 31/10/2026). Ưu tiên cài qua npm (`@colbymchenry/codegraph`, có provenance) và kiểm bằng `npm audit signatures`.
- **Telemetry bật mặc định** (`TELEMETRY.md`): gửi `machine_id` ngẫu nhiên, phiên bản, OS/arch, Node major, cờ CI; sự kiện `install` (agent nào), `index` (**tên ngôn ngữ** có trong repo), `usage_rollup` (tên tool/lệnh mỗi ngày), `uninstall`. Không gửi code hay đường dẫn. Endpoint ingest là mã công khai trong `telemetry-worker/` và **áp allowlist trường** — minh bạch hiếm thấy. Tắt: `codegraph telemetry off`, `CODEGRAPH_TELEMETRY=0`, **`DO_NOT_TRACK=1` (luôn được tôn trọng)**, hoặc `--no-telemetry` cho từng MCP server; installer tương tác hỏi trước với toggle mặc định bật. Ngoài ra MCP server kiểm phiên bản mới trên GitHub tối đa 1 lần/ngày (`CODEGRAPH_NO_UPDATE_CHECK=1`).
- **Daemon nền:** MCP server khởi chạy daemon theo dõi file cho mỗi dự án; daemon đang chạy giữ cài đặt telemetry của server đã khởi động nó cho tới khi thoát.

### 2f.3 So sánh và dùng thế nào

| | codegraph | Graphify (§2e) | Understand-Anything (mục 01 §3b) |
|---|---|---|---|
| ★ (30–31/10) | 76k | 140k | 89k |
| Dạng | MCP server + daemon, tự đồng bộ | CLI Python + skill, dựng lại khi cần | Plugin pipeline 10 agent dùng LLM |
| Telemetry | Bật mặc định, allowlist công khai | Không | Không |
| CI test | Không (chạy tay) | Có (484 file test) | Có (67 file test) |
| Điểm mạnh | Truy vấn caller/callee/impact nhanh, cập nhật liên tục khi code đổi | Nhãn EXTRACTED/INFERRED, đa phương tiện | Guided tour cho người học |

**Dùng khi** agent cần hỏi "ai gọi hàm này / sửa cái này vỡ gì" liên tục trong repo lớn đang thay đổi. Cấu hình tối thiểu an toàn: cài qua npm có provenance, đặt `DO_NOT_TRACK=1` (tắt cả telemetry lẫn update check), thêm `.codegraph/` vào `.gitignore`, ghim phiên bản vì nhịp ~20 commit/ngày. Không chạy song song với Graphify/Understand-Anything (§2d "Cách dùng" điểm 4).

**Nguồn §2f:** clone github.com/colbymchenry/codegraph 31/10/2026 (blob:none, 1.802 commit, HEAD 2008e2f 30/10/2026; README.md (MCP Tools, Verified releases, Measured cross-file coverage), TELEMETRY.md, install.sh, telemetry-worker/, codegraph-kernel/, package.json, `__tests__/`, .github/workflows/{release,deploy-site}.yml; git shortlog) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/colbymchenry/codegraph.json (31/10/2026) · getcodegraph.com

## 2g. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại số sao, license, trạng thái của 17 repo GitHub đã có trong mục 16 (GitHub search API, `meta_all` ngày 31/10/2026); với repo có `pushed_at` đáng ngờ thì clone nông để xem commit thật của nhánh mặc định. (2) Tìm repo lớn còn thiếu: 14 truy vấn GitHub (topic `documentation`, `static-site-generator`, `openapi`; từ khoá "llms.txt", "documentation mcp", "deepwiki", "codebase prompt", "docs coding agents" cho repo tạo sau 1/10/2025). Từ ~40 ứng viên chưa có trong kho, chọn **7 repo**, clone `--filter=blob:none` và đọc mã (LICENSE, manifest, installer, module telemetry, workflow CI). **Không cài, không chạy script nào.** Số sao đọc 31/10/2026.

### 2g.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (12/10 → 31/10/2026) | Hệ quả |
|---|---|---|
| `facebook/docusaurus` | **Chuyển sang org `meta/docusaurus`** (GitHub redirect); 66,6k★, push 30/10 | Catalog đang ghi tên cũ và không có số sao; link cũ vẫn chạy nhờ redirect, nên đổi khi tích hợp |
| `coderamp-labs/gitingest` | API báo push 28/10, nhưng **nhánh `main` vẫn đứng ở `4e259a0` (16/8/2025)**: push mới là của nhánh Renovate | Nhận định §2b vẫn đúng: hơn 14 tháng không có commit tính năng, ưu tiên repomix |
| `upstash/context7` | 64k★ (catalog chưa có số) | Vẫn là MCP docs phổ biến nhất mục |
| `yamadashy/repomix` | 28,8k → 29,1k | Ổn định |
| `zensical/zensical` | 5,9k → 6,1k | Vẫn 0.0.x |
| `Graphify-Labs/graphify` · `colbymchenry/codegraph` | 140k · 76,1k (hồ sơ §2e, §2f cùng ngày) | Không đổi |
| `sphinx-doc/sphinx` | GitHub báo `NOASSERTION` | Không phải đổi license: file là `LICENSE.rst` (BSD-2-Clause), GitHub không nhận dạng được |
| `squidfunk/mkdocs-material` · `withastro/starlight` · `fuma-nama/fumadocs` · `AnswerDotAI/llms-txt` | 27,6k · 9,5k · 13,5k · 2,7k (catalog chưa có số) | llms-txt push cuối 24/9/2026, nhịp chậm |

Các repo còn lại (vitepress, mdBook, docsify, deepwiki-open, codeflow) dao động dưới 2%, không có repo nào bị archive.

### 2g.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `mermaid-js/mermaid` | Sơ đồ dạng mã | 90,9k · MIT | 31/10/2026 | Sơ đồ từ văn bản, nhúng trong Markdown của GitHub/GitLab/Docusaurus/VitePress | 889 tác giả; mặc định `securityLevel: strict` |
| `DeusData/codebase-memory-mcp` | Code knowledge graph | 47,9k · MIT | 31/10/2026 | MCP server viết bằng C: đồ thị code + docs + hạ tầng, 17 tool, 162 grammar | ~78% commit một người; tạo 2/2026 |
| `GitbookIO/gitbook` | Trình render docs | 29,1k · **GPL-3.0** | 30/10/2026 | Mã nguồn phần hiển thị site GitBook: có route `llms.txt`, `llms-full.txt`, Markdown từng trang, MCP | Nội dung vẫn lấy từ API GitBook |
| `langchain-ai/openwiki` | Wiki cho agent | 17,6k · MIT | 30/10/2026 | CLI + MCP viết wiki Markdown cho repo, mỗi "Claim" trỏ về dòng mã nguồn | **Telemetry bật sẵn**; từ 10/10 chỉ còn bump dependency |
| `scalar/scalar` | Tài liệu API | 16,4k · MIT | 31/10/2026 | API reference từ OpenAPI + API client offline + `openapi-to-markdown` cho LLM | Nút "Agent" và proxy gọi dịch vụ Scalar |
| `repowise-dev/repowise` | Code knowledge graph | 8,1k · **AGPL-3.0** | 31/10/2026 | Index code + git + test, dashboard, MCP, sinh docs (LLM tuỳ chọn) | Telemetry opt-out; cài "đọc URL rồi tự cài" |
| `mufeedvh/code2prompt` | Gói codebase cho LLM | 7,7k · MIT | 7/9/2026 | CLI Rust gói repo thành một prompt có cây thư mục, đếm token | Không quét secret; im từ 7/9 |

### 2g.3 Hồ sơ ngắn

- **mermaid.** Chuẩn de facto cho "sơ đồ là văn bản": 16.645 commit từ 11/2014, 889 tác giả, bản 12.2.0 (13/10/2026), 25 workflow ghim SHA 97/99. Gói `mermaid` có 37 thư mục sơ đồ trong `src/diagrams/`; layout ELK và tidy-tree tách gói riêng. An toàn: `config.schema.yaml` để mặc định `securityLevel: strict` (mã hoá HTML, tắt click); chế độ `loose`/`antiscript` cho phép HTML trong nhãn, chỉ bật khi nguồn sơ đồ tin được. Không telemetry trong thư viện; Plausible chỉ nằm ở site docs. Với agent, mermaid là định dạng sơ đồ rẻ token nhất để đưa vào `AGENTS.md`/ADR. Cài: `npm install mermaid`.
- **codebase-memory-mcp.** 5.003 commit từ 25/2/2026, 233 tác giả nhưng Martin Vogel 3.902 commit (~78%); 148 trailer Claude. Toàn bộ backend viết bằng C, vendor sqlite3/mimalloc/yyjson; ✅ README ghi 162 ngôn ngữ, đếm được đúng 162 thư mục grammar. Index cả Docker, Kubernetes, Terraform, CI và tài liệu, nên rộng hơn codegraph (§2f). ✅ "Không telemetry": grep `src/` không thấy endpoint thu thập; host mạng duy nhất là GitHub (cập nhật) và Hugging Face (model chat cục bộ của CBM Lens, chỉ khi bật). Chuỗi cung ứng tốt nhất trong đợt: `install.sh` tải `checksums.txt` rồi so `sha256` trước khi giải nén, release có `attest-build-provenance`, SBOM, cosign, quét VirusTotal; 184/206 action ghim SHA. Lưu ý: checksum lấy từ cùng release nên chỉ chống hỏng khi tải; muốn chống release bị giả thì kiểm attestation (`gh attestation verify`). Số đo "Linux kernel 3 phút" là tự công bố trên M3 Pro **(chưa xác minh)**. Cài: `curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash` (tốt hơn: tải release, kiểm attestation, rồi chạy).
- **GitbookIO/gitbook.** Không phải GitBook tự host: README nói rõ repo chỉ là phần **render** nội dung đã xuất bản (Next.js, Bun), dữ liệu vẫn lấy qua API GitBook. Đáng đọc vì đây là cài đặt thật của docs-for-AI ở §2: route `llms.txt`, `llms-full.txt` (có phân trang), `~gitbook/markdown/[page]` trả Markdown từng trang, `~gitbook/mcp` (có route auth) và component `WebMCP`. License **GPL-3.0**; README yêu cầu fork public hoặc mua license thương mại nếu muốn giữ riêng. 0/45 action ghim SHA.
- **openwiki (LangChain).** Tạo 22/6/2026, 484 commit, 111 tác giả, v0.7.2. Chạy hai cách: trong coding agent (dùng phiên model của agent, 10 host gồm Claude Code, Codex, Cursor, Kiro, Antigravity) hoặc CLI độc lập với 14 provider. Điểm hay: **Grounded Claims**, mỗi sự kiện trong wiki trỏ về `repo://src/x.ts#L40-L82`; khi mã đổi, chỉ các claim có bằng chứng thay đổi bị đánh dấu cần cập nhật. Vòng MCP `openwiki_begin → submit_plan → next_page → submit_page → finish` để agent không tự tuyên bố xong. Có workflow mẫu cập nhật wiki trong CI. **Telemetry bật mặc định** (PostHog `us.i.posthog.com`, ID cài ngẫu nhiên); tắt bằng `OPENWIKI_TELEMETRY_DISABLED=1` hoặc `DO_NOT_TRACK=1`, xem trước payload bằng `--telemetry-file`. ⚠️ README ghi "không thu IP", nhưng comment trong `client.ts` nói IP bị bỏ nhờ cài đặt phía server PostHog, client không chặn được. CI ghim SHA 28/28. Nhịp phát triển gần như dừng từ 10/10 (6 commit, toàn bump dependency). Cài: `npm install -g openwiki` (Node ≥22.22).
- **scalar.** Monorepo 7.955 commit, 269 tác giả, 1.224 trailer Claude; 16 integration (FastAPI, Hono, NestJS, .NET, Docusaurus, Starlight…). Liên quan docs-for-AI: gói `@scalar/openapi-to-markdown` sinh Markdown thân thiện LLM từ OpenAPI, component `AgentScalar` và nút "Open MCP" trong API reference. PostHog là **plugin tuỳ chọn**, không nạp thì không theo dõi (test e2e ghi rõ bản standalone không có). Agent chat gọi `scalar.com`/`proxy.scalar.com`; nút "thử request" có thể đi qua proxy của Scalar nếu cấu hình `proxyUrl`, nên với API nội bộ hãy tự host proxy hoặc tắt. Cài: `npm install @scalar/api-reference`.
- **repowise.** 3.677 commit từ 23/3/2026 (1.107 commit từ 12/10), Raghav Chamadiya ~67%. Index không cần LLM (đồ thị, git, độ phủ test, dead code); LLM chỉ khi sinh văn xuôi, gọi thẳng provider bằng key của người dùng. Telemetry **opt-out** (tên lệnh + môi trường thô), tự tắt khi `DO_NOT_TRACK`, CI hoặc stderr không phải TTY. ⚠️ Cách cài đầu README là bảo agent "đọc `https://docs.repowise.dev/setup.md` rồi tự cài": chỉ dẫn lấy từ URL lúc chạy, không ghim phiên bản. Benchmark "agent mở 3 file thay vì 7" là tự đo **(chưa xác minh)**. License **AGPL-3.0**; có bản hosted và bản thương mại. 0/56 action ghim SHA. Cài: `uv tool install repowise` rồi `repowise init --yes --no-prose`.
- **code2prompt.** CLI Rust (crate `code2prompt` 4.3.0, tag mới nhất v4.2.0), có SDK Python `code2prompt-rs`, TUI, template Handlebars, đếm token bằng tiktoken. So với repomix (§2b): không có bước quét secret (không thấy module nào trong `crates/`), nên cần `.gitignore`/bộ lọc chặt. Nhịp chậm: 0 commit từ 12/10. Cài: `cargo install code2prompt` hoặc `brew install code2prompt`.

**Đã cân nhắc, không thêm:** `yusufkaraaslan/Skill_Seekers` (15,3k, docs → skill Claude; hợp mục 20 hơn), `opendatalab/MinerU` (82,9k, PDF → Markdown; thuộc mục 15), `Redocly/redoc` (26k) và `swagger-api/swagger-ui` (29,1k) (API docs kinh điển, không có lớp AI), `xerj-org/xerj` (17,9k, search engine cho agent), `AIDotNet/OpenDeepWiki` (3,7k), `MicrosoftDocs/mcp` (2k, MCP docs chính chủ, nhỏ).

### 2g.4 Mẫu chung rút ra

1. **Docs-for-AI đã thành tính năng có sẵn của nền tảng**: GitBook render `llms.txt` + Markdown từng trang + MCP; Scalar có `openapi-to-markdown` + nút MCP. Tự viết llms.txt bằng tay chỉ cần khi framework chưa có.
2. **Cụm "code knowledge graph cho agent" đông lên**: Graphify, codegraph (§2e–2f), nay thêm codebase-memory-mcp và repowise. Khác biệt đáng chọn không còn là "có graph" mà là **chuỗi cung ứng** (checksum + attestation như codebase-memory-mcp) và **telemetry** (không có / opt-out / bật sẵn).
3. **Gắn sự kiện với bằng chứng**: Grounded Claims của openwiki (dòng mã cụ thể) cùng hướng với nhãn `EXTRACTED/INFERRED` của Graphify. Docs sinh bởi LLM chỉ đáng tin khi mỗi câu trỏ được về nguồn và biết lúc nào nguồn đổi.
4. **`pushed_at` của GitHub không phải ngày commit**: gitingest báo push 28/10 nhưng `main` đứng từ 8/2025. Luôn xem commit của nhánh mặc định.
5. **Telemetry bật sẵn tiếp tục lan** (openwiki, repowise ở mức opt-out); `DO_NOT_TRACK=1` tắt được cả hai.

**Nguồn §2g:** GitHub search API 31/10/2026 (`repo:` cho repo cũ, 14 truy vấn topic/từ khoá) · clone nông `coderamp-labs/gitingest`, `AsyncFuncAI/deepwiki-open`, `sphinx-doc/sphinx` (commit nhánh mặc định) · clone `--filter=blob:none` 7 repo mới, đọc: mermaid (`packages/mermaid/package.json`, `src/schemas/config.schema.yaml`, `src/diagrams/`, workflows), codebase-memory-mcp (LICENSE, README (Security, Performance), `install.sh`, `.github/workflows/{release,_build}.yml`, `vendored/`, grep host trong `src/`), GitbookIO/gitbook (LICENSE, README, `packages/gitbook/src/app/sites/**/{llms.txt,llms-full.txt,~gitbook/markdown,~gitbook/mcp}`), openwiki (README (Telemetry, How it works), `package.json`, `src/telemetry/{config,client,types}.ts`, `.github/workflows/checks.yml`), scalar (LICENSE, README, `packages/api-reference/src/plugins/posthog/README.md`, `test/configuration/telemetry.e2e.ts`, `packages/agent-chat/src/api.ts`, `packages/openapi-to-markdown/README.md`, `packages/types/src/api-reference/api-reference-configuration.ts`), repowise (LICENSE, README (Privacy, Hosted), `packages/cli/src/repowise/cli/platform/telemetry/{consent,flusher}.py`), code2prompt (LICENSE, README, `crates/`, `crates/code2prompt-core/Cargo.toml`) · https://github.com/meta/docusaurus

## 2h. Nâng trần 2/11/2026: cổng lint văn xuôi, chính tả, link và khung Diátaxis (yêu cầu người dùng)

> Tìm repo **chưa có trong catalog** ở ba lớp: chuẩn, cổng máy, đầu bảng. GitHub search API 2/11/2026; clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, cấu trúc, file luật. **Không cài, không chạy.**

**Trần hiện tại:**

- Mục mạnh ở lớp **dựng và phân phối** docs: SSG (§1, §2b), docs-for-AI (llms.txt, Context7, GitBook, Scalar ở §2, §2g), code knowledge graph (§2c–§2f).
- Chưa có lớp nào **kiểm chất lượng nội dung**: không lint văn phong, không kiểm chính tả, không kiểm link hỏng, không có khung phân loại tài liệu. Docs cho agent (llms.txt, AGENTS.md) càng cần các cổng này vì agent làm theo từng chữ và từng link.
- Kho này chạy `markdownlint-cli2` trong CI nhưng engine `markdownlint` chưa có hồ sơ.

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `evildmp/diataxis-documentation-framework` | Chuẩn (nguyên lý gốc) | 1,3k · **CC-BY-SA-4.0** (GitHub báo `NOASSERTION` (license "Other") vì nội dung `LICENSE.rst` đã được định dạng lại bằng markup reST/markdown nên không khớp với văn bản chuẩn CC-BY-SA-4.0, dù GitHub vẫn nhận ra đây là file giấy phép) | 6/8/2026 | Khung Diátaxis của Daniele Procida: tách docs thành tutorial, how-to, reference, explanation theo nhu cầu người đọc; nguồn Sphinx của diataxis.fr, dịch 10 ngôn ngữ | Là hướng dẫn, không có công cụ kiểm; trích nội dung phải giữ CC-BY-SA |
| `vale-cli/vale` | Cổng máy (văn phong) | 6,3k · MIT | 31/10/2026 | Linter văn xuôi hiểu markup; luật là YAML; nạp sẵn style Microsoft, Google, Red Hat qua `Packages`; AWS, NVIDIA, GitLab dùng (theo README) | Repo đã chuyển từ `errata-ai/vale`; `vale sync` tải style qua mạng; chưa có style tiếng Việt **(chưa xác minh)** |
| `DavidAnson/markdownlint` | Cổng máy (cấu trúc Markdown) | 6,4k · MIT | 20/10/2026 | Engine của `markdownlint-cli2` mà kho này đang dùng; 53 trang luật trong `doc/`, hỗ trợ custom rule | Chỉ kiểm cú pháp, không kiểm nội dung |
| `lycheeverse/lychee` | Cổng máy (link) | 4,1k · MIT hoặc Apache-2.0 | 26/10/2026 | Kiểm link bất đồng bộ (Rust) cho Markdown, HTML, file văn bản; `--cache`, `--include-fragments` (kiểm cả `#anchor`), `GITHUB_TOKEN` tránh rate limit; có `lychee-action` | Link ngoài gây flaky: cần cache, `--cache-exclude-status '429'` và danh sách bỏ qua |
| `streetsidesoftware/cspell` | Cổng máy (chính tả) | 1,7k · MIT | 28/10/2026 | Spell check cho code và docs, từ điển theo ngôn ngữ/stack; repo `cspell-dicts` **có thư mục `vi_VN`** (kiểm `ls-tree` 2/11/2026) | Nhiều false positive với tên riêng; cần từ điển dự án |
| `crate-ci/typos` | Cổng máy (lỗi gõ) | 4,2k · MIT hoặc Apache-2.0 | 1/11/2026 | Bắt lỗi gõ sai phổ biến với mục tiêu "low false positives so you can run on PRs"; nhanh, có Action và pre-commit | Chỉ bắt lỗi gõ đã biết, không phải từ điển đầy đủ; chủ yếu tiếng Anh |

**Đã cân nhắc, không thêm:** `langchain-ai/mcpdoc` (1k★, đưa llms.txt vào IDE qua MCP) đã **archive**; `get-alex/alex` (5,1k★) push cuối 27/11/2024; `textlint/textlint` (3,2k★) trùng vai với Vale, hợp hơn khi cần luật tiếng Nhật/Trung.

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. Giữ `markdownlint-cli2` (đã có) và thêm `lychee --cache --include-fragments` cho mọi file `.md` và `llms.txt`: link hỏng là lỗi docs-for-AI rẻ nhất để bắt.
2. Thêm `typos` vào PR (gần như không false positive); `cspell` với từ điển dự án và `vi_VN` khi docs có tiếng Việt.
3. Áp Diátaxis khi sắp lại docs của SSG ở §1/§2b: mỗi trang thuộc đúng một loại; `llms.txt` (§2) liệt kê theo đúng bốn nhóm đó để agent biết trang nào là reference.
4. Vale với style Microsoft hoặc Google ở mức `warning` cho docs tiếng Anh; tự viết luật YAML cho thuật ngữ nội bộ và từ cấm.
5. Docs sinh bởi LLM (openwiki, repowise §2g): chạy cùng bộ cổng trên đầu ra trước khi merge, cùng với yêu cầu trỏ về nguồn ở §2g.4.

**Nguồn §2h:** GitHub search API 2/11/2026 (`repo:` từng repo; truy vấn "diataxis in:name", "llms.txt in:name,description") · clone `--depth 1 --filter=blob:none` 2/11/2026: vale-cli/vale (LICENSE, README.md, `cmd/vale/`), lycheeverse/lychee (LICENSE-MIT, LICENSE-APACHE, README.md mục CLI và GitHub token), streetsidesoftware/cspell (LICENSE, README.md, `packages/`), streetsidesoftware/cspell-dicts (`git ls-tree dictionaries/`), crate-ci/typos (LICENSE-*, README.md), DavidAnson/markdownlint (LICENSE, README.md, `doc/`), evildmp/diataxis-documentation-framework (LICENSE.rst, `source/`, `translation/`) · `.markdownlint-cli2.yaml` của kho · https://diataxis.fr · https://vale.sh · https://lychee.cli.rs · https://cspell.org · https://github.com/langchain-ai/mcpdoc

<a id="docs-version-trust-2026-11-02"></a>

## 2i. Nâng trần 2/11/2026: đúng phiên bản, nguồn có chủ sở hữu và độ mới của tri thức (rà soát toàn diện)

> Mở sâu sau §2h trong cùng ngày; không phải tin hai dự án vừa ra mắt. Đã đọc LICENSE, metadata GitHub, CI và file chính ở hai HEAD dưới đây. Mức bằng chứng **đọc mã/cấu hình**; chưa gọi API Context7, build Backstage hay kiểm một hệ docs production. Số sao đọc 2/11/2026; ngày commit là HEAD nhánh mặc định, khác `pushed_at` của cả repo.

### 2i.1 Khoảng trống sau lint và tài liệu cho agent

§2h xử lý câu chữ, chính tả và link; §2g đã yêu cầu docs sinh từ code trỏ nguồn. Còn ba câu hỏi cần trả lời trước khi agent dùng tài liệu để sửa code: **nguồn nào chịu trách nhiệm**, **docs áp cho dependency/version nào**, và **được build/index/review lần nào**. Link sống, timestamp mới và điểm tìm kiếm cao không tự chứng minh API trong đoạn trích đúng với lockfile của ứng dụng.

| Repo | Hồ sơ | ★ · license (2/11/2026) | HEAD · ngày commit | Giá trị / giới hạn |
|---|---|---|---|---|
| `upstash/context7` | Đọc sâu dự án đã có §2 | 64.069 · MIT cho mã trong repo | `18d6f5d632d4cf53c464f36c79d2e4caa19a8e56` · 2/11/2026 | MCP/CLI/SDK lấy snippet tài liệu public; có library ID/version. API guide cho phép **fallback thành công** khi version số chưa được index; cần kiểm served version |
| `backstage/backstage` — TechDocs + Software Catalog | Hồ sơ mới | 34.765 · Apache-2.0 | `24deeed9605d2afa54c2e7456912317fa8a1dcee` · 31/10/2026 | Docs-as-code gắn entity/owner của catalog, build/publish/cache và reader; ETag/build timestamp giúp đồng bộ. Là nền tảng portal nhiều thành phần, không cần thiết cho một site tài liệu nhỏ |

### 2i.2 Context7: ID có version chưa đủ để tái lập

**Cơ chế đọc được.** `packages/mcp/src/lib/api.ts` dựng request `/v2/context` với `query`, `libraryId` và tùy chọn ngôn ngữ; base URL mặc định là API tại `context7.com`, có biến cấu hình để đổi endpoint. Mô tả tool cũng nói rõ query gửi tới API và yêu cầu không đưa secrets, thông tin cá nhân hay code riêng tư vào câu hỏi. MIT của MCP/client không chứng minh backend index có thể tự host chỉ bằng checkout này. [API client](https://github.com/upstash/context7/blob/18d6f5d632d4cf53c464f36c79d2e4caa19a8e56/packages/mcp/src/lib/api.ts), [endpoint mặc định](https://github.com/upstash/context7/blob/18d6f5d632d4cf53c464f36c79d2e4caa19a8e56/packages/mcp/src/lib/constants.ts), [tool schema và mô tả dữ liệu gửi](https://github.com/upstash/context7/blob/18d6f5d632d4cf53c464f36c79d2e4caa19a8e56/packages/mcp/src/index.ts).

**Điều kiện version thật.** API guide ở HEAD này ghi: version số chưa index vẫn có thể trả thành công bằng tag khớp số, release mới hơn cùng dòng hoặc docs hiện tại; JSON có đối tượng `version` mô tả bản đã phục vụ, còn text bắt đầu bằng note nếu fallback. Branch/channel không index vẫn có thể trả `404 version_not_found`, nên không suy rộng rằng mọi chuỗi version đều fallback. Client MCP đọc nội dung text rồi trả về tool; chưa thấy cổng tự đối chiếu phiên bản với lockfile của repo người dùng trong đường gọi đã đọc. Vì vậy, ứng dụng đích nên giữ cả **requested version** lẫn **served version**, và khi yêu cầu đúng bản mà không có thì chuyển sang docs/tag nguồn gốc. [Đặc tả hành vi fallback trong repo](https://github.com/upstash/context7/blob/18d6f5d632d4cf53c464f36c79d2e4caa19a8e56/docs/api-guide.mdx#L235), [kiểu response MCP](https://github.com/upstash/context7/blob/18d6f5d632d4cf53c464f36c79d2e4caa19a8e56/packages/mcp/src/lib/types.ts).

**Cổng và giới hạn.** Workflow chạy lint, format, build, typecheck, test và SDK integration có điều kiện theo nguồn PR/secret. Những cổng này kiểm implementation, không chứng minh mọi snippet trả về chạy được trên mọi version thư viện. README quảng bá giảm API ảo/lỗi thời là định vị sản phẩm; chưa có phép đo độc lập trong đợt này chứng minh loại bỏ hallucination. Phương án thay thế: docs chính thức theo version/tag, bản docs snapshot của dự án, hoặc code/source đã ghim; Context7 hợp cho truy vấn tiện dụng khi có thể kiểm lại nguồn và version. [CI](https://github.com/upstash/context7/blob/18d6f5d632d4cf53c464f36c79d2e4caa19a8e56/.github/workflows/test.yml), [LICENSE](https://github.com/upstash/context7/blob/18d6f5d632d4cf53c464f36c79d2e4caa19a8e56/LICENSE).

### 2i.3 Backstage TechDocs: độ mới kỹ thuật và chủ sở hữu nội dung

**Kiến trúc.** Backstage khởi nguồn từ Spotify, hiện nằm trong CNCF theo README đã đọc. Software Catalog lưu entity và `spec.owner`; annotation `backstage.io/techdocs-ref` nối entity đến nguồn docs. TechDocs tách prepare → generate → publish → reader. Với production, tài liệu chính thức khuyến nghị build ở CI của repo nguồn, publish site sang storage bên ngoài, backend đọc và reader hiển thị; không bắt backend dựng lại mọi site khi có người đọc. Có thể dùng SSG độc lập ở §1 thay vì triển khai cả Backstage nếu chỉ cần một bộ docs. [Kiến trúc chính thức](https://backstage.io/docs/features/techdocs/architecture/), [catalog descriptor](https://github.com/backstage/backstage/blob/24deeed9605d2afa54c2e7456912317fa8a1dcee/docs/features/software-catalog/descriptor-format.md), [ví dụ gắn docs với entity](https://github.com/backstage/backstage/blob/24deeed9605d2afa54c2e7456912317fa8a1dcee/plugins/techdocs-backend/examples/documented-component/catalog-info.yaml).

**Độ mới có thể quan sát.** Builder đọc `etag` trong `techdocs_metadata.json` rồi hỏi preparer; khi không thay đổi thì bỏ generate. `DocsSynchronizer` so `build_timestamp` giữa storage và cache để invalidate các object. Đây là freshness của artifact/cache, **không phải ngày người có trách nhiệm đã xác minh nội dung**; một docs page sai có thể được build lại hôm nay. `spec.owner` giúp tìm người chịu trách nhiệm, không tự chứng minh họ đã review từng trang. [Builder](https://github.com/backstage/backstage/blob/24deeed9605d2afa54c2e7456912317fa8a1dcee/plugins/techdocs-backend/src/DocsBuilder/builder.ts), [đồng bộ timestamp/cache](https://github.com/backstage/backstage/blob/24deeed9605d2afa54c2e7456912317fa8a1dcee/plugins/techdocs-backend/src/service/DocsSynchronizer.ts).

**Trust và vận hành.** Reader có HTML transformer dùng DOMPurify và hook cho link/iframe/meta/attribute; có test sanitizer và workflow kiểm docs/E2E. Sanitization HTML giải quyết một lớp nguy cơ render, **không lọc mọi chỉ dẫn gây nhiễu khi văn bản được đưa vào LLM**. Mô hình quyền đọc tài liệu/storage vẫn phải cấu hình theo portal đích; tài liệu kiến trúc khuyến nghị tách credential publish của CI và credential đọc của backend. Không gửi docs nội bộ qua API hosted chỉ vì công cụ retrieval có client mã mở. [Sanitizer](https://github.com/backstage/backstage/blob/24deeed9605d2afa54c2e7456912317fa8a1dcee/plugins/techdocs/src/reader/transformers/html/transformer.ts), [test](https://github.com/backstage/backstage/blob/24deeed9605d2afa54c2e7456912317fa8a1dcee/plugins/techdocs/src/reader/transformers/html/transformer.sanitizer.test.tsx), [LICENSE](https://github.com/backstage/backstage/blob/24deeed9605d2afa54c2e7456912317fa8a1dcee/LICENSE).

### 2i.4 Ma trận chọn và tiêu chí tin cậy

| Nhu cầu | Cách chọn | Bằng chứng giữ lại | Cổng đề xuất ở dự án tích hợp |
|---|---|---|---|
| Hỏi nhanh SDK/thư viện public | Context7; đối chiếu docs nguồn theo release | Package/version từ lockfile, library ID, requested/served version, URL nguồn và thời điểm lấy | Bản phục vụ khớp yêu cầu; nếu không khớp thì báo mismatch và lấy nguồn ghim; chạy ví dụ tối thiểu trên dependency thật |
| Docs nội bộ có nhiều dịch vụ/nhóm | Backstage Catalog + TechDocs nếu đã có portal hoặc cần ownership tập trung | Entity/owner, commit nguồn, timestamp build, người/ngày review nội dung | Owner còn hợp lệ; link sang source hoạt động; ví dụ/runbook được kiểm trong CI riêng của dịch vụ |
| Di trú version hay quyết định quan trọng | Docs/tag/source gốc ghim commit, có thể dùng Context7 để tìm trước | API signature/changelog của đúng release, kết quả test migration | Không chấp nhận HTTP 200 hay build mới như bằng chứng tương thích |
| Một repo/site nhỏ | SSG ở §1 + metadata trang + pipeline ở §2h | Nguồn, version áp dụng, reviewer và ngày kiểm | Không thêm portal chỉ để có timestamp; duy trì cùng bộ bằng chứng nhẹ hơn |

### 2i.5 Ghép nguồn → bản docs → truy xuất → kiểm code

1. **Nguồn có định danh:** giữ URL chính thức, package/service, version/tag/commit và owner của trang. Ngày index, ngày build và ngày review là ba trường khác nhau; metadata review/owner ở cấp trang là đề xuất của kho, không phải tính năng tự có của mọi công cụ.
2. **Build/publish có dấu vết:** với TechDocs dùng pipeline repo nguồn và storage; kèm commit nguồn, artifact và kết quả kiểm. Giữ lint/link/Diátaxis §2h, không xem chúng là bằng chứng ngữ nghĩa API.
3. **Truy xuất có ranh giới:** câu hỏi gửi Context7 không chứa nội dung nhạy cảm; lưu nguồn/phiên bản thực của kết quả. Docs truy xuất là dữ liệu tham khảo, không có quyền thay đổi chỉ dẫn của người dùng hay quyền tool của agent (mục 12).
4. **Kiểm tương thích bằng việc nhỏ:** ví dụ code phải compile/typecheck/test với lockfile của ứng dụng; runbook phải được diễn tập phù hợp (mục 09), câu trả lời retrieval phải qua eval (mục 07). Freshness chỉ là một tín hiệu chọn tài liệu.
5. **Tái kiểm theo thay đổi có ý nghĩa:** dependency đổi major, source page bị sửa/redirect, owner rời nhóm hoặc test ví dụ hỏng thì mở lại đánh giá. Thời hạn review do dự án đặt theo rủi ro; không có ngưỡng số ngày phổ quát được chứng minh trong đợt này.

**Đã đổi sau §2h:** sửa dòng Context7 ở §2 để không đồng nhất tài liệu “mới nhất” với tài liệu “đúng phiên bản”; thêm hai lớp owner/provenance và freshness có bằng chứng bên cạnh cổng văn xuôi. Không đánh dấu index mới hay ETag trùng là kết luận nội dung kỹ thuật đúng.

**Nguồn §2i:** metadata GitHub API 2/11/2026; các permalink §2i.2–§2i.3; nguồn chính thức ngoài repo [Context7 API Guide](https://context7.com/docs/api-guide), [TechDocs architecture](https://backstage.io/docs/features/techdocs/architecture/), [TechDocs how-to](https://backstage.io/docs/features/techdocs/how-to-guides/). Đã đọc Context7 `LICENSE`, `docs/api-guide.mdx`, `packages/mcp/src/{index.ts,lib/api.ts,lib/constants.ts,lib/types.ts}`, `.github/workflows/test.yml`; Backstage `LICENSE`, catalog descriptor/example, builder/synchronizer/HTML transformer và sanitizer test, `.github/workflows/{verify_docs-quality,verify_e2e-linux}.yml`. **Chưa gọi API hay tái lập build, test và portal của các nguồn.**

## 2j. Hồ sơ trailhq/Trail-Code (Trail-code, tên cũ graft): bản đồ code + “learnings” cho coding agent, telemetry bật mặc định (ảnh README người dùng gửi, đọc mã 3/11/2026)

> Ảnh là phần đầu README: "Trail-code (previously graft) by Trail", "The self-learning context layer for coding agents", bảng Code map / Learnings, Trendshift "#4 Repository Of The Day" (TypeScript), cùng các badge "11K", "npm v0.28.0", "downloads 102K/month", "node >=20", "typescript strict", "license MIT", "telemetry anonymous, opt-out", "OpenSSF Scorecard 7.2". Đã clone `--filter=blob:none` đủ lịch sử, HEAD `b9c2e23e9b579200dba83d47e8dbdd8a488b6988` (2/11/2026). **Không cài, không chạy**: cài gói npm sẽ chạy postinstall có gửi sự kiện (xem dưới).

### 2j.1 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kết quả | Đối chiếu (3/11/2026) |
|---|---|---|
| ★ "11K" | ✅ | 11.040★, 981 fork, 282 issue+PR mở (GitHub search API) |
| "license MIT" | ✅ | `LICENSE` MIT, dòng copyright "Context Graph Engine contributors"; `package.json` `"license": "MIT"` |
| "npm v0.28.0" | ⚠️ cũ một bản | npm `@trailhq/trail-code` và `@nanonets/graft` đều đã lên **0.28.1** (registry). Tag git chỉ tới `v0.21.1`, tức tag đi sau bản npm 7 minor |
| "downloads 102K/month" | ✅ gần đúng | Badge **cộng hai gói** (`.github/scripts/npm-downloads-badge.mjs`). Kỳ 3/10–1/11: `@nanonets/graft` 84.387 + `@trailhq/trail-code` 13.316 = **97.703**. Phần lớn lượt tải vẫn là tên cũ |
| "node >=20", "typescript strict" | ✅ | Khớp README và tsconfig (không kiểm sâu) |
| "telemetry anonymous, opt-out" | ✅ nhưng cần đọc kỹ | Bật mặc định. Xem §2j.3 |
| "OpenSSF Scorecard 7.2" | ✅ | api.securityscorecards.dev: 7.2 (2/11/2026). CI ghim action theo **SHA**, chạy `npm test` (513 file test), có CodeQL và Scorecard |
| "Your code, read on your machine" | ✅ đúng một phần | Map dựng bằng tree-sitter, không model, không mạng. `trail build --deep` gửi tóm tắt tới model mà người dùng chọn |

### 2j.2 Nó làm gì (đọc mã)

- **Graft map**: chỉ mục hàm và nơi gọi, dạng thư mục markdown liên kết dưới `graft/`, tự đồng bộ ở mỗi truy vấn (gồm cả sửa chưa commit). Có MCP server, `trail grep`/`trail map`, `trail viz`.
- **Tích hợp sâu với Claude Code** (mặc định chọn): `trail init` gộp các khối hook vào `.claude/settings.json`, không đè (session-start, prompt, pre-bash, pre-edit, post-bash, post-edit, stop), kèm statusline. Hook pre-bash có thể trả `permissionDecision: deny` cho guardrail có sẵn (`no-timeout`, `prod-after-beta`). Mỗi prompt tự kéo node và learnings liên quan vào ngữ cảnh. Sửa file thì in "blast radius". Định kỳ đọc **nhánh mở của đồng đội** để báo khi trùng hàm.
- **Learnings**: file trong `.trail/learnings/` (commit qua git) hoặc `~/.trail` (cá nhân). `trail init` có bước "cold start": đọc **transcript Claude Code cũ** của repo và **review comment của 50 PR gần nhất** (qua `gh` của người dùng), rồi để Claude Code của người dùng đề xuất learnings (tốn quota Claude của người dùng). Có thêm "skills" tự học từ lệnh lặp lại.
- **Benchmark tự công bố**: SWE-bench Verified **50 instance**: 27/50 → 33/50, ít hơn 23% token, chấm bằng `swebench` 4.1.0 chính thức. Sweep 162 lượt cho kết quả ít hơn 46% tool call và 60% thời gian, đo trên harness của chính họ. Mẫu nhỏ, chưa có bên độc lập chạy lại **(chưa xác minh)**.

### 2j.3 Dữ liệu và rủi ro

- ⚠️ **Telemetry PostHog bật mặc định.** `TELEMETRY.md` liệt kê từng sự kiện, và `src/telemetry/contract.ts` thực thi allowlist: số đếm chỉ gửi theo bucket, chuỗi chỉ thuộc tập cố định. Key chỉ được chèn vào gói npm lúc publish (`scripts/stamp-telemetry-key.mjs`), nên bản clone hoặc fork không gửi gì. Tắt bằng `trail telemetry disable` hoặc `DO_NOT_TRACK=1`; CI không gửi. Xem trước bằng `trail telemetry debug`.
- ⚠️ **Sự kiện `install` gửi ngay trong `npm install`.** `scripts/postinstall.mjs` ghi sự kiện rồi bật một tiến trình tách rời để đẩy lên ngay, **trước khi** người dùng có cơ hội chạy `trail telemetry disable`. Muốn không gửi thì phải đặt `DO_NOT_TRACK=1` **trước khi cài**, hoặc cài với `--ignore-scripts`.
- Hook Stop **đọc transcript** của agent sau mỗi lượt có dùng Trail để đếm câu "saved ~N tokens". Theo `TELEMETRY.md`, chỉ hai bộ đếm dạng bucket được gửi **(theo tài liệu, chưa tự lần hết mã)**.
- **Kết nối Trail workspace** (dịch vụ trả phí) sẽ gửi learnings đã commit của các repo được thêm, **kể cả learnings trên nhánh đồng đội đã push**. Mặc định không kết nối. Lệnh trong sản phẩm sẽ đưa link đăng nhập cho agent chuyển tiếp ("nudge", có sự kiện `brain_signup_*`).
- Hai tên gói cùng mã (`@nanonets/graft`, `@trailhq/trail-code`), dòng dõi từ Nanonets. Nhịp đổi nhanh: 702 commit từ 3/7/2026; `Shrish Dwivedi` 374, `anirudhkumar-nanonets` 181; 132 trailer Claude. Tag git đi sau bản npm.
- Hook tiêm ngữ cảnh ở mọi prompt và đổi hành vi agent (rủi ro tin map hoặc learnings cũ, giống Graphify §2e.3). Learnings là file trong repo nên ai push được là đưa được chỉ dẫn vào ngữ cảnh agent của cả đội. Cần review `.trail/learnings/` như review mã.

### 2j.4 So với cùng loại

| Tool | ★ (gần nhất) | License | Telemetry | Khác |
|---|---|---|---|---|
| **trailhq/Trail-Code** | 11k (3/11) | MIT | **Bật mặc định**, allowlist trong mã, install event lúc postinstall | Map + learnings đội + skills tự học, hook sâu cho Claude Code, có SWE-bench n=50 |
| `Graphify-Labs/graphify` (§2e) | 141k (3/11) | Apache-2.0 | Không | Graph đa phương tiện, nhãn EXTRACTED/INFERRED, không có lớp learnings |
| `colbymchenry/codegraph` (§2f) | 76k (31/10) | MIT | Bật mặc định | MCP Rust + SQLite, file-watch |
| `Egonex-AI/Understand-Anything` (mục 01 §3b) | 89k (30/10) | MIT | – | Pipeline LLM, hướng tới người học |

### 2j.5 Dùng thế nào

- Cài với `DO_NOT_TRACK=1` đặt sẵn (hoặc `npm i -g --ignore-scripts`), ghim phiên bản (`@trailhq/trail-code@0.28.1`), rồi chạy `trail telemetry disable` một lần.
- Đọc diff của `.claude/settings.json` sau `trail init`. Bỏ bước cold start nếu transcript hoặc review cũ có thông tin nhạy cảm. Không kết nối workspace với repo khách hàng.
- Không cài chồng với Graphify hoặc codegraph (§2d điểm 4). Chọn Trail khi giá trị nằm ở **learnings đội qua git**, chọn Graphify khi cần map tất định không telemetry.

**Nguồn §2j:** ảnh README người dùng gửi 3/11/2026 · clone https://github.com/trailhq/Trail-Code HEAD `b9c2e23e9b579200dba83d47e8dbdd8a488b6988` (README.md: What stays on your machine, SWE-bench Verified, Claude Code deep integration; TELEMETRY.md; LICENSE; package.json; `scripts/{postinstall,stamp-telemetry-key}.mjs`; `src/claude/pre-bash.ts`; `.github/workflows/ci.yml`; `.github/scripts/npm-downloads-badge.mjs`; `git shortlog`, `git tag`) · registry.npmjs.org `@trailhq/trail-code`, `@nanonets/graft` (latest 0.28.1) · api.npmjs.org downloads last-month 3/10–1/11/2026 · api.securityscorecards.dev (7.2, 2/11/2026) · GitHub search API `repo:trailhq/Trail-Code` 3/11/2026.

<a id="factory-docs-executable-2026-11-04"></a>

## 2k. Nâng trần 4/11/2026: tài liệu là hợp đồng chạy được của xưởng phần mềm

**Trần và khoảng trống.** §2h đã có lint/link; §2i có owner, provenance và đúng phiên bản; §2j có tri thức codebase. Xưởng vẫn có thể phát hành một hướng dẫn đẹp nhưng ví dụ đã hỏng, hoặc runbook chưa từng phục hồi được hệ thống. Bước sâu hơn là nối **mỗi lời hứa kỹ thuật quan trọng với một phép kiểm** ở repo sản phẩm. Phần này đọc mã và CI upstream, không chạy ví dụ hay benchmark ngoài kho; đây là thiết kế tích hợp, chưa là kết quả nghiệm thu.

### 2k.1 Sybil: lấy ví dụ ngay trong docs đưa vào test runner

| Thuộc tính | Kết quả đọc 4/11/2026 |
|---|---|
| Repo / tác giả | `simplistix/sybil`, Chris Withers và cộng đồng; công cụ kiểm ví dụ tài liệu Python |
| License · phiên bản | MIT trong `LICENSE.txt`; HEAD `de4cdc5a24d5c8879bf3db1089924f51bd25c972`; `pyproject.toml` yêu cầu Python ≥3.11; không thu thập sao |
| Cơ chế | Parser tìm vùng ví dụ trong reST/Markdown/MyST; tích hợp pytest tạo `SybilItem` cho từng example, `runtest()` gọi `example.evaluate()` và gắn fixtures vào namespace |
| Đường thực thi | `PythonEvaluator` dùng `compile(..., 'exec')` rồi `exec` trong namespace; đây là **thực thi mã tài liệu**, không phải sandbox. Chỉ chạy nguồn đã review trong môi trường test có quyền giới hạn |
| CI đã đọc | Workflow `ci.yml` gọi reusable workflow `cjw296/python-workflow/.../uv-ci.yml@v2`; repo có fixture pass/fail. Tham chiếu tag workflow vẫn là phụ thuộc cần kiểm khi vendor |
| Giới hạn | Chỉ vùng do parser/pattern chọn mới thành test. Code block chạy hết nhưng không có assertion có thể vẫn không chứng minh kết quả; ví dụ bị skip hay không được collect phải được báo riêng |

[Collector và callsite]( https://github.com/simplistix/sybil/blob/de4cdc5a24d5c8879bf3db1089924f51bd25c972/src/sybil/integration/pytest.py ) · [evaluator Python]( https://github.com/simplistix/sybil/blob/de4cdc5a24d5c8879bf3db1089924f51bd25c972/src/sybil/evaluators/python.py ) · [mẫu khai báo parser]( https://github.com/simplistix/sybil/blob/de4cdc5a24d5c8879bf3db1089924f51bd25c972/docs/examples/quickstart/conftest.py ) · [license]( https://github.com/simplistix/sybil/blob/de4cdc5a24d5c8879bf3db1089924f51bd25c972/LICENSE.txt ) · [CI]( https://github.com/simplistix/sybil/blob/de4cdc5a24d5c8879bf3db1089924f51bd25c972/.github/workflows/ci.yml ).

### 2k.2 Chọn đúng lớp kiểm

| Nhu cầu | Baseline / lựa chọn | Bằng chứng và phần còn thiếu |
|---|---|---|
| Ví dụ Python trong docs | `doctest` chuẩn; Sybil khi cần parser/fixture từ nhiều định dạng; `sphinx.ext.doctest` nếu đã dùng Sphinx (§1) | Báo cáo số ví dụ collect/pass/fail/skip; assertion trên giá trị/side effect quan trọng. Không ép stack JS/Go dùng Python chỉ để có doctest |
| Văn phong/thuật ngữ | Vale; CSpell; markdownlint (§2h) | Kiểm văn bản, không chứng minh API tương thích. Với Vale, `--no-exit` có thể biến lỗi lint thành mã thoát 0; không dùng nó làm cổng blocking |
| Hợp đồng SDK/API | Ví dụ phải compile/typecheck/test với lockfile thật; đối chiếu API contract ở mục 29 | Báo cáo version/dependency và kết quả request; renderer HTML thành công không kiểm đường gọi |
| Runbook vận hành | Diễn tập có phạm vi trong môi trường thử; liên kết mục 33 | Chứng cứ khôi phục, thời gian và mất dữ liệu; không chạy lệnh phá hủy chỉ vì nó nằm trong docs |

Chi tiết Vale được đọc lại ở HEAD `0d9e80234ba63323fefa027b5698467cf477c46d` (MIT): `main.go` chọn exit 2 khi có tài liệu không lint được, exit 1 khi `hasErrors` và không `--no-exit`, còn lại exit 0. Luật/style và mức severity phải được review, không lấy một lệnh có output làm bằng chứng CI đang chặn. [Đường exit]( https://github.com/vale-cli/vale/blob/0d9e80234ba63323fefa027b5698467cf477c46d/cmd/vale/main.go ) · [cờ CLI]( https://github.com/vale-cli/vale/blob/0d9e80234ba63323fefa027b5698467cf477c46d/cmd/vale/flag.go ) · [CI đa nền tảng]( https://github.com/vale-cli/vale/blob/0d9e80234ba63323fefa027b5698467cf477c46d/.github/workflows/test.yml ).

### 2k.3 Luồng tích hợp và tiêu chí nghiệm thu

1. Mỗi trang gắn owner, version áp dụng và nguồn như §2i; chọn loại Diátaxis để tách tutorial khỏi reference và giải thích kiến trúc.
2. Với hướng dẫn quan trọng, trỏ đến ví dụ có assertion ngay trong docs hoặc test của repo sản phẩm; tránh sao chép cùng đoạn code thành hai bản trôi khác nhau.
3. CI kiểm lint/link trước, rồi collect và chạy ví dụ bằng runtime/lockfile của sản phẩm. Lưu danh sách file và số ví dụ; **zero collected** không được ghi là “docs đã được kiểm”.
4. Xuất artifact gồm commit tài liệu, commit ứng dụng, dependency lock, báo cáo test và site build; thay dependency/API/CLI thì chạy lại các ví dụ bị ảnh hưởng.
5. Chặn phát hành nếu ví dụ luồng chính hỏng, API bị bỏ mà docs còn dạy, hoặc runbook bắt buộc không có bằng chứng diễn tập còn hiệu lực theo chính sách nhóm. Lint/style có thể chia severity, không biến mọi cảnh báo câu chữ thành lỗi sản phẩm.
6. Portal Backstage (§2i) phù hợp khi cần catalog owner và nhiều dịch vụ; SSG đơn giản vẫn đủ với một repo. Lớp kiểm trên không phụ thuộc phải triển khai portal.

**Đã nâng sâu:** từ “docs hợp lệ và có nguồn” sang ví dụ thực thi được và artifact gắn với release. Không tự sửa/cài pipeline của dự án khác trong kho này.

**Nguồn §2k:** các permalink trên; [README Sybil]( https://github.com/simplistix/sybil/blob/de4cdc5a24d5c8879bf3db1089924f51bd25c972/README.rst ), [manifest]( https://github.com/simplistix/sybil/blob/de4cdc5a24d5c8879bf3db1089924f51bd25c972/pyproject.toml ), [Vale LICENSE]( https://github.com/vale-cli/vale/blob/0d9e80234ba63323fefa027b5698467cf477c46d/LICENSE ). Đã đọc mã/LICENSE/CI tại SHA ghi trong hồ sơ; chưa chạy upstream.

## 3. Nguồn

- https://www.mintlify.com/library/best-llms-txt-platforms · https://dupple.com/learn/best-documentation-tools · https://ekline.io/blog/docusaurus-alternatives · https://www.pkgpulse.com/guides/best-documentation-frameworks-2026 · https://docsalot.dev/blog/best-mintlify-alternatives · https://affine.pro/blog/best-technical-documentation-software-tools-for-developers
- https://upstash.com/blog/context7-llmtxt-cursor · https://upstash.com/blog/new-context7 · https://glama.ai/mcp/servers/upstash/context7 · https://www.npmjs.com/package/@upstash/context7-mcp · https://tooldirectory.ai/tools/context7
- https://codersera.com/blog/llms-txt-complete-guide-2026/ · https://limy.ai/blog/llms-txt-in-2026-the-full-guide · https://aisaasradar.com/article/llms-txt-adoption-data-2026 · https://seeklab.io/blog/what-is-llmstxt-the-honest-2026-guide/
- §2b (12/10/2026): https://github.com/vuejs/vitepress · https://github.com/rust-lang/mdBook · https://github.com/sphinx-doc/sphinx · https://github.com/zensical/zensical · https://github.com/docsifyjs/docsify · https://github.com/yamadashy/repomix · https://github.com/AsyncFuncAI/deepwiki-open · https://github.com/coderamp-labs/gitingest · https://github.com/shuding/nextra · https://github.com/mintlify/starter
- §2c (12/10/2026): https://github.com/braedonsaunders/codeflow (clone đầy đủ, HEAD `b0e82d1`: README.md, index.html, cli/codeflow.mjs, card/action.yml, card/lib/analyzer.js, card/README.md, .github/workflows/, tests/) · https://codeflow-five.vercel.app/ · https://github.com/braedonsaunders · https://themenonlab.blog/blog/codeflow-github-architecture-visualizer · https://www.skills.sh/akillness/jeo-skills/codeflow · https://github.com/ahmedkhaleel2004/gitdiagram · https://github.com/sverweij/dependency-cruiser · https://github.com/MaibornWolff/codecharta
