# 10 · Local LLM Inference, Vector DB, RAG & Agent Memory

> Chạy model tại chỗ, lưu trữ vector, RAG và bộ nhớ dài hạn cho agent. Số sao ước lượng 7–10/2026, các nguồn lệch nhau nhiều.

## 1. Inference engine / runtime

| Dự án | Repo | License | ★ (ước lượng) | Vai trò | Ghi chú |
|---|---|---|---|---|---|
| **Ollama** | ollama/ollama | MIT | ~170–180k | CLI/daemon chạy model local, API tương thích OpenAI | Wrapper trên llama.cpp; dễ nhất cho dev |
| **llama.cpp** | ggml-org/llama.cpp | MIT | ~85–130k | Engine C/C++ nền tảng (GGUF, quantization, CPU/GPU/Metal) | Nền của Ollama, LM Studio, nhiều app desktop |
| **vLLM** | vllm-project/vllm | Apache-2.0 | ~80–90k | Serving engine đa người dùng (PagedAttention, continuous batching) | Chuẩn production cho open-weight |
| **SGLang** | sgl-project/sglang | Apache-2.0 | ~20–29k | Serving + RadixAttention, structured generation | Đối thủ vLLM, mạnh về workflow stateful |
| **LM Studio** | (đóng) | Proprietary | – | GUI desktop chạy model local | Không mã mở |
| **Open WebUI** | open-webui/open-webui | BSD-3 (có điều khoản) | – | Giao diện chat tự host nối Ollama/OpenAI API | |
| **TensorRT-LLM / MLX / llamafile** | nvidia · ml-explore · mozilla-ai | – | – | NVIDIA tối ưu / Apple Silicon / single-file | Theo phần cứng |

**Chọn:** dev cá nhân → Ollama; serve nhiều user → vLLM (hoặc SGLang); nhúng/edge → llama.cpp.

## 2. Vector database

| DB | Repo | License | ★ | Thế mạnh | Giới hạn |
|---|---|---|---|---|---|
| **Milvus** | milvus-io/milvus | Apache-2.0 | ~42k | Quy mô tỷ vector, phân tán | Vận hành phức tạp |
| **Qdrant** | qdrant/qdrant | Apache-2.0 | ~25k+ (nguồn cũ 11.5k) | Rust, filtering mạnh, recall cao | |
| **Chroma** | chroma-core/chroma | Apache-2.0 | ~20k+ (nguồn cũ 7k) | Nhẹ, nhúng trong app, prototype | Quy mô nhỏ |
| **Weaviate** | weaviate/weaviate | BSD-3 | ~15k | Hybrid search, module hóa | |
| **pgvector** | pgvector/pgvector | PostgreSQL | ~17k (nguồn cũ 4.5k) | Dùng ngay trong Postgres | Ma sát vận hành > 10–50M vector (pgvectorscale cải thiện) |
| **LanceDB** | lancedb/lancedb | Apache-2.0 | – | Serverless, nhúng, định dạng Lance | |
| Pinecone, Turbopuffer | (đóng) | – | – | Managed | |

**Benchmark mâu thuẫn** (AIMultiple: pgvector QPS cao nhất, Qdrant recall cao nhất; 50M-vector test khác lại nghiêng pgvectorscale) → **đo trên dữ liệu của mình**.

## 3. RAG framework & graph RAG

| Dự án | Repo | ★ | Ghi chú |
|---|---|---|---|
| LlamaIndex | run-llama/llama_index | ~48k | Xem mục 02 |
| **Microsoft GraphRAG** | microsoft/graphrag | – | RAG trên đồ thị tri thức, tổng hợp cộng đồng (community summaries) |
| **LightRAG** | HKUDS/LightRAG | – | Graph + vector RAG nhẹ, nhanh hơn GraphRAG |
| RAGFlow | infiniflow/ragflow | – | RAG engine có UI, parse tài liệu sâu |
| Haystack | deepset-ai/haystack | ~20k | Pipeline RAG production |

## 3b. Kiểm hai ảnh của Brij Kishore Pandey: "RAG Evolution" và "The $0 AI architecture stack" (ảnh người dùng gửi, 2026-10-13)

