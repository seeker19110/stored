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

## 2c. Kiểm ảnh "AI Engineer Interview Questions" (ảnh người dùng gửi, 2026-10-12)

> Infographic 20 ô, mỗi ô một câu hỏi + câu trả lời 1–2 dòng, ghi tên **Rathnakumar Udayakumar (@rathanuday)**. Kiểm từng câu trả lời với nguồn gốc (paper, docs nhà cung cấp, OWASP) và chỉ chỗ trong kho có câu trả lời sâu hơn.

### 2c.1 Hồ sơ nguồn

| Mục | Thông tin (12/10/2026) |
|---|---|
| Người đăng | Rathnakumar Udayakumar (LinkedIn `rathanuday`, ~48,9k follower theo trang bài đăng). Nền tảng **quản lý sản phẩm**, không phải kỹ sư ML: theo ZoomInfo từng là Senior PM ở IBM, Product Lead ở Clara Analytics, Product Leader ở Netradyne, nay đồng sáng lập Open Atlas và Nextazy **(nguồn tổng hợp bên thứ ba, chưa xác minh)**; có 2 sách tự xuất bản (*Product Management 101*, *The ABCs of Data Science*). GitHub `rathanuday` không có repo công khai |
| Kiểu nội dung | Infographic giải thích AI/LLM (agent, RAG, failure mode, câu hỏi phỏng vấn) trên LinkedIn; cuối bài thường quảng bá dịch vụ tư vấn visa O-1/EB-1A và cộng đồng Open Atlas |
| Gốc của ảnh | Không tìm thấy bài gốc đã đánh chỉ mục; không thấy bản sớm hơn ghi tên người khác. Tự thiết kế hay đăng lại: **(chưa xác minh)** |

### 2c.2 Từng ô: đúng tới đâu, thiếu gì, đọc thêm ở đâu

Ký hiệu: ✅ đúng và đủ cho mức "câu trả lời 30 giây" · ⚠️ đúng nhưng thiếu ý mà người phỏng vấn sẽ hỏi tiếp · ❌ sai hoặc lỗi thời.

