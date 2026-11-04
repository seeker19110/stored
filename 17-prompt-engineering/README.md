# 17 · Prompt Engineering, Prompt Optimization & System Prompt Collections

## 1. Hướng dẫn & tài nguyên

| Tài nguyên | Repo / URL | ★ | Ghi chú |
|---|---|---|---|
| **Prompt Engineering Guide** (DAIR.AI) | dair-ai/Prompt-Engineering-Guide | ~78–79k (9/2026) | Nay bao phủ cả context engineering, RAG, agents; promptingguide.ai |
| **Anthropic Prompt Library & docs** | docs.anthropic.com (prompt engineering, prompt generator, Claude cookbook) | – | Kỹ thuật XML tags, few-shot, chain-of-thought, prefill |
| **OpenAI Cookbook / Prompt guide** | openai/openai-cookbook | 76,6k (12/10/2026) | Xem §2b |
| **awesome-chatgpt-prompts** | f/awesome-chatgpt-prompts | – | Fatih Kadir Akın; prompts.chat |
| **Google Prompting guide (Gemini)** | – | – | |
| Learn Prompting | learnprompting.org | – | Khóa học mở |

## 2. Prompt optimization / "programming, not prompting"

| Dự án | Repo | ★ | Cách tiếp cận |
|---|---|---|---|
| **DSPy** (Stanford NLP) | stanfordnlp/dspy | ~38–39k (9/2026, v3.3.1) | Module hóa (Signature, Module), optimizer (BootstrapFewShot, MIPROv2, GEPA) tự tối ưu prompt/weights theo metric |
| TextGrad | zou-group/textgrad | – | "Gradient" bằng ngôn ngữ tự nhiên |
| Promptfoo | promptfoo/promptfoo | – | Đánh giá/so sánh prompt (mục 07) |
| LangSmith Hub, PromptLayer, Langfuse Prompts | – | – | Quản lý version prompt |
| awesome-dspy | ganarajpr/awesome-dspy | – | Tài nguyên DSPy |

## 2b. Structured output & thư viện lập trình LLM (đã xác minh 2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **567-labs/instructor** | 14,0k | MIT | commit 10/10/2026; v1.17.0 (9/9) | Output có cấu trúc kiểm bằng Pydantic, chạy với OpenAI, Anthropic, Google, Ollama; README nói hơn 3 triệu lượt tải/tháng | Retry khi validate lỗi đồng nghĩa thêm lượt gọi LLM và chi phí |
| **dottxt-ai/outlines** | 15,9k | Apache-2.0 | commit 24/8/2026; v1.3.3 (6/8) | Ràng buộc ngay lúc decode (JSON Schema, regex, grammar) nên output hợp lệ theo cấu trúc | Bảo đảm đầy đủ cần truy cập logit, tức model local **(chưa xác minh)** |
| **guidance-ai/guidance** | 21,8k | MIT | commit 21/5/2026; 0.3.2 (18/3) | Ngôn ngữ sinh có ràng buộc (`gen()` theo regex/grammar), tự "tua nhanh" các token mà grammar đã cố định | Chậm lại: không commit từ 5/2026 |
| **BoundaryML/baml** | 9,4k | Apache-2.0 | 0.22.0 (12/10/2026) | Ngôn ngữ có kiểu để viết "prompt function"; kiểu giữ ở runtime; gọi được từ TS, Python, Go, C#, Java | DSL mới + bước codegen; vẫn 0.x |
| **anthropics/claude-cookbooks** (trước là anthropic-cookbook) | 53,4k | MIT | commit 10/10/2026 | Công thức chính thức cho Claude: tool use, RAG, prompt caching, sub-agent | Chỉ cho Claude; vài link trong README còn dùng tên cũ |
| **openai/openai-cookbook** | 76,6k | MIT | commit 9/10/2026 | Ví dụ và hướng dẫn chính thức cho OpenAI API (cookbook.openai.com), nhận cookbook bên thứ ba đã review | Notebook cũ có thể dùng API đã bị thay **(chưa xác minh)** |

**Không nên bắt đầu mới với (kiểm 12/10/2026):**

- `anthropics/courses` (22,9k★): **archive 15/9/2026**, license CC BY-NC 4.0 (phi thương mại).
- `anthropics/prompt-eng-interactive-tutorial` (38,5k★): commit cuối 8/4/2024, không thấy file LICENSE — vẫn đọc để học được, nhưng nội dung đã cũ 2,5 năm.
- `microsoft/promptflow` (11,2k★): **ngừng phát triển tính năng 20/4/2026, nghỉ hẳn 20/4/2027**; Microsoft hướng dẫn chuyển sang Microsoft Agent Framework (mục 02).
- `microsoft/LLMLingua` (6,7k★): commit code cuối 28/10/2025 (9/2026 chỉ ghim CI); `microsoft/poml` (5,0k★): commit cuối 20/9/2025; `MadcowD/ell` (5,8k★): commit cuối 5/6/2025.

**Chọn nhanh:** gọi API đóng (Claude, GPT) cần JSON đúng schema → instructor (hoặc structured output có sẵn của nhà cung cấp); model local cần bảo đảm tuyệt đối → outlines; nhóm đa ngôn ngữ muốn hợp đồng có kiểu → BAML; tối ưu prompt theo metric → DSPy (bảng trên).

## 2c. nokia-applied-research/AnyJev: đọc quyết định có kiểu kèm xác suất từ LLM mở, không cần huấn luyện (link người dùng gửi, 2026-10-16)

**Kết luận:** đáng dùng khi agent chạy model mở và cần **phân loại hoặc định tuyến kèm độ tin** (chọn 1 trong K nhãn, có/không, chấm thang điểm). Phần không cần huấn luyện (`Decider`, mức `L0`) là cách đóng gói gọn ba kỹ thuật đã có bài báo. Số liệu trong README khớp với JSON trong repo, nhưng ô được nêu nổi bật là một trong những ô đẹp nhất. Dự án còn rất mới (Pre-Alpha, 0.3.0) và chưa có ai kiểm chứng độc lập.

### 2c.1 Là gì, và "Jev" là gì

- **Jev** là model "System One" **đóng, chạy qua API** của startup TypeSafe AI (San Francisco), mở early access ngày 15/9/2026. Nó trả quyết định có kiểu (Choice, Score, yes/no) kèm xác suất thay vì sinh văn bản. Các con số 70–500 ms và 0,042 USD cho 1 triệu token đầu vào đều do TypeSafe tự công bố (The Register).
- **AnyJev** là bản mở, giao diện "kiểu Jev", Apache-2.0. README và `CREDITS.md` ghi rõ "Not affiliated with TypeSafe AI or Jev". Gồm hai phần:
  - `Decider`: đọc quyết định từ **bất kỳ LLM mở nào** qua backend transformers, vLLM, SGLang hoặc llama.cpp. Không huấn luyện, không cần nhãn.
  - `Tacit`: 5 checkpoint 1,7B–9B **tự chưng cất** từ Qwen3/Qwen3.5 (Apache-2.0). Model học trả lời trong một lượt forward đáp án mà nó đạt được khi suy luận. Với `adaptive=True`, một phần quyết định có giới hạn được chuyển sang suy luận.
