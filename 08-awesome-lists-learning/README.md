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

### 2d.2 Repo thứ ba cùng tác giả: `cporter202/ai-growth-stack` (ảnh người dùng gửi, 2026-10-16)

> Ảnh chụp README: tiêu đề "API Growth Stack", bốn huy hiệu (APIS 6 · CATEGORIES 6 · STATUS ACTIVE · UPDATED REGULARLY), banner "AI Growth Stack · github.com/cporter202/ai-growth-stack", câu "A curated collection of powerful AI-powered APIs for website optimization, SEO, conversions, and social media growth… not fluff", nút "Buy me a coffee" và avatar "Chris Porter". Đã clone đầy đủ để đọc.

| Mục | Thông tin (16/10/2026) |
|---|---|
| Repo | `cporter202/ai-growth-stack` · **229★, 70 fork** (shields.io); **7 commit trong 15 phút ngày 21/12/2025**, không có commit nào sau đó; commit cuối (`5ccfb8f`) còn dính nguyên câu nhắc mặc định của git trong tiêu đề ("# Please enter the commit message…") |
| Nội dung thật | **Chỉ một file `README.md`** (302 dòng). Không có code, không có ví dụ, **không có LICENSE**, dù mục "License" của README nói repo là "documentation and examples" |
| 6 "API" | Website Data Extraction · AI SEO Analysis · AI Conversion Optimization · AI Website Copywriter · AI Landing Page Optimizer · AI Social Media Content Generator. **Cả 13 link "View on RapidAPI" đều trỏ về cùng một trang hồ sơ người dùng** (`rapidapi.com/user/contact-_OGid12Eu`), không link nào trỏ tới trang của một API cụ thể. Trang này cần JavaScript nên không đọc được danh sách API thật |
| Ai bán | `apidataframe.com` ("API DataFrame", "Professional APIs for Developers") bán **đúng 6 API này** cộng 3 API trích email/số điện thoại/link mạng xã hội, chỉ qua RapidAPI, không công bố giá hay tên người vận hành. Mục License của README dẫn điều khoản "RapidAPI and API DataFrame". Quan hệ giữa tác giả và API DataFrame **không được công bố** (chưa xác minh là chủ hay affiliate) |
| Liên hệ với §2d | Nút cà phê dẫn tới `buymeacoffee.com/viralwavestudio`; bio GitHub của tác giả quảng bá ViralWaveStudio.com. Banner là ảnh sinh bằng AI (tên file "Generated Image December 21, 2025"), lưu trên cùng Firebase project `facesift` như §2d |

**Kiểm từng ô trong ảnh:**

| Ô | Kiểm | Ghi chú |
|---|---|---|
| Tiêu đề "API Growth Stack" | ⚠️ | Banner và tên repo là "**AI** Growth Stack"; hai tên lệch nhau ngay trên cùng một màn hình |
| APIS 6 · CATEGORIES 6 | ✅ | Đúng 6 mục, mỗi mục một "category", nhưng không mục nào có link riêng |
| STATUS ACTIVE | ❌ | Huy hiệu tĩnh (`img.shields.io/badge/STATUS-ACTIVE`), không đo gì; repo không đổi từ 21/12/2025 |
| UPDATED REGULARLY | ❌ | Huy hiệu tĩnh; commit cuối cách ngày đọc gần 10 tháng. Dòng cuối README ghi "Last updated: December 2024", **trước cả ngày tạo repo** |
| "A curated collection… not fluff" | ⚠️ | Không phải tuyển chọn từ nhiều nhà cung cấp: cả 6 là danh mục sản phẩm của một bên bán (API DataFrame) mà README không nói rõ. Phần "Key Features", "Why It's Powerful" là văn quảng cáo chung chung, không có endpoint, giá, giới hạn hay ví dụ gọi |
| Buy me a coffee | ✅ | Link thật, tới tài khoản `viralwavestudio` |

**Tổng:** 2✅ / 2⚠️ / 2❌.

**Đánh giá:** đây là trang quảng cáo cho các API trả phí trên RapidAPI, không phải bộ sưu tập hay tài liệu kỹ thuật. 229★ cho một README không code, không đổi trong 10 tháng, cho thấy số sao của nhóm repo này không phản ánh nội dung (cùng mô hình §2d: 894★, bỏ dở từ 12/2025). Không có LICENSE nên không được phép tái sử dụng nội dung.

**Muốn làm đúng việc này:** trích dữ liệu web và kiểm SEO thì có công cụ mã mở tự chạy được: Crawl4AI, Firecrawl (mục 11), Lighthouse CI cho hiệu năng/SEO kỹ thuật (mục 13). Nếu vẫn cần API trả phí, tìm thẳng trên marketplace, đọc giới hạn và giá của **từng API cụ thể**, và chạy thử gói miễn phí trước. Viết nội dung marketing bằng LLM thì gọi thẳng model, không cần lớp API trung gian không rõ model bên dưới.

**Quy tắc rút ra (bổ sung §2d, §2d.1):** huy hiệu "STATUS ACTIVE / UPDATED REGULARLY" mà URL là `img.shields.io/badge/...` là huy hiệu tĩnh tự gõ, không phải số đo; so với ngày commit cuối. Khi N mục "khác nhau" cùng trỏ về một link, đó là một sản phẩm được trình bày như một danh sách.

### 2d.3 Repo thứ tư & năm cùng tác giả: `marketing-apis-that-drive-roi` + `social-growth-apis-for-creators` (ảnh "4 GitHub repos worth bookmarking", 2026-10-18)

> Ảnh slide của Chris Porter giới thiệu 4 repo; hai repo đầu là của chính `cporter202`. Đã clone cả hai để đọc. Cùng khuôn mẫu §2d–§2d.2, lần này là **danh mục API gắn link affiliate Apify**.

| Mục | Thông tin (18/10/2026) |
|---|---|
| Repo | `cporter202/marketing-apis-that-drive-roi` (slide: 27★/8 fork) · `cporter202/social-growth-apis-for-creators` (slide: 49★/14 fork); cả hai push 17/10/2026, **không có LICENSE** |
| Nội dung thật | Chỉ README + vài thư mục, mỗi thư mục một README là **bảng link tới actor trên Apify store**. marketing: **290 API** (đúng badge) chia 5 nhóm; social: 6 nhóm. Không có code, không có ví dụ gọi, không có đánh giá chất lượng/giá từng actor |
| Mục đích (affiliate) | **3.089 link** mang mã giới thiệu Apify `?fpr=p2hrc6` trên cả hai repo. README mở đầu bằng lời mời vào **cộng đồng Skool trả phí** ("Vibe Coding with Chris") + link Facebook cá nhân; `META.json` có `source_path` ("marketing-apis-290") cho thấy sinh từ khuôn chung |
| Khác §2d.1 | Lần này **không có khung "Affiliate disclosure"** rõ như `make-com-automation-recipes`; người đọc không được báo mọi link đều gắn mã giới thiệu |