| # | Câu hỏi | Ảnh trả lời | Đánh giá | Ý cần bổ sung khi trả lời thật | Đọc sâu trong kho |
|---|---|---|---|---|---|
| 01 | LLM là gì, hoạt động ra sao | Dự đoán token kế tiếp, transformer, dữ liệu lớn | ⚠️ | Chỉ đúng với giai đoạn pretrain; model chat còn qua **post-training** (SFT, RLHF/RLAIF, DPO). Nên nói thêm tokenizer và cửa sổ ngữ cảnh | mục 08 §2b (`LLMs-from-scratch`, `nanochat`) |
| 02 | Kiến trúc transformer | Self-Attention → Feed-Forward → Add & Norm; "xử lý song song" | ⚠️ | Sơ đồ đặt Add & Norm **một lần ở cuối**, trong khi mỗi sublayer (attention, FFN) đều có residual + norm riêng; paper gốc dùng post-LN, LLM hiện đại dùng **pre-LN/RMSNorm**. Thiếu multi-head, positional encoding (RoPE), causal mask. "Song song" đúng khi train/prefill, còn **sinh token vẫn tuần tự** (KV cache) | mục 08 §2b; mục 10 §1 (inference) |
| 03 | RAG là gì, vì sao dùng | Truy xuất dữ liệu ngoài để grounding, giảm hallucination | ✅ | Giảm chứ không loại bỏ hallucination; truy xuất sai sinh lỗi mới. Nêu lý do thứ hai: dữ liệu mới/riêng tư mà không cần huấn luyện lại | mục 10 §3 |
| 04 | Embedding hoạt động ra sao | Văn bản → vector nhiều chiều mang nghĩa | ✅ | So bằng cosine/dot product; query và tài liệu phải dùng **cùng model**; đổi model là phải embed lại toàn bộ | mục 10 §2, mục 18 (embedding tiếng Việt) |
| 05 | Fine-tuning khác prompting | Prompting ở inference, fine-tuning đổi trọng số | ⚠️ | Thiếu lựa chọn thứ ba là RAG và tiêu chí chọn: prompting → RAG (thiếu kiến thức) → fine-tuning (thiếu hành vi/định dạng, cần rẻ hơn ở quy mô). Nhắc LoRA/PEFT | mục 17 §2, mục 07 (Overmind: trace → LoRA) |
| 06 | Đánh giá hệ LLM/RAG | Accuracy, relevance, faithfulness, correctness, human eval | ⚠️ | Tách **eval truy xuất** (recall@k, MRR) và **eval sinh** (faithfulness, answer relevance); cần golden dataset; LLM-as-judge phải hiệu chỉnh với nhãn người; chạy eval trong CI | mục 07 |
| 07 | Metric phổ biến | BLEU/ROUGE, faithfulness, relevance, context precision/recall, human eval | ⚠️ | BLEU/ROUGE đo trùng n-gram, **tương quan kém với đánh giá của người** cho văn bản mở; chỉ hợp với dịch/tóm tắt có đáp án. Thiếu LLM-as-judge, pass@k (code), tỉ lệ hoàn thành task (agent), chi phí và độ trễ | mục 07 (Ragas, DeepEval, Promptfoo, Inspect AI) |
| 08 | Xử lý hallucination | RAG nguồn tin cậy, trích dẫn, guardrail, kiểm output, người duyệt | ✅ | Trích dẫn cũng có thể bịa → kiểm trích dẫn khớp đoạn nguồn; cho phép model trả "không biết"; structured output + validate schema | mục 12 §2, mục 17 §2b |
| 09 | Agent là gì | Plan → Act → Observe, dùng tool, vòng phản hồi | ✅ | Đây là ReAct. Thiếu **điều kiện dừng** và ngân sách (số bước, token, tiền) — câu hỏi tiếp theo hay gặp | mục 03 §1–2, mục 21 §8 |
| 10 | Thiết kế multi-agent | Vai trò, giao thức, bộ nhớ chung, điều phối | ⚠️ | Thiếu câu "**có nên dùng không**": Anthropic khuyên "tìm giải pháp đơn giản nhất, chỉ thêm phức tạp khi cần"; theo bài về hệ research của họ, agent đơn tốn ~4× và multi-agent ~15× token so với chat. Nêu A2A, cách cô lập (git worktree) và cách gộp kết quả | mục 03 §1, §5; mục 04 §3 |
| 11 | Tool calling | LLM gọi API, hàm, hệ thống ngoài | ⚠️ | Chính xác hơn: model chỉ **sinh lời gọi có cấu trúc** (tên + JSON tham số); **ứng dụng** thực thi và trả kết quả (ngoại lệ: "server tool" như web search do nhà cung cấp chạy). Điểm này quyết định chỗ đặt kiểm quyền. Nêu MCP | mục 04 §2, mục 12 |
| 12 | Xây context cho agent | Bộ nhớ ngắn hạn, dài hạn, kiến thức truy xuất | ⚠️ | Thiếu **context engineering**: output tool chiếm phần lớn cửa sổ, compaction/tóm tắt, context rot, giữ dữ liệu lớn ngoài cửa sổ | mục 03 §4, §8b (context-mode); mục 10 §4 |
| 13 | MLOps | CI/CD, model registry, monitoring, retrain, versioning | ✅ | Với ứng dụng LLM gọi API: **version prompt**, ghim phiên bản model, eval chạy trong CI thay cho retrain | mục 07, mục 13 §4 |
| 14 | Giám sát production | Độ trễ, lỗi, chi phí, drift, chất lượng output, alert | ✅ | Thêm **tracing** từng bước agent (OpenTelemetry GenAI), phản hồi người dùng làm tín hiệu chất lượng | mục 07 (Langfuse, Phoenix, OpenLLMetry) |
| 15 | Xử lý dữ liệu | Nguồn tin cậy, làm sạch, privacy, bộ eval | ✅ | Thêm phân quyền tài liệu khi truy xuất (người dùng chỉ thấy tài liệu họ được phép xem) | mục 12 |
| 16 | Model drift | Phân phối dữ liệu đổi; kiểm thống kê, phân phối embedding | ✅ | Với API: nhà cung cấp **đổi model ngầm** sau alias → ghim phiên bản cụ thể và chạy lại eval khi nâng cấp | mục 07 |
| 17 | Responsible AI | Fairness, bias, minh bạch, tuân thủ, người giám sát | ⚠️ | Không nhắc **bảo mật**: prompt injection là LLM01 trong OWASP Top 10 for LLM 2025; agent có tool làm rủi ro này thành hành động thật | mục 12 §1 |
| 18 | Hệ RAG end-to-end | Ingest → Embed → Store → Retrieve → Generate | ⚠️ | Thiếu các bước tạo khác biệt: chunking có cấu trúc, **hybrid search** (BM25 + vector), **reranking**, viết lại query, lọc theo quyền, cache, eval từng khâu | mục 10 §2–3 (GraphRAG, LightRAG), mục 08 §2b (`RAG_Techniques`) |
| 19 | Thách thức mở rộng | Độ trễ, chi phí, lưu trữ, serving, độ bền | ✅ | Nêu đòn bẩy cụ thể: **prompt caching**, batching, chọn model theo tầng (router), streaming, giới hạn tốc độ | mục 10 §1, §6 (gateway/router) |
| 20 | Bài toán mở | Làm rõ, yêu cầu, giải pháp, trade-off, lặp | ✅ | Khung chung của system design; thêm "đo bằng gì" (eval) trước khi chọn kiến trúc | mục 08 §3 (Alex Xu) |

