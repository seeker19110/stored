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
| Vigil, Rebuff | – | – | Chuyên phát hiện prompt injection | Lớp bổ sung; **Rebuff đã archive 16/5/2025** (§3d) |
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
| **Policy-as-code**: OPA/conftest (`policy/*.rego`) | Chặn PR vi phạm chính sách (quyền route, cấu trúc workflow) ngay trong CI — qlkh chạy 14 job (mục 23 §3.3) |
| **SBOM**: syft → CycloneDX; `check_sbom.py`, `check_licenses.py` | Sinh SBOM mỗi build, gate license; pip-audit/`dotnet list package --vulnerable` hằng tuần (bẫy "lỗ hổng trôi dù lockfile không đổi", Sales-Hunter) |
| **Hash-locked installs**: `ci/tool-checksums.txt`, `verify_download.py`, GitHub Action pin SHA | Không "curl pipe sh"; tool tải về phải khớp checksum; hook `block-pipe-to-shell.sh` (dhcb) |
| **Mutation testing**: mutmut, Stryker, hoặc script tự viết | Kiểm test có phát hiện được lỗi không (xem mục 07) |
| **Rulesets-as-code**: `.github/rulesets/main.json` | Bảo vệ nhánh có version, review được (case-study-ft41, Dhcb-Tools) |
| **Hook Claude Code chặn sửa cấu hình**: `protect-config.sh`, `config-protection.sh` | `deny` sửa migration đã áp/vendor; `ask` khi sửa eslint/tsconfig/coverage-baseline/workflows — chống "làm cổng xanh bằng nới cấu hình" (xboss, dhcb) |

### 3b. Mô hình an toàn cho bridge loopback (agent điều khiển app desktop)

Từ Dhcb-Tools `SECURITY.md` (Revit/AutoCAD HTTP bridge 127.0.0.1): bind IPv4 loopback; token ACL + khoá dò; `Origin`/`Sec-Fetch-Site` lạ → 403; kiểm `Host` chống DNS rebinding; khoá khởi chạy `?k=`; chính sách đường dẫn (không ghi `.bat/.ps1/.lnk`); opener không proxy/không redirect; regex có trần thời gian; chặn CSV formula injection; "504 = có thể đã chạy, đừng gửi lại"; write qua MCP cần **chuỗi xác nhận theo lệnh** (`DELETE_UNUSED`…) và `dryRun` → `confirm` với `previewToken`. Cùng họ: REA (`morluto/rea`) **authority fail-closed** theo capability, mỗi call `approved: true`, replay cần `plan_digest`.

### 3c. Skill pack tấn công cho agent (dual-use) — chỉ dùng khi có ủy quyền

- `SnailSploit/claude-red` (fork `seeker19110/Claude-Red`, MIT, v0.3.0): 78 SKILL.md red-team trong 23 nhóm (AD, AI security, API, auth, cloud, web…), manifest máy đọc `claude-skills.json`, `install.sh --category`; `SECURITY.md` nêu intended-use. Chi tiết mục 23 §6.2.
- Promptfoo red-team (bảng trên) cho LLM app; AgentDojo cho agent có tool.
- **Điều kiện:** pentest có hợp đồng/scope, CTF, nghiên cứu phòng thủ; không chạy lên hạ tầng không được phép. Ghi scope vào skill (Claude-Red làm vậy ở mỗi SKILL.md).

### 3d. Repo bảo mật nổi tiếng đã xác minh (2026-10-12)

