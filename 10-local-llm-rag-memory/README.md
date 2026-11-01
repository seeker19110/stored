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
| **Hindsight** | vectorize-io/hindsight | MIT | ~50k (16/10/2026, shields) | Retain → recall (vector + BM25 + graph + reranker) → reflect; bank theo thời gian, mental model | 1.0 ngày 15/10/2026; Memlake là bản trả phí. Xem §4d |
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

## 4d. vectorize-io/hindsight 1.0: tự chạy bản MIT, tối ưu Postgres, và thay thế cho Memlake trả phí (yêu cầu người dùng, 2026-10-16)

> Người dùng gửi lời giới thiệu: "Hindsight vừa lên 1.0, gần 50K sao, có Memlake nhanh gần 50 lần Postgres… nhưng phần mạnh nhất lại nằm sau cánh cửa trả phí", và nhờ "lấy hết". Mục này chỉ đi đường hợp pháp: dùng trọn phần MIT, tối ưu backend miễn phí, và chỉ ra phương án mã mở khác cho phần trả phí. Không bẻ khoá hay dùng chui bản Enterprise. Đã cài `hindsight-api` 1.0.0 từ PyPI và tự chạy; đọc tài liệu chính thức trên hindsight.vectorize.io và config của gói đã cài.

### 4d.1 Phần miễn phí và phần trả phí

| | Mã mở (MIT, tự chạy) | Hindsight Cloud | Enterprise |
|---|---|---|---|
| Lõi nhớ (retain, recall, reflect, mental model, entity graph) | ✅ "same memory engine" | ✅ | ✅ |
| Lưu trữ | PostgreSQL (pgvector) hoặc Oracle | Do Vectorize quản lý (phần lớn chạy Memlake) | PostgreSQL hoặc **Memlake** trên object storage |
| Model | Tự mang LLM + embedding | Có sẵn | Có sẵn hoặc Bedrock/Vertex/Azure |
| Truy cập | API key tự đặt | Console, team, API key | Thêm SSO, MFA bắt buộc, mạng riêng, hỗ trợ theo hợp đồng |
| Giá | Miễn phí | Trả trước theo credit, tặng $5 | Hợp đồng, không công bố |

- **Repo:** `vectorize-io/hindsight` · ~50k★, MIT; 3.681 commit, tag `v1.0.0`; Vectorize công bố 50.000★ sau 350 ngày (15/10/2026). Có paper (arXiv 2512.12818, ACL 2026 demo).
- **Memlake** (13/10/2026): bộ máy lưu trữ bằng Rust đặt dữ liệu trên S3/GCS, server chỉ là cache. Thuộc **Enterprise**, **không có trong repo**, không công bố giấy phép hay giá.
- **Câu "nhanh gần 50 lần Postgres" không có trong bài của Vectorize.** Bài đưa thông lượng recall 207 so với 19, 106 so với 0,45, 113 so với 4 và 2 recall/s (khoảng 11× tới 235× tuỳ tải), p99 một lần recall 106–113 ms so với 513 ms – 5,3 s. Postgres trong phép thử là **primary 4 vCPU dùng chung với các tenant dev khác**; cấu hình máy của Memlake không ghi. Số liệu do chính Vectorize đo.
- **Chính Vectorize ghi Postgres "great" cho bank dưới khoảng 50k memory.** Giới hạn họ nêu: recall chậm dần khi bank lớn (7 qps ở 33k, 1,9 qps ở 164k memory trên 4 vCPU); full-text search có sẵn của Postgres chấm điểm mọi dòng khớp; khoảng 190 KB WAL mỗi memory, ghi tối đa 55–80 memory/s.

### 4d.2 Tự chạy bản MIT (16/10/2026)

