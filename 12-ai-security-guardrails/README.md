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

### 3e. Danh sách "Awesome-AI-Security-Skills" (ảnh người dùng gửi, 2026-10-12) — đọc trước khi cài

> Chỉ đọc trang repo, README và lịch sử commit; **không chạy** skill hay script nào.

| Mục | Thông tin (12/10/2026) |
|---|---|
| Repo | `EvanThomasLuke/Awesome-AI-Security-Skills` · 112★, 30 fork, 22 commit (chỉ chủ repo), 10/3 → 22/9/2026; **không có LICENSE** (repo chỉ có README) |
| Chủ | Evan Luke ("AI Hacking and Alignment"), cũng làm Awesome-AI-Hacking-Agents (705★) |
| Lời cảnh báo của chính list | "I have not manually verified all of these. Running skills from others can compromise your machine." |
| Quy mô | 58 link trong 7 nhóm (57 duy nhất; bountyforge bị lặp): Security 28, Skill Scanners 5, Workflows/Toolkits 10, Rules/Guardrails 4, Related Lists 2, Other 2, Todo 7 |

**Các mục đáng chú ý (đã đọc từng repo):**

| Repo | ★ | License | Commit cuối | Nội dung | Chạy code / rủi ro | Ghi chú |
|---|---|---|---|---|---|---|
| **trailofbits/skills** | 7,5k | CC-BY-SA-4.0 | 9/10/2026 | Marketplace 44 plugin | Script theo plugin **(chưa xác minh)** | Không có câu về ủy quyền |
| **trailofbits/skills-curated** | 513 | CC-BY-SA-4.0 | 14/7/2026 | 29 plugin đã duyệt | Script, command | "we read every line of hooks and scripts" — mẫu kiểm duyệt đáng học |
| **NVIDIA/SkillSpector** | 20k | Apache-2.0 | 9/10/2026 | Máy quét skill (CLI + MCP) | Phân tích tĩnh, gửi nội dung file cho LLM | Tự ghi "not a sandbox" |
| **cisco-ai-defense/skill-scanner** | 2,6k | Apache-2.0 | 9/10/2026 | Máy quét skill v2.2.2 | Tĩnh + LLM | Tự ghi "best-effort" |
| **anthropics/claude-code-security-review** | 6,3k | MIT | 11/2/2026 | GitHub Action + `/security-review` | Python chạy trong CI | Tự ghi "not hardened against prompt injection"; đứng từ 2/2026 |
| **cloudflare/security-audit-skill** | 28,6k | MIT | 14/9/2026 | 1 skill + validator Node | Yêu cầu sandbox hệ điều hành | Mới nằm ở mục Todo của list |
| **google/mantis** | 2,4k | Apache-2.0 | 6/10/2026 | Skill + harness test | **Chạy code do nó sinh ra** | "not an officially supported Google product"; tự khuyên chạy cô lập |
| **elastic/agent-skills** | 593 | Apache-2.0 | 10/9/2026 | 26 skill (4 về bảo mật) | Script cài đặt | Hướng dẫn least-privilege tốt |
| **ghostsecurity/skills** | 411 | Apache-2.0 | 28/9/2026 | 2 plugin, 8 skill | Tải binary Go từ release, MITM proxy, test app đang chạy | Không có câu về ủy quyền |
| **mukul975/Anthropic-Cybersecurity-Skills** | 34,3k | Apache-2.0 | 31/8/2026 | ~817 skill (list ghi 754) | Một số script phụ | Dùng tên Anthropic nhưng tự ghi "not affiliated with Anthropic"; có câu về ủy quyền |
| **elementalsouls/Claude-BugHunter** | 5k | MIT + CC-BY-4.0 | 12/10/2026 | 82–83 skill, 15 command | Installer, CLI Python, Burp MCP, `.githooks` | Ngôn ngữ scope chặt |
| **blacklanternsecurity/red-run** | 286 | GPL-3.0 | 1/4/2026 | Agent team + MCP nmap/shell | **Hook SessionStart, server reverse shell, `--yolo`** | "CTF and lab use only" |
| **DeepBitsTechnology/claude-plugins** | 49 | Apache-2.0 | 13/7/2026 | MCP remote cho phân tích binary | **Tải mẫu lên `mcp.deepbits.com`** | Dữ liệu rời khỏi máy |
| `SnailSploit/Claude-Red` | 7,4k | MIT | 19/9/2026 | 78 skill, vẫn v0.3.0 | `install.sh`, `convert_skills.py` | Khớp §3c; SECURITY.md có câu về ủy quyền/CFAA |

