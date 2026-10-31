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

## 3. Nguồn

- https://www.mintlify.com/library/best-llms-txt-platforms · https://dupple.com/learn/best-documentation-tools · https://ekline.io/blog/docusaurus-alternatives · https://www.pkgpulse.com/guides/best-documentation-frameworks-2026 · https://docsalot.dev/blog/best-mintlify-alternatives · https://affine.pro/blog/best-technical-documentation-software-tools-for-developers
- https://upstash.com/blog/context7-llmtxt-cursor · https://upstash.com/blog/new-context7 · https://glama.ai/mcp/servers/upstash/context7 · https://www.npmjs.com/package/@upstash/context7-mcp · https://tooldirectory.ai/tools/context7
- https://codersera.com/blog/llms-txt-complete-guide-2026/ · https://limy.ai/blog/llms-txt-in-2026-the-full-guide · https://aisaasradar.com/article/llms-txt-adoption-data-2026 · https://seeklab.io/blog/what-is-llmstxt-the-honest-2026-guide/
- §2b (12/10/2026): https://github.com/vuejs/vitepress · https://github.com/rust-lang/mdBook · https://github.com/sphinx-doc/sphinx · https://github.com/zensical/zensical · https://github.com/docsifyjs/docsify · https://github.com/yamadashy/repomix · https://github.com/AsyncFuncAI/deepwiki-open · https://github.com/coderamp-labs/gitingest · https://github.com/shuding/nextra · https://github.com/mintlify/starter
- §2c (12/10/2026): https://github.com/braedonsaunders/codeflow (clone đầy đủ, HEAD `b0e82d1`: README.md, index.html, cli/codeflow.mjs, card/action.yml, card/lib/analyzer.js, card/README.md, .github/workflows/, tests/) · https://codeflow-five.vercel.app/ · https://github.com/braedonsaunders · https://themenonlab.blog/blog/codeflow-github-architecture-visualizer · https://www.skills.sh/akillness/jeo-skills/codeflow · https://github.com/ahmedkhaleel2004/gitdiagram · https://github.com/sverweij/dependency-cruiser · https://github.com/MaibornWolff/codecharta
