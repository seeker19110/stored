# 17 · Prompt Engineering, Prompt Optimization & System Prompt Collections

## 1. Hướng dẫn & tài nguyên

| Tài nguyên | Repo / URL | ★ | Ghi chú |
|---|---|---|---|
| **Prompt Engineering Guide** (DAIR.AI) | dair-ai/Prompt-Engineering-Guide | ~78–79k (9/2026) | Nay bao phủ cả context engineering, RAG, agents; promptingguide.ai |
| **Anthropic Prompt Library & docs** | docs.anthropic.com (prompt engineering, prompt generator, Claude cookbook) | – | Kỹ thuật XML tags, few-shot, chain-of-thought, prefill |
| **OpenAI Cookbook / Prompt guide** | openai/openai-cookbook | – | |
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

## 3. Bộ sưu tập system prompt (học cách các sản phẩm lớn thiết kế)

| Repo | Nội dung | Ghi chú |
|---|---|---|
| `x1xhlol/system-prompts-and-models-of-ai-tools` | System prompt của Cursor, Devin, v0, Manus, Claude Code, Windsurf… | Rất nhiều sao; nguồn "rò rỉ", dùng để học cấu trúc, không sao chép |
| `anthropics/anthropic-cookbook`, Claude system prompt công khai (docs) | Anthropic công bố system prompt của Claude.ai theo phiên bản | Chính thức |
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