- Có HTTP gateway `python -m anyjev.serve` (`POST /v1/decide`). Gateway **không có xác thực**, mặc định chỉ nghe ở 127.0.0.1.

### 2c.2 Cách hoạt động (đọc mã ở HEAD `b03158e`, 12/10/2026)

| Mức | Làm gì | Gốc kỹ thuật |
|---|---|---|
| `raw` | Một prompt, softmax giới hạn trên token nhãn (A, B, C…) | — |
| `L0`, bước 1 | Đọc K phép xoay vòng thứ tự lựa chọn để mỗi lựa chọn đứng ở mọi vị trí, rồi lấy trung bình **log-prob** (`anyjev/calibrate/permute.py`). Nếu thiên lệch vị trí là cộng tính trên logit thì nó bị triệt tiêu đúng | Permutation debiasing, Zheng et al., ICLR 2024 (arXiv 2309.03882) |
| `L0`, bước 2 | Chia cho prior nhãn rồi chuẩn hoá lại (`contextual.py`). Mặc định ước lượng prior bằng trung bình chạy trên các đầu vào thật, hệ số 0,75 | Batch Calibration, Zhou et al., ICLR 2024; tuỳ chọn content-free theo Zhao et al., ICML 2021 |
| Rotation budget | Dừng sớm khi biên log-odds vượt ngưỡng. Ngưỡng được chứng nhận bằng cận Clopper–Pearson so với đáp án đọc đủ K, nên không cần nhãn. README: trung bình 7,2/18 phép xoay, thông lượng gấp 2,2–2,7 lần | Của AnyJev |
| Tacit `one_forward` / `cot` | Một prefill. Khi biên giữa 2 lựa chọn đầu < `tau`, model suy luận lại; tối đa `max_cot_share` (20%) của 1.000 quyết định gần nhất | Của AnyJev |

Điểm tốt về kỷ luật kỹ thuật:

- `Decider` **không bao giờ sinh token**, nên không có bước parse nào có thể hỏng.
- Mỗi `Decision` mang `level`. Gọi `require="L0"` sẽ từ chối kết quả ở mức yếu hơn.
- `tests/test_readme_numbers.py` kiểm các bảng trong README khớp với JSON đã commit.
- `AGENTS.md` của repo cấm số bịa và cấm agent tự `git commit`.
- Lõi chỉ phụ thuộc numpy. Gói chỉ gọi mạng tới server vLLM do người dùng cấu hình (`urllib` trong `backends/vllm.py` và `tacit.py`); không thấy telemetry.

### 2c.3 Kiểm số liệu (đọc JSON trong `bench/results_v01/2026-09-22/`, 11 model × 3 tác vụ, n = 300, một seed)

- **Ô nổi bật khớp JSON.** Qwen3-8B trên BANKING77-20: tỷ lệ đổi đáp án khi đảo thứ tự 0,230 → 0,073; accuracy 0,747 → 0,803; ECE 0,240 → 0,184; tỷ lệ tự quyết được ở sai ≤ 5% là 7,7% → 46,3%.
- **Nhất quán ở tác vụ 20 lựa chọn.** Trên cả 22 ô (11 model × banking20/newsgroups), `L0` giảm tỷ lệ đổi đáp án và tăng accuracy. Model nhỏ hưởng nhiều nhất: SmolLM2-1.7B trên newsgroups tăng 0,257 → 0,637.
- **Không đồng đều ở "tự quyết được ≤ 5%".** Đây chính là dòng README gọi là quan trọng nhất:
  - Ở tác vụ nhị phân `injection`, chỉ số này **sụp**: Qwen3-8B 0,313 → 0,013; Qwen3-4B 0,117 → 0,020.
  - Qwen3-32B giảm cả accuracy (0,857 → 0,827) lẫn coverage ở `injection`, và giảm coverage ở newsgroups (0,557 → 0,470).
  - `docs/limitations.md` tự thừa nhận: coverage ở n = 300 có phương sai cao, và prior theo batch làm giảm accuracy khi một nhãn áp đảo.
- **Bảng xếp hạng Decision Index 0.3.** Đây là Space cộng đồng `multimodalart/jev-decision-index` trên Hugging Face, không phải của TypeSafe.
  - Điểm 60,22 được người duy trì bảng chạy lại: phần private và độ trễ 98/260/1.080 ms, khớp 98,18% số quyết định.
  - "Hạng 5/149" là **hạng theo nhóm hoà** (cách nhau ≤ 0,9 điểm) tại 12/10. Ở snapshot 15/10, xếp theo điểm thì là **10/168** (`rank_v` = 10, `rank_tie` = 5). Đứng trên nó có Jev 1.14 (61,53); đầu bảng 66,26.
  - Cấu hình nộp bảng là 2 phép xoay, Gemma-4-31B FP8, khác mặc định thư viện.
- **Tacit** (JevBench public 0,823 → 0,887 khi bật adaptive cho Tacit-9B) là số tự báo cáo. JevBench là dự án cá nhân của `fstandhartinger`, MIT, độc lập với TypeSafe.
- **Chưa tự chạy được.** Lệnh cài và chạy test của repo bị bộ phân loại quyền chặn vì là mã bên ngoài. Các con số trên đọc từ JSON, không chạy lại.

### 2c.4 Ai làm, độ tin cậy

- Org GitHub "Nokia Applied Research" có 7 repo public, không huy hiệu verified, không thành viên công khai. arXiv 2610.00831 (30/9/2026, tự ghi "early report") ghi đơn vị "Nokia, Sunnyvale, CA" cho 7/9 tác giả. Không tìm được trang nokia.com nào nhắc nhóm này, nên **(chưa xác minh)** là nhóm chính thức của Nokia.
- Commit đầu 21/9/2026; 56 commit; 7 người đóng góp. Tác giả chính Jiamu "Morris" Zhang dùng email rice.edu/case.edu. Backend SGLang và llama.cpp do người ngoài đóng góp.
- Phiên bản: PyPI 0.0.1 (21/9) → 0.3.0 (6/10/2026). Classifier "Development Status :: 2 - Pre-Alpha". ~1,3k★ (shields 16/10/2026).
- Bài báo bên ngoài chủ yếu là MarkTechPost (23/9/2026) và các trang tổng hợp chép README. Không thấy thảo luận Hacker News, phản biện hay tái hiện độc lập.

### 2c.5 Khi nào dùng, lưu ý khi đưa vào sản phẩm

- **Hợp:** định tuyến ticket hoặc intent, gắn nhãn, phát hiện prompt injection bằng model mở tự host. Cần xác suất để đặt ngưỡng "tự quyết / chuyển người", và không có nhãn để huấn luyện bộ phân loại.
- **Không hợp:**
  - API đóng không trả log-prob đầy đủ, như Claude. Khi đó dùng structured output (§2b) và eval riêng.
  - Bài toán có > 26 lựa chọn: `Decider` dừng ở 26.
  - Bài toán đã có đủ nhãn: một bộ phân loại tinh chỉnh thường rẻ hơn K lượt prefill.