- `pip install hindsight-api` (1.0.0, MIT): venv khoảng **6,8 GB** vì kéo PyTorch và model cục bộ (embedding `BAAI/bge-small-en-v1.5` 384 chiều, reranker cross-encoder `ms-marco-MiniLM-L-6-v2`). Bản Docker `ghcr.io/vectorize-io/hindsight` và Helm chart cũng có; bản "slim" nhẹ hơn nếu dùng embedding qua API.
- **Postgres nhúng (pg0) không chạy dưới quyền root** (`initdb: cannot be run as root`). Trong container chạy root, dùng Postgres ngoài: PostgreSQL 17 + `postgresql-17-pgvector` 0.8.7, đặt `HINDSIGHT_API_DATABASE_URL`.
- **Chạy không cần API key nào:** `HINDSIGHT_API_LLM_PROVIDER=none` (retain lưu theo chunk, không trích fact; reflect trả 400, đúng như tài liệu) + embedding và reranker cục bộ. Kết quả: retain 4 mục, 3 câu recall tiếng Việt và tiếng Anh đều trả **đúng mục ở vị trí đầu**, mỗi câu **0,16–0,19 giây** trên CPU. Schema tạo 25 bảng, gồm `audit_log`, `webhooks`, `mental_models`, `entities`, `memory_links`.
- **Muốn đủ trích fact và reflect mà không tốn phí:** `HINDSIGHT_API_LLM_PROVIDER=ollama` (hoặc `lmstudio`, `llamacpp` qua `HINDSIGHT_API_LLM_BASE_URL`); trên máy yếu đặt `HINDSIGHT_API_LLM_MAX_CONCURRENT=2`, `HINDSIGHT_API_LLM_TIMEOUT=300`, `HINDSIGHT_API_CONSOLIDATION_LLM_BATCH_SIZE=2`. Danh sách provider còn có `claude-code`, `openai-codex`, `github-copilot` để dùng thuê bao sẵn có (chưa thử).

### 4d.3 Tối ưu backend Postgres miễn phí

Tên biến lấy từ `hindsight_api/config.py` của gói 1.0.0:

| Việc | Biến | Ghi chú |
|---|---|---|
| Chọn chỉ mục vector | `HINDSIGHT_API_VECTOR_EXTENSION` = `pgvector` (mặc định) · `vchord` · `pgvectorscale` · `scann` | pgvectorscale (DiskANN) hoặc VectorChord cho bank lớn và embedding trên 2.000 chiều (giới hạn HNSW của pgvector) |
| Chọn bộ tìm từ khoá (BM25) | `HINDSIGHT_API_TEXT_SEARCH_EXTENSION` = `native` (mặc định) · `vchord` · `pg_textsearch` · `pgroonga` · `pg_search` | `native` là full-text có sẵn, chính là chỗ bài Memlake chê. **Ngôn ngữ mặc định `english`** (`HINDSIGHT_API_TEXT_SEARCH_EXTENSION_NATIVE_LANGUAGE`): nội dung tiếng Việt sẽ bị stem theo tiếng Anh. Nên dùng `simple` hoặc `pgroonga` (hỗ trợ đa ngôn ngữ; cần cài từ kho apt của Groonga, không có trong kho PGDG đã thử) |
| Tách đọc / ghi | `HINDSIGHT_API_READ_DATABASE_URL` + `HINDSIGHT_API_READ_DB_POOL_MIN_SIZE`/`MAX_SIZE` | Recall đọc từ read replica, giảm tải primary |
| Pool kết nối | `HINDSIGHT_API_DB_POOL_MIN_SIZE` (5) / `MAX_SIZE` (100) | |
| Giảm CPU reranker | `HINDSIGHT_API_RERANKER_MAX_CANDIDATES` 300 → 100; `HINDSIGHT_API_RERANKER_PROVIDER=flashrank` trên máy chỉ có CPU; `HINDSIGHT_API_RERANKER_LOCAL_BUCKET_BATCHING` | Tài liệu performance ghi bucket batching nhanh hơn 36–54% |
| Giảm chi phí LLM khi ghi | `HINDSIGHT_API_RETAIN_BATCH_ENABLED=true` | Tài liệu ghi giảm khoảng 50% chi phí trích xuất (OpenAI, Groq) |
| Chia nhỏ bank | Một bank cho mỗi người dùng/agent/dự án, giữ dưới khoảng 50k memory | Theo chính ngưỡng Vectorize nêu |
| Mở rộng ngang | Nhiều instance API sau load balancer, chung một Postgres; Postgres có quản lý (RDS, Cloud SQL, Supabase, Neon đã được thử) | |

### 4d.4 Thay cho Memlake: không thay được backend, phải đổi hệ

Tài liệu storage ghi rõ **"Hindsight does not abstract storage behind a generic interface"**: chỉ có Postgres và Oracle, không có lớp backend để cắm LanceDB, Qdrant hay S3. Muốn bộ nhớ agent nằm trên object storage mà vẫn mã mở thì phải dùng hệ khác (shields 16/10/2026):