**Đánh giá:** không phải "awesome list" trung lập mà là **danh mục affiliate dẫn về Apify store**, bọc trong phễu cộng đồng trả phí — đúng mô hình §2d/§2d.2. "290 API" chỉ là các actor bất kỳ trên Apify, không tuyển chọn hay kiểm chất lượng; badge sao không phản ánh nội dung (nhóm repo này quảng bá chéo để gom sao).

**Muốn dùng scraper/API thật:** tìm thẳng trên **apify.com/store** (không qua link `?fpr=`), đọc giá + giới hạn + đánh giá của **từng actor cụ thể**, chạy thử free tier; scraper mã mở tự host thì có Crawl4AI, Firecrawl (mục 11). Cho API mạng xã hội, cân nhắc điều khoản nền tảng và mục 12 trước khi giao token.

**Quy tắc (bổ sung §2d–§2d.2):** repo "N trăm API" mà mỗi link đều cùng một tham số giới thiệu (`?fpr=`, `?pc=`, `?ref=`) là danh mục affiliate; đếm `grep -rho 'fpr=[a-z0-9]*'` để thấy quy mô. Cùng một tác giả/cùng avatar + "Buy me a coffee"/Skool lặp lại qua nhiều repo là dấu hiệu phễu, không phải tuyển chọn.

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

## 2g. Kiểm ảnh "The Roadmap to Mastering Agentic AI Systems in 2026" (Vinod Chugani, KDnuggets, ảnh người dùng gửi, 2026-10-16)

> Ảnh chụp đầu bài trên **KDnuggets** (Vinod Chugani, 13/10/2026, mục Artificial Intelligence) kèm infographic "The Roadmap to Building Agentic AI Systems in 2026 — from single agents to production-ready, real-world impact", chia 4 cấp: (1) Single Agent Reasoning Loops, (2) Stateful Memory and Graph-Based Flows, (3) Multi-Agent Collaboration, (4) Operational Hardening; đáy là vòng "continuous feedback and evolution". Đã đọc toàn bài. Infographic không ghi tác giả hay công cụ vẽ, và tiêu đề trong ảnh ("Building") khác tiêu đề bài ("Mastering").

### 2g.1 Từng cấp: ảnh và bài viết

| Cấp | Ảnh vẽ | Bài viết nói thêm | Đánh giá | Chỗ cần sửa / bổ sung |
|---|---|---|---|---|
| 1. Single agent loop | Input → Reasoning (plan) → Tool call → Result → Reflection; "plan → act → observe → refine" | ReAct, Plan-and-Solve, Reflection, Tree of Thoughts; function calling; kiểm output bằng Pydantic/TypeChat; ghép context động | ⚠️ | Vòng trong ảnh **không có lối ra**: thiếu điều kiện dừng do máy kiểm và trần số vòng, đúng chỗ agent thật hay hỏng (mục 03, mục 21 §8). Kiểm output có cấu trúc là ý tốt của bài nhưng không có trong ảnh |
| 2. Stateful memory + graph | Long-term memory, state, knowledge sources quanh "graph orchestrator"; conditional flow, tool node, sub-task | Working / episodic (vector) / semantic (knowledge graph) memory; chain vs graph; **checkpoint** để rollback, resume, debug; LangGraph, AutoGen | ⚠️ | Checkpoint và điểm dừng chờ người (human-in-the-loop) là lý do chính để dùng graph, nhưng ảnh không vẽ. Bài vẫn gợi ý **AutoGen**, trong khi README của AutoGen ghi "now in maintenance mode… New users should start with Microsoft Agent Framework" (mục 02) |
| 3. Multi-agent | Coordinator + research/analysis/execution agent, shared context, handoff, synthesize | Hierarchical, debate-and-critique, peer-to-peer; message schema có cấu trúc; giải xung đột bằng vote/hỏi lại/chuyển người; AutoGen, CrewAI, **MCP** | ⚠️ | Không nói cái giá: Anthropic đo hệ multi-agent dùng **khoảng 15× token** so với chat, và không hợp với việc mà các agent phải dùng chung context hoặc phụ thuộc nhau nhiều (phần lớn việc code). Bài gọi MCP là chuẩn cho giao tiếp nhưng MCP là giao thức agent ↔ tool/context; giao thức agent ↔ agent là **A2A**, bài không nhắc (mục 04 §3) |
| 4. Operational hardening | Observability, monitoring, guardrails, evaluation, logging & auditing, reliable infra, CI/CD | Circuit breaker, trần độ sâu đệ quy, trần token; **sandbox** chạy code (Docker, e2b, WebAssembly); LangSmith, Arize Phoenix; đánh giá theo **trajectory** | ⚠️ | Phần này của bài tốt hơn ảnh: ảnh bỏ mất sandbox và trần chi phí. Cả hai đều **không nhắc prompt injection**, rủi ro số 1 khi agent đọc dữ liệu ngoài rồi gọi tool (OWASP LLM01, mục 12), cũng không có cổng người duyệt cho hành động không đảo ngược |

**Tổng:** 0✅ / 4⚠️ / 0❌. Không có ô sai; mỗi cấp đều thiếu đúng phần làm agent an toàn và rẻ.

### 2g.2 Sai ở cấu trúc "4 cấp nối tiếp"

1. **Thiếu cấp 0: có cần agent không.** Anthropic (*Building Effective Agents*) khuyên bắt đầu bằng workflow cố định (prompt chaining, routing, parallelization) và chỉ dùng agent khi không đoán trước được các bước. Lộ trình bắt đầu thẳng từ agent loop dễ khiến người học dùng agent cho việc mà một workflow làm rẻ và dễ kiểm hơn (mục 03 §1).
2. **Multi-agent không phải "cấp trên" của single agent.** Nó là một lựa chọn có giá (15× token, khó gỡ lỗi), hợp với việc song song hoá được như nghiên cứu, không hợp với phần lớn việc code. Mũi tên 3 → 4 ngụ ý ai cũng phải đi qua multi-agent mới tới production.
3. **"Hardening" không đợi tới cấp 4.** Eval, trace, trần chi phí và sandbox cần có từ agent đầu tiên; để cuối cùng là cách tạo ra demo không lên được production (mục 07, mục 21 §8: "mọi loop phải có 4 số").

### 2g.3 Đọc gì thay / đọc kèm