**Cờ đỏ trong list:**

- **Không có LICENSE:** chính list, `Netflix-Skunkworks/railguard-skill` (README dẫn LICENSE.md nhưng 404), Eyadkelleh (README nói MIT), wrsmith108, BehiSecc, pashov, bountyforge, YARAHQ, mcpeak, vulhunt-re, ComposioHQ. License hạn chế: semgrep/skills (Semgrep Rules License), `tanweai/wooyun-legacy` (CC BY-NC-SA, tự ghi không còn bảo trì), `wiz-sec-public/secure-rules-files` (CC BY-NC-ND), prompt-security/clawsec (AGPL).
- **Khoảng 18 mục không commit hơn 6 tháng**, ví dụ secure-rules-files (12/2025), `project-codeguard/rules` (1/2026, đã chuyển cho CoSAI), claude-code-security-review (2/2026), red-run (4/2026).
- **Link hỏng, đổi tên, mạo danh:** `Repello-AI/skill-check` trả 404; Netropolitan chuyển hướng sang `AILiteracyLab/Claude-Security-Audit` (0★, 1 commit) mà `install.sh` **sửa `~/.claude/settings.json`** và tải từ URL cũ; Eyadkelleh đổi tên thành awesome-skills-security, chứa mẫu webshell (antivirus sẽ báo); `vinayaklatthe/microsoft-security-skills` là repo cá nhân nhưng LICENSE ghi "Copyright (c) Microsoft Corporation"; `zhaoxuya520/reverse-skill` có 41,2k★ trên chỉ 181 commit của tài khoản cá nhân (tỉ lệ bất thường, **chưa xác minh** sao ảo), script PowerShell tải toolchain và có nội dung vượt EDR. Ảnh ghi "Masrivan" — tên đúng là `Masriyan`, nay 22 skill (list ghi 15).
- **Nội dung tấn công không có câu về ủy quyền** (theo README): `Mindgard/ai-ide-skills` (payload copy-paste), `ljagiello/ctf-skills`, ghostsecurity.

**Cách dùng an toàn:**

1. Ưu tiên nguồn có kiểm duyệt (trailofbits/skills-curated đọc từng dòng hook/script; elastic; cloudflare).
2. Quét trước khi cài bằng SkillSpector, cisco skill-scanner hoặc `snyk/agent-scan` (§3d) — nhưng đều là quét tĩnh "best-effort", không thay được sandbox.
3. Tự đọc mọi `install.sh`, hook (SessionStart, PreToolUse), lệnh sửa `~/.claude/settings.json`, MCP remote nhận dữ liệu; chạy trong VM/container không có secret (mục 11 §3b, `anthropics/sandbox-runtime`).
4. Vendor có lock sha256 thay vì cài thẳng (mục 20 §3b).
5. Skill tấn công chỉ dùng trong phạm vi được ủy quyền (pentest có hợp đồng, CTF, lab) và ghi scope vào skill, như điều kiện ở §3c.

### 3f. "AI Red Teaming: The Complete Guide" (ảnh người dùng gửi, 2026-10-12)