> Hai trang của cùng một carousel 17 trang (ghi "10 / 17" và "12 / 17"), ký tên **Brij Kishore Pandey (@brijpandeyji)**, người viết nội dung AI phổ thông trên LinkedIn/X. Không tìm thấy bài gốc đã đánh chỉ mục (13/10/2026); đánh giá dựa trên nội dung ảnh, đối chiếu docs chính thức. Trang 09/17 ("How to become an AI engineer in 2026") kiểm ở mục 08 §2f.

### 3b.1 "Classic RAG vs GraphRAG vs Agentic RAG"

| Cột | Ảnh nói | Đánh giá | Chỗ cần sửa / bổ sung |
|---|---|---|---|
| Classic RAG | Query → Embed → Vector DB → Top-k → Prompt + LLM → Answer; hợp FAQ, câu hỏi một bước | ⚠️ | Đây là bản **naive**. RAG "cổ điển" chạy production thường có thêm **hybrid search** (BM25 + vector), **reranking**, viết lại câu hỏi và lọc theo quyền — mấy bước này thường đáng làm trước khi lên GraphRAG (§3, mục 08 §2c ô 18) |
| GraphRAG | Query → **trích entity + quan hệ** → knowledge graph → duyệt subgraph → tóm tắt + LLM | ⚠️ | Vẽ việc trích entity/quan hệ như bước **lúc truy vấn**. Với Microsoft GraphRAG, đồ thị và bản tóm tắt cộng đồng được dựng **lúc index** (gọi LLM trên từng chunk — nguồn chi phí chính); lúc hỏi chỉ trích entity của câu hỏi rồi tìm cục bộ (local search) hoặc map-reduce qua tóm tắt cộng đồng (global search). Hạn chế "chi phí dựng và bảo trì đồ thị" thì đúng; LightRAG (§3) là lựa chọn rẻ hơn |
| Agentic RAG | Agent lập kế hoạch → chọn vector/graph/web/tool → tổng hợp → tự đánh giá, lặp nếu yếu → trả lời | ⚠️ | Ý đúng, nhưng "tự đánh giá" bằng chính model là lời khai (mục 03 §8c): cần **ngân sách vòng lặp** và eval ngoài. Thiếu rủi ro **prompt injection gián tiếp** khi agent đọc web/tài liệu (mục 12 §1) |
| Thông điệp cuối | "Năng lực tăng ở mỗi bước, chi phí và quản trị cũng tăng; chọn cách đơn giản nhất qua được eval" | ✅ | Lời khuyên đúng nhất của ảnh. Nhưng mũi tên "retrieves → connects → reasons" dễ đọc thành tiến hoá thay thế; thực tế ba kiểu **hợp ba loại câu hỏi khác nhau** (một bước / nhiều bước theo quan hệ / nhiều nguồn, động) và Agentic RAG thường dùng hai kiểu kia làm tool |

### 3b.2 "The $0 AI architecture stack: nine layers, all open-source or free tier"

| Tầng | Ảnh ghi | Có thật $0? | Ghi chú (đọc 13/10/2026) |
|---|---|---|---|
| Frontend | Next.js, Streamlit, Vercel | ⚠️ | Next.js, Streamlit: mã mở. **Vercel Hobby chỉ cho dùng cá nhân, phi thương mại** (docs Vercel, fair use) và có trần (4 CPU-giờ, 1 triệu invocation/tháng; vượt thì chờ 30 ngày) |
| Orchestrator | LangGraph, CrewAI | ✅ | Cả hai MIT; nền tảng hosted của họ mới tính phí |
| LLM | Ollama, Gemma, Llama, Mistral, Qwen "chạy local" | ⚠️ | Không tốn tiền license nhưng **tốn phần cứng**; license model khác nhau: Llama theo Llama Community License (không phải OSI, có điều khoản quy mô và chính sách sử dụng), Gemma theo điều khoản riêng của Google **(chưa xác minh bản mới nhất)**, nhiều model Mistral/Qwen là Apache-2.0. Đọc license từng model trước khi dùng thương mại |
| RAG | LlamaIndex, Qdrant, ChromaDB | ✅ | MIT/Apache-2.0; Qdrant Cloud có gói miễn phí nhỏ |
| MCP tools | MCP, GitHub, Gmail | ✅ (có điều kiện) | Giao thức và server miễn phí; Gmail cần OAuth app Google, scope nhạy cảm có thể phải qua thẩm định. Cấp tool cho agent là bề mặt tấn công (mục 12) |
| Code agent | **Claude Code**, Aider | ❌ | **Claude Code không có gói $0**: docs ghi "requires a Pro, Max, Team, Enterprise, or Console account. The free claude.ai plan does not include Claude Code access." Aider (Apache-2.0) thì $0 nếu ghép với model local |
| Data | SQLite, DuckDB, Supabase | ⚠️ | SQLite, DuckDB: mã mở, $0. Supabase Free: 2 project, 500 MB DB mỗi project; project free bị tạm dừng khi không hoạt động **(chưa xác minh số ngày trong lần đọc này)** |
| Observability | Arize Phoenix, Langfuse | ✅ (lưu ý license) | Langfuse core MIT, tự host được; **Phoenix là Elastic License 2.0** — source-available, không phải "open-source" theo OSI (catalog mục 07) |
| Deploy | Docker, Cloudflare, Hugging Face | ⚠️ | Docker không phải nơi host. **Không gói miễn phí nào trong ảnh chạy được Ollama với GPU**; HF Spaces CPU miễn phí có ngủ khi không dùng; Cloudflare Workers không chạy Ollama. Luồng "Ollama generates" ở cột phải mâu thuẫn với tầng Deploy $0 |