| Tài liệu | Vì sao |
|---|---|
| Anthropic, *Building Effective Agents* (12/2024) và *How we built our multi-agent research system* (13/6/2025) | Cấp 0 (workflow trước agent) và số liệu thật về chi phí, giới hạn của multi-agent |
| `microsoft/ai-agents-for-beginners`, `huggingface/agents-course` (§2b) | Thực hành đủ 4 cấp, có bài chấm điểm; bản tiếng Việt cho bộ của Microsoft |
| Mục 21 §2 (hai bài harness của Anthropic) và §10c (AI-native SDLC) | Cấp 4 làm thật: harness, cổng máy, giới hạn vòng, người duyệt ở cổng |
| Microsoft Agent Framework thay cho AutoGen; LangGraph cho graph + checkpoint (mục 02) | Danh sách framework của bài có một mục đã ngừng phát triển |

**Dùng ảnh thế nào:** được làm sơ đồ tổng quan một trang về các khái niệm. Khi dạy lại, thêm cấp 0 ("workflow trước, agent sau"), chuyển eval/trace/trần chi phí/sandbox lên từ cấp 1, coi multi-agent là lựa chọn có giá chứ không phải bậc tiếp theo, và thay AutoGen bằng Microsoft Agent Framework.

## 2h. Kiểm ảnh "SEO không thiếu việc, nhưng AI đang thay đổi cuộc chơi" (danhnolan.com, ảnh người dùng gửi, 2026-10-25)

> Infographic tiếng Việt của **Danh Nolan** (danhnolan.com, người đào tạo SEO/GEO/AI Search ở TP.HCM). Ảnh là bảng 5 cấp (SEO Junior → Executive → Specialist → Lead → Manager/Head) × 7 mảng việc (Onpage, Technical, Content, Entity, GEO/AI Search, Offpage), mỗi ô tô màu theo mức AI tự động hóa được (đỏ: tự động hóa phần lớn; cam: AI hỗ trợ đáng kể, cần người duyệt; xám: cần phán đoán/chịu trách nhiệm). Kết luận của ảnh: "AI thay tác vụ, không tự động thay cả vai trò". Trang chủ danhnolan.com không có bài viết đi kèm ảnh (đọc 25/10/2026). Mục này đối chiếu ảnh với tài liệu chính thức của Google, nghiên cứu độc lập, và các skill SEO cho agent đang có trên GitHub.

### 2h.1 Ảnh đúng ở đâu

- **Khung "tác vụ, không phải vai trò"** khớp cách các nghiên cứu về mức tiếp xúc AI chia công việc thành tác vụ. Ảnh cũng tự ghi rõ "không phải dự báo mất việc".
- **Các ô đỏ ở cấp Junior/Executive là việc agent làm được ngay hôm nay**, có skill mã mở cho từng việc. Ví dụ `AgriciDaniel/claude-seo` (~20k★, MIT, đọc mã 25/10/2026) có:
  - 26 skill cho audit kỹ thuật, schema, sitemap, hreflang, nội dung, GEO và backlink;
  - script gọi Search Console, GA4, CrUX;
  - không telemetry; API trả phí (DataForSEO, Ahrefs, Firecrawl) là extension tùy chọn.
- **Cột "giá trị con người" khớp yêu cầu của Google**: Google cho phép dùng AI tạo nội dung, nhưng yêu cầu "manually factcheck and review all AI-generated content… before publishing", kể cả title, meta description và alt text (*Using generative AI content*, cập nhật 1/10/2026). Đó chính là bước "biên tập và kiểm chứng" ở ô cam.

### 2h.2 Ảnh thiếu hoặc nói quá

| Ô trong ảnh | Đối chiếu | Kiểm |
|---|---|---|
| **GEO / AI Search** là một mảng riêng, có "chiến lược AI Search" | Google: "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary"; không cần schema riêng; lưu lượng từ AI features được gộp vào báo cáo Performance, loại "Web" của Search Console (*AI features and your website*, cập nhật 10/12/2025). Với Google, "GEO" phần lớn vẫn là SEO nền tảng. Nghiên cứu *GEO: Generative Engine Optimization* (Aggarwal và cộng sự, KDD 2024) báo cáo tăng hiển thị "tới 40%" trên benchmark GEO-bench của chính nhóm, chứ không đo trên AI Overviews | ⚠️ |
| Junior "Nhập answer-first theo mẫu" được tô đỏ | Sản xuất hàng loạt theo mẫu là đúng kiểu **scaled content abuse**: "Using generative AI tools or other similar tools to generate many pages without adding value for users" (*Spam policies*, cập nhật 28/8/2026). Spam policy cũng bao gồm "attempting to manipulate generative AI responses in Google Search". Ảnh không nhắc ranh giới này | ⚠️ |
| Offpage: "Tìm danh sách nguồn", "Soạn thư outreach" tô đỏ | Tự động hóa được, nhưng gửi thư outreach hàng loạt do AI viết dễ thành spam, và mua hoặc đổi link vi phạm chính sách link spam. Phần cần người làm là quan hệ thật, như ở cột Lead | ⚠️ |
| Technical: Junior/Executive "Rà lỗi, sửa lỗi phổ biến" tô đỏ | Rà lỗi thì agent làm tốt. "Sửa" cần quyền deploy, test và rollback trên site thật, không chỉ cần AI | ⚠️ |
| Không có hàng **đo lường** | Thiếu một thay đổi lớn: Pew Research (dữ liệu 2025, 900 người dùng Mỹ, 68.879 lượt tìm) thấy người dùng nhấp kết quả thường ở **8%** lượt khi có AI summary, so với **15%** khi không có; chỉ ~1% nhấp link nguồn trong summary. Search Console không tách riêng traffic AI Overviews. Vì vậy mọi cấp cần đo lại KPI (hiển thị, chuyển đổi, không chỉ click) | ❌ thiếu |
| Không có hàng **kiểm soát crawler và snippet** | Một quyết định "AI Search" thật nằm ở `robots.txt`, `nosnippet`, `max-snippet`, `noindex` (Google ghi đây là cách giới hạn nội dung hiển thị trong Search), và việc chặn hay mở cho bot AI khác (Cloudflare, GPTBot…). Ảnh bỏ hẳn | ❌ thiếu |
| Mức "Rất cao → Rất thấp" ở hàng "Mức độ tác vụ tiếp xúc AI" | Không kèm nguồn hay số đo. Ảnh ghi "đánh giá dựa trên thực tế ứng dụng AI hiện nay", tức là nhận định của tác giả **(chưa xác minh)** | ⚠️ |

### 2h.3 Công cụ SEO/GEO cho agent (shields 25/10/2026)