| Hệ | ★ · license | Lưu trữ | Khác Hindsight |
|---|---|---|---|
| `topoteretes/cognee` | ~32k · Apache-2.0 | Mặc định file: SQLite + **LanceDB** + Kuzu; LanceDB đọc ghi thẳng `s3://` | Pipeline memory + knowledge graph; gần nhất với "memory trên object storage" |
| `mem0ai/mem0` | ~67k · Apache-2.0 | Nhiều vector store để chọn | Lớp memory trích fact theo user/session (§4) |
| `getzep/graphiti` | ~32k · Apache-2.0 | Neo4j/FalkorDB | Đồ thị tri thức theo thời gian |
| `lancedb/lancedb` | ~12k · Apache-2.0 | Tách storage và compute, `lancedb.connect("s3://…")`, S3/GCS/Azure/MinIO | Chỉ là kho vector; Mastra, CrewAI dùng làm memory |
| `milvus-io/milvus` | ~46k · Apache-2.0 | Lưu bền trên object storage (MinIO/S3) theo kiến trúc phân tán | Kho vector cỡ lớn, vận hành nặng |

**Khuyến nghị:** với agent cá nhân hoặc đội nhỏ, bản MIT trên Postgres là đủ; tối ưu theo 4d.3 trước khi nghĩ tới Memlake. Chỉ khi bank thật sự vượt hàng trăm nghìn memory, hoặc cần hàng nghìn bank, mới so cognee + LanceDB trên S3 với giá Enterprise. Muốn đúng Memlake thì liên hệ Vectorize; không có đường hợp pháp nào để tự host Memlake miễn phí.

**Nguồn §4d:** https://github.com/vectorize-io/hindsight (MIT, tag v1.0.0) · https://pypi.org/project/hindsight-api/ (1.0.0, cài và chạy 16/10/2026) · https://hindsight.vectorize.io/blog/2026/10/15/hindsight-50k-stars · https://hindsight.vectorize.io/blog/2026/10/13/memlake · https://hindsight.vectorize.io/cloud-enterprise/overview · https://hindsight.vectorize.io/developer/storage · https://hindsight.vectorize.io/developer/installation · https://hindsight.vectorize.io/developer/configuration · https://hindsight.vectorize.io/developer/performance · https://arxiv.org/pdf/2512.12818 · https://aclanthology.org/2026.acl-demo.27.pdf · https://trendshift.io/repositories/15603 · https://docs.lancedb.com/storage · https://lancedb.com/blog/case-study-cognee · https://www.cognee.ai/blog/fundamentals/how-cognee-builds-ai-memory · https://mastra.ai/integrations/databases/lancedb

## 4e. thedotmack/claude-mem: trí nhớ giữa các phiên bằng hook + AI nén (yêu cầu người dùng, clone 2026-10-30)

> Kho trước đây chỉ có claude-mem dưới dạng dòng bảng (mục 03 §8b, §4c ở trên, mục 20 §3g). Đây là hồ sơ đầy đủ. Đã clone đủ lịch sử (blob:none), đọc README, SECURITY.md, CHANGELOG, `plugin/hooks/hooks.json`, `src/services/telemetry/`, `src/npx-cli/commands/telemetry.ts`, `evals/read-gate/`, workflow CI. **Không chạy installer, không đăng nhập.**

### 4e.1 Hồ sơ nhanh

| Mục | Thông tin (đọc 30/10/2026) |
|---|---|
| Repo | github.com/thedotmack/claude-mem · **106k★, 9,3k fork** (shields) · **Apache-2.0** (file LICENSE + NOTICE) · v15.6.0; commit cuối 29/10/2026 · 53 issue, 73 PR mở |
| Lịch sử | **3.767 commit** từ 6/9/2025, 323 tác giả; Alex Newman (`thedotmack`) 2.565 commit; 4.175 dòng trailer `Co-Authored-By: Claude` (nhiều hơn số commit — gần như toàn bộ do Claude viết); `posthog[bot]` 65 commit |
| Cơ chế | **11 hook trên 9 sự kiện** (Setup, SessionStart ×3, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, Stop, SubagentStop, SessionEnd) ghi lại thao tác → **worker Bun** ở `127.0.0.1:37777` gọi model nén thành *observation* + tóm tắt phiên → lưu `~/.claude-mem/` (SQLite FTS5 + Chroma) → SessionStart chèn lại ngữ cảnh. Kho trước ghi "5 hook" — đã lỗi thời |
| Truy xuất | 4 tool MCP theo mẫu 3 lớp: `search` (chỉ mục ~50–100 token/kết quả) → `timeline` → `get_observations` (đầy đủ theo ID); skill `mem-search`; web viewer tại cổng 37777 |
| File Read Gate | PreToolUse trên `Read`: **chặn đọc nguyên file code ≥ 32 KB đã có observation**, buộc agent dùng `smart_outline`/`smart_unfold` (tree-sitter) hoặc đọc theo `offset/limit`. Bật mặc định từ v13.32 (`CLAUDE_MEM_FILE_READ_GATE_ENABLED`) |
| Đa host | Claude Code (plugin marketplace hoặc `npx claude-mem install`), OpenCode, T3 Code, Antigravity, Cursor, Pi, DeepSeek Harness, OMP, Grok Bot, Hermes, OpenClaw |
| Kiểm thử | 1.098 file test; eval thật `evals/read-gate/` chạy qua `claude plugin eval` (3 ca × 3 lần, giới hạn US$10), chứng minh gate bật vẫn trả lời/sửa đúng và rẻ hơn khi tắt |