**Tổng:** 3 ✅, 5 ⚠️, 1 ❌. Ảnh tự ghi đúng ở chân trang: "kiểm giới hạn từng free tier trước khi phụ thuộc vào nó". Đọc đúng thì đây là **stack prototype chạy trên máy mình**, không phải stack production $0: hai thứ phải trả tiền đầu tiên là **GPU để chạy model** (hoặc API model) và **coding agent** nếu dùng Claude Code.

**Bổ sung khi dùng thật:** thêm eval (mục 07: Promptfoo, Ragas, DeepEval) — ảnh RAG khuyên "pick the simplest one that passes your evals" nhưng ảnh stack lại không có tầng eval riêng ngoài trace; thêm gateway/router để đổi giữa model local và API khi tải tăng (§6).

## 4. Agent memory (bộ nhớ dài hạn)

| Dự án | Repo | License | ★ (18/9/2026, Atlan) | Cách tiếp cận | Ghi chú |
|---|---|---|---|---|---|
| **Mem0** | mem0ai/mem0 | Apache-2.0 | ~65.6k | Memory layer trích xuất/hợp nhất "facts" theo user/session | Phổ biến nhất; tranh cãi benchmark với Zep |
| **Zep / Graphiti** | getzep/graphiti | Apache-2.0 | ~31k | Đồ thị tri thức theo thời gian (temporal KG) | Zep-product không còn self-host, Graphiti thì có |
| **Letta** (MemGPT) | letta-ai/letta | Apache-2.0 | ~24.8k | Agent tự quản lý memory tiers như OS | Nguồn gốc paper MemGPT |
| **cognee** | topoteretes/cognee | Apache-2.0 | ~30k | Memory + knowledge graph pipeline | |
| LangMem | langchain-ai/langmem | MIT | – | Memory cho LangGraph | |
| Hindsight | – | MIT | ~4k | Nhỏ | |
| agent-memory (X-Agents tự viết) | seeker19110/X-Agents | – | – | SQLite + candidate pipeline: memory phải qua đề xuất → duyệt → ghi | Mục 23 §3.1; Hermes `safe-ai-state-authority` cùng ý |

**Benchmark LongMemEval:** Zep báo 63.8–75.1%, Mem0 báo Zep chỉ 58.4% và tự nhận 49% → số liệu chéo nhà cung cấp không đáng tin; chọn theo kiến trúc (fact-store vs temporal graph vs OS-style).

**Ghi chú từ repo của chủ kho (mục 23):** X-Agents chọn **không dùng pgvector** cho bộ nhớ nhỏ (SQLite + FTS đủ, tránh vận hành Postgres); Anthropic **không có embedding API** → embedding local (Ollama `nomic-embed-text`) hoặc Voyage.

## 4b. Kiểm ảnh: rohitg00/agentmemory, bộ nhớ dài hạn cho coding agent (ảnh người dùng gửi, 2026-10-13)