| Repo | ★ · license | Commit cuối | Ghi chú |
|---|---|---|---|
| `coreyhaines31/marketingskills` | ~56k · MIT | 10/2026 | Bộ skill marketing tổng quát, có SEO audit (mục 20 §3f) |
| `AgriciDaniel/claude-seo` | ~20k · MIT | 22/10/2026 | 26 skill + 19 agent + script Python. Có **cổng chặn nội dung mỏng** trong `seo-programmatic`: dừng cứng khi vượt 500 trang mà không có lý do, gắn cờ khi nội dung riêng mỗi trang < 40%. Script Indexing API tự ghi rõ chỉ dùng cho JobPosting/BroadcastEvent. `content_humanize.py` chỉ thay cụm từ khuôn mẫu và xóa ký tự Unicode ẩn, tự nói không gỡ được watermark thống kê. Cài qua `git clone` + `install.sh` (README khuyên đọc trước khi chạy) |
| `zubair-trabzada/geo-seo-claude` | ~11k · MIT | 10/2026 | Skill GEO cho Claude Code **(chưa đọc mã)** |
| `TheCraigHewitt/seomachine` | ~7,5k · MIT | 10/2026 | Workspace viết nội dung SEO **(chưa đọc mã)** |
| `aaron-he-zhu/seo-geo-claude-skills` | ~229 · Apache-2.0 | 9/2026 | 20 skill theo khung CORE-EEAT |

### 2h.4 Dùng ảnh thế nào

- **Hợp** để phân việc trong nhóm SEO: ô đỏ giao cho agent nhưng có người duyệt đầu ra; ô cam là AI viết nháp, người sửa và ký; ô xám giữ cho người.
- **Đọc kèm** ba trang chính thức của Google: *AI features and your website*, *Using generative AI content*, *Spam policies* (mục scaled content abuse). Ba trang này đặt ranh giới cho mọi ô đỏ.
- **Thêm hai hàng ảnh thiếu**: đo lường (KPI khi click giảm) và kiểm soát crawler/snippet. Đây là việc của Lead/Manager.
- **Nếu dùng agent làm ô đỏ:** chọn skill có cổng chặn nội dung mỏng như `claude-seo`; đặt giới hạn chi phí cho API trả phí; không cho agent tự đăng hàng loạt trang hay tự gửi outreach.

**Nguồn §2h:** ảnh người dùng gửi 25/10/2026 · https://danhnolan.com (trang chủ, 25/10/2026) · https://developers.google.com/search/docs/appearance/ai-features (cập nhật 10/12/2025) · https://developers.google.com/search/docs/fundamentals/using-gen-ai-content (cập nhật 1/10/2026) · https://developers.google.com/search/docs/essentials/spam-policies (cập nhật 28/8/2026) · https://arxiv.org/abs/2311.09735 (GEO, KDD 2024) · Pew Research qua thewrap.com/ai-summaries-google-article-clicks-half và emarketer.com/content/google-ai-summaries-ending-search-sessions-reducing-click-through-behavior · github.com/AgriciDaniel/claude-seo (clone blob:none 25/10/2026, 412 commit, HEAD 6be93f4; README.md, PRIVACY.md, skills/seo-programmatic/SKILL.md, scripts/{content_humanize,indexing_notify}.py, install.sh) · img.shields.io/github/{stars,license,last-commit}/… cho 7 repo SEO/GEO (25/10/2026) · bên thứ ba: ppc.land/scaled-content-abuse · techcrunch.com/2024/03/05/google-takes-aim-at-seo-optimized-junk-pages-and-spam-with-new-search-update

## 2i. Kiểm ảnh "50 kho lưu trữ GitHub hữu ích" (infographic tiếng Việt, ảnh người dùng gửi, 2026-10-25)

> Infographic tiếng Việt không ghi tác giả: "50 kho lưu trữ GitHub hữu ích — tuyển chọn các kho chất lượng để học hỏi, xây dựng, tự động hóa và đổi mới". Mỗi ô có tên repo, mô tả một dòng và link (nhiều link bị cắt). Đã kiểm **cả 50 mục**: lấy số sao, license và commit cuối qua shields (25/10/2026); dùng `git ls-remote` so HEAD để phát hiện repo đã đổi chỗ (cùng hash = GitHub đang chuyển hướng); đọc README của các mục có vấn đề (nanoGPT, Bumblebee, iFixAi, awesome-claude-skills, TradingAgents, maigret); đối chiếu với hồ sơ đã có trong kho.

### 2i.1 Bảng kiểm (shields 25/10/2026)