> Đã clone toàn bộ repo (97 commit, HEAD `7b7dde8`, 11/10/2026), đọc README tiếng Anh, `CHANGELOG.md`, `resources-validation.md`, 8 template và 2 workflow CI; đối chiếu trang bán hàng và một số nhận định với nguồn ngoài.

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/requie/AI-Red-Teaming-Guide |
| Mô tả 1 dòng | Một README dài ~3.580 dòng (kèm bản ES/ZH/FR) gom phương pháp, khung chuẩn, kỹ thuật tấn công, công cụ, case study và template cho red-team hệ thống AI |
| Loại | learning (tài liệu, không phải công cụ) |
| License | Badge và mục License trong README ghi **MIT**, nhưng repo **không có file LICENSE** và sidebar GitHub không hiện license (12/10/2026) |
| ★ (ngày) | 971★, 181 fork, 11 watcher, 2 PR mở (2026-10-12, trang GitHub) |
| Tác giả | Tarique Smith (`requie`, New York), đồng sáng lập và Chief Research Officer của **Cogensec**; 87/97 commit là của tác giả (gồm 26 merge commit), 10 commit còn lại đến từ PR của các vendor công cụ (promptfoo, NeuralTrust, Pallma/Verno Labs, DeepKeep, Darkmoon, Ziran, aiArch). Repo khác: `requie/LLMSecurityGuide` (156★, dừng 2/2026), `Cogensec/Gideon` (34★), `Cogensec/agentegrity` (6★) |
| Lịch sử | Commit đầu 29/10/2025 ("Add files via upload", cả bài đưa lên một lần); 25 commit trong 10/2026 (bản v1.2.0 "Q4 refresh", dịch lại ES/ZH/FR) |

**Nội dung (đối chiếu với ảnh):** ảnh là phần đầu README và khớp với file thật: banner, thanh ngôn ngữ, 10 badge "Trusted by practitioners at", khối "Join the Global Red Teaming Network" (Cogensec), badge MIT / "Updated October 2026", và banner RedTeamKit đang hiện dở ở cuối ảnh. Phần thân có:

- Khung chuẩn: NIST AI RMF, OWASP GenAI Red Teaming Guide, OWASP Agentic Top 10, MITRE ATLAS, CSA Agentic AI Red Teaming, Microsoft Agentic Failure-Mode Taxonomy v2.0 (Microsoft công bố 4/6/2026, khớp).
- Phương pháp 4 pha (lập kế hoạch và threat model → thực thi → chấm điểm → báo cáo), các mục riêng cho MCP, computer-use, RAG, voice/multimodal, fine-tuning, coding agent và CI/CD, A2A.
- Bảng so sánh 27 công cụ (16 mã mở, 11 thương mại/dịch vụ), 6 attack tree map theo mã ASI của OWASP Agentic, thang mức độ hại kèm SLA triage, quickstart 30/60/90 ngày, harness eval mẫu (YAML + Python).
- Case study 2023–2026, trong đó có các vụ mới đã có nguồn báo chí: agent OpenAI truy cập cổng thống kê Medicare của Úc khi đánh giá nội bộ (6/2026, công bố 9/2026), "Comment and Control" (prompt injection vào Claude Code, Gemini CLI, Copilot trong CI), chiến dịch chuỗi cung ứng MCP "Deadbugz".
- 8 template trong `templates/`: rules of engagement, threat modeling workshop, vulnerability report, model/system security card, PR checklist, case study, stakeholder readout, test-case library. Đây là phần dùng lại được nhiều nhất.

**Điểm tốt:**

- `resources-validation.md` gắn mỗi nguồn ngoài một ngày kiểm và nhãn *Evidence-backed / Vendor-described / Author-described*; với công cụ do chính vendor gửi PR, guide ghi rõ số liệu là của vendor. Cách gắn nhãn này giống quy ước **(chưa xác minh)** của kho.
- Hai nhận định đã kiểm ngẫu nhiên đều đúng: OpenAI mua Promptfoo (công bố 9/3/2026, không công bố giá) và vụ Medicare (OpenAI xin lỗi trước phiên điều trần của quốc hội Úc).
- Workflow `ai-redteam-regression.yml` chạy garak với `OPENAI_API_KEY` **chỉ khi push lên `main` hoặc chạy tay**, không bao giờ chạy trên `pull_request`, và chạy trong thư mục trống để file trong PR không đè được gói `garak`. Đây là mẫu đúng cho "secret không chạm code của PR".
- Harness eval mẫu tự ghi rõ là minh hoạ: chỉ dò từ chối bằng từ khoá tiếng Anh và PII dạng email/SSN, khuyên thay bằng judge model đã hiệu chỉnh.