| Repo | ★ (12/10) | License | Hoạt động gần nhất | Vì sao chất lượng | Lưu ý |
|---|---|---|---|---|---|
| **NVIDIA/garak** | 9,5k | Apache-2.0 | v0.17.0 (9/9/2026), commit 10/10 | Máy quét lỗ hổng LLM của NVIDIA, có paper (arXiv 2406.11036); quét được HF, OpenAI, NIM, Bedrock, REST | Probe chứa prompt tấn công: chỉ quét hệ thống được phép; 273 issue mở |
| **microsoft/PyRIT** | 4,6k | MIT | v1.1.0 (4/9/2026), commit 12/10 | Framework red-team AI tạo sinh của Microsoft, đã lên 1.x, có whitepaper; báo lỗ hổng qua MSRC | Repo cũ `Azure/PyRIT` đã archive 27/3/2026 — sửa link cũ |
| **meta-llama/PurpleLlama** | 4,4k | MIT (eval, CodeShield); weights theo Llama Community License | 29/9/2026 | Một repo gồm Llama Guard (phân loại nội dung), Prompt Guard (phát hiện injection), CodeShield (lọc code không an toàn), CyberSecEval 1–3 | Weights không theo license OSI; commit gần đây chủ yếu bảo trì type-check |
| **semgrep/semgrep** | 17,0k | Engine LGPL-2.1; rule theo Semgrep Rules License v1.0 | v1.180.0 (7/10/2026) | SAST theo mẫu cho nhiều ngôn ngữ, chạy local, rule viết giống code; phát hành hằng tuần | Bản Community chỉ phân tích trong một file/hàm; rule không OSI (lý do có fork Opengrep) |
| **google/osv-scanner** | 11,2k | Apache-2.0 | v2.7.0 (12/10/2026) | Quét dependency và container image theo dữ liệu OSV.dev, chạy offline được; Google bảo trì | Guided remediation còn thử nghiệm; tài liệu chia V1/V2 |
| **aquasecurity/trivy** | 38,4k | Apache-2.0 | v0.75.0 (1/10/2026) | Một binary quét lỗ hổng, cấu hình sai, secret, SBOM cho image, K8s, repo, cloud | **Bị xâm nhập 3/2026 (CVE-2026-33634)**: bản v0.69.4 và GitHub Action bị cài backdoor → ghim Action theo SHA, kiểm checksum |
| **sigstore/cosign** | 6,4k | Apache-2.0 | v3.1.3 và v2.6.5 (6/8/2026) | Ký và minh bạch cho container/binary; ký keyless qua Fulcio + nhật ký Rekor, hỗ trợ KMS và khoá phần cứng | v2 và v3 bảo trì song song; bản lớn tiếp theo chuyển sang sigstore-go |
| **ossf/scorecard** | 5,8k | Apache-2.0 | v5.6.0 (12/10/2026) | Chấm điểm sức khoẻ bảo mật dự án mã mở (0–10 mỗi check), quét hơn 1,3 triệu repo hằng tuần, có Action và REST API | Điểm là heuristic, không phải phát hiện lỗ hổng; dataset BigQuery đã ngừng |
| **snyk/agent-scan** (trước là invariantlabs-ai/mcp-scan) | 3,1k | Apache-2.0 | 6/10/2026 | Quét agent, MCP server và agent skill tìm prompt injection; tự tìm config Claude/Cursor/Windsurf | Khi quét có thể **chạy** server MCP stdio → chạy trong sandbox; không nhận đóng góp ngoài |

**Nhận xét:**

- Vụ Trivy là ví dụ trực tiếp cho quy tắc "Action pin SHA + hash-locked tool" ở bảng §3: chính công cụ bảo mật cũng là một mắt xích chuỗi cung ứng. Wiz và Barracuda mô tả nhóm TeamPCP cài backdoor vào bản phát hành và Action; con số 178 release bị xoá chỉ thấy trong kết quả tìm kiếm **(chưa xác minh)**.
- Cập nhật bảng §2: `protectai/rebuff` đã archive (16/5/2025); cả 7 repo của `lakeraai` đã archive (Lakera Guard vẫn là dịch vụ đóng); `splx-ai/agentic-radar` không commit từ 27/11/2025.
- Với repo dùng MCP/skill: chạy `agent-scan` (trong sandbox) mỗi khi thêm server hoặc skill mới; dùng garak hoặc PyRIT khi cần red-team model/app có ủy quyền.
- AgentDojo (§4) chỉ có 910★ (MIT, commit cuối 2/6/2026) nhưng vẫn là benchmark prompt injection chuẩn.