| # | Repo | ★ | License | Commit cuối | Kiểm |
|---|---|---|---|---|---|
| 1 | `ifixai-ai/iFixAi` | 34k | Apache-2.0 | 10/2026 | ⚠️ Tên đúng là `iFixAi` (ảnh cắt). Chẩn đoán agent "lệch mục tiêu". ⚠️ 34k★/1,7k fork nhưng PyPI ~481 lượt tải/tháng; README dẫn site thương mại |
| 2 | `public-apis/public-apis` | 492k | MIT | 10/2026 | ✅ |
| 3 | `codecrafters-io/build-your-own-x` | 556k | **không ghi** | 7/2026 | ✅ |
| 4 | `kamranahmedse/developer-roadmap` | 370k | tự đặt/khác | 10/2026 | ✅ License tự đặt |
| 5 | `EbookFoundation/free-programming-books` | 400k | CC-BY-4.0 | 10/2026 | ✅ |
| 6 | `donnemartin/system-design-primer` | 376k | tự đặt/khác | 3/2026 | ✅ |
| 7 | `jwasham/coding-interview-university` | 363k | CC-BY-SA-4.0 | 12/2024 | ✅ Commit cuối 12/2024 |
| 8 | `jlevy/the-art-of-command-line` | 163k | **không ghi** | 7/2023 | ⚠️ Đứng yên từ 7/2023 |
| 9 | `practical-tutorials/project-based-learning` | 288k | MIT | 10/2026 | ✅ |
| 10 | `getify/You-Dont-Know-JS` | 185k | tự đặt/khác | 1/2026 | ✅ |
| 11 | `trimstray/the-book-of-secret-knowledge` | 253k | MIT | 11/2024 | ⚠️ Đứng yên từ 11/2024 |
| 12 | `yangshun/tech-interview-handbook` | 143k | MIT | 8/2026 | ✅ |
| 13 | `awesome-selfhosted/awesome-selfhosted` | 330k | tự đặt/khác | 10/2026 | ✅ |
| 14 | `trekhleb/javascript-algorithms` | 197k | MIT | 7/2026 | ✅ |
| 15 | `Chalarangelo/30-seconds-of-code` | 129k | CC-BY-4.0 | 9/2026 | ✅ CC-BY-4.0 |
| 16 | `github/gitignore` | 176k | CC0-1.0 | 10/2026 | ✅ |
| 17 | `ollama/ollama` | 185k | MIT | 10/2026 | ✅ |
| 18 | `langchain-ai/langchain` | 148k | MIT | 10/2026 | ✅ |
| 19 | `n8n-io/n8n` | 209k | tự đặt/khác | 10/2026 | ✅ License fair-code (Sustainable Use), không OSI |
| 20 | `openclaw/openclaw` | 393k | MIT | 10/2026 | ✅ Hồ sơ mục 02 |
| 21 | `langgenius/dify` | 159k | tự đặt/khác | 10/2026 | ✅ Apache-2.0 có điều khoản thêm |
| 22 | `langflow-ai/langflow` | 156k | MIT | 10/2026 | ✅ |
| 23 | `mem0ai/mem0` | 68k | Apache-2.0 | 10/2026 | ✅ |
| 24 | `browser-use/browser-use` | 119k | MIT | 10/2026 | ✅ |
| 25 | `crewAIInc/crewAI` | 60k | MIT | 10/2026 | ✅ |
| 26 | `geekan/MetaGPT` | 71k | MIT | 1/2026 | ⚠️ Đã chuyển sang `FoundationAgents/MetaGPT` |
| 27 | `microsoft/autogen` | 62k | CC-BY-4.0 | 10/2026 | ⚠️ **Chế độ bảo trì**; kế nhiệm là Microsoft Agent Framework (mục 02) |
| 28 | `Aider-AI/aider` | 50k | Apache-2.0 | 5/2026 | ⚠️ Commit cuối 5/2026 |
| 29 | `microsoft/markitdown` | 192k | MIT | 10/2026 | ✅ |
| 30 | `open-webui/open-webui` | 157k | tự đặt/khác | 10/2026 | ✅ License riêng giữ thương hiệu |
| 31 | `soxoj/maigret` | 39k | MIT | 10/2026 | ✅ OSINT: dựng hồ sơ một người từ username trên ~5.900 trang. Dual-use, cần cơ sở pháp lý khi dùng |
| 32 | `TauricResearch/TradingAgents` | 114k | Apache-2.0 | 10/2026 | ✅ Khung nghiên cứu, README không phải lời khuyên đầu tư |
| 33 | `browserbase/stagehand` | 26k | MIT | 10/2026 | ✅ |
| 34 | `mendableai/firecrawl` | 195k | AGPL-3.0 | 10/2026 | ⚠️ Đã chuyển sang `firecrawl/firecrawl`; **AGPL-3.0** |
| 35 | `huggingface/transformers` | 168k | Apache-2.0 | 10/2026 | ✅ |
| 36 | `vllm-project/vllm` | 95k | Apache-2.0 | 10/2026 | ✅ |
| 37 | `ggml-org/llama.cpp` | 132k | MIT | 10/2026 | ✅ |
| 38 | `run-llama/llama_index` | 53k | MIT | 10/2026 | ✅ |
| 39 | `karpathy/nanoGPT` | 64k | MIT | 11/2025 | ❌ README tự ghi "very old and deprecated" (11/2025), dùng `karpathy/nanochat` |
| 40 | `infiniflow/ragflow` | 93k | Apache-2.0 | 10/2026 | ✅ |
| 41 | `supermemoryai/supermemory` | 31k | MIT | 10/2026 | ✅ |
| 42 | `ComposioHQ/awesome-claude-skills` | 78k | **không ghi** | 7/2026 | ⚠️ Không có LICENSE; chép lại skill tài liệu của Anthropic (`document-skills`, "All rights reserved"); link UTM về Composio |
| 43 | `perplexityai/bumblebee` | 5.1k | Apache-2.0 | 10/2026 | ✅ Trình quét **chỉ đọc** lockfile, extension, cấu hình MCP trên máy dev (Go, v0.1.2), không phải "bảo mật AI" chung |
| 44 | `comfyanonymous/ComfyUI` | 143k | GPL-3.0 | 10/2026 | ⚠️ Đã chuyển sang `Comfy-Org/ComfyUI`; GPL-3.0 |
| 45 | `deepseek-ai/DeepSeek-V3` | 105k | MIT | 8/2025 | ⚠️ Ảnh trỏ tới tổ chức, không phải một repo; repo model (vd. DeepSeek-V3, commit cuối 8/2025) là trọng số + inference, không phải mã huấn luyện |
| 46 | `lobehub/lobe-chat` | 83k | tự đặt/khác | 10/2026 | ⚠️ Đã đổi tên thành `lobehub/lobehub`; license cộng đồng có điều kiện thương mại |
| 47 | `freeCodeCamp/freeCodeCamp` | 458k | BSD-3-Clause | 10/2026 | ✅ |
| 48 | `jwasham/coding-interview-university` | 363k | CC-BY-SA-4.0 | 12/2024 | ❌ **Trùng #7** |
| 49 | `langchain-ai/langchain` | 148k | MIT | 10/2026 | ❌ Trùng #18 (hoặc LangGraph; link bị cắt) |
| 50 | `n8n-io/n8n` | 209k | tự đặt/khác | 10/2026 | ❌ **Trùng #19** |

**Tổng:** 50 ô nhưng chỉ **47 repo khác nhau**: #48 trùng #7, #50 trùng #19, #49 trỏ `langchain-ai/l…` (trùng #18 nếu là LangChain). Repo tồn tại cả 50, không link nào chết. Còn lại:

- **4 repo đã đổi chỗ** (cùng HEAD với tên mới): MetaGPT → `FoundationAgents/MetaGPT`, Firecrawl → `firecrawl/firecrawl`, ComfyUI → `Comfy-Org/ComfyUI`, Lobe Chat → `lobehub/lobehub`. Link cũ vẫn chạy nhờ chuyển hướng, nhưng script hay lockfile nên dùng tên mới.
- **2 repo đã thôi phát triển chính:** nanoGPT (chính Karpathy ghi "deprecated", chuyển sang nanochat) và AutoGen (bảo trì, nhường cho Microsoft Agent Framework). **3 tài liệu đứng yên** từ 2023–2024 (the-art-of-command-line, the-book-of-secret-knowledge, coding-interview-university) vẫn đọc được, nhưng phần công cụ có thể đã cũ.
- **License cần đọc trước khi dùng thương mại:** n8n (Sustainable Use, không OSI), Firecrawl (**AGPL-3.0**), ComfyUI (GPL-3.0), Open WebUI và LobeHub (license riêng có điều kiện thương hiệu/thương mại), Dify (Apache-2.0 kèm điều khoản). `ComposioHQ/awesome-claude-skills` không có LICENSE mà lại chép skill tài liệu của Anthropic ghi "All rights reserved".
- **Mô tả sai hoặc lệch:**
  - #43 Bumblebee không phải "công cụ bảo mật AI" chung, mà là trình quét chỉ đọc cho phản ứng sự cố chuỗi cung ứng trên máy dev, có đọc cả cấu hình MCP.
  - #45 trỏ tới cả tổ chức DeepSeek, không phải một kho mã.
  - #1 iFixAi có số sao rất lệch so với lượt tải PyPI **(chưa xác minh là sao ảo; cần thận trọng)**.