**Tổng:** 10 ✅, 10 ⚠️, 0 ❌. Không ô nào sai hẳn; điểm yếu là câu trả lời dừng ở định nghĩa, trong khi phỏng vấn thật hỏi tiếp "khi nào không dùng", "đo bằng gì", "hỏng thế nào".

### 2c.3 Chủ đề ảnh bỏ sót (thường gặp năm 2026)

- **Bảo mật LLM/agent:** prompt injection (trực tiếp và gián tiếp qua tài liệu RAG, output tool), quyền tối thiểu cho tool, sandbox → mục 12, mục 11.
- **Structured output** và validate schema → mục 17 §2b.
- **Kinh tế token:** prompt caching, chọn model theo tầng, ước chi phí một tác vụ → mục 10 §6.
- **Inference:** KV cache, quantization, batching liên tục (vLLM, SGLang) → mục 10 §1.
- **Giao thức agent:** MCP, A2A, Agent Skills → mục 04.
- **Coding agent và harness:** vòng lặp agent dài hạn, cổng kiểm bằng máy, git worktree → mục 01, 03, 21.

### 2c.4 Tài liệu ôn phỏng vấn tương tự

★ và lần push cuối đọc qua GitHub search ngày 12/10/2026; không repo nào archive.

| Tài liệu | ★ | License | Push cuối | Có câu trả lời thật? | Ghi chú |
|---|---|---|---|---|---|
| Chip Huyen, *AI Engineering* (O'Reilly, ebook 12/2024, bản in 1/2025) + `chiphuyen/aie-book` | 17,8k | không LICENSE | 7/2026 | Có (sách) | Nền tảng tốt nhất cho cả 20 ô; repo chỉ là tài liệu đi kèm (mục 08 §2b) |
| `KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub` | 1,1k | Apache-2.0 | 2/2026 | **Có**, 115 câu trong `Interview_QA/` | Có quảng cáo sách trả phí |
| `amitshekhariitbhu/ai-engineering-interview-questions` | 3,4k | Apache-2.0 | 12/10/2026 | Chủ yếu danh sách câu hỏi, link ra blog/video | Phủ chủ đề mới nhất: MCP, LLMOps, eval, safety |
| `alexeygrigorev/data-science-interviews` | 10,2k | CC-BY-4.0 | 9/2026 | Có | ML/DS cổ điển, ít LLM |
| `chiphuyen/ml-interviews-book` | 4,8k | không LICENSE | 3/2025 | Phần lớn chỉ câu hỏi | Sách miễn phí 2021, trước thời LLM |
| `Devinterview-io/llms-interview-questions` | 1,1k | không LICENSE | 2/2026 | 15/63 câu trong README | Phần còn lại sau tường phí devinterview.io |
| `llmgenai/LLMInterviewQuestions` | 2,0k | không LICENSE | 2/2025 | **Không**, đáp án trong khoá trả phí | Tránh |

Gợi ý: sách *AI Engineering* cho nền tảng → KalyanKS để luyện câu trả lời viết sẵn → danh sách amitshekhar để rà chủ đề mới → các mục kho ở cột "Đọc sâu" để có ý trade-off/đo/hỏng.

### 2c.5 Dùng ảnh thế nào

Tốt làm **checklist chủ đề** trong một trang; không đủ làm câu trả lời. Khi ôn, với mỗi ô hãy chuẩn bị thêm ba ý: một trade-off (khi nào không dùng), một cách đo, một kiểu hỏng; cột "Đọc sâu trong kho" ở bảng §2c.2 chỉ chỗ có sẵn các ý đó.

## 2d. Repo "khoá học" là phễu quảng cáo: `cporter202/automate-for-growth` (ảnh người dùng gửi, 2026-10-12)

> Ảnh chụp README "🚀 Automate Content for Growth — The Complete Course for Scaling Your Social Media Presence" (11 module, nút Star 829, Buy me a coffee, avatar "Chris Porter"). Repo tìm được qua GitHub search, clone đầy đủ để đọc.

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `cporter202/automate-for-growth` · **~894★**, 228 fork; tạo 5/12/2025, **push cuối 9/12/2025**; 9 commit trong 4 ngày, 1 tác giả; **không có LICENSE**; homepage viralwavestudio.com |
| Nội dung thật | 16 file Markdown (~39k từ), **không có code**; 11 module (video Sora 2, "brand authority", đăng đa nền tảng, bulk content, blog, analytics, API, team, case study) |
| Mục đích | Hướng người đọc tới **ViralWave Studio**: 41 link tới viralwavestudio.com, 7 tới `api.viralwavestudio.com`; thư mục `ai-content-generation-tool/` tự gọi sản phẩm là "#1 AI Content Generation Tool" kèm mã giảm 15%; module API chỉ có ví dụ gọi API của chính sản phẩm đó |
| Liên hệ tác giả – sản phẩm | Repo không công bố quan hệ giữa tác giả (Facebook `chris.porter.7731`) và ViralWave Studio **(chưa xác minh là chủ sản phẩm hay affiliate)**; ảnh trong README lưu trên Firebase project `facesift` |
| Case study | Không tên, không nguồn: "0 → 4.000 follower trong 90 ngày", "engagement 6,8%", "US$25.000 doanh thu"; 3 link trong cả module. **Không kiểm chứng được** |

**Đánh giá:** không phải tài liệu học về tự động hoá nội dung mà là tài liệu bán hàng đặt trên GitHub; số sao không nói gì về chất lượng (repo bỏ dở từ 12/2025, ảnh của video quảng bá vẫn kêu gọi star). Không có LICENSE nên về mặt pháp lý không được phép tái sử dụng nội dung.

**Muốn tự động hoá nội dung mạng xã hội thật thì đọc:** n8n, Activepieces (mục 05, mục 21 §6) để dựng pipeline đăng bài; mục 19 và 22 cho sinh video/motion; mục 12 trước khi giao token tài khoản mạng xã hội cho bất kỳ dịch vụ bên thứ ba nào.

**Dấu hiệu nhận ra "khoá học" kiểu này:** đa số link trỏ về một sản phẩm, không có code chạy được, không LICENSE, case study không tên, commit dồn trong vài ngày rồi dừng, README đặt lời kêu gọi star và donate trước mục lục.

### 2d.1 Repo thứ hai cùng tác giả: `cporter202/make-com-automation-recipes` (ảnh người dùng gửi, 2026-10-13)

> Ảnh chụp README "Make.com Automation Recipes — 600+ pre-built workflows & templates" (badge Templates 600+, Categories 12, License MIT; khung "Affiliate disclosure"). Đã clone đầy đủ để đọc.

| Mục | Thông tin (13/10/2026) |
|---|---|
| Repo | `cporter202/make-com-automation-recipes` · **16★, 0 fork** (shields.io); 4 commit: "Initial commit" 8/12/2025, rồi **3 commit cách nhau 7 giây** ngày 12/10/2026 (dựng danh mục 600 template, banner AI, thêm MIT) |
| Nội dung thật | Chỉ 3 file: `README.md` (779 dòng), `LICENSE` (MIT), `assets/hero.png`. **Không có template nào trong repo**: 600 dòng là link tới **thư viện template công khai của chính Make.com** (600 ID khác nhau, thử ngẫu nhiên đều trả 200), chia đều **đúng 50 mục × 12 nhóm** |
| Dấu hiệu sinh tự động | Tên mỗi mục là slug URL đổi sang Title Case ("…With Openai **S** Whisper…"), không có mô tả, không ghi ai làm template, không ghi template dùng bao nhiêu operation |
| Mục đích | **Mọi** link Make.com (603/603) mang mã đối tác `?pc=viralwave` — cùng ViralWave mà repo `automate-for-growth` (§2d) quảng bá. Khác repo trước: lần này **có ghi rõ affiliate** ngay đầu README |
| License | MIT chỉ áp cho README do tác giả viết; bản thân các template thuộc Make.com và người đóng góp gallery, không phải "MIT" |

**Đánh giá:** không phải bộ sưu tập do tác giả xây mà là trang mục lục có link giới thiệu (affiliate) dẫn vào gallery mà Make đã có sẵn và có tìm kiếm, lọc theo app. Không có giá trị thêm ngoài cách chia nhóm. Có công khai affiliate nên trung thực hơn §2d, nhưng badge "600+ templates" dễ hiểu nhầm là template nằm trong repo.

**Muốn mẫu tự động hoá thật:** dùng thẳng gallery chính thức `make.com/en/templates` (không qua link affiliate); nếu cần tự host và đọc được mã thì xem n8n (mục 05, mục 21 §6) và thư viện workflow công khai của n8n (`n8n.io/workflows`). Trước khi bật một template, kiểm quyền OAuth nó xin và số operation mỗi lần chạy, vì gói miễn phí của Make tính theo operation.

**Quy tắc rút ra (bổ sung §2d):** repo "N trăm template/prompt" mà chỉ có một README → đếm link theo tên miền và tham số (`?pc=`, `?ref=`, `utm_`), xem các commit có dồn trong vài giây không. Hai dấu hiệu này đủ để nhận ra danh mục sinh tự động phục vụ affiliate.

## 2e. Kiểm ảnh "Layers of AI: From classical methods to autonomous AI systems" (ảnh người dùng gửi, 2026-10-13)

> Infographic 6 tầng xếp chồng, mũi tên đi lên, mỗi tầng 5 ô: Classical AI → Machine Learning → Neural Networks → Deep Learning → Generative AI → Agentic AI. Ghi nguồn **AIForLeaders.com**.

### 2e.1 Hồ sơ nguồn

| Mục | Thông tin (13/10/2026) |
|---|---|
| Nguồn | aiforleaders.com: newsletter AI hằng ngày cho lãnh đạo doanh nghiệp, do **Adam Danyal** sáng lập, đồng viết với Julia Danyal (theo FAQ của trang). Trang tự nhận "50K+ leaders" đăng ký và "1.6M+ on LinkedIn"; có link "Get AI Certified" sang chiefaileader.com (không ghi giá). Số liệu là tự công bố **(chưa xác minh)** |
| Kiểu nội dung | Infographic phổ thông cho người không chuyên; bản "Layers of AI"/"7 Layers of AI" được nhiều tài khoản LinkedIn đăng lại, có bản kèm link đăng ký aiforleaders.com. Không tìm thấy bài gốc đã đánh chỉ mục |
| Cách làm ảnh | Hai ô "Audio & Image Models" và "Multimodal Models" dùng **cùng một biểu tượng**, ô giữa tầng Classical AI chỉ ghi "AI" dưới biểu tượng kính lúp → nhiều khả năng ảnh do công cụ sinh ảnh dựng và không được soát lại **(chưa xác minh)** |

### 2e.2 Từng tầng: đúng tới đâu

Ký hiệu: ✅ đúng · ⚠️ đúng nhưng gây hiểu sai hoặc thiếu ý · ❌ sai.

| Tầng | Ảnh ghi | Đánh giá | Chỗ cần sửa / bổ sung | Đọc sâu |
|---|---|---|---|---|
| Classical AI | Symbolic AI, Expert Systems, "AI" (kính lúp), Knowledge Representation, Logic & Reasoning | ⚠️ | Ô "AI" gần như chắc là **Search** (tìm kiếm trạng thái: A\*, minimax) bị ghi sai nhãn. Thiếu **planning cổ điển** (STRIPS 1971) — chính là gốc của ô "Planning" ở tầng trên cùng | AIMA (Russell & Norvig) |
| Machine Learning | Supervised, Unsupervised, Classification, Reinforcement Learning, Regression | ⚠️ | Trộn hai trục: **kiểu học** (supervised, unsupervised, RL) và **bài toán** (classification, regression — đều là bài toán supervised). Thiếu đánh giá mô hình (train/test, overfitting) và các thuật toán không phải mạng nơ-ron (cây quyết định, SVM) | mục 08 §2b (`mlabonne/llm-course`) |
| Neural Networks | Perceptrons, Cost Functions, Backpropagation, Activation Functions, Hidden Layers | ✅ | Hàm mất mát không riêng của mạng nơ-ron (hồi quy logistic cũng có); thiếu gradient descent/optimizer — động cơ thật của backprop | `labmlai/annotated_deep_learning_paper_implementations` (§2b) |
| Deep Learning | Transformers, LSTMs, RNNs, CNNs, Autoencoders | ✅ | LSTM là một loại RNN (hai ô chồng nhau). Có thể thêm attention, huấn luyện quy mô lớn trên GPU | `rasbt/LLMs-from-scratch`, `karpathy/nanochat` (§2b) |
| Generative AI | LLMs, Diffusion Models, Audio & Image Models, Multimodal Models, VAEs | ⚠️ | Hai ô trùng biểu tượng và chồng nghĩa (audio/image ⊂ multimodal). Thiếu **GAN** (họ mô hình sinh ảnh lớn trước diffusion). Thiếu **post-training** (SFT, RLHF/DPO) — chỗ tầng ML (RL) quay lại ở tầng trên | mục 14, 19, 22 (multimodal, video, motion) |
| Agentic AI | Memory, Planning, Agents, Tool Use, Autonomous Execution | ⚠️ | Ô "Agents" nằm trong tầng "Agentic AI" là lặp lại tên. Thiếu thứ phân biệt hệ agent chạy được với demo: **vòng lặp + điều kiện dừng**, guardrail/người duyệt, eval, giao thức (MCP, A2A) | mục 03 (§8c ảnh "How AI Agents Work"), 02, 04, 21 |

**Tổng:** 2 ✅, 4 ⚠️, 0 ❌. Các ô đều là khái niệm có thật; sai ở **cấu trúc** hơn là ở từng ô.

### 2e.3 Sai ở cấu trúc "xếp tầng"

1. **Bốn tầng dưới lồng nhau, hai tầng trên thì không.** Neural Networks ⊂ ML, Deep Learning ⊂ Neural Networks là quan hệ tập con thật (cách vẽ vòng tròn lồng nhau AI ⊃ ML ⊃ DL phổ biến trong giáo trình). Generative AI chỉ **phần lớn** nằm trong deep learning (mô hình sinh cũng có n-gram, HMM, GMM). Agentic AI không phải loại mô hình mà là **kiến trúc hệ thống**: model + harness chạy vòng lặp, dùng tool (mục 03 §1, §8c); nó có thể dùng model không sinh văn bản và cả thành phần cổ điển (planner, rule).
2. **Mũi tên đi lên ngụ ý trình tự lịch sử, nhưng lịch sử không thẳng.** Perceptron (Rosenblatt, 1958) ra đời gần như cùng lúc với thuật ngữ "machine learning" (Samuel, 1959); "agent" và "planning" là khái niệm trung tâm của AI cổ điển (giáo trình AIMA định nghĩa AI là nghiên cứu "intelligent agents" từ 1995). Tầng "Agentic AI" năm 2024–2026 là cách cũ chạy trên model mới, không phải tầng mới xây trên Generative AI.
3. **Tầng dưới không bị thay thế.** Hệ luật/expert system vẫn chạy nhiều phần mềm ra quyết định; trong agent hiện đại, phần "luật cứng" (quyền, ngân sách, cổng kiểm) chính là lớp cổ điển bọc quanh LLM.

### 2e.4 Tài liệu tốt hơn cho cùng mục đích

| Tài liệu | Quy mô / license | Vì sao |
|---|---|---|
| Russell & Norvig, *Artificial Intelligence: A Modern Approach* (AIMA, bản 4, 2020) + `aimacode/aima-python` | repo ~8,8k★ (13/10/2026, shields.io), MIT, commit gần nhất 6/2026 | Phủ đủ 6 tầng với quan hệ đúng (search, logic, planning, học máy, deep learning, agent); code Python cho từng thuật toán |
| `microsoft/generative-ai-for-beginners` → `microsoft/ai-agents-for-beginners` | đã có ở §2b, có bản tiếng Việt | Hai tầng trên cùng, có bài thực hành |
| `rasbt/LLMs-from-scratch`, `karpathy/nanochat` | đã có ở §2b | Hiểu Deep Learning → Generative AI từ bên trong |

**Dùng ảnh thế nào:** được làm "bản đồ thuật ngữ" một trang cho người không chuyên. Khi giải thích lại, nói rõ hai tầng trên không phải tập con của tầng dưới, và đừng đọc mũi tên như dòng thời gian. Với người làm sản phẩm, ảnh "How AI Agents Work" (mục 03 §8c) hữu ích hơn vì nói agent chạy thế nào chứ không chỉ liệt kê tên.

## 2f. Kiểm ảnh "How to become an AI engineer in 2026" (Brij Kishore Pandey, ảnh người dùng gửi, 2026-10-13)

> Trang **09 / 17** trong cùng carousel với hai trang đã kiểm ở mục 10 §3b ("10 / 17" RAG, "12 / 17" $0 stack), ký tên **Brij Kishore Pandey (@brijpandeyji)**. Ảnh chia 13 ô kỹ năng quanh dòng "AI Engineer 2026 — 13 areas. Ship systems, measure them, repeat." và khẩu hiệu cuối "Skip the math degree. Ship the system. Repeat." Logo nhận ra chắc chắn: OpenAI, Anthropic, Gemini, Meta, LlamaIndex, PostgreSQL, NVIDIA, Python, Docker, Git, vLLM, Hugging Face, Mistral, GitHub, X. Các logo còn lại (ô 04, 05, 07, 08, 10, 11) **(chưa xác minh)** là sản phẩm nào.

### 2f.1 Từng ô

| # | Ô | Nội dung trong ảnh | Đánh giá | Ghi chú |
|---|---|---|---|---|
| 01 | LLM fundamentals | Transformer, token; context window; sampling, reasoning model | ✅ | Đủ cho người dùng API. Đọc kèm: rasbt/LLMs-from-scratch (§2b) |
| 02 | Prompt + context engineering | System prompt, few-shot; structured output; ghép context | ✅ | "Context assembly" đúng trọng tâm 2026 hơn "prompt engineering" thuần |
| 03 | RAG systems | Embedding, chunking; hybrid search, rerank; GraphRAG | ✅ | Ô này có đủ hybrid search và rerank — đúng phần mà trang 10/17 bỏ sót |
| 04 | Agentic systems | Tool use, MCP; memory, planning; multi-agent | ✅ | Thiếu ý "khi nào **không** nên dùng agent": workflow cố định thường rẻ và dễ kiểm hơn (mục 03) |
| 05 | AI gateways + routing | Route model, fallback; theo dõi chi phí; rate limit | ✅ | Ví dụ mã mở: LiteLLM (~61k★), mục 10 |
| 06 | Guardrails + safety | Phòng prompt injection; che PII; kiểm output | ⚠️ | Chữ "defense" dễ hiểu nhầm là chặn được. OWASP LLM01 ghi rõ chưa có cách phòng chống chắc chắn; cách làm thật là **giới hạn thiệt hại**: quyền tối thiểu cho tool, tách nội dung ngoài, người duyệt hành động rủi ro, test đối kháng (mục 12) |
| 07 | Observability + evals | Tracing, LLM-as-judge; golden set; phát hiện drift | ✅ | LLM-as-judge phải hiệu chỉnh với nhãn người chấm trước khi tin (mục 07) |
| 08 | Production AI engineering | Streaming, caching; async, rate limit; latency budget | ✅ | "Rate limits" lặp lại ô 05 |
| 09 | Software engineering | Python async, FastAPI; Git, Docker, Postgres; test, CI/CD | ⚠️ | Đúng nhưng chỉ Python. Một phần lớn sản phẩm AI 2026 viết bằng TypeScript (Vercel AI SDK, Mastra, Next.js); nên biết ít nhất đọc được |
| 10 | Inference + deployment | vLLM, quantization; serverless GPU; autoscaling | ✅ | Chỉ cần khi tự host model; đa số đội dùng API trước |
| 11 | Multimodal | Vision, tài liệu; giọng nói, ảnh, video; OCR | ✅ | Xem mục 14 |
| 12 | Ecosystem fluency | Model mở; paper, benchmark; Hugging Face | ✅ | Benchmark công khai hay bị nhiễm dữ liệu huấn luyện; tự đo trên golden set của mình (ô 07) đáng tin hơn |
| 13 | Career compounding | Ship công khai; open source; viết và dạy | ✅ | |
| — | "Skip the math degree" | Khẩu hiệu cuối | ⚠️ | Không cần bằng toán, nhưng **xác suất thống kê cơ bản** là bắt buộc để làm eval đúng: cỡ mẫu, khoảng tin cậy, so A/B, đọc phương sai giữa các lần chạy LLM |

**Tổng:** 11 ✅, 3 ⚠️, không ô nào sai. Đây là trang tốt nhất trong ba trang của carousel đã kiểm.

### 2f.2 Ảnh bỏ sót

- **Fine-tuning và dataset engineering.** Không có ô nào nhắc. Sách *AI Engineering* (Chip Huyen, O'Reilly 2025) dành chương 7 cho "khi nào nên và không nên fine-tune" và một chương riêng cho dataset engineering. Kỹ năng quyết định "RAG hay fine-tune hay chỉ sửa prompt" là phần phân biệt AI engineer với người chỉ gọi API.
- **Bảo mật chuỗi cung ứng của agent:** MCP server, skill, plugin cài từ nguồn ngoài; bí mật trong cấu hình agent (mục 12 §3e). Ô 06 chỉ nói về input/output của model.
- **Thiết kế sản phẩm và UX cho AI:** hiển thị độ không chắc chắn, cho người dùng sửa và phản hồi, thu feedback làm dữ liệu eval (chương cuối của sách Chip Huyen).
- **Dùng coding agent hằng ngày** (Claude Code, Codex, Cursor) — kỹ năng thực tế nhất của AI engineer 2026 nhưng ảnh không nhắc (mục 01).
- **Pháp lý và quyền riêng tư** khi xử lý dữ liệu người dùng: GDPR, EU AI Act; ở Việt Nam là Nghị định 13/2023 về dữ liệu cá nhân.

### 2f.3 Tài liệu tương tự để đối chiếu (★ qua shields.io, 13/10/2026)

| Nguồn | ★ / dạng | Khác ảnh |
|---|---|---|
| chiphuyen/aie-book (sách *AI Engineering*) | ~18k, repo tài nguyên đi kèm sách | Có fine-tuning, dataset engineering, user feedback; nặng về eval |
| roadmap.sh/ai-engineer (kamranahmedse/developer-roadmap, ~369k) | Roadmap tương tác | Định nghĩa AI engineer là người **dùng** model có sẵn, khác ML engineer/researcher; có mục câu hỏi "có cần bằng cấp không" |
| patchy631/ai-engineering-hub | ~38k, MIT | Tập ví dụ code RAG/agent chạy được, bổ sung phần thực hành mà ảnh không có |
| microsoft/generative-ai-for-beginners (§2b) | ~121k | Khoá có bài tập, có bản tiếng Việt |

### 2f.4 Dùng ảnh thế nào

Dùng được làm **danh sách tự kiểm** 13 mảng. Trước khi dùng làm lộ trình học: thêm ô fine-tuning/dataset, sửa ô 06 thành "giới hạn thiệt hại prompt injection", và học thống kê cơ bản trước ô 07. Thứ tự học hợp lý: 01 → 02 → 09 → 03 → 07 → 04 → 06 → 05/08 → 10/11; ô 12–13 làm song song suốt.

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
- §2c ảnh "AI Engineer Interview Questions" (12/10/2026): https://www.linkedin.com/in/rathanuday · https://www.linkedin.com/posts/rathanuday_ai-agents-dont-fail-because-theyre-not-activity-7411823219176865792-xB4z · https://www.zoominfo.com/p/Rathnakumar-Udayakumar/-1632233212 (bên thứ ba) · https://www.goodreads.com/author/show/29625821.Rathnakumar_Udayakumar · kiểm nội dung: https://arxiv.org/abs/1706.03762 (§3.1 post-LN) · https://arxiv.org/abs/2002.04745 (Pre-LN) · https://arxiv.org/abs/2302.13971 (LLaMA, RMSNorm) · https://arxiv.org/abs/2303.16634 (G-Eval: BLEU/ROUGE tương quan thấp với người) · https://www.anthropic.com/engineering/building-effective-agents · https://www.anthropic.com/engineering/multi-agent-research-system (4×/15× token) · https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview · https://genai.owasp.org/llmrisk/llm01-prompt-injection/ · tài liệu ôn: https://github.com/chiphuyen/aie-book, https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub, https://github.com/amitshekhariitbhu/ai-engineering-interview-questions, https://github.com/alexeygrigorev/data-science-interviews, https://github.com/chiphuyen/ml-interviews-book, https://github.com/Devinterview-io/llms-interview-questions, https://github.com/llmgenai/LLMInterviewQuestions
- §2d (12/10/2026): https://github.com/cporter202/automate-for-growth (clone đầy đủ, 9 commit, HEAD 2cc3193) · https://viralwavestudio.com · bản sao 0★: arnelnrose/automate_for_growth, klikydigital/automate-for-growth
- §2e ảnh "Layers of AI" (13/10/2026): https://aiforleaders.com (FAQ: Adam Danyal, Julia Danyal) · bản đăng lại trên LinkedIn: https://de.linkedin.com/in/meheli-sinha, https://sa.linkedin.com/in/alhadlaq · kiểm nội dung: https://cvw.cac.cornell.edu/AI-overview/machine-learning/functionality-and-implementation (sơ đồ lồng nhau là quy ước dạy học) · https://lib.conestogac.on.ca/genai/learn-more · https://aima.cs.berkeley.edu · https://github.com/aimacode/aima-python · https://langchain.com/blog/the-anatomy-of-an-agent-harness
- §2d.1 (13/10/2026): https://github.com/cporter202/make-com-automation-recipes (clone đầy đủ, 4 commit, HEAD 6fa1e09; 16★ shields) · https://www.make.com/en/templates (gallery chính thức; thử https://www.make.com/templates/11218, /10893 → 200) · https://n8n.io/workflows
- §2f ảnh Brij "How to become an AI engineer in 2026" (13/10/2026): https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ("unclear if there are fool-proof methods of prevention") · https://roadmap.sh/ai-engineer · https://github.com/chiphuyen/aie-book (README: chương fine-tuning, dataset engineering) · https://github.com/patchy631/ai-engineering-hub · shields.io: aie-book ~18k, ai-engineering-hub ~38k MIT, developer-roadmap ~369k, litellm ~61k