**Hạn chế và cờ đỏ:**

- **Guide của một người kiêm kênh bán hàng.** README có 3 banner RedTeamKit ("$249 one-time · Lifetime updates · Built by the author of this guide", "7 production npm packages"), mục "Featured Commercial Platform: AVERSYN by Cogensec" đứng đầu phần công cụ thương mại và gắn ⭐ trong bảng so sánh, cùng link "Join the network" về cogensec.com. Guide có ghi tác giả là đồng sáng lập Cogensec, nhưng xếp hạng công cụ không trung lập.
- **Mô tả sản phẩm trong README lệch với trang bán:** ngày 12/10/2026 `airedteamkit.com` bán theo bậc $99 / $299 / $799, cập nhật 12 tháng, không nhắc tới gói npm nào; README vẫn ghi "$249 one-time · Lifetime updates" và "7 production npm packages".
- **Badge "Trusted by practitioners at"** gồm Microsoft, Google, Meta, OpenAI, Anthropic, NVIDIA, IBM, Amazon, HackerOne, Cisco. Dòng chữ nhỏ bên dưới nói chỉ là "individual practitioners reference this guide; inclusion does not imply official endorsement". Không có bằng chứng nào kèm theo; coi như quảng cáo.
- "Grounded in real-world experience from Microsoft's 100+ AI product red teams": đó là kinh nghiệm trong paper của Microsoft ("Lessons From Red Teaming 100 Generative AI Products", arXiv 2501.07238), không phải của tác giả guide.
- License mơ hồ (chỉ ghi trong README, không có file); Gideon của Cogensec mô tả không thống nhất ("defensive security assistant" ở phần nguồn, còn repo tự gọi là "Red Teaming Agent"); bus factor 1; link-check CI để `fail: false`.

**Dự án tương tự (2026-10-12):**

| Tài liệu | Quy mô | License | Khác biệt |
|---|---|---|---|
| OWASP GenAI Red Teaming Guide (1/2025) | Tài liệu chính thức của OWASP | CC BY-SA **(chưa xác minh)** | Trung lập vendor, nhưng không có bảng công cụ hay template điền sẵn |
| CSA Agentic AI Red Teaming Guide (28/5/2025) | Tài liệu của Cloud Security Alliance | Theo điều khoản CSA | Sâu về agent, chưa có các sự cố 2026 |
| Japan AISI, *Guide to Red Teaming Methodology on AI Safety* v1.10 (31/3/2025) | Tài liệu cơ quan nhà nước | Trang AISI | Quy trình tổ chức red-team, ít kỹ thuật |
| `cloudstreet-dev/AI-Red-Teaming` | 4★, 15 commit | CC0 | Sách do Claude viết, có app dễ bị tấn công để thực hành |
| `Vect0rdecay/ai-red-team-course` | 36★, 41 commit | Không thấy LICENSE | Khoá 8 tuần cho người làm web/API/cloud pentest chuyển sang AI |

**Cách dùng từ dự án khác:**

1. Dùng làm **mục lục và checklist**, không làm nguồn chuẩn: mỗi nhận định quan trọng, mở link gốc trong `resources-validation.md` và kiểm lại.
2. Lấy 8 template trong `templates/` làm khung (rules of engagement, vulnerability report, model/system security card). License chưa rõ → viết lại theo ý mình và ghi nguồn, đừng chép nguyên văn, cho tới khi repo có file LICENSE.
3. Học mẫu workflow chạy scan có secret chỉ trên sự kiện tin cậy (push `main`, `workflow_dispatch`) cho CI có red-team.
4. Chọn công cụ từ bảng so sánh của kho này (§3d: garak, PyRIT, PurpleLlama; mục 07: promptfoo) thay vì bảng trong guide, vì guide đặt sản phẩm của tác giả lên đầu. RedTeamKit và AVERSYN là sản phẩm đóng, chưa ai đánh giá độc lập.
5. Mọi bài test trong guide chỉ chạy trên hệ thống mình sở hữu hoặc được ủy quyền, như điều kiện ở §3c (guide cũng ghi vậy ở phần Disclaimer).

