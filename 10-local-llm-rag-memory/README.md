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