- **Lưu ý vận hành:**
  1. **Prior batch là trạng thái theo tiến trình.** Phân phối của một câu hỏi phụ thuộc nhẹ vào các request trước, nên kết quả không tái lập hoàn toàn. Với hệ đa tenant, nên tách `Decider` theo tenant hoặc dùng `prior="content_free"`/`"none"`.
  2. **vLLM** phải chạy với `--logprobs-mode processed_logprobs`. Nếu không, nhãn nằm ngoài top log-prob sẽ ném `LabelTokenError`; trước bản sửa #13 nó bị đọc thành -30 một cách im lặng.
  3. **Gateway không có xác thực.** Không bind ra ngoài 127.0.0.1 nếu chưa có proxy xác thực đứng trước.
  4. Một quyết định leo lên `cot` tốn **vài giây**: cap giới hạn số quyết định leo, không giới hạn thời gian của từng quyết định.
  5. Hãy tự đo lại coverage trên dữ liệu của mình (xem 2c.3) trước khi tin vào ngưỡng "tự quyết".

**Nguồn §2c:** https://github.com/nokia-applied-research/AnyJev (clone 16/10/2026; đọc README.md, AGENTS.md, CREDITS.md, ROADMAP.md, CHANGELOG.md, docs/levels.md, docs/limitations.md, anyjev/calibrate/{permute,contextual}.py, anyjev/serve.py, pyproject.toml, bench/results_v01/2026-09-22/*.json, bench/results_decision_index/2026-10-12/*.json, examples/decision_index/README.md) · https://pypi.org/pypi/anyjev/json · https://arxiv.org/abs/2610.00831 · https://huggingface.co/spaces/multimodalart/jev-decision-index (data/v03.json, data/methodology.json, snapshot 15/10/2026) · https://huggingface.co/morriszjm/AnyJev-L0-Gemma-4-31B · https://huggingface.co/morriszjm/Tacit-9B · https://github.com/fstandhartinger/jevbench · https://www.theregister.com/a/5296711 · https://www.marktechpost.com/2026/09/23/nokia-open-sources-anyjev-a-training-free-layer-that-turns-any-open-llm-into-a-calibrated-decision-model/ (chỉ đọc tiêu đề, trang trả 403) · https://arxiv.org/abs/2309.03882 · https://arxiv.org/abs/2309.17249 · https://arxiv.org/abs/2102.09690

## 3. Bộ sưu tập system prompt (học cách các sản phẩm lớn thiết kế)

| Repo | Nội dung | Ghi chú |
|---|---|---|
| `x1xhlol/system-prompts-and-models-of-ai-tools` | System prompt của Cursor, Devin, v0, Manus, Claude Code, Windsurf… | Rất nhiều sao; nguồn "rò rỉ", dùng để học cấu trúc, không sao chép |
| `anthropics/claude-cookbooks` (tên cũ anthropic-cookbook, URL cũ chuyển hướng), Claude system prompt công khai (docs) | Anthropic công bố system prompt của Claude.ai theo phiên bản | Chính thức |
| `elder-plinius/CL4R1T4S` | Prompt nhiều sản phẩm | Nguồn không chính thức |

## 4. Nguyên tắc rút ra (2026)

1. **Context engineering > prompt engineering**: cấu trúc ngữ cảnh, tool, memory quan trọng hơn câu chữ (mục 03).
2. Prompt là **code**: version hóa, test bằng eval (Promptfoo/DeepEval), tối ưu bằng DSPy/GEPA thay vì chỉnh tay.
3. Với agent: nêu rõ vai trò, công cụ, tiêu chí dừng, định dạng output; đặt dữ liệu không tin cậy vào thẻ riêng (mục 12).
4. Few-shot + XML tags + "think step by step"/extended thinking vẫn hiệu quả; tránh prompt quá dài làm loãng cache.

## 4b. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại sao, license, ngày push của **13 repo** mục 17 trong catalog (GitHub search API, 31/10/2026). (2) Tìm repo lớn còn thiếu: truy vấn "prompt engineering", "system prompts", "prompt optimization", `topic:prompt-management`, `topic:prompt-engineering`, và "prompt" tạo sau 1/10/2025, lọc theo `data/projects.json`. Bỏ qua kho prompt ảnh/video và repo "jailbreak". Chọn **7 repo**, clone `--filter=blob:none`, đọc LICENSE, manifest, cấu trúc, CI, file Docker/cấu hình, grep mạng và telemetry. **Không chạy script nào của các repo.**

### 4b.1 Repo cũ: điều đã đổi

| Repo | Thay đổi (→ 31/10/2026) | Hệ quả |
|---|---|---|
| `f/awesome-chatgpt-prompts` | **Đổi tên thành `f/prompts.chat`**, 175,4k★. Nay là app Next.js (Prisma, Sentry) kèm `prompts.csv` 180k dòng. LICENSE ghi **hai license**: code MIT, nội dung prompt CC0, nên GitHub báo `NOASSERTION` | Catalog nên đổi `repo` và ghi "MIT (code) + CC0 (prompt)" |
| `x1xhlol/system-prompts-and-models-of-ai-tools` | Catalog `null`; nay **144,4k★**, GitHub nhận **GPL-3.0**, push 12/10 | Bổ sung số và license; GPL áp lên phần biên soạn, không làm prompt của hãng thành mã mở |
| `dair-ai/Prompt-Engineering-Guide` | Push cuối **11/3/2026** (gần 8 tháng); 79,7k★ | Nội dung web promptingguide.ai có thể vẫn cập nhật **(chưa xác minh)**; repo coi như tĩnh |
| `zou-group/textgrad` | Catalog `null`; nay 3,8k★ MIT, **push cuối 25/7/2025** (hơn 15 tháng) | Ngừng phát triển; dùng GEPA hoặc DSPy (dưới) |
| `guidance-ai/guidance` | Push cuối 21/5/2026 | Như §2b đã ghi: chậm lại |
| `stanfordnlp/dspy`, `567-labs/instructor`, `BoundaryML/baml`, cookbook Anthropic/OpenAI | Dao động dưới 5%, đều push trong tháng 10 | Không đổi |

### 4b.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `anthropics/prompt-eng-interactive-tutorial` | Khoá học chính chủ | 39k · **không có LICENSE** | 7/4/2024 (`master`) | 9 chương + 3 phụ lục dạng notebook, bản 1P và Bedrock | Model 2024, 9 commit |
| `linshenkx/prompt-optimizer` | Công cụ tối ưu prompt | 40,1k · **AGPL-3.0-only** (từ 30/10/2025) | 30/10/2026 | Web, desktop, extension Chrome, Docker, MCP; v2.13.0 | **Docker lộ API key**, `/mcp` không xác thực |
| `gepa-ai/gepa` | Tối ưu prompt bằng phản tư | 7,2k · MIT | 31/10/2026 | Thư viện Python tiến hoá prompt theo Pareto; là optimizer GEPA trong DSPy | Số liệu marketing lấy từ blog |
| `danielmiessler/Fabric` | Thư viện prompt + CLI | 44,5k · MIT | 29/10/2026 | 265 "pattern" (`system.md`) + CLI Go với ~15 nhà cung cấp | Không có eval cho pattern |
| `asgeirtj/system_prompts_leaks` | System prompt rò rỉ | 70,5k · CC0 | 31/10/2026 | 1.856 file, 649 của Anthropic, cập nhật hằng ngày | Bản quyền văn bản thuộc hãng |
| `elder-plinius/CL4R1T4S` | System prompt rò rỉ | 51,7k · AGPL-3.0 | 22/9/2026 | 80 file, 26 hãng/sản phẩm, một người duy trì | Đã nhắc ở §3, chưa có hồ sơ |
| `Piebald-AI/claude-code-system-prompts` | Prompt Claude Code theo phiên bản | 13k · MIT | 30/10/2026 | 1.057 file prompt/tool/agent của Claude Code v2.1.316, đếm token bằng API | Quảng cáo sản phẩm Piebald |