> Ảnh là danh sách thư mục trang repo trên điện thoại: `rohitg00/agentmemory` Public, Issues 217, commit gần nhất của `mvanhorn` "yesterday", các thư mục `.claude-plugin` (4 months ago), `.codex-plugin` (2 months ago), `.github`, `READMEs`, `assets`, `benchmark`, `deploy`, `docs`, `eval`, `examples/python`. Đã clone toàn bộ repo (568 commit, HEAD `36eb328` 13/10/2026), đọc README, `SECURITY.md`, `GOVERNANCE.md`, `MAINTAINERS.md`, `benchmark/LONGMEMEVAL.md`, `benchmark/COMPARISON.md`, rồi tự build và chạy test.

### 4b.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 13/10/2026) |
|---|---|
| Repo | `rohitg00/agentmemory` · ~29k★, ~2,6k fork, **Apache-2.0** · bản v0.9.30 · ~274 issue, ~287 PR mở · npm `@agentmemory/agentmemory` ~36,3k lượt tải/tháng (13/9–12/10/2026) |
| Tác giả | Rohit Ghumare (`rohitg00`, ghi "Independent" trong `MAINTAINERS.md`): ~468/568 commit; 53 tên tác giả. Cũng là chủ `awesome-claude-code-toolkit` (mục 08). Commit đầu 25/2/2026 |
| Làm gì | Ghi lại mọi lần agent dùng tool qua hook (PostToolUse, Stop/SessionEnd, SessionStart), nén thành bộ nhớ có cấu trúc, rồi đầu phiên sau tìm lại và chèn vào ngữ cảnh (mặc định ≤ 2.000 token) |
| Tìm kiếm | BM25 (mặc định, không cần key) + vector (`all-MiniLM-L6-v2` chạy cục bộ khi đặt `EMBEDDING_PROVIDER=local`) + đồ thị tri thức (tùy chọn) |
| Giao diện | 54 MCP tool, REST `:3111`, viewer `:3113`; plugin cho Claude Code, Codex, Cursor; adapter cho Copilot CLI, Gemini CLI, OpenCode, Hermes, OpenClaw, pi… (README ghi 20 adapter) |
| Nền | Chạy trên **iii engine** (`iii-hq/iii`, ~19k★) bản ghim v0.22.1: iii thay Express, CSDL, hàng đợi, pm2 và OTEL. Lưu trạng thái bằng file (mặc định) hoặc Redis |

### 4b.2 Kiểm từng ô trong ảnh

| Ô trong ảnh | Kiểm | Ghi chú |
|---|---|---|
| Thời điểm chụp | ⚠️ cũ | Mọi mốc thời gian khớp với ngày ~26/7/2026: commit "yesterday" của `mvanhorn` là `d8b5267` (Matt Van Horn, 25/7/2026, thêm cờ `--data-dir`); `.codex-plugin` sửa lần cuối 12/5; `.claude-plugin` 27/3. Ảnh cũ khoảng 2,5 tháng |
| Issues 217 | ⚠️ cũ | Nay ~274 issue mở |
| "mvanhorn" là người commit gần nhất | ⚠️ dễ hiểu sai | Matt Van Horn chỉ có 2 commit. Gần như toàn bộ mã do chủ repo viết; nay commit gần nhất là của Rohit Ghumare |
| Các thư mục `.claude-plugin`, `.codex-plugin`, `benchmark`, `eval`, `deploy`… | ✅ | Còn đủ; thêm `.cursor-plugin`, `integrations/`, `packages/`, `website/` không thấy trong ảnh vì bị cắt ở "View all files" |
| Public | ✅ | Apache-2.0 |

**Tổng:** 2✅ / 3⚠️ / 0❌. Ảnh không sai, nhưng là ảnh danh sách file nên gần như không nói gì về sản phẩm; mọi ô ⚠️ đều do chụp từ 7/2026.

### 4b.3 Điều ảnh không nói (đọc mã và tự chạy)