- **Dual-use:** #31 maigret dựng hồ sơ cá nhân từ username, chỉ dùng khi có cơ sở pháp lý theo quy định bảo vệ dữ liệu cá nhân.

### 2i.2 Ảnh gom ba nhóm khác nhau

| Nhóm | Mục | Nên đọc ở |
|---|---|---|
| Học lập trình (tài liệu, lộ trình) | #2–16, #47–48 | Mục 08 §1–§3 (build-your-own-x, developer-roadmap, system-design-primer đã có hồ sơ) |
| Hạ tầng LLM và agent | #17–30, #33–41, #44–46 | Mục 02, 05, 10, 11, 14 (đa số đã có hồ sơ và đã kiểm license) |
| Công cụ ngách | #1, #31, #32, #42, #43 | Bảng trên; Bumblebee hợp với §3 mục 12 (chuỗi cung ứng) |

**Dùng thế nào:** coi ảnh là danh sách tên để tra, không phải danh sách để cài. Trước khi dùng một mục: thay tên repo cũ bằng tên mới; bỏ nanoGPT và AutoGen cho dự án mới; đọc license nếu nhúng vào sản phẩm. Với agent tự chủ (browser-use, OpenClaw, crewAI), đọc hồ sơ an toàn trong kho trước.

**Nguồn §2i:** ảnh người dùng gửi 25/10/2026 · img.shields.io/github/{{stars,license,last-commit}}/<repo>.json cho 47 repo (25/10/2026) · `git ls-remote` so HEAD: comfyanonymous/ComfyUI = Comfy-Org/ComfyUI, geekan/MetaGPT = FoundationAgents/MetaGPT, mendableai/firecrawl = firecrawl/firecrawl, lobehub/lobe-chat = lobehub/lobehub · README: github.com/karpathy/nanoGPT (thông báo 11/2025), github.com/perplexityai/bumblebee (26 commit, v0.1.2), github.com/ifixai-ai/iFixAi (331 commit từ 27/4/2026), github.com/ComposioHQ/awesome-claude-skills (`document-skills/*/LICENSE.txt`), github.com/TauricResearch/TradingAgents, github.com/soxoj/maigret · img.shields.io/pypi/dm/ifixai.json · bên thứ ba: decrypt.co/368944/perplexity-open-source-bumblebee-ai-scanner-mcp-infection-malware · discuss.pytorch.kr/t/ifixai-ai-45/11296 · pypi.org/project/iFixAi

## 2j. Nâng cấp 31/10/2026: rà repo lớn (awesome list và khoá học)

> Hai việc. (1) Đọc lại sao, license, ngày push của **31 repo** mục 08 đã có trong catalog (GitHub search API, 31/10/2026). (2) Tìm repo lớn còn thiếu: 7 truy vấn GitHub (`topic:awesome-list llm`, "awesome agents", "awesome claude", `topic:awesome ai`, "llm course tutorial", "for-beginners", và "awesome" tạo sau 1/10/2025), lọc theo `data/projects.json`. Chọn **7 repo**, clone `--filter=blob:none` và đọc file thật. Với awesome list, "độ sâu" là: sao, commit cuối, license đọc từ file, số mục đếm được, **thử 10 link** (lấy đều trong danh sách; link GitHub kiểm bằng `git ls-remote` vì proxy chặn trang HTML của github.com), người duy trì. **Không chạy script nào của các repo.**

### 2j.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (12/10 → 31/10/2026) | Hệ quả |
|---|---|---|
| `kamranahmedse/developer-roadmap` | **Đã chuyển sang `nilbuild/developer-roadmap`** (370,9k★, GitHub báo `NOASSERTION`, push 31/10/2026); tìm theo tên cũ không còn kết quả | Catalog nên đổi `repo`; link cũ vẫn chuyển hướng **(chưa xác minh)** |
| `Shubhamsaboo/awesome-llm-apps` | ~105k → **143,6k** (+37%) | Vẫn là danh sách "có code" lớn nhất §2 |
| `hesreallyhim/awesome-claude-code` | ~45k → **57k**; GitHub báo `NOASSERTION` | Bảng §2 ghi "37–55k" đã cũ |
| `AgriciDaniel/claude-seo` | ~20k → **25k** | §2h |
| `mlabonne/llm-course` | Push cuối **5/2/2026** (gần 9 tháng) | Coi là tài liệu tĩnh; §2b đã ghi "ít commit" |
| `KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub` | Push cuối **9/2/2026** | Bộ câu hỏi không theo kịp chủ đề 2026 (§2c.3) |
| `wong2/awesome-mcp-servers` · `EvanLi/Github-Ranking` | Catalog ghi `null`; nay **4,4k★ MIT** (push 13/7) · **12,7k★ MIT** (push 31/10) | Bổ sung số và license |
| `rasbt/LLMs-from-scratch`, `donnemartin/system-design-primer`, `NirDiamant/RAG_Techniques` | GitHub báo `NOASSERTION` | Không đổi license: catalog giữ license đã đọc trong file (Apache-2.0 + phần sách; CC BY 4.0; phi thương mại) |

Các repo khác dao động dưới 5%. `ai-engineering-from-scratch` ở §3 mục 8 ghi "(chưa xác minh)": nay đã xác minh, xem `rohitg00/…` dưới đây.