### 4b.3 Hồ sơ ngắn

- **Anthropic Prompt Engineering Interactive Tutorial.** Khoá nền tảng tốt nhất để học cấu trúc prompt (vai trò, tách dữ liệu bằng thẻ XML, prefill, few-shot, chống bịa, chuỗi prompt, tool use). Nhưng nhánh `master` chỉ có **9 commit, dừng 7/4/2024**; "push 28/8/2026" là nhánh vá `awscli`. Notebook gọi `claude-3-haiku-20240307`; kiểm model đó còn được phục vụ trước khi chạy **(chưa xác minh)**. Repo **không có file LICENSE** nên mặc định giữ mọi quyền: học và tham khảo được, không chép vào sản phẩm. Kỹ thuật vẫn đúng; tài liệu mới hơn ở docs.claude.com và `anthropics/courses`.
- **prompt-optimizer (linshenkx).** 1.039 commit, 881 của tác giả chính; monorepo pnpm 6 gói (core, ui, web, desktop, extension, mcp-server), CI chạy `test:gate` và Playwright e2e. Đổi license **MIT → AGPL-3.0-only ngày 30/10/2025**; file LICENSE có đoạn đầu riêng nên GitHub báo `NOASSERTION`. Kiểm lời quảng cáo: ✅ bản web và desktop gọi thẳng nhà cung cấp AI. ❌ Bản Docker thì khác: `docker/generate-config.sh` **ghi mọi biến `VITE_*` (gồm API key) vào `config.js` phục vụ cho trình duyệt** và in chúng ra log container. `nginx.conf` đặt **`auth_basic off` cho `/mcp`** ngay cả khi có `ACCESS_PASSWORD`, trong khi MCP server dùng chính các key đó. `docker-compose.yml` mặc định `ACCESS_PASSWORD=123456`. Nếu dùng: chạy bản desktop/extension, hoặc Docker chỉ trên `127.0.0.1`, không đặt key qua env.
- **GEPA.** Thư viện của nhóm tác giả bài *GEPA: Reflective Prompt Evolution* (arXiv 2507.19457), 937 commit, 72 tác giả, **32% commit có trailer Claude**. `pyproject.toml` có **`dependencies = []`**: gói lõi không kéo phụ thuộc, `litellm`, `mlflow`, `wandb` nằm ở extra `full` và loại trừ có ghi chú từng bản `litellm` lỗi wheel. Có 71 file test, workflow `dspy_contract.yml` và `dspy_compatibility.yml` kiểm GEPA vẫn khớp với `dspy.GEPA`. ⚠️ Bảng "35x faster than RL" trong README: paper nói **ít lượt rollout hơn tới 35 lần**, không phải nhanh hơn theo thời gian; các số "32% → 89%", "55% → 82%" dẫn tới blog, không có dữ liệu tái lập trong repo. Cài: `pip install gepa` (hoặc dùng qua `dspy.GEPA`).
- **Fabric (Daniel Miessler).** 4.500 commit, 311 tác giả; người commit nhiều nhất là Kayvan Sylvan (1.403), không phải tác giả gốc. CLI Go (`go 1.26`), plugin cho Anthropic, OpenAI, Gemini, Bedrock, Ollama, LM Studio, Claude Code, Codex… Mỗi pattern là `system.md` (+ `user.md`) kiểu "IDENTITY and PURPOSE / OUTPUT INSTRUCTIONS"; **41/265 pattern còn câu "Take a deep breath and think step by step"** (mẹo 2023). Không có eval cho pattern, CI chỉ test code Go. ⚠️ LICENSE MIT ghi "Copyright (c) 2012-2024 Scott Chacon and others", có vẻ chép từ dự án khác khi thêm file 29/8/2024. Không thấy telemetry. Cài: `brew install fabric-ai` hoặc `winget install danielmiessler.Fabric`; README còn đưa `curl … | bash`.
- **system_prompts_leaks (Ásgeir Thor Johnson).** 897 commit, 300 từ 1/7/2026, cập nhật trong ngày khi Claude Code ra bản (commit 31/10 ghi v2.1.316). 649/1.856 file thuộc thư mục Anthropic (Claude.ai, Claude Code, Cowork, Claude Design, Artifact types…). README hứa "full verbatim… carefully curated" nhưng **không mô tả cách trích xuất hay kiểm chứng**. Đầu README là quảng cáo Latitude qua link rút gọn `workers.dev`. License CC0 chỉ áp cho phần người biên soạn đóng góp; văn bản prompt vẫn thuộc các hãng.
- **CL4R1T4S (Pliny).** 206 commit, một tác giả, 80 file. Mục đích tự nêu là "minh bạch AI"; phần đóng góp kêu gọi "Leak, extract, or reverse-engineer". AGPL-3.0 trên văn bản không phải của tác giả có hiệu lực pháp lý không rõ. Dùng như nguồn so sánh, không phải nguồn chuẩn.
- **claude-code-system-prompts (Piebald).** Tách prompt Claude Code thành 1.057 file (393 system, 283 tool, 204 data, 103 agent, 74 skill), mỗi bản phát hành một commit "vX (+N tokens)". `tools/updatePrompts.js` đếm token bằng API `count_tokens` của Anthropic và lấy ngày phát hành từ npm, nên số token là đo thật ✅. ⚠️ README ghi "350 → 515 prompt", còn repo có 1.057 file: cách đếm khác nhau, chưa rõ. Hữu ích để **so sánh diff prompt giữa các phiên bản** khi viết harness; cùng rủi ro bản quyền như baoyu-design (mục 06 §7p.5).

**Về ba kho prompt rò rỉ:** kho này chỉ ghi nhận để học cấu trúc (thứ tự phần, cách mô tả tool, quy tắc an toàn), **không trích nội dung**. Với prompt của Anthropic, nguồn chính thức là trang system prompt công khai trong docs (§3).

### 4b.4 Mẫu chung rút ra

1. **Prompt "đã tối ưu" cần eval, không cần thêm mẹo**: GEPA có test, contract với DSPy và benchmark trong paper; Fabric có 265 pattern nhưng không có eval nào. Quy tắc §4 mục 2 ("prompt là code, test bằng eval") vẫn đúng và là chỗ phân biệt.
2. **Lời "chạy hoàn toàn phía client" chỉ đúng cho bản nào đó**: prompt-optimizer đúng ở bản desktop, sai ở bản Docker (key vào `config.js`, `/mcp` mở). Kiểm từng hình thức triển khai.
3. **License nhảy giữa các bản**: prompt-optimizer MIT → AGPL; prompts.chat tách MIT/CC0; tutorial Anthropic không có LICENSE. Ghi license theo ngày đọc.
4. **Prompt rò rỉ đã thành nguồn cập nhật theo giờ** (system_prompts_leaks, Piebald). Hữu ích để theo dõi thay đổi harness, nhưng không có quy trình kiểm chứng và quyền sở hữu không rõ.
5. **Repo chính chủ cũng có thể bị bỏ lại**: tutorial của Anthropic 39k★ nhưng dừng từ 4/2024. Sao không phải thước đo độ mới.