- **Test:** README ghi "3,300+ tests passing". Tự chạy `npx vitest run` (không tính test tích hợp) ngày 13/10/2026: **3.339 pass, 7 fail, 4 skip / 3.350**. 6 ca fail ở `openclaw-connect.test.ts` là do chưa `npm run build`; build xong chạy lại thì 22/22 pass. Ca còn lại (`viewer-host`) fail vì sandbox không có IPv6 `::1`. Tuy vậy huy hiệu workflow `ci.yml` trên `main` đang **"failing"** (shields 13/10/2026; chưa xác minh job nào đỏ).
- **Benchmark cần đọc kỹ.** 95,2% R@5 trên LongMemEval-S là **độ phủ truy xuất** (có ít nhất một phiên đúng trong top 5), không có LLM trả lời hay chấm. Bảng "vs Competitors" đặt số này cạnh Mem0 68,5% và Letta 83,2% đo trên **LoCoMo**, tức là hai benchmark và hai thước đo khác nhau. `benchmark/COMPARISON.md` tự ghi cảnh báo "apples vs oranges", nhưng bảng trong README thì không. Chính README cũng ghi MemPalace chỉ dùng vector đạt 96,6%, cao hơn agentmemory.
- **Phụ thuộc engine không phải mã mở chuẩn OSI.** agentmemory là Apache-2.0, nhưng thư mục `engine/` của iii (phần chạy thật) theo **Elastic License 2.0**; SDK mới là Apache-2.0. Không chặn dùng nội bộ, nhưng cần lưu ý nếu định cung cấp dịch vụ cho bên thứ ba.
- **Bảo mật mặc định khá:** REST, viewer và engine bind `127.0.0.1`; có `AGENTMEMORY_SECRET` (Bearer) khi triển khai từ xa; có bộ lọc bí mật trước khi lưu; telemetry của iii tắt mặc định (`III_TELEMETRY_ENABLED=false`); file iii tải bằng curl có kiểm SHA256 trong README. Điểm trừ: không commit lockfile (giải thích trong `SECURITY.md`), và `SECURITY.md` ghi "6 production deps" trong khi `package.json` có 10.
- **Bộ nhớ ghi lại mọi lời gọi tool** của agent. Cần xem trước thư mục dữ liệu (`~/.local/share/agentmemory` trên Linux) có được backup/mã hóa theo chính sách của dự án không, nhất là repo có dữ liệu khách hàng.
- **Một người duy trì:** `GOVERNANCE.md` theo mẫu MVG của Linux Foundation, tự nhận "single-maintainer reality" và có kế hoạch thêm maintainer.

### 4b.4 So sánh & dùng thế nào

| Hướng | Ví dụ (shields 13/10/2026) | Khác agentmemory |
|---|---|---|
| Bộ nhớ dạng API/fact-store | Mem0 (~67k★, Apache-2.0), supermemory (~31k★, MIT) | Dịch vụ/thư viện chung cho mọi app; agentmemory chuyên cho coding agent qua hook |
| Agent tự quản bộ nhớ | Letta (~25k★, Apache-2.0) | Là runtime agent đầy đủ, không cắm vào Claude Code/Codex |
| Bộ nhớ có sẵn của agent | `CLAUDE.md`/`MEMORY.md`, memory bank của Cline | Không cần server; đủ cho repo nhỏ, nhưng nạp nguyên văn vào ngữ cảnh |
| Tự viết, có duyệt | agent-memory của X-Agents (mục 23 §3.1) | Bộ nhớ phải qua đề xuất → duyệt → ghi; agentmemory ghi tự động |

- **Hợp khi:** dùng nhiều coding agent trên cùng dự án và muốn một kho nhớ chung, tìm được, chạy cục bộ.
- **Với repo của chủ kho:** các repo đã dùng `PROGRESS.md`/`TRAPS.md`/`docs/work` làm "bộ nhớ có duyệt", và luật "nội dung ngoài là dữ liệu" (ADR-0009). Nếu thử agentmemory, nên giữ nó ở vai trò tra cứu, không thay các file đó; tắt chèn tự động đầu phiên ở repo nhạy cảm, và kiểm bộ lọc bí mật trước khi bật.

**Nguồn §4b:** https://github.com/rohitg00/agentmemory (clone đầy đủ, HEAD 36eb328; README, SECURITY.md, GOVERNANCE.md, MAINTAINERS.md, package.json, benchmark/LONGMEMEVAL.md, benchmark/COMPARISON.md, test/openclaw-connect.test.ts, src/cli/engine-launch.ts) · https://www.npmjs.com/package/@agentmemory/agentmemory · https://api.npmjs.org/downloads/point/last-month/@agentmemory/agentmemory · https://trendshift.io/repositories/25123 · https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2 · https://github.com/iii-hq/iii (README mục License: engine ELv2, SDK Apache-2.0) · https://www.sourcepulse.org/projects/27459985 · https://tessl.io/registry/skills/github/rohitg00/agentmemory/agentmemory-architecture · https://arxiv.org/abs/2410.10813 (LongMemEval) · https://snap-stanford.github.io/LoCoMo/ · https://github.com/mem0ai/mem0 · https://github.com/letta-ai/letta · https://github.com/supermemoryai/supermemory