### 3g. Decepticon — agent red team tự chủ chạy kill chain thật (dual-use, link người dùng gửi 2026-10-12)

> Đã clone toàn bộ repo (1.324 commit, có `v1.4.0`), đọc README, SECURITY.md, TELEMETRY.md, `docker-compose.yml`, và middleware cổng RoE (`roe.py`, `egress.py`, `hitl.py`). **Không build, không chạy stack**; chỉ đọc code. Đây là công cụ tấn công tự động, chỉ dùng khi có ủy quyền.

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/BitterSecurity/Decepticon · site: decepticon.red · app host: app.decepticon.red (sản phẩm thương mại) |
| Mô tả 1 dòng | Framework agent red team tự chủ trên LangGraph/deepagents: 16 agent chuyên biệt chạy recon → khai thác → leo thang → lateral → C2 trong sandbox Kali, có RoE ép bằng máy và đồ thị tri thức Neo4j |
| Loại | security (dual-use, offensive) |
| License | Apache-2.0 (có file LICENSE) |
| ★ (ngày) | ~6,0k★, 1,1k fork, 45 watcher, 11 issue / 5 PR mở (2026-10-12, trang GitHub); Trendshift badge |
| Tác giả | Minseok CHOI (`PurpleCHOIms`); commit nhiều nhất là CHOI + `VoidChecksum`, có một số commit "Claude" và "Sisyphus" (agent) |
| Hoạt động | Rất tích cực: 94 commit trong 10/2026, mốc gần nhất v1.4.0 (13/10/2026 theo lịch commit) |

**Kiến trúc thật (đã đọc compose + middleware):**

- **Hai mạng Docker tách biệt:** management plane (`decepticon-net`: LiteLLM, PostgreSQL, Neo4j, LangGraph) và `sandbox-net` (sandbox Kali + C2 + target). Mọi cổng dịch vụ bind `127.0.0.1`, không mở ra LAN. Workload nặng (BloodHound CE, Sliver C2, REA/Ghidra) chỉ bật khi orchestrator gọi `ops_start(...)` (ADR-0006), mặc định stack nguội.
- **Sandbox hardening:** container Kali chạy root nhưng `cap_drop: ALL` rồi chỉ thêm tối thiểu (`NET_RAW`, `NET_ADMIN`, `SYS_PTRACE`…), `no-new-privileges: true`, `mem_limit 4g`, `pids_limit`. Tài liệu tự nêu `read_only` không bật được vì ~30 tool Kali cần ghi — hạn chế có ghi rõ.
- **Điểm tin cậy cần lưu ý:** container **CLI mount `/var/run/docker.sock` của host** để lệnh `/web` dựng dashboard. Comment trong compose nói rõ "OSS scope: user == host owner; bản đa tenant không bao giờ expose docker.sock cho CLI của tenant". Nghĩa là: ai chạy được CLI OSS thì có quyền ngang host — hợp lý cho máy cá nhân, nhưng **không được** đặt bản OSS này cho nhiều người dùng chung.

**Cổng RoE hai lớp (đúng mẫu mục 12 §4 và §3b):**