### 2j.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `rohitg00/ai-engineering-from-scratch` | Khoá học | 76,1k · MIT | 29/10/2026 | 542 bài trong 20 phase, code Python/TS/Rust/Julia, có bản README tiếng Việt | Gần như một người viết, 7 tháng tuổi |
| `sickn33/agentic-awesome-skills` | Kho skill + danh mục | 48,9k · MIT (code) + CC BY 4.0 (nội dung) | 31/10/2026 | 2.886 `SKILL.md`, installer npm ghim phiên bản, MCP "AAS Core" | Cài cả bộ làm phình ngữ cảnh |
| `VoltAgent/awesome-openclaw-skills` | Awesome list | 53,5k · MIT | 30/10/2026 | 5.213 skill OpenClaw lọc từ ClawHub, chia 30 nhóm | "Curated, not audited"; link đi qua `clawskills.sh` |
| `github/awesome-copilot` | Kho tuỳ biến chính chủ | 40,6k · MIT | 30/10/2026 | 222 agent, 193 instruction, 448 skill, 110 plugin, 8 hook cho Copilot | Quét rủi ro PR chỉ là "soft gate" |
| `e2b-dev/awesome-ai-agents` | Awesome list | 30,7k · **CC BY-NC-SA 4.0** | 21/8/2026 | 215 agent (mở và đóng), mỗi mục có category/mô tả/link | **Nội dung đứng yên từ 2024**, commit 2026 chỉ gắn UTM |
| `aishwaryanr/awesome-generative-ai-guide` | Lộ trình + danh sách khoá | 30,1k · MIT | 28/10/2026 | ~116 khoá ngoài + khoá miễn phí tự soạn, ngân hàng câu hỏi phỏng vấn | Kèm quảng cáo khoá Maven trả phí |
| `microsoft/mcp-for-beginners` | Khoá học | 17,6k · MIT | 30/10/2026 | 13 module MCP, mẫu đa ngôn ngữ, 54 bản dịch (có `vi`) | Không có CI cho code mẫu; SDK ghim `>=` |

### 2j.3 Awesome list: đếm mục và thử link

| Repo | Số mục (đếm 31/10) | 10 link thử | Người duy trì | Ghi chú |
|---|---|---|---|---|
| `VoltAgent/awesome-openclaw-skills` | 5.213 dòng `- [` trong `categories/*.md` (badge ghi 5.200, README ghi 5.300+) | **10/10 sống** (trang `clawskills.sh`; slug giả trả 404, nên 200 là thật) | VoltAgent (Necati Özmen, ~300/566 commit), 161 tác giả | README công bố đã loại 7.215 skill (4.065 spam, 373 độc hại theo báo cáo bảo mật công khai, 886 crypto…). CI chỉ bắt PR phải có link ClawHub. Repo lỡ commit `.claude/settings.local.json` chứa đường dẫn máy tác giả. Badge vẫn trỏ tên cũ `awesome-clawdbot-skills` |
| `e2b-dev/awesome-ai-agents` | 215 mục `## [` | 7 sống, **2 chết** (`encode.software` hết phân giải, ảnh `useinput.com`), 1 không kiểm được (trang org GitHub) | E2B (Tereza Tizkova ~340/473 commit) | Commit theo năm: 345 (2023), 120 (2024), 3 (2025), 5 (2026); 5 commit gần nhất đều là **thêm `utm_source` vào link e2b.dev**. LICENSE là CC BY-NC-SA 4.0 nên GitHub báo `NOASSERTION`; không chép nội dung vào sản phẩm thương mại |
| `aishwaryanr/awesome-generative-ai-guide` | `courses.md`: 116 link ngoài; 695 file (khoá tự soạn, 134 file phỏng vấn) | **9/10 sống**, 1 YouTube trả 429 (giới hạn tần suất, không phải chết) | Aishwarya Naresh Reganti (LevelUp Labs), 32 tác giả; 55/508 commit có trailer Claude | README tự ghi "một số listing bên ngoài có thể cần trả phí"; mỗi trang dẫn sang khoá Maven có phí |
| `sickn33/agentic-awesome-skills` | 2.886 `SKILL.md` trong `skills/` (+5.988 bản trong `plugins/`); mô tả ghi "2.884+" ✅ | `docs/sources/sources.md` có 64 link upstream: **10/10 sống** | `sickn33` (Nick), 502 tác giả; 899 commit của bot | Phần lớn mục là file trong repo, nên "link rot" ít liên quan; rủi ro là chất lượng từng skill |
| `github/awesome-copilot` | 222 / 193 / 448 / 110 / 8 (agent / instruction / skill / plugin / hook) | 10/10 là link `aka.ms` cài vào VS Code, trỏ về file `main` của chính repo | GitHub (Aaron Powell ~790 commit), 598 tác giả | Link cài trỏ `main`, không ghim commit |

### 2j.4 Hồ sơ ngắn

- **`rohitg00/ai-engineering-from-scratch`.** Tạo 18/3/2026, 2.631 commit, **2.368 commit của Rohit Ghumare** (nhịp 725 commit tháng 4, 808 tháng 10). Lời "542 lessons, 20 phases" ✅ khớp số thư mục `phases/*/*`. Có 1.423 file code trong `phases/`, CI `curriculum.yml` chạy `audit_lessons.py` và test lab chứng chỉ; bản dịch README do workflow chạy **NLLB-200 ngay trong runner** (không gửi API ngoài). Thư mục `certifications/claude` là tài liệu ôn **không chính thức**, tự ghi "confirm facts in the official…" và dẫn trang FAQ của Anthropic. `i18n/vi/README.md` chỉ dịch README, bài học vẫn tiếng Anh. Rủi ro: một người viết rất nhanh, chất lượng từng bài chưa ai đánh giá độc lập **(chưa xác minh)**. Học trên web hoặc `git clone https://github.com/rohitg00/ai-engineering-from-scratch`.
- **`sickn33/agentic-awesome-skills`.** Không chỉ là danh sách: monorepo có app web (Supabase, Vercel), 14 workflow (CodeQL, dependency-review, `skill-review` dùng Tessl khi có token), `LICENSE-CONTENT` tách CC BY 4.0 cho nội dung. Installer đáng học: README hướng dẫn **`npm exec --yes --ignore-scripts --package=agentic-awesome-skills@20.3.0 -- agentic-awesome-skills --release 20.3.0 --path .agents/skills --skills brainstorming,systematic-debugging --dry-run`**, tức ghim phiên bản, tắt script npm, xem trước rồi mới ghi. `tools/bin/install.js` chỉ gọi `git` và registry npm. Thận trọng: cài `--all` đưa hàng nghìn mô tả skill vào ngữ cảnh; README tự cảnh báo Antigravity bị quá tải.
- **`VoltAgent/awesome-openclaw-skills`.** Cùng chủ với `VoltAgent/awesome-agent-skills` (đã có trong catalog). Bảng "đã loại 7.215" là điểm cộng hiếm thấy, nhưng README nói rõ **"curated, not audited"** và khuyên xem báo cáo VirusTotal trên ClawHub trước khi cài. Mọi link đi qua `clawskills.sh` (site của VoltAgent) chứ không thẳng tới ClawHub, nên danh sách phụ thuộc một domain trung gian. Có khối quảng cáo Cloudways kèm mã giảm giá. Cài: `openclaw skills install <slug>` hoặc `npx clawhub install <slug>`.
- **`github/awesome-copilot`.** Repo chính chủ GitHub, 2.947 commit, 1.044 commit từ 1/7/2026. **64 workflow**, trong đó `pr-risk-scan.yml` chạy `eng/pr-risk-scan.mjs` với 5 luật regex: lời lẽ "bỏ qua guardrail", `curl | bash`, `npx -y`/`uvx`, lệnh chạy gói động, phiên bản không ghim. Kết quả chỉ được **bình luận vào PR (soft gate)**, không chặn merge. Có cả `resource-staleness-report` và `duplicate-resource-detector` viết bằng GitHub Agentic Workflows. Cài: `copilot plugin install <plugin>@awesome-copilot`.
- **`e2b-dev/awesome-ai-agents`.** Danh sách agent sớm nhất (6/2023) và được dẫn nhiều nhất. Đến 2026 nó là **tài liệu lịch sử**: hầu như không có mục mới sau 2024, nhiều agent trong list có thể đã ngừng (chưa kiểm từng mục), và commit gần đây chỉ gắn UTM cho link sản phẩm E2B. License CC BY-NC-SA (phi thương mại, chia sẻ tương tự), GitHub không nhận ra. Dùng để tra lịch sử, không để chọn công cụ.
- **`aishwaryanr/awesome-generative-ai-guide`.** Kết hợp danh sách khoá, lộ trình theo cấp, cập nhật nghiên cứu và **ngân hàng câu hỏi phỏng vấn** (bổ sung cho §2c.4). Commit đều (60 từ 1/7). Mỗi khoá có ký hiệu miễn phí/ngoài/video và năm. Nhược: lẫn quảng cáo khoá trả phí của chính tác giả.
- **`microsoft/mcp-for-beginners`.** 13 module từ khái niệm tới lab, README nói theo **MCP spec 2026-07-28** (khớp mục 04), có `02-Security`. 8.415 file là bản dịch tự động (`localizeflow[bot]` 831 commit), có `translations/vi` (cập nhật 19/9/2026, chậm hơn bản gốc). **Không có workflow CI nào**, nên 26 manifest mẫu trong `03-GettingStarted` (npm, pip, .NET, Maven) không được build tự động; mẫu TypeScript khai báo `"@modelcontextprotocol/sdk": ">=1.32.0"`, có thể kéo SDK v2 thay đổi API. Khi học, ghim phiên bản SDK trước khi chạy.