## 4c. Gentleman-Programming/engram: bộ nhớ dài hạn cho coding agent bằng một binary Go (link người dùng gửi, 2026-10-16)

> Đã clone toàn bộ repo (1.126 commit, HEAD `9c4382f` 15/10/2026, tag v3.4.0), đọc README, DOCS.md, SECURITY.md, TRADEMARKS.md, `plugin/claude-code/` (hooks.json, scripts), `internal/server`, `internal/store`, `internal/mcp`, và tự chạy test hai package lõi.

### 4c.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 16/10/2026) |
|---|---|
| Repo | `Gentleman-Programming/engram` · ~7,3k★, 752 fork, **MIT** · site engram.gentlemanprogramming.com · tạo 16/2/2026 |
| Tác giả | Daniel Rosales 482 commit, Alan Buscaglia 409 (+82 dưới `Alan-TheGentleman`); thuộc hệ sinh thái Gentle-AI của cộng đồng Gentleman Programming. Tên "Engram" và logo là **thương hiệu** của Alan Buscaglia (`TRADEMARKS.md`), không ảnh hưởng license MIT của mã |
| Kiến trúc | **Một binary Go** (Go 1.25) + **SQLite FTS5** ở `~/.engram/engram.db`; cùng dữ liệu qua 4 cửa: MCP stdio, HTTP API, CLI, TUI. Không cần Node, Python hay Docker |
| Quy mô mã | 512 file Go (347 file test), ~74k dòng mã không tính test; 13 workflow CI (gồm `release-gap-audit`, `pr-size-notice`, chính sách issue/PR) |
| MCP | **26 tool** `mem_*` (save, search, context, timeline, session start/end/summary, judge/compare cho xung đột, pin, review, doctor…), khớp DOCS.md "MCP Tools (26 tools)". Một bài tổng hợp ghi "19 tool" là số cũ |
| Agent hỗ trợ | 14 đích cài: Claude Code, Codex, OpenCode, Gemini CLI, Cursor, Windsurf, Kiro, Antigravity, VS Code Copilot, Qwen Code, Pi, Kilo, Kimi, CommandCode; lệnh `engram setup <agent>` |

### 4c.2 Đọc mã: cách nó nhớ

- **Agent tự quyết điều cần nhớ, không có LLM nén ngầm.** Agent gọi `mem_save` với tiêu đề, loại và các trường What/Why/Where/Learned; engram chỉ lưu và đánh chỉ mục FTS5. Khác claude-mem (dùng AI nén mỗi phiên thành observation) và agentmemory (engine riêng). DOCS ghi rõ quyết định "why no raw auto-capture".
- **Chỉ nghe loopback.** HTTP server bind `127.0.0.1` (mặc định cổng 7437), có tuỳ chọn Unix socket (`ENGRAM_SOCKET`).
- **Thẻ `<private>…</private>` bị xoá ở hai tầng** (plugin và store) trước khi lưu bất cứ thứ gì.
- **Không thấy telemetry.** Grep mã Go không có SDK analytics; lời gọi mạng duy nhất ngoài cloud là kiểm bản mới qua `api.github.com/repos/…/releases/latest`.
- **Tự chạy test 16/10/2026:** `go test ./internal/store/...` **ok** (91,8 giây), `./internal/mcp/...` **ok** (35,8 giây).

### 4c.3 Điều cần biết trước khi cài

