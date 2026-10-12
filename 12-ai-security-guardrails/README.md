# 12 · AI Security, Guardrails & Agent Safety

> Rủi ro bảo mật của LLM/agent/MCP và công cụ phòng thủ. Bổ sung cho mục 09 (checklist deploy) và mục 04 (giao thức).

## 1. Khung rủi ro chuẩn (OWASP GenAI Security Project)

| Tài liệu | Mốc | Nội dung chính |
|---|---|---|
| **OWASP Top 10 for LLM Applications** (2025) | 2023 → bản 2025 | LLM01 Prompt Injection, LLM02 Sensitive Info Disclosure, LLM03 Supply Chain, LLM04 Data/Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector/Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption |
| **OWASP Top 10 for Agentic Applications** | 12/2025 | ASI01 Goal hijack, ASI02 Tool misuse, ASI03 Identity/privilege abuse, ASI04 Supply chain, ASI05 Unexpected code execution, ASI06 Memory & context poisoning, ASI07 Insecure inter-agent comms, ASI08 Cascading failures, ASI09 Human-agent trust exploitation, ASI10 Rogue agents (tên mục theo bản tóm tắt vendor, cần đối chiếu bản gốc) |
| **OWASP MCP Top 10** | 2026, repo `OWASP/www-project-mcp-top-10` | MCP03 Tool poisoning, MCP05 Command injection… ; 30+ CVE liên quan MCP chỉ trong 1–2/2026 **(chưa xác minh)** |

**Vấn đề cốt lõi:** mô tả tool, tài liệu retrieve, output tool đều đi vào context như văn bản "đáng tin" → agent coi là lệnh. Phòng thủ: treat retrieved content as untrusted, least-agency tool scoping, validate tham số, cô lập quyền, human-in-the-loop cho hành động không đảo ngược.

## 2. Công cụ guardrails mã mở

| Công cụ | Repo | License | Điểm mạnh | Ghi chú |
|---|---|---|---|---|
| **NeMo Guardrails** (NVIDIA) | NVIDIA/NeMo-Guardrails | Apache-2.0 | 5 loại rail: input, dialog, retrieval, execution, output; Colang cho hội thoại đa lượt | Bản v0.22 (5/2025) được trích dẫn, kiểm tra repo để cập nhật |
| **LLM Guard** (Protect AI) | protectai/llm-guard | MIT | ~35 scanner: prompt injection, PII, toxicity, secrets; chạy như API server | |
| **Guardrails AI** | guardrails-ai/guardrails | Apache-2.0 | Validator output, structured output, Guardrails Hub | |
| **Promptfoo** (red-team) | promptfoo/promptfoo | MIT | Quét red-team theo OWASP LLM/Agentic Top 10 | Xem mục 07 |
| Vigil, Rebuff | – | – | Chuyên phát hiện prompt injection | Lớp bổ sung |
| **Lakera Guard** | (đóng) | Proprietary | API cloud phát hiện injection | Thương mại |
| OpenGuardrails, OneShield | arXiv 2510.19169, 2507.21170 | – | Nền tảng guardrail cấu hình được | Nghiên cứu |

## 3. Bảo mật chuỗi cung ứng & secrets (cho coding agent)

| Công cụ | Vai trò |
|---|---|
| gitleaks, trufflehog | Quét secret trong repo & git history (mục 09 yêu cầu quét toàn history) |
| Dependabot, Renovate, Snyk, OSV-Scanner, Trivy | SCA/dependency & container scan |
| Semgrep, CodeQL | SAST |
| OWASP ZAP | DAST |
| Sigstore/cosign, SLSA | Ký & chứng thực artifact |

## 4. Benchmark & nghiên cứu

- **AgentDojo** (NeurIPS 2024): benchmark tấn công/phòng thủ prompt injection cho agent có tool – được trích dẫn nhiều nhất.
- "MCP Pitfall Lab" (arXiv 2604.21477), "Securing the AI Agent: Multi-Layer Red Teaming" (2606.31227), "AgentGuardian" (2601.10440), "Before the Tool Call: Deterministic Pre-Action Authorization" (2603.20953).
- Quy tắc thực hành (rút ra): (1) allowlist tool + tham số; (2) tách kênh dữ liệu và kênh lệnh; (3) log-only trước khi enforce chính sách mới; (4) sandbox mọi code agent sinh ra (mục 11); (5) review người cho hành động bên ngoài (push, gửi mail, thanh toán).

## 5. Nguồn

- https://cycode.com/blog/owasp-top-10-agentic-applications/ · https://cycode.com/blog/owasp-mcp-top-10/ · https://github.com/OWASP/www-project-mcp-top-10 · https://www.imperva.com/blog/owasp-llm-top-10-what-comes-next-agentic-mcp/ · https://www.promptfoo.dev/docs/red-team/owasp-agentic-ai/ · https://www.lakera.ai/blog/the-progressive-breach-model-behind-the-owasp-top-10-for-agentic-applications · https://blog.alexewerlof.com/p/owasp-top-10-ai-llm-agents
- https://www.getmaxim.ai/articles/best-ai-guardrails-tools-in-2026/ · https://appsecsanta.com/nemo-guardrails · https://appsecsanta.com/llm-guard · https://dev.to/agdex_ai/best-ai-agent-security-guardrails-tools-in-2026-llm-guard-vs-nemo-vs-guardrails-ai-5e5d · https://www.turingpost.com/p/aisecuritytools
- arXiv 2601.10440 · 2507.21170 · 2510.19169 · 2609.06543 · 2604.21477 · 2606.31227 · 2603.20953