**Nguồn §4b:** GitHub search API 31/10/2026 (`repo:` cho 13 repo cũ và 7 repo mới; 6 truy vấn chủ đề) · `meta_all.json`/`status_all.json` đợt rà 31/10 · clone `--filter=blob:none` 8 repo, đọc: f/prompts.chat (LICENSE, cây gốc, prompts.csv), anthropics/prompt-eng-interactive-tutorial (README.md, cây `Anthropic 1P/`, `AmazonBedrock/`, nhánh), linshenkx/prompt-optimizer (LICENSE và lịch sử, README.md, docker/{docker-compose.yml, nginx.conf, generate-config.sh, generate-auth.sh}, middleware.js, packages/mcp-server/{README.md, src/config/environment.ts}, .github/workflows/test.yml), gepa-ai/gepa (LICENSE, pyproject.toml, README.md, .github/workflows/, tests/), danielmiessler/Fabric (LICENSE và lịch sử, README.md, go.mod, internal/plugins/ai/, data/patterns/*/system.md, .github/workflows/patterns.yaml), asgeirtj/system_prompts_leaks (LICENSE, README.md, cây thư mục), elder-plinius/CL4R1T4S (LICENSE, README.md), Piebald-AI/claude-code-system-prompts (LICENSE, README.md, tools/updatePrompts.js, cây system-prompts/) · https://arxiv.org/abs/2507.19457

## 4c. Nâng trần 2/11/2026: định dạng prompt có spec, công cụ so sánh, red-team và tối ưu có cổng validation (yêu cầu người dùng)

> Tìm repo **chưa có trong catalog** ở ba lớp: chuẩn, cổng máy, đầu bảng. GitHub search API 2/11/2026 (`repo:` và truy vấn "red teaming llm", "prompt testing", "prompt injection benchmark"); clone `--depth 1 --filter=blob:none`, đọc LICENSE, README, `pyproject`/`package.json`, module telemetry. **Không cài, không chạy.**

**Trần hiện tại:**

- Mục có hướng dẫn (§1), optimizer (DSPy, GEPA ở §2, §4b), structured output (§2b) và kho system prompt (§3, §4b). Nguyên tắc §4 mục 2 "prompt là code, test bằng eval" có, nhưng công cụ eval/red-team nằm ở mục 07 và 12 (promptfoo, garak, PyRIT), mục này chưa có.
- Prompt chưa có **định dạng file chuẩn**: mỗi dự án tự đặt chuỗi trong code, nên không lint, không diff, không chạy lại được giữa các runtime.
- Chưa có benchmark prompt injection để đo phòng thủ của prompt, và optimizer ở §4b chưa nói gì về **cổng validation giữ lại** (held-out) khi chấp nhận thay đổi.

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `microsoft/prompty` | Chuẩn (định dạng file) | 1,3k · MIT | 21/10/2026 | `.prompty` = Markdown + frontmatter (model, connection, template); v2 có spec (`spec/spec.md`, TypeSpec trong `schema/`) và **conformance vectors** dùng chung cho runtime Python, TypeScript, Rust, C#; extension VS Code chạy bằng F5; có OpenTelemetry | Đổi lớn từ v1 lên v2; runtime Go/Java/Swift còn dở **(chưa xác minh)** |
| `google/dotprompt` | Chuẩn (định dạng file) | 573 · Apache-2.0 | 5/10/2026 | Định dạng prompt thực thi được dựa trên Handlebars, dùng trong Firebase Genkit; spec viết thành YAML test (`spec/*.yaml`) chạy chung cho JS, Python, Go, Rust, Java, Dart; có OpenSSF Scorecard | Ít sao; gắn với hệ Genkit |
| `ianarawjo/ChainForge` | Đầu bảng (so sánh prompt) | 3,0k · MIT | 29/10/2026 | Môi trường dạng luồng để so prompt × model × tham số, node đánh giá (Python, so ground truth), vẽ kết quả; kèm 188 flow chuyển từ OpenAI evals | Hợp khám phá hơn CI; bản web giới hạn tính năng |
| `confident-ai/deepteam` | Cổng máy (red-team) | 3,1k · Apache-2.0 | 23/10/2026 | 50+ lỗ hổng (PII, prompt leakage, BOLA, SSRF, tool metadata poisoning…) và nhiều kiểu tấn công, chấm bằng LLM judge chạy cục bộ; có guardrails | ❌ **Telemetry bật mặc định**: `deepteam/telemetry.py` lấy IP công khai qua `api.ipify.org` rồi gửi kèm span tới New Relic, cùng PostHog và Sentry (key viết cứng). Tắt bằng `DEEPTEAM_TELEMETRY_OPT_OUT=YES`; không đọc `DO_NOT_TRACK` |
| `liu00222/Open-Prompt-Injection` | Cổng máy (benchmark) | 510 · MIT | 27/9/2026 | Bộ công cụ học thuật (slide của tác giả đặt ở duke.edu) chuẩn hoá tấn công/phòng thủ prompt injection, đo ASV; có detector DataSentinel và PromptLocate | Checkpoint tải từ Google Drive, không ghim băm; ví dụ dùng PaLM2 cũ |
| `microsoft/SkillOpt` | Đầu bảng (optimizer) | 18,8k · MIT | 29/10/2026 | Coi tài liệu skill/prompt là tham số để huấn luyện: sửa add/delete/replace có giới hạn, **chỉ nhận sửa khi điểm validation held-out tăng**; sản phẩm là `best_skill.md` 300–2.000 token, không thêm lượt gọi lúc chạy | Số "tốt nhất 52/52 ô" là tự công bố (paper arXiv 2605.23904) **(chưa xác minh)**; `SkillOpt-Sleep` đọc transcript Claude Code/Codex/Cursor của người dùng |

**Stack nâng trần** (lợi ích/công sức giảm dần):

1. Đưa prompt ra file có spec: `.prompty` (đa runtime, hệ Microsoft) hoặc `.prompt` của dotprompt (hệ Genkit). File riêng thì diff, review và chạy eval được như code (§4 mục 2).
2. Eval hồi quy bằng promptfoo (mục 07) trên chính các file đó; ChainForge để khám phá nhanh trước khi chốt test case.
3. Red-team trước khi phát hành: deepteam hoặc garak/PyRIT (mục 12), luôn đặt `DEEPTEAM_TELEMETRY_OPT_OUT=YES`; đo phòng thủ injection bằng Open-Prompt-Injection.
4. Tối ưu: DSPy/GEPA (§2, §4b) cho pipeline, SkillOpt cho prompt/skill dạng tài liệu. Với mọi optimizer, giữ quy tắc của SkillOpt: **tách tập validation, chỉ nhận thay đổi làm điểm tăng**.
5. Quản lý phiên bản prompt (Langfuse, LangSmith ở §2) lưu cùng điểm eval, không chỉ lưu văn bản.

**Nguồn §4c:** GitHub search API 2/11/2026 · clone `--depth 1 --filter=blob:none` 2/11/2026: microsoft/prompty (LICENSE, README.md, `spec/`, `schema/model/conformance/`, `runtime/`), google/dotprompt (LICENSE, README.md, `spec/`), ianarawjo/ChainForge (LICENSE.md, README.md), confident-ai/deepteam (LICENSE.md, README.md, `deepteam/telemetry.py`), liu00222/Open-Prompt-Injection (LICENSE, README.md), microsoft/SkillOpt (LICENSE, README.md, pyproject.toml, `docs/sleep/README.md`, grep telemetry) · https://github.com/microsoft/prompty · https://github.com/google/dotprompt · https://chainforge.ai · https://www.trydeepteam.com · https://github.com/liu00222/Open-Prompt-Injection · https://arxiv.org/abs/2605.23904

<a id="core-prompt-optimization"></a>

## 4d. Nâng trần 2/11/2026: optimizer có holdout thật và ngân sách kiểm chứng (mở rộng cùng ngày)

> Mở rộng chiều sâu trong cùng đợt 2/11/2026, không phải công bố các repo vừa ra mắt. Hai repo dưới đã có trong catalog: đọc lại LICENSE, CI và nhánh mặc định bằng clone chỉ đọc; SHA đối chiếu GitHub API. Mức bằng chứng **code-read**; không chạy/build repo ngoài, hiệu năng và hành vi thực tế **(chưa xác minh)**. Số sao/trạng thái đọc 2026-11-02; ngày commit tính theo UTC, tách khỏi `pushed_at`.

| Repo đã có | ★ · license (2026-11-02) | HEAD nhánh mặc định | Vai trò đọc sâu |
|---|---|---|---|
| `stanfordnlp/dspy` | 38.885 · MIT | 2026-10-29 · `25162c4f` | Lập trình prompt và adapter GEPA có budget |
| `gepa-ai/gepa` | 7.245 · MIT | 2026-10-31 · `8c7b697a` | Reflective search. Pareto validation và giới hạn đo |

**Trần còn thiếu:** §4c khuyên “validation held-out”, nhưng thư viện không luôn ép tách tập. Mục này thêm đường đọc từ **API optimizer → tập dùng chọn ứng viên → ngân sách → phép chấm cuối**, để một điểm validation tăng không bị hiểu nhầm thành model tổng quát tốt hơn.

### DSPy: chữ ký có kiểu không thay metric và dữ liệu tách biệt

- [`dspy.GEPA`](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/dspy/teleprompt/gepa/gepa.py#L377) buộc chọn đúng một trong `auto`, `max_full_evals`, `max_metric_calls`; trace/feedback giúp optimizer đề xuất sửa prompt. Chi phí search gồm model đích, model reflection và grader, nên số metric call không tự quy đổi thành một trần USD.
- Adapter ở SHA đọc này ghi **`max_reflection_cost` chưa hỗ trợ** và từ chối tham số đó vì DSPy LM thiếu giao diện tổng cost GEPA cần. Không chép một cấu hình GEPA standalone sang DSPy rồi tin đã có cùng cap. Đặt trần metric + timeout/quota ngoài và đối soát token/cost thực.
- [`MIPROv2.compile`](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/dspy/teleprompt/mipro_optimizer_v2.py#L113) nhận train/val, dùng validation để tìm instruction/few-shot; final test phải tách khỏi cả hai. Output có kiểu/khớp Signature chỉ là hợp đồng dữ liệu, chưa là metric chất lượng. [CI upstream](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/.github/workflows/run_tests.yml) có lint/type/test và workflow scan; đây không phải kết quả tối ưu của ứng dụng đang dùng kho.

### GEPA standalone: `valset=None` tái dùng trainset

- [`optimize()`](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/src/gepa/api.py#L153) nói rõ nếu không truyền `valset` thì dùng lại trainset; mã tạo `val_loader=train_loader`. Tên “validation” trong kết quả vì thế **không bảo đảm dữ liệu held-out**. Người tích hợp phải chia tập theo nguồn/episode và truyền valset khác thật.
- [`GEPAEngine`](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/src/gepa/core/engine.py#L116) dùng namespace cache riêng khi val loader khác train loader; đây là bảo vệ cache index, không phát hiện hai bộ có nội dung trùng/near-duplicate. Tập validation vẫn tham gia chọn ứng viên/Pareto, nên cần một final test chưa dùng chọn prompt.
- API có metric/stop callback và resume `run_dir`; nếu thay dữ liệu, metric hay model mà tái dùng run state cũ, điểm cũ không tự trở thành thí nghiệm hợp lệ. Paper GEPA cung cấp bằng chứng trong điều kiện tác giả đo; không suy ra sẽ hơn RL/prompt tay trên mọi task. [CI](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/.github/workflows/run_tests.yml) kiểm thư viện, **(chưa xác minh)** benchmark cho miền của người tích hợp.

**Ma trận chọn mức tối ưu**

| Bài toán | Bắt đầu bằng | Cổng nhận thay đổi |
|---|---|---|
| Ít dữ liệu, chưa có metric tin cậy | Prompt thủ công + ChainForge/Promptfoo §4c | Assertion và nhãn người trước khi tăng search |
| Pipeline nhiều module, cần kiểu và few-shot | DSPy/MIPROv2 | Validation tách theo nguồn + final test độc lập |
| Có trajectory/feedback giàu thông tin | DSPy GEPA hoặc GEPA adapter | Budget toàn search; không chọn bằng chính final test |
| Chỉ sửa tài liệu skill/prompt | SkillOpt §4c hoặc GEPA adapter phù hợp | Eval trigger/quality và safety regression |
| Cần cam kết $ cứng | Optimizer + gateway/quota/time cap | Đối soát reflection/grader/model, không chỉ metric-call count |

**Cách ghép:** xác định metric và negative control bằng mục 07; chia train/validation/final test trước search, kiểm dedup; ghi seed/model/prompt version và toàn bộ budget; chọn **một** optimizer để có baseline; đánh giá ứng viên thắng một lần trên final test kèm safety/structured-output regression; lưu prompt tối ưu cùng cấu hình và điểm đo (Prompty/Dotprompt §4c). Khi đổi dữ liệu/metric, tạo run/version mới. Chỉ chuyển sang fine-tuning khi lỗi còn lại có bằng chứng do năng lực model thay vì retrieval/tool/prompt, đối chiếu mục model adaptation khi chọn hướng đó.

**Nguồn phần mở rộng:** [1](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/LICENSE) · [2](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/dspy/teleprompt/gepa/gepa.py) · [3](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/dspy/teleprompt/mipro_optimizer_v2.py) · [4](https://github.com/stanfordnlp/dspy/blob/25162c4fc05c2d2d019b0ffb5b6b2a9f315ec007/.github/workflows/run_tests.yml) · [5](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/LICENSE) · [6](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/src/gepa/api.py) · [7](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/src/gepa/core/engine.py) · [8](https://github.com/gepa-ai/gepa/blob/8c7b697a71977980afc7537dac0881e784eef99f/.github/workflows/run_tests.yml) · [9](https://arxiv.org/abs/2507.19457) · [10](https://openreview.net/pdf?id=RQm2KQTM5r)

## 4e. Kiểm khung RCCOF của Danh Nolan (Role, Context, Constraint, Output format, Few-shot): “đặc tả mở” có DOI nhưng không có dữ liệu đo (link người dùng gửi, 3/11/2026)

> Người dùng gửi https://danhnolan.com/en/rccof. Đã đọc trang tiếng Anh, bản ghi Zenodo 10.5281/zenodo.22856974 qua API, PDF đính kèm (`RCCOF_Framework_Specification_v1.0-v3.pdf`, 7.519 byte, 2 trang) và bản ghi liên quan 10.5281/zenodo.22843346. Đối chiếu với docs prompt chính thức của Anthropic (platform.claude.com, "Prompting best practices", đọc 3/11/2026).

### 4e.1 Nó là gì

| Thuộc tính | Giá trị |
|---|---|
| Tác giả | Danh Nolan (Văn Hùng Danh), danhnolan.com, ORCID 0009-0007-7906-5091. Trang có Zalo và số điện thoại để liên hệ học "master program" có phí (không ghi giá) |
| Ngày, phiên bản | v1.0, đăng Zenodo 20/9/2026 (loại **Report**, tác giả tự nộp, không qua bình duyệt); trang web cập nhật 24/9/2026. Zenodo ghi 58 lượt xem, 14 lượt tải (3/11/2026) |
| Nội dung | Prompt gồm 5 lớp: **R**ole (vai trò chuyên môn), **C**ontext (persona, search intent, "emotional trigger", dữ kiện đã kiểm), **C**onstraint (giới hạn độ dài, cấm từ sáo, "không bịa ngoài dữ kiện"), **O**utput format (ví dụ H2 + đoạn trả lời trước 40–60 từ + 3 gạch đầu dòng + CTA), **F**ew-shot (1–2 đoạn mẫu). Ba quy tắc: đặt [TASK] cuối prompt; mọi số liệu phải nằm trong Context; bắt phân tích phản đối của người dùng trước khi viết. "Quy tắc 70/30": 70% giá trị đến từ con người |
| License | **Tự mâu thuẫn trên trang**: mục quyền ghi "All rights reserved" với văn bản gốc, còn FAQ và Zenodo ghi **CC BY 4.0** |
| Hệ sinh thái | Cùng tác giả còn DLN, WGS, SQA-200, SEO Master, EP-9, 4-ZIA, E-PROVE, PIOC, SIUM-1, MME-GA4; bản ghi Zenodo liên quan là "Decision Ladder Navigation™ (DLN)" (technical note, 19/9/2026) |

### 4e.2 Kiểm nhận định

| Nhận định | Kết quả | Căn cứ |
|---|---|---|
| "eliminates over 95% of factual hallucinations in enterprise generation benchmarks" (trang web) | ❌ không có nguồn | PDF trên Zenodo không có benchmark, bộ dữ liệu, model, phương pháp đo hay con số 95%. Trang web không nêu tên benchmark. PDF còn tự ghi "guarantees 100% Brand Voice alignment" và "Replicates 100% authentic Brand Voice DNA" mà không có bằng chứng |
| Biên tập giảm từ 45–90 phút xuống 5–10 phút mỗi bài | ❌ không có nguồn | Không có dữ liệu đi kèm |
| "Deterministic" control architecture | ⚠️ sai khái niệm | Prompt không làm đầu ra của LLM thành tất định; chỉ thu hẹp phân phối. Muốn chắc chắn về định dạng thì dùng structured output hoặc schema (mục 17 §2b) và cổng kiểm sau sinh |
| "A prohibition contracts the space of acceptable outputs where a recommendation only expands it" (lệnh cấm hiệu quả hơn khuyến nghị) | ⚠️ ngược với docs của nhà cung cấp | Anthropic khuyên "**Tell Claude what to do instead of what not to do**" và xếp "NEVER use ellipses" là cách kém hiệu quả hơn so với giải thích lý do. Danh sách từ cấm vẫn có ích, nhưng kiểm bằng linter sau sinh chắc hơn là chỉ cấm trong prompt (mục 18 §5d, mục 06 §7i) |
| Rule 1: đặt task ở đầu khiến model "bắt đầu sinh trước khi đọc Constraints phía sau" | ⚠️ đúng khuyến nghị, sai cơ chế | Model đọc toàn bộ prompt trước khi sinh token đầu tiên. Khuyến nghị đặt câu hỏi ở cuối có căn cứ khác: Anthropic ghi "Queries at the end can improve response quality by up to 30 percent in tests", chủ yếu với tài liệu dài, nhiều nguồn |
| Rule 2: mọi số liệu phải được cung cấp, "do not infer or fabricate" | ✅ hợp lý | Đây là grounding cơ bản. Tuy vậy cấm trong prompt không đảm bảo; cần kiểm đối chiếu dữ kiện sau sinh |
| Few-shot 1–2 đoạn mẫu | ✅ nhưng ít | Anthropic khuyên **3–5 ví dụ**, đa dạng, bọc trong thẻ `<example>` để không bị chép nguyên mẫu |
| Tính mới | ⚠️ | Năm thành phần đều đã có trong hướng dẫn chính thức (vai trò, ngữ cảnh, định dạng, ví dụ) và trong các khung viết tắt phổ biến có trước như CO-STAR, RISEN, CRISPE (kho chưa có hồ sơ riêng cho các khung này). Điểm riêng là áp vào nội dung marketing và AEO |

### 4e.3 Dùng thế nào

- Dùng như một **checklist nhớ** khi viết prompt nội dung: có vai trò, dữ kiện, ràng buộc, định dạng và ví dụ chưa. Không coi đây là "đặc tả" hay "tiêu chuẩn": nó không có bộ kiểm, phiên bản máy đọc hay dữ liệu đo.
- Thay câu cấm bằng mô tả điều muốn có kèm lý do; giữ danh sách từ cấm nhưng chặn bằng linter (design-os-vietnamese, antislop).
- Đo thật trước khi tin con số: cùng bộ đề bài, có và không dùng khung, chấm hallucination bằng đối chiếu dữ kiện (mục 07 cho công cụ eval).
- Một DOI Zenodo chỉ cho biết tài liệu đã được lưu trữ và trích dẫn được; nó **không** có nghĩa là đã được bình duyệt hay kiểm chứng.

**Nguồn §4e:** https://danhnolan.com/en/rccof (đọc 3/11/2026) · https://zenodo.org/api/records/22856974 và PDF `RCCOF_Framework_Specification_v1.0-v3.pdf` · https://zenodo.org/api/records/22843346 · https://doi.org/10.5281/zenodo.22856974 · https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (mục "Add context to improve performance", "Control the format of responses", "Use examples effectively", "Long context prompting").

<a id="factory-prompt-release-2026-11-04"></a>

## 4f. Nâng trần 4/11/2026: prompt là artifact phát hành, có ranh giới tin cậy và cổng hồi quy

**Trần và khoảng trống.** §4c–§4d đã có định dạng prompt, optimizer, holdout và ngân sách. Phần còn thiếu cho xưởng là **artifact nào được deploy**, ai có quyền đổi endpoint/model, và cách trả về bản cũ khi metric sản phẩm xấu đi. Kết quả tối ưu tốt trên validation không tự cấp quyền nạp mọi file optimizer gửi sang.

### 4f.1 Đọc sâu DSPy: state JSON và chương trình pickle có quyền khác nhau

`stanfordnlp/dspy` (MIT), HEAD `c941671b1d2b6e208d472e93f954632b94000277` đọc ngày 4/11/2026. `BaseModule.save` tách lưu state (`.json`/`.pkl`) khỏi lưu toàn chương trình (`save_program=True`, cloudpickle). `BaseModule.load` mặc định `allow_pickle=False`; nhánh `.pkl` từ chối nếu chưa cho phép. Hàm top-level `dspy.load` cho chương trình cũng yêu cầu `allow_pickle=True` trước khi gọi `cloudpickle.load`. Bật cờ này là chấp nhận một nguồn có thể thực thi code, không chỉ là chọn định dạng nén. [State save/load và callsite]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/dspy/primitives/base_module.py ) · [whole-program load]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/dspy/utils/saving.py ).

Ở `Predict.load_state`, `_sanitize_lm_state` mặc định loại các khóa `api_base`, `base_url`, `model_list`; cờ `allow_unsafe_lm_state` mở đường giữ các khóa này và cho phép class LM tùy biến. Kết luận chỉ áp dụng đường state-load đã đọc, không khẳng định mọi nhánh import/plugin đều bị sandbox. Vì vậy bản prompt được review phải kèm schema, hash và cấu hình model/endpoint độc lập do môi trường kiểm soát. **JSON ít quyền thực thi hơn pickle không có nghĩa nội dung JSON đáng tin để đưa vào prompt.** [Sanitize và LM callsite]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/dspy/predict/predict.py ).

Loader so dependency versions với metadata đã lưu và **cảnh báo** khi lệch; không coi cảnh báo đó là kiểm tương thích bắt buộc. CI upstream có lint/test/build nhưng chưa chạy ở đây; khả năng round-trip artifact và chất lượng sau deploy phải kiểm trong ứng dụng đích. [CI]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/.github/workflows/run_tests.yml ) · [license]( https://github.com/stanfordnlp/dspy/blob/c941671b1d2b6e208d472e93f954632b94000277/LICENSE ).

### 4f.2 Ma trận lựa chọn và ranh giới

| Cách làm | Khi có ích | Cổng còn cần |
|---|---|---|
| Prompt thủ công, file review trong git | Tác vụ nhỏ, baseline rẻ và dễ audit | Contract đầu ra, eval hồi quy, model/config ghim; không mặc định cần optimizer |
| DSPy / GEPA (§2, §4d) | Có metric nhiệm vụ và corpus đủ để tối ưu | Train/validation/test tách đúng; artifact/source được tin; phí tính cả search/judge/retry, không chỉ lượt inference cuối |
| BAML / Outlines / Instructor (§2b) | Kiểu/schema, parsing và retry structured output | Schema pass không chứng minh tính đúng ngữ nghĩa hay quyền gọi tool; cần kiểm dữ kiện và quyền ở ứng dụng |
| Prompty / Dotprompt (§4c) | Định dạng prompt có thể review và chạy giữa runtime | Conformance với phiên bản runtime; secret/endpoint quản ở môi trường, không chép vào artifact |

### 4f.3 Luồng prompt → bản phát hành → theo dõi

1. Định nghĩa contract: input có provenance, output schema, quy tắc từ chối khi thiếu dữ liệu và metric nghiệp vụ. Tập case gồm tiếng Việt, không dấu, input nhiễu và trường hợp không nên gọi tool.
2. Ghim nguồn corpus và quyền dữ liệu; tách nhóm theo khách hàng/thời gian/tài liệu để tránh cùng nội dung rơi vào train và test. Tập tối ưu không thay tập nghiệm thu giữ kín.
3. Tối ưu có ngân sách; lưu baseline cố định cùng model, tool, retrieval và giới hạn tương đương. Không thay metric sau khi thấy kết quả rồi gọi đó là cải thiện đã xác nhận.
4. Đóng gói prompt/state + schema + model/config ID + dependency lock + bộ case/version + kết quả theo từng nhóm + hash. State JSON được kiểm schema; pickle chỉ từ nguồn đã tin và môi trường phù hợp; không lấy artifact không rõ nguồn chỉ vì `load` hỗ trợ.
5. Cổng phát hành kiểm hồi quy chất lượng, tỷ lệ lỗi parse/từ chối sai, tool call ngoài dự kiến, latency phân vị và tổng phí trên ngưỡng do sản phẩm đặt. Nêu số case thực chạy, skip, lỗi provider và bất định; không đổi lỗi API thành pass.
6. Canary và theo dõi drift ở mục 07/28; giữ bundle cũ để rollback nguyên prompt/config/retrieval phù hợp, không chỉ một chuỗi system prompt. Input thu hồi về eval phải được xử lý quyền truy cập và dữ liệu cá nhân.

**Tiêu chí chấp nhận:** có bundle định danh duy nhất, baseline và held-out report cùng schema; người/CI có thể đối chiếu artifact chạy thật với artifact đã duyệt; khi provider/model đổi có lượt kiểm mới. Đây là yêu cầu thiết kế của kho, chưa phải cam kết tính năng tự có của DSPy.

**Nguồn §4f:** permalink implementation/LICENSE/CI DSPy trên; đối chiếu cơ chế optimizer, spec và eval ở §4c–§4d. Không tuyên bố tái lập chất lượng/chi phí hay chạy model upstream trong đợt đọc này.

## 5. Nguồn

- https://github.com/dair-ai/Prompt-Engineering-Guide · https://www.star-history.com/dair-ai/prompt-engineering-guide/ · https://dev.to/web_dev-usman/10-github-repos-every-serious-prompt-writer-should-be-using-21jk
- https://github.com/stanfordnlp/dspy · https://futureagi.com/blog/what-is-dspy-2026/ · https://www.promptquorum.com/power-local-llm/dspy-review · https://github.com/ganarajpr/awesome-dspy · https://github.com/dx-corp/dspy-0to1-guide
- https://en.wikipedia.org/wiki/Fatih_Kadir_Akin
- §2b (12/10/2026): https://github.com/567-labs/instructor · https://github.com/dottxt-ai/outlines · https://github.com/guidance-ai/guidance · https://github.com/BoundaryML/baml · https://github.com/anthropics/claude-cookbooks · https://github.com/openai/openai-cookbook · https://github.com/anthropics/courses · https://github.com/anthropics/prompt-eng-interactive-tutorial · https://github.com/microsoft/promptflow · https://github.com/microsoft/promptflow/tree/main/migration-guide/PromptFlow-to-MAF · https://github.com/microsoft/LLMLingua · https://github.com/microsoft/poml · https://github.com/MadcowD/ell
