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

## 5. Nguồn

- https://github.com/dair-ai/Prompt-Engineering-Guide · https://www.star-history.com/dair-ai/prompt-engineering-guide/ · https://dev.to/web_dev-usman/10-github-repos-every-serious-prompt-writer-should-be-using-21jk
- https://github.com/stanfordnlp/dspy · https://futureagi.com/blog/what-is-dspy-2026/ · https://www.promptquorum.com/power-local-llm/dspy-review · https://github.com/ganarajpr/awesome-dspy · https://github.com/dx-corp/dspy-0to1-guide
- https://en.wikipedia.org/wiki/Fatih_Kadir_Akin
- §2b (12/10/2026): https://github.com/567-labs/instructor · https://github.com/dottxt-ai/outlines · https://github.com/guidance-ai/guidance · https://github.com/BoundaryML/baml · https://github.com/anthropics/claude-cookbooks · https://github.com/openai/openai-cookbook · https://github.com/anthropics/courses · https://github.com/anthropics/prompt-eng-interactive-tutorial · https://github.com/microsoft/promptflow · https://github.com/microsoft/promptflow/tree/main/migration-guide/PromptFlow-to-MAF · https://github.com/microsoft/LLMLingua · https://github.com/microsoft/poml · https://github.com/MadcowD/ell