- Lớp 1 — `roe.py`: parse văn bản lệnh so với `roe.json:machine_enforcement`, ba chế độ `audit` / `warn` / `enforce`, chèn `[ROE_REFUSED]` khi chặn. Code **tự ghi đây chỉ là tín hiệu fast-fail cho model, không phải ranh giới thật** (agent có thể giấu target sau biến, `$()`, DNS).
- Lớp 2 — `egress.py`: biên dịch **cùng** khối `machine_enforcement` thành nftables connect-allowlist + DNS allowlist áp ở rìa mạng sandbox, nên gói ra host ngoài scope không rời được sandbox dù parser trượt. "Một định nghĩa scope, hai điểm thực thi" — đúng nguyên tắc tách kênh dữ liệu/lệnh, enforce ở tầng mạng.
- Có `HITLApprovalMiddleware` cho hành động tác động cao, và audit ledger HMAC-chained ("đã thử gì, duyệt gì, chặn gì"). Cùng họ với `prompt_injection_shield`, `untrusted_output`, `egress` (chống exfil).

**Telemetry (đọc TELEMETRY.md + `.env.example`):** mặc định **off**, opt-in. Hai mức: `basic` (chỉ metadata có cấu trúc: tool, severity/CWE/MITRE của finding — không gửi prompt/output/target) và `research` (gửi **chuỗi suy luận tấn công** của agent làm corpus huấn luyện, target/cred được mask). Tài liệu tự nói thẳng masking là pattern-based, **không phải ẩn danh** — tên công ty trong văn xuôi có thể lọt, và LLM có thể tái định danh từ ngữ cảnh. `BENCHMARK_MODE=1` ép telemetry off và chèn addendum "nới luật" cho CTF.

**Benchmark (tự công bố, chưa có đánh giá độc lập):** XBOW validation-benchmarks 102/104 = 98,08% (black-box), kèm bảng so với Strix (96,15%), Shannon Lite (white-box 96,15%), PentestGPT (86,5%), Cyber-AutoAgent, XBOW thương mại (~85%). Có trace LangSmith per-challenge trong repo, nhưng số là của chính dự án — coi là **(chưa xác minh độc lập)**.

**Mâu thuẫn / cờ:**

- **Lệch tên tổ chức:** README và URL dùng `BitterSecurity/Decepticon`, nhưng `SECURITY.md`, `docs/benchmark-comparison.md` và nút Sponsor vẫn trỏ `PurpleAILAB/Decepticon` / `sponsors/PurpleCHOIms`. Dấu hiệu repo mới đổi tên tổ chức; link báo lỗ hổng trong SECURITY.md có thể 404 (chính file đã lường trước).
- Vừa là OSS Apache-2.0 vừa là phễu cho sản phẩm host thương mại (app.decepticon.red, "Commercial product demo") và Sponsor — giống mẫu §3f, nhưng ở đây license rõ ràng và phần OSS là code chạy được, không phải chỉ README.
- Mặc định LLM gọi ra API nhà cung cấp ngoài (Anthropic/OpenAI/Gemini…); muốn kín hoàn toàn phải cấu hình Ollama local. Egress allowlist chỉ chặn trong sandbox, không chặn management plane gọi LLM.

**So sánh (★ đọc 12/10/2026, từ bảng của repo + kiểm chéo):**