- **Hook Claude Code lưu nguyên văn prompt cục bộ.** `UserPromptSubmit` gửi prompt tới server cục bộ (`POST /prompts`) sau một bước "capture decision" của mã Go. Dữ liệu ở `~/.engram/engram.db` dạng văn bản thường; ai đọc được thư mục home là đọc được lịch sử prompt.
- **Hook chèn chỉ thị vào mọi lượt.** Mỗi prompt, hook thêm context "CRITICAL FIRST ACTION - Execute this ToolSearch NOW…" liệt kê ~34 tên tool. Tốn context mỗi lượt và là chỉ thị mạnh chồng lên chỉ thị của dự án (xem mục 03 §8b về chi phí context của plugin bộ nhớ).
- **Git Sync ghi bộ nhớ vào repo.** `engram sync` xuất observation mới vào thư mục `.engram/` trong repo dưới dạng chunk nén (không gồm prompt). Nội dung không bọc `<private>` sẽ đi vào lịch sử git và tới mọi người clone repo. Repo công khai thì không nên dùng, hoặc phải quét gitleaks thư mục này trước khi commit.
- **Cài từ marketplace Claude Code chưa đủ.** Marketplace chỉ cài tài nguyên plugin, không đăng ký MCP server; phải chạy `engram setup claude-code`.
- **Engram Cloud là phần tự host, tuỳ chọn.** Chạy bằng `docker-compose.cloud.yml` + Postgres hoặc image GHCR; phải `engram cloud enroll` từng project. Chế độ có xác thực bắt buộc đặt `ENGRAM_JWT_SECRET` khác mặc định, và token chỉ in ra một lần.
- **Phát triển rất nhanh.** 1.126 commit trong 8 tháng, release candidate xen kẽ bản ổn định; SECURITY.md chỉ hỗ trợ bản ổn định mới nhất. Nên ghim phiên bản.

### 4c.4 So sánh và dùng thế nào

| Công cụ | ★ (16/10/2026, shields) | License | Khác engram |
|---|---|---|---|
| **Gentleman-Programming/engram** | ~7,3k | MIT | Một binary Go, SQLite FTS5, agent tự ghi; 26 tool MCP, TUI |
| `thedotmack/claude-mem` (mục 03 §8b) | ~101k | Apache-2.0 | Hook ghi phiên rồi **AI nén** thành observation; SQLite + Chroma |
| `rohitg00/agentmemory` (§4b) | ~30k | Apache-2.0 (engine iii là ELv2) | Bộ nhớ qua hook, có benchmark truy xuất; engine không phải OSI |
| `mem0ai/mem0` (§4) | ~67k | Apache-2.0 | Lớp bộ nhớ tổng quát cho ứng dụng LLM, dùng vector và LLM trích xuất |
| `basicmachines-co/basic-memory` | ~4,2k | **AGPL-3.0** | Bộ nhớ là file Markdown người đọc được, qua MCP |

- **Hợp khi:** muốn bộ nhớ giữa các phiên cho nhiều agent khác nhau, không muốn kéo theo Node/Python hay vector DB, và muốn agent ghi có chủ đích thay vì tự động nén mọi thứ.
- **Cấu hình an toàn tối thiểu:** ghim bản ổn định (vd v3.4.0); không dùng Git Sync trên repo công khai, hoặc thêm gitleaks cho `.engram/`; dạy agent bọc dữ liệu nhạy cảm trong `<private>`; nếu tự host cloud thì bật chế độ có xác thực và đặt secret riêng.
- **Không cài chồng** với claude-mem hay agentmemory: cả ba cùng hook vào SessionStart/UserPromptSubmit và cùng chèn context, nên chọn một (khớp nguyên tắc "không chồng pack chỉnh hành vi" ở mục 20 §3g).

**Nguồn §4c:** https://github.com/Gentleman-Programming/engram (clone đầy đủ 16/10/2026, 1.126 commit, HEAD 9c4382f; README.md, DOCS.md, SECURITY.md, TRADEMARKS.md, LICENSE, go.mod, plugin/claude-code/{hooks/hooks.json,scripts/user-prompt-submit.sh}, internal/server/server.go, internal/store/store.go, internal/mcp/, .github/workflows/; tự chạy `go test` internal/store và internal/mcp: ok) · shields 16/10/2026 (engram 7,3k★/752 fork; claude-mem 101k; agentmemory 30k; mem0 67k; basic-memory 4,2k) · https://pkg.go.dev/github.com/Gentleman-Programming/engram/cmd/engram · https://lobehub.com/mcp/gentleman-programming-engram · https://engram.gentlemanprogramming.com/

## 6. LLM gateway / router & "CLI thuê bao làm backend"