## 4. Benchmark & nghiên cứu

- **AgentDojo** (NeurIPS 2024): benchmark tấn công/phòng thủ prompt injection cho agent có tool – được trích dẫn nhiều nhất.
- "MCP Pitfall Lab" (arXiv 2604.21477), "Securing the AI Agent: Multi-Layer Red Teaming" (2606.31227), "AgentGuardian" (2601.10440), "Before the Tool Call: Deterministic Pre-Action Authorization" (2603.20953).
- Quy tắc thực hành (rút ra): (1) allowlist tool + tham số; (2) tách kênh dữ liệu và kênh lệnh; (3) log-only trước khi enforce chính sách mới; (4) sandbox mọi code agent sinh ra (mục 11); (5) review người cho hành động bên ngoài (push, gửi mail, thanh toán); (6) **allowlist dạng glob phải chạy sau bộ tách lệnh nối** (`;`, `&&`, `|`) — ví dụ phản diện: Personal Jarvis áp whitelist `git log *` trước bộ phân loại `command_impact`, nên `git log; rm …` được hạ về `safe`, và mặc định `approval_mode = "bypass"` (mục 01 §3c.3, phân tích tĩnh 2026-10-12); (7) **plugin MCP không được đưa tool ra ngoài sandbox của host**: context-mode chặn `curl`/`WebFetch` rồi chuyển sang `ctx_execute` có toàn quyền mạng trong tiến trình MCP server, "sandbox" chỉ là tiến trình con mang theo gần hết env (mục 03 §8b).

## 5. Nguồn

- Mục 23 §3.3, §4.3, §4.4, §6.2, §6.4 (qlkh, xboss, Dhcb-Tools, Claude-Red, REA; đọc 2026-10-12) · https://github.com/SnailSploit/claude-red · https://github.com/morluto/rea · https://www.openpolicyagent.org/ · https://github.com/anchore/syft
- https://cycode.com/blog/owasp-top-10-agentic-applications/ · https://cycode.com/blog/owasp-mcp-top-10/ · https://github.com/OWASP/www-project-mcp-top-10 · https://www.imperva.com/blog/owasp-llm-top-10-what-comes-next-agentic-mcp/ · https://www.promptfoo.dev/docs/red-team/owasp-agentic-ai/ · https://www.lakera.ai/blog/the-progressive-breach-model-behind-the-owasp-top-10-for-agentic-applications · https://blog.alexewerlof.com/p/owasp-top-10-ai-llm-agents
- https://www.getmaxim.ai/articles/best-ai-guardrails-tools-in-2026/ · https://appsecsanta.com/nemo-guardrails · https://appsecsanta.com/llm-guard · https://dev.to/agdex_ai/best-ai-agent-security-guardrails-tools-in-2026-llm-guard-vs-nemo-vs-guardrails-ai-5e5d · https://www.turingpost.com/p/aisecuritytools
- arXiv 2601.10440 · 2507.21170 · 2510.19169 · 2609.06543 · 2604.21477 · 2606.31227 · 2603.20953
- §3d (12/10/2026): https://github.com/NVIDIA/garak · https://github.com/microsoft/PyRIT · https://github.com/Azure/PyRIT · https://github.com/meta-llama/PurpleLlama · https://github.com/semgrep/semgrep · https://github.com/opengrep/opengrep · https://github.com/google/osv-scanner · https://github.com/aquasecurity/trivy · https://www.wiz.io/blog/trivy-compromised-teampcp-supply-chain-attack · https://trust.barracuda.com/security/information/trivy-supply-chain-compromise · https://stack.watch/vuln/CVE-2026-33634/ · https://github.com/sigstore/cosign · https://github.com/ossf/scorecard · https://github.com/snyk/agent-scan · https://github.com/protectai/rebuff · https://github.com/lakeraai · https://github.com/splx-ai/agentic-radar · https://github.com/ethz-spylab/agentdojo