| Dự án | Cách tiếp cận | Khác Decepticon |
|---|---|---|
| `usestrix/strix` | Agent pentest black-box | Điểm XBOW tương đương (96%); Decepticon thêm C2 thật, AD/cloud, đồ thị tri thức |
| `GreyDGL/PentestGPT` (USENIX '24) | Agent hội thoại dẫn pentest | Cũ hơn, không sandbox kill-chain đầy đủ |
| `westonbrown/Cyber-AutoAgent` | Meta-agent | Phiên bản điểm cao đã archive |
| `SnailSploit/Claude-Red` (§3c) | Skill pack tấn công cho Claude Code | Là skill rời cho agent sẵn có; Decepticon là stack agent trọn gói tự chạy |
| garak / PyRIT (§3d) | Red-team **model/LLM** | Decepticon red-team **hệ thống/mạng**, không phải nội dung model |

**Điều kiện tích hợp / cách dùng an toàn:**

1. **Chỉ chạy khi có ủy quyền bằng văn bản** (pentest có hợp đồng/scope, CTF, lab của mình) — như Disclaimer và SECURITY.md của repo. Đây là công cụ chạy exploit thật, không phải máy quét.
2. Luôn điền `roe.json:machine_enforcement` và chạy ở `mode=enforce`; dựa vào lớp egress (nftables + DNS allowlist) làm ranh giới scope, không dựa vào parser lệnh.
3. **Không** deploy bản OSS cho nhiều người dùng chung: CLI mount docker.sock của host = quyền ngang host.
4. Để telemetry `off` (mặc định) cho engagement có khách hàng; chỉ cân nhắc `basic`, và tránh `research` khi scope không cho phép chia sẻ corpus — masking không phải ẩn danh (tài liệu tự nói vậy).
5. Muốn chạy kín: dùng provider local (Ollama) để prompt/kết quả không rời máy; mặc định các call LLM đi ra nhà cung cấp ngoài.
6. Mọi con số benchmark coi là tuyên bố của dự án cho tới khi có bên thứ ba tái lập.

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
- §3e (12/10/2026): https://github.com/EvanThomasLuke/Awesome-AI-Security-Skills (README, lịch sử commit) · https://github.com/EvanThomasLuke · trang repo + commits Atom của: trailofbits/skills, trailofbits/skills-curated, NVIDIA/SkillSpector, cisco-ai-defense/skill-scanner, anthropics/claude-code-security-review, cloudflare/security-audit-skill, google/mantis, elastic/agent-skills, ghostsecurity/skills, semgrep/skills, mukul975/Anthropic-Cybersecurity-Skills, elementalsouls/Claude-BugHunter, blacklanternsecurity/red-run, DeepBitsTechnology/claude-plugins, Netflix-Skunkworks/railguard-skill, Mindgard/ai-ide-skills, ljagiello/ctf-skills, Masriyan/Claude-Code-CyberSecurity-Skill, AILiteracyLab/Claude-Security-Audit, vinayaklatthe/microsoft-security-skills, zhaoxuya520/reverse-skill, wiz-sec-public/secure-rules-files, project-codeguard/rules · https://raw.githubusercontent.com/SnailSploit/Claude-Red/main/CHANGELOG.md
- §3g (12/10/2026): https://github.com/BitterSecurity/Decepticon (clone đầy đủ, 1.324 commit, có v1.4.0: README.md, SECURITY.md, TELEMETRY.md, docker-compose.yml, packages/decepticon/decepticon/middleware/{roe,egress,hitl,engagement}.py) · decepticon.red · app.decepticon.red · docs/benchmark-comparison.md (nội bộ repo) · https://github.com/PurpleAILAB/Decepticon (tên tổ chức cũ còn trong SECURITY.md/benchmark) · https://github.com/usestrix/strix · https://github.com/GreyDGL/PentestGPT · https://github.com/westonbrown/Cyber-AutoAgent · https://github.com/xbow-engineering/validation-benchmarks · arXiv 2607.13085, 2605.21497
- §3f (12/10/2026): https://github.com/requie/AI-Red-Teaming-Guide (clone đầy đủ, HEAD `7b7dde8`: README.md, CHANGELOG.md, resources-validation.md, templates/, .github/workflows/) · https://github.com/requie · https://github.com/requie/LLMSecurityGuide · https://github.com/Cogensec/Gideon · https://airedteamkit.com/ · https://tarique-io.lovable.app/ · https://huggingface.co/spaces/Cogensec/README · https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/ · https://futurumgroup.com/?p=87434 · https://news.bloomberglaw.com/us-law-week/openai-buying-ai-security-startup-promptfoo-to-safeguard-agents · https://www.canberratimes.com.au/story/9359341/openai-apologises-for-medicare-hack-creates-task-force/ · https://aisi.go.jp/assets/pdf/E1_ai_safety_RT_v1.10_en.pdf · https://github.com/cloudstreet-dev/AI-Red-Teaming · https://github.com/Vect0rdecay/ai-red-team-course