### 4e.2 Dữ liệu rời máy (SECURITY.md tự khai, đối chiếu mã 30/10/2026)

"Lưu cục bộ" chỉ đúng với phần lưu trữ. Nội dung phiên **rời máy** qua các kênh sau:

- **Telemetry bật mặc định:** usage analytics + thông báo lỗi/stack trace đã lọc gửi **PostHog**, định danh bằng UUID cài đặt. Tắt: `npx claude-mem telemetry disable`, `CLAUDE_MEM_TELEMETRY=0` hoặc `DO_NOT_TRACK=1` (thắng mọi cấu hình).
- **Model nén observation:** mặc định qua **Claude Agent SDK** → gửi prompt và transcript tới API Anthropic, dùng **token OAuth Claude Code đọc từ keychain** (không gửi token đi nơi khác, nhưng **tiêu quota gói** của người dùng cho mỗi lần nén). Có thể đổi sang Gemini, OpenRouter, hoặc endpoint OpenAI-compatible (gồm Ollama/LM Studio/vLLM cục bộ — cách duy nhất để không gửi transcript ra ngoài).
- **Cài đặt mời đăng nhập cmem.ai:** installer mở trình duyệt đăng nhập (magic link) để bật "claude-mem observer" hosted, **dùng thử 30 ngày** "memory runs off-plan"; hết hạn tự quay về gói Anthropic trừ khi trả phí. Bỏ qua bằng `--provider …`, `CLAUDE_MEM_ONLINE_OPTIN=false`, hoặc chạy non-interactive. Bản Grok Bot mặc định dùng **CMEM Pro** hosted.
- **Cloud Sync tùy chọn:** đẩy observation, tóm tắt phiên, **prompt người dùng** và to-do/work state lên tài khoản cmem.ai.
- **Chroma embedding** có thể gọi API từ xa tùy cấu hình `chroma-mcp`; version check gọi GitHub/npm.
- Có thẻ `<private>…</private>` để loại nội dung khỏi kho cục bộ.

### 4e.3 Điều cần biết trước khi cài

- **Chi phí ẩn:** mỗi phiên kéo thêm lượt gọi model nền để nén — tốn quota gói hoặc tiền API; README gọi bản hosted là "up to 100% more usage from your plan", tức chính nó thừa nhận phần nén ăn đáng kể vào gói.
- **Đổi hành vi agent:** Read Gate chặn đọc file lớn; SessionStart chèn context cũ có thể lạc hậu so với code hiện tại. Agent trả lời "theo trí nhớ" cần được kiểm lại bằng file thật.
- **Không cài chồng** với engram (§4c) hay agentmemory: cùng hook SessionStart/UserPromptSubmit và cùng chèn context.
- **Mô hình kinh doanh đang đẩy về hosted** (observer cmem.ai, CMEM Pro): cấu hình `--provider` rõ ràng ngay lúc cài để không vô tình đưa transcript lên dịch vụ thứ ba.
- Tốc độ phát hành rất nhanh (v15.x, nhiều bản mỗi tuần) → ghim phiên bản cho team.

### 4e.4 So sánh và dùng thế nào

| Công cụ | ★ (30/10) · license | Ai quyết định điều cần nhớ | Dữ liệu |
|---|---|---|---|
| `thedotmack/claude-mem` | 106k · Apache-2.0 | **LLM nén tự động** từ mọi thao tác | Cục bộ + telemetry mặc định + model nén (thường là cloud) |
| `Gentleman-Programming/engram` (§4c) | xem §4c · MIT | **Agent tự gọi** `mem_save` | Một binary Go, SQLite cục bộ, không LLM nền |
| `vectorize-io/hindsight` (§4d) | xem §4d · MIT | Hệ memory server có truy xuất nhiều chiến lược | Tự chạy (Postgres) hoặc bản trả phí |
| Có sẵn: `CLAUDE.md` + auto-memory của Claude Code | – | Người dùng/agent ghi tay | File trong repo, không thêm dịch vụ |