### 2j.5 Mẫu chung rút ra

1. **"Awesome list" đã thành kho nội dung**: 3/5 danh sách lớn mới (agentic-awesome-skills, awesome-copilot, openclaw-skills) chứa hoặc trỏ tới mã chạy được (skill, hook, plugin). Kiểm tra lúc này là kiểm **chuỗi cung ứng**, không chỉ kiểm link chết.
2. **Cổng tự động ít khi chặn thật**: risk-scan của awesome-copilot chỉ bình luận; CI của openclaw-skills chỉ đòi link ClawHub. Lớp lọc thật nằm ở registry (ClawHub + VirusTotal) hoặc người duyệt.
3. **Link rot thấp ở list còn sống, cao ở list đứng yên**: 10/10 ở openclaw-skills và sources của agentic-awesome-skills; 2/10 chết ở e2b. Ngày commit cuối không đủ: e2b "push 21/8/2026" nhưng nội dung dừng từ 2024.
4. **License nội dung khác license code**: CC BY-NC-SA (e2b), MIT + CC BY (agentic-awesome-skills), MIT + CC0 (prompts.chat, mục 17). GitHub báo `NOASSERTION` hoặc sai; đọc file.
5. **Sao tăng nhanh ở repo một người viết bằng agent**: ai-engineering-from-scratch (76k trong 7 tháng). Nội dung có CI kiểm cấu trúc nhưng chưa có đánh giá sư phạm độc lập.

**Nguồn §2j:** GitHub search API 31/10/2026 (`repo:` cho repo cũ và mới; 7 truy vấn chủ đề) · `meta_all.json`/`status_all.json` đợt rà 31/10 · clone `--filter=blob:none` 7 repo, đọc: rohitg00/ai-engineering-from-scratch (LICENSE, README.md, i18n/, phases/ (cây), .github/workflows/{curriculum,translate}.yml, certifications/claude/README.md), sickn33/agentic-awesome-skills (LICENSE, LICENSE-CONTENT, package.json, README.md, tools/bin/install.js, .github/workflows/skill-review.yml, docs/sources/sources.md), VoltAgent/awesome-openclaw-skills (LICENSE, README.md, categories/*.md, .github/workflows/pr-check.yml, .claude/settings.local.json), github/awesome-copilot (LICENSE, README.md, .github/workflows/pr-risk-scan.yml, eng/pr-risk-scan.mjs, docs/README.agents.md), e2b-dev/awesome-ai-agents (LICENSE.md, README.md, lịch sử commit), aishwaryanr/awesome-generative-ai-guide (LICENSE.md, README.md, courses.md), microsoft/mcp-for-beginners (LICENSE, README.md, 03-GettingStarted/01-first-server/solution/typescript/package.json, .github/) · thử link bằng curl và `git ls-remote` 31/10/2026 · https://github.com/nilbuild/developer-roadmap · https://clawskills.sh · https://aiengineeringfromscratch.com

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
- §2d.2 (16/10/2026): https://github.com/cporter202/ai-growth-stack (clone đầy đủ, 7 commit 21/12/2025, chỉ README.md; 229★/70 fork shields) · https://rapidapi.com/user/contact-_OGid12Eu (trang cần JavaScript, không đọc được danh sách) · https://apidataframe.com (9 API, chỉ qua RapidAPI, không tên người vận hành) · https://github.com/cporter202 (40 repo, bio ViralWaveStudio.com) · https://www.buymeacoffee.com/viralwavestudio
- §2g (16/10/2026): https://www.kdnuggets.com/the-roadmap-to-mastering-agentic-ai-systems-in-2026 (Vinod Chugani, 13/10/2026, đọc toàn bài) · https://github.com/microsoft/autogen (README: "now in maintenance mode… New users should start with Microsoft Agent Framework"; 61,4k★) · https://www.anthropic.com/engineering/multi-agent-research-system (13/6/2025: agent ~4×, multi-agent ~15× token so với chat) · https://www.anthropic.com/engineering/building-effective-agents · https://machinelearningmastery.com/the-roadmap-for-mastering-agentic-ai-in-2026/ (bài khác cùng chủ đề)
- §2f ảnh Brij "How to become an AI engineer in 2026" (13/10/2026): https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ("unclear if there are fool-proof methods of prevention") · https://roadmap.sh/ai-engineer · https://github.com/chiphuyen/aie-book (README: chương fine-tuning, dataset engineering) · https://github.com/patchy631/ai-engineering-hub · shields.io: aie-book ~18k, ai-engineering-hub ~38k MIT, developer-roadmap ~369k, litellm ~61k
