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