- **Dùng khi:** làm việc dài hạn trên cùng dự án, muốn agent nhớ quyết định/bugfix cũ mà không phải tự ghi. Cấu hình tối thiểu an toàn: `DO_NOT_TRACK=1`, provider rõ ràng (model local nếu code nhạy cảm), không bật Cloud Sync, dùng `<private>` cho secret.
- **Không dùng khi:** repo có dữ liệu khách hàng/bí mật mà chưa chạy model nén cục bộ; hoặc phiên cloud tạm thời (claude.ai/code) — kho `~/.claude-mem/` mất theo container.
- **Bài học đáng lấy kể cả khi không cài:** mẫu truy xuất 3 lớp (chỉ mục rẻ → timeline → chi tiết theo ID) và cổng đọc file lớn có eval chứng minh tiết kiệm — áp được cho MCP tự viết (mục 04, mục 23).

**Nguồn §4e:** clone github.com/thedotmack/claude-mem 30/10/2026 (blob:none, 3.767 commit, HEAD 325afb6 29/10/2026, v15.6.0; README.md, SECURITY.md (Data Storage, Permissions), CHANGELOG.md (File Read Gate v13.32), LICENSE, NOTICE, plugin/hooks/hooks.json, plugin/.claude-plugin/, src/services/telemetry/{common,cli-telemetry}.ts, src/npx-cli/commands/telemetry.ts, evals/read-gate/README.md, .github/workflows/*; git shortlog, đếm trailer và file test bằng script) · img.shields.io/github/{stars,forks,license,last-commit,v/release,issues,issues-pr}/thedotmack/claude-mem.json (30/10/2026) · docs.claude-mem.ai (search-tools, architecture, cloud-sync, telemetry)

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

## 6b. Nâng cấp 31/10/2026: rà repo lớn

> Cách làm: đọc lại sao, license, trạng thái của 30 repo GitHub đã có trong mục 10 (GitHub API, 31/10/2026). Tìm repo còn thiếu bằng 14 truy vấn GitHub search (`local llm inference`, `rag`, `vector database`, `agent memory`, `llm gateway`, topic `rag`/`local-llm`, và `created:>2025-10-01` cho repo mới). Lọc bỏ repo đã có ở bất kỳ mục nào trong `data/projects.json`, chọn **7 repo**, clone `--filter=blob:none` rồi đọc LICENSE, manifest, cấu trúc thư mục, CI, và grep host mạng/telemetry. **Không cài dependency, không chạy script của repo.** Số liệu đọc ngày 31/10/2026.

### 6b.1 Trạng thái repo cũ

| Repo | Thay đổi | Hệ quả |
|---|---|---|
| `ggml-org/llama.cpp` | ~100k → **133,0k** | Bảng §1 ghi "~85–130k" đã cũ |
| `sgl-project/sglang` | ~25k → **38,3k** | Vẫn xếp sau vLLM (96,0k) nhưng khoảng cách hẹp lại |
| `ollama/ollama` · `vllm-project/vllm` · `infiniflow/ragflow` | 185,5k · 96,0k · 93,3k | RAGFlow lớn gần bằng vLLM; bảng §3 chưa có số |
| Vector DB §2 | Milvus 46,5k · Qdrant 35,4k · Chroma 29,6k · pgvector 23,5k · Weaviate 16,9k · LanceDB 11,8k | Các số "~15–25k" và "nguồn cũ" trong §2 đều thấp hơn thực tế; catalog bổ sung sao còn thiếu |
| `HKUDS/LightRAG` · `microsoft/graphrag` | 40,5k · 36,5k | LightRAG đã vượt GraphRAG |
| `songquanpeng/one-api` | Push cuối **9/1/2026** | Gần 10 tháng đứng yên. Bản fork tiếp nối là `QuantumNous/new-api` (51,1k, AGPL), xem dưới |
| `Portkey-AI/gateway` | Push cuối **25/5/2026** | Hơn 5 tháng không push; kiểm tra lại trước khi chọn |
| `BerriAI/litellm` · `pgvector` · `weaviate` | GitHub báo `NOASSERTION` | Không phải đổi license: LiteLLM có thư mục `enterprise/` license riêng **(chưa xác minh)**, pgvector dùng PostgreSQL License, Weaviate BSD-3 mà GitHub không nhận diện |
| `thedotmack/claude-mem` · `vectorize-io/hindsight` | 107,8k · 57,0k | Hồ sơ §4d, §4e vẫn đúng |

### 6b.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `MemPalace/mempalace` | Agent memory | 60,2k · MIT | 31/10/2026 | Lưu nguyên văn hội thoại, tìm ngữ nghĩa (Chroma), MCP + hook cho coding agent | 7 tháng tuổi; từng rút lại số benchmark |
| `VectifyAI/PageIndex` | RAG không vector | 39,9k · MIT | 30/10/2026 | Dựng cây mục lục cho tài liệu dài, LLM "đọc" cây để lấy trang | Chế độ local vẫn gọi LLM API; nhiều tính năng ở cloud |
| `volcengine/OpenViking` | Context DB cho agent | 41,2k · **AGPL-3.0** | 31/10/2026 | Hệ file ảo `viking://` gộp tài liệu, memory, skill; tóm tắt L0/L1/L2 | Đổi Apache-2.0 → AGPL ngày 30/3/2026 |
| `mudler/LocalAI` | Inference runtime | 50,1k · MIT | 31/10/2026 | API kiểu OpenAI/Anthropic/ElevenLabs, backend tách thành image kéo khi cần | Mặc định nghe mọi interface, không API key |
| `exo-explore/exo` | Inference phân tán | 48,1k · Apache-2.0 | 28/10/2026 | Ghép nhiều máy Mac thành cụm, tensor parallel qua RDMA Thunderbolt 5 | Chỉ macOS Apple Silicon; tag cuối 23/4/2026 |
| `docling-project/docling` | Parse tài liệu cho RAG | 69,9k · MIT | 31/10/2026 | PDF/DOCX/PPTX/… → Markdown/JSON, có OCR, VLM, MCP | License weights model riêng (chưa xác minh) |
| `QuantumNous/new-api` | LLM gateway | 51,1k · **AGPL-3.0 + điều khoản §7** | 31/10/2026 | Kế thừa one-api: quản lý key, quota, nhiều kênh, API OpenAI/Claude/Gemini | Bắt giữ ghi công trên UI |

### 6b.3 Hồ sơ ngắn

- **MemPalace.** Python (lõi Rust đang tách ra `crates/`), 2.532 commit từ 4/4/2026, 191 tác giả, 205 commit (8%) có trailer Claude; `pyproject` ghi tác giả "milla-jovovich", người viết nhiều nhất là Igor Lins e Silva (1.439 commit). Cấu trúc wing/room/drawer chỉ là metadata filter trên Chroma (có backend Milvus). `docs/HISTORY.md` ghi rõ các lần sửa sai: 14/4/2026 bỏ bảng so sánh trộn **R@5 retrieval** của mình với **QA accuracy** của Mem0/Zep, rút "+34% palace boost" và "100% với Haiku rerank" (được tinh chỉnh bằng cách nhìn 3 câu sai). Số còn giữ: 96,6% R@5 LongMemEval chế độ raw, file kết quả có trong `benchmarks/` ✅. "Không gì rời máy trừ khi bật" ✅ phần lớn: tự tắt telemetry của Chroma, model embedding 300 MB tải lười từ Hugging Face. Có cảnh báo **site giả phát tán malware** (11/4/2026). Cài: `uv tool install mempalace && mempalace init <dir>`.
- **PageIndex.** Ý tưởng: thay vector index bằng cây mục lục, LLM duyệt cây để chọn trang. Mã nguồn có module `flash/` dựng cây bằng heuristic (không cần LLM) cho PDF có text. "Local mode" vẫn cần API key LLM (README ví dụ OpenAI) và tải bảng giá model của LiteLLM từ `raw.githubusercontent.com` lúc chạy; `client.py` trỏ `api.pageindex.ai` cho chế độ cloud. Page Search API và File System (hàng triệu tài liệu) là dịch vụ trả phí. `pyproject` ghim `litellm <1.106` kèm ghi chú "1.107.0 was malware", một ví dụ ghim phiên bản vì sự cố chuỗi cung ứng. CI có CodeQL và dependency-review. Cài: `pip install -U pageindex`.
- **OpenViking (ByteDance/Volcengine).** 3.058 commit từ 29/1/2026, 334 tác giả, 18% commit có trailer Claude; 36 workflow. Bố cục ngữ cảnh 3 tầng (L0 một câu, L1 tổng quan, L2 nguyên bản) giúp agent đọc tóm tắt trước khi mở file. Benchmark trong README (LoCoMo 24% → 82% với OpenClaw…) chạy bằng model Doubao của Volcengine; **tự đo, chưa xác minh**. License: commit "lisence: change the main lisence to AGPL-3.0" ngày 30/3/2026 đổi từ Apache-2.0; CLI Rust và `examples/` vẫn Apache-2.0. Cài khuyến nghị là `curl -fsSL https://openviking.ai/install | bash` (chạy script từ xa); có `pip install openviking`.
- **LocalAI.** Go, 8.832 commit (khoảng 40% từ bot cập nhật và dependabot), 290 tác giả, tag v4.12.1 (23/10/2026). Hơn 40 backend Python (vllm, whisperx, voxcpm, vibevoice, kokoro…) dựng thành image riêng, chỉ kéo khi model cần ✅. ⚠️ `core/cli/run.go`: địa chỉ mặc định `:8080` (mọi interface) và `LOCALAI_API_KEY` để trống thì **không xác thực**: lệnh `docker run -p 8080:8080` trong README mở API ra mạng. Bản DMG macOS không ký. Cài: `docker run -ti --name local-ai -p 127.0.0.1:8080:8080 localai/localai:latest`.
- **exo.** Python + Rust, dùng MLX và MLX distributed. `PLATFORMS.md`: Tier 1 chỉ có Mac (M3 Ultra, M4 Pro, M4/M5); Linux CUDA/CPU còn "planned" ⚠️. Số tăng tốc "1,8× trên 2 máy, 3,2× trên 4 máy" là của tác giả, chưa xác minh. Nhịp chậm lại: 109 commit từ 1/7/2026, tag cuối v1.0.71 ngày 23/4/2026. Không thấy telemetry; app tự kiểm tra bản cập nhật. Cài: `brew install --cask exo`.
- **Docling (LF AI & Data, gốc IBM).** 1.830 commit, 418 tác giả, phát hành rất dày (v2.145.0 ngày 29/10/2026). Đọc PDF (layout, bảng, công thức), Office, HTML, EPUB, email, audio/video (qua ASR); xuất Markdown/JSON/DocTags; có MCP server và `docling-serve`. Code MIT; model layout/OCR/VLM (GraniteDocling…) tải từ Hugging Face với license riêng **(chưa xác minh từng model)**. Chạy được offline sau khi tải model. Cài: `pip install docling`.
- **new-api.** Go + React, 6.656 commit, bản fork của one-api (MIT) chuyển sang AGPL-3.0. `NOTICE` thêm điều khoản theo AGPL §7: bản sửa đổi có giao diện phải giữ dòng "Frontend design and development by New API contributors." và link về repo. README có lệnh Docker bind `127.0.0.1:3000` ✅ (an toàn hơn LocalAI). Có relay cho Claude/Codex/Gemini; dùng để chia sẻ gói thuê bao thì rơi vào **vùng xám ToS** như §6. Cài: `docker run --name new-api -d -p 127.0.0.1:3000:3000 -v "$(pwd)/data:/data" calciumion/new-api:latest`.

Đã cân nhắc nhưng chưa thêm: `opendatalab/MinerU` (82,9k, parse PDF, GitHub báo `NOASSERTION`), `unslothai/unsloth` (78,9k, fine-tune), `datalab-to/marker` (40,7k, license weights cần đọc riêng), `janhq/jan` (45,2k), `supermemoryai/supermemory` (31,5k), `Tencent/WeKnora` (36,1k), `mozilla-ai/llamafile` (26,5k, đã nhắc ở §1), `alibaba/zvec` (16,2k).

### 6b.4 Mẫu chung rút ra

1. **Số benchmark memory/RAG phải đọc kèm tên metric.** MemPalace tự rút bảng trộn R@5 với QA accuracy; OpenViking đo bằng model của chính hãng. Trước khi so sánh, kiểm repo có file kết quả và lệnh tái lập hay không.
2. **"Local" không có nghĩa là không gọi mạng.** PageIndex local vẫn gọi API LLM và GitHub, MemPalace và Docling tải model từ Hugging Face, exo tự kiểm cập nhật. Muốn chạy air-gapped phải tải trước model và chặn egress.
3. **Bind mặc định quyết định độ an toàn của server inference.** LocalAI nghe `:8080` không xác thực; new-api hướng dẫn bind `127.0.0.1`. Trong template, ép bind loopback và bắt buộc API key khi lộ ra mạng.
4. **License dịch chuyển sang copyleft** ở hạ tầng agent: OpenViking (Apache → AGPL), new-api (one-api MIT → AGPL + điều khoản ghi công). Nhúng vào dịch vụ SaaS thì phải công bố mã sửa đổi.
5. **Ghim dependency theo sự cố cụ thể** (PageIndex ghim LiteLLM `<1.106` vì 1.107.0 bị cài malware) là thói quen nên chép.

**Nguồn §6b:** GitHub search API 31/10/2026 (14 truy vấn + `repo:` cho 30 repo cũ và 7 repo mới) · clone `--filter=blob:none`, đọc: mempalace (LICENSE, README.md, pyproject.toml, docs/HISTORY.md, benchmarks/, `mempalace/__init__.py`, hooks/, .github/workflows/), PageIndex (LICENSE, README.md, pyproject.toml, pageindex/client.py, pageindex/utils.py, pageindex/flash/), OpenViking (LICENSE, README.md, pyproject.toml, commit đổi license, .github/workflows/), LocalAI (LICENSE, README.md, core/cli/run.go, backend/), exo (LICENSE, README.md, PLATFORMS.md, src/, rust/), docling (LICENSE, README.md, pyproject.toml, packages/), new-api (LICENSE, NOTICE, README.en.md) · https://github.com/MemPalace/mempalace · https://github.com/VectifyAI/PageIndex · https://github.com/volcengine/OpenViking · https://github.com/mudler/LocalAI · https://github.com/exo-explore/exo · https://github.com/docling-project/docling · https://github.com/QuantumNous/new-api

## 7. Nguồn

- https://dev.to/sreeraj-sreenivasan/the-complete-guide-to-local-llm-inference-tools-in-july-2026-llamacpp-ollama-vllm-sglang-and-4mh1 · https://blog.starmorph.com/blog/local-llm-inference-tools-guide · https://openalternative.co/blog/best-local-llm-tools · https://www.storagereview.com/best/local-llm-tools · https://deepresearch.ninja/2026/06/Open-Source-LLM-Inference-Projects-A-Comprehensive-Comparative-Analysis/ · https://www.digitalapplied.com/blog/run-local-llms-ollama-vs-lm-studio-vs-vllm-2026-guide
- https://atlan.com/know/top-vector-databases-enterprise-ai/ · https://www.firecrawl.dev/blog/best-vector-databases · https://aimultiple.com/open-source-vector-databases · https://vdf.ai/blog/best-vector-database-for-rag/ · https://www.marktechpost.com/2026/05/10/best-vector-databases-in-2026-pricing-scale-limits-and-architecture-tradeoffs-across-nine-leading-systems/ · https://lakefs.io/blog/best-vector-databases/
- https://github.com/BerriAI/litellm · https://github.com/Portkey-AI/gateway · https://github.com/songquanpeng/one-api · https://github.com/Helicone/helicone · mục 23 §5 (đọc 2026-10-12)
- https://atlan.com/know/best-ai-agent-memory-frameworks-2026/ · https://dev.to/plur9/mem0-vs-letta-vs-zep-which-should-you-use-for-agent-memory-1n8m · https://www.developersdigest.tech/blog/best-ai-agent-memory-providers-2026 · https://thegenios.com/blog/open-source-memory-layers-2026/ · https://niteagent.com/blog/ai-agent-memory-comparison-2026/ · https://medium.com/@wasowski.jarek/i-compared-5-ai-agent-memory-systems-across-6-dimensions-none-wins-6a658335ed0a
- §3b ảnh của Brij Kishore Pandey (13/10/2026): https://code.claude.com/docs/en/setup (mục Authenticate: không có gói free) · https://vercel.com/docs/plans/hobby (phi thương mại, trần dùng) · https://supabase.com/docs/guides/platform/billing-on-supabase (2 project, 500 MB) · https://microsoft.github.io/graphrag/ (index vs query) · https://blog.dailydoseofds.com/p/rag-vs-graph-rag-vs-agentic-rag · https://blog.premai.io/advanced-rag-methods-simple-hybrid-agentic-graph-explained · https://www.besthub.dev/articles/high-concurrency-rag-when-to-use-classic-graph-or-agentic-architecture-2ab88f96c9dd