| Dự án | Repo | License | ★ | Vai trò | Ghi chú |
|---|---|---|---|---|---|
| **LiteLLM** | BerriAI/litellm | MIT | ~60,9k (theo docs X-Agents, chưa xác minh) | Proxy OpenAI-compatible 100+ provider, budget, key ảo | Chuẩn de-facto |
| **Portkey Gateway** | Portkey-AI/gateway | MIT | – | Gateway nhanh, fallback/retry/load-balance | |
| **OpenRouter** | (đóng) | – | – | Router cloud, 1 key nhiều model, free tier | |
| **one-api / new-api** | songquanpeng/one-api | MIT | – | Quản lý key, quota, nhiều kênh (TQ) | |
| **Helicone** | Helicone/helicone | Apache-2.0 | – | Proxy + observability | |
| **ai-gateway** (chủ kho) | seeker19110/ai-gateway | MIT | – | Node 3 dep: pool đa tài khoản, cooldown theo lỗi, `/mcp` Streamable HTTP | Mục 23 §5 |
| **Plugin-4-Hermes / Hermes-Agents bridge** (chủ kho) | seeker19110/Plugin-4-Hermes | MIT | – | OAuth Antigravity → Gemini/Claude qua Code Assist; bridge :8100 xoay tài khoản | **Vùng xám ToS** |

**Mẫu đáng nhớ:** (1) **taxonomy lỗi → cooldown**: chỉ 401/403/429/quota mới failover tài khoản; `unsupported model` ≠ cooldown; stream và non-stream cùng logic (Hermes `provider-proxy-engineering`); (2) **CLI thuê bao làm LLM endpoint**: `claude -p --tools "" --no-session-persistence` và `codex exec --sandbox read-only --output-schema` trả text/tool-request, host là executor duy nhất — dùng gói thuê bao thay API key, nhưng phụ thuộc điều khoản của nhà cung cấp; (3) **pool `fill_first`** dùng hết 1 tài khoản rồi mới xoay để giữ cache; (4) **stack 0đ**: Groq free tier + Ollama + OpenCode Zen (`config/hermes-free-tier.example.yaml`); cho model local chỉ lộ ≤8 tool và dùng structured outputs (`format` = JSON Schema) (Dhcb-Tools `docs/ai-offline.md`).

## 7. Nguồn

- https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1 · https://blog.starmorph.com/blog/local-llm-inference-tools-guide · https://openalternative.co/blog/best-local-llm-tools · https://www.storagereview.com/best/local-llm-tools · https://deepresearch.ninja/2026/06/Open-Source-LLM-Inference-Projects-A-Comprehensive-Comparative-Analysis/ · https://www.digitalapplied.com/blog/run-local-llms-ollama-vs-lm-studio-vs-vllm-2026-guide
- https://atlan.com/know/top-vector-databases-enterprise-ai/ · https://www.firecrawl.dev/blog/best-vector-databases · https://aimultiple.com/open-source-vector-databases · https://vdf.ai/blog/best-vector-database-for-rag/ · https://www.marktechpost.com/2026/05/10/best-vector-databases-in-2026-pricing-scale-limits-and-architecture-tradeoffs-across-nine-leading-systems/ · https://lakefs.io/blog/best-vector-databases/
- https://github.com/BerriAI/litellm · https://github.com/Portkey-AI/gateway · https://github.com/songquanpeng/one-api · https://github.com/Helicone/helicone · mục 23 §5 (đọc 2026-10-12)
- https://atlan.com/know/best-ai-agent-memory-frameworks-2026/ · https://dev.to/plur9/mem0-vs-letta-vs-zep-which-should-you-use-for-agent-memory-1n8m · https://www.developersdigest.tech/blog/best-ai-agent-memory-providers-2026 · https://thegenios.com/blog/open-source-memory-layers-2026/ · https://niteagent.com/blog/ai-agent-memory-comparison-2026/ · https://medium.com/@wasowski.jarek/i-compared-5-ai-agent-memory-systems-across-6-dimensions-none-wins-6a658335ed0a
- §3b ảnh của Brij Kishore Pandey (13/10/2026): https://code.claude.com/docs/en/setup (mục Authenticate: không có gói free) · https://vercel.com/docs/plans/hobby (phi thương mại, trần dùng) · https://supabase.com/docs/guides/platform/billing-on-supabase (2 project, 500 MB) · https://microsoft.github.io/graphrag/ (index vs query) · https://blog.dailydoseofds.com/p/rag-vs-graph-rag-vs-agentic-rag · https://blog.premai.io/advanced-rag-methods-simple-hybrid-agentic-graph-explained · https://www.besthub.dev/articles/high-concurrency-rag-when-to-use-classic-graph-or-agentic-architecture-2ab88f96c9dd
