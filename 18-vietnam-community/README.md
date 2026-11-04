# 18 · Hệ sinh thái AI & lập trình Việt Nam

> Model tiếng Việt mã mở, toolkit NLP, dữ liệu, cộng đồng và sự kiện. Nhiều mục chỉ có 1 nguồn, cần bổ sung khi có link cụ thể (theo WORKFLOW.md).

## 1. Model ngôn ngữ tiếng Việt mã mở

| Model | Tổ chức | Ghi chú |
|---|---|---|
| **PhoGPT** (PhoGPT-4B, 4B-Chat, 7B5) | VinAI Research | Chuỗi LLM tiếng Việt mở 2023; vẫn được dùng làm baseline nghiên cứu 2026 (VietBinoculars, VietAIDetector) |
| **Vistral / Vistral-V** | Viet-Mistral · Vi-VLM | Mistral-7B tinh chỉnh tiếng Việt; Vistral-V là VLM tiếng Việt (cập nhật giữa 2024) |
| **ViGPT** | DopikAI-Labs | LLM đơn ngữ, instruction-tuned, mã + trọng số công khai |
| **URA-LLaMA / GemSUra / MixSUra** | URA, ĐH Bách Khoa TP.HCM | Tinh chỉnh từ LLaMA-2, Gemma, Mixtral; benchmark tiếng Việt |
| **Ghost-7b** | cộng đồng | zephyr-7b-beta tinh chỉnh 50% EN / 50% VI |
| **14B-R1** | GreenNode (VNG) | "LLM suy luận mở tiếng Việt đầu tiên" (9/2025) **(chưa xác minh)** |
| PhoBERT, ViT5, BARTpho, XPhoneBERT | VinAI, VietAI | Encoder/seq2seq nền tảng |
| Qwen/Gemma/Llama bản đa ngôn ngữ | – | Thường tốt hơn model VN chuyên biệt ở quy mô lớn |

## 2. Toolkit NLP tiếng Việt

| Toolkit | Repo | Ghi chú |
|---|---|---|
| **underthesea** | undertheseanlp/underthesea | v9.5.0 (5/2026); từ v9.3 định vị là "Agentic AI Toolkit" có NLP tiếng Việt: tách từ, POS, NER, phân loại, sentiment |
| **VnCoreNLP** | vncorenlp/VnCoreNLP | Java, 1 jar, GPL-3; tách từ, POS, NER, dependency parsing (NAACL 2018) |
| pyvi, PhoNLP, VnCoreNLP-python | – | |
| **awsome-vietnamese-nlp** | vndee/awsome-vietnamese-nlp | Danh sách tổng hợp tài nguyên NLP tiếng Việt – điểm khởi đầu |

## 3. Dữ liệu & benchmark

- **ViGen** (10/2025): bộ dữ liệu tiếng Việt mã mở "đầu tiên" gắn với Chiến lược AI quốc gia đến 2030, lộ trình 2026–2027; SotaTek và nhiều doanh nghiệp đóng góp.
- Stanford CRFM *Crossing Linguistic Horizons*: đánh giá toàn diện LLM tiếng Việt.
- VietBinoculars / VietAIDetector (2025–2026): phát hiện văn bản AI tiếng Việt.

## 4. Tổ chức, cộng đồng, sự kiện

| Tên | Loại | Ghi chú |
|---|---|---|
| VinAI Research (Hùng Bùi) | Lab | NeurIPS/ICML, mở PhoGPT, PhoBERT |
| VietAI | Cộng đồng/giáo dục | ViT5, khóa học |
| Zalo AI, FPT AI, Viettel AI, GreenNode (VNG) | Doanh nghiệp | Zalo AI Challenge, FPT AI Factory (NVIDIA), Viettel–NVIDIA Vietnam AI Open Hackathon 2026 (GenAI, Agentic, Physical AI) |
| VFOSSA | Hiệp hội mã nguồn mở | Software Freedom Day 2026: AI mở, blockchain, PQC, phần cứng mở |
| Codex Community Hackathon Hanoi (27/6/2026) | Sự kiện | 271 đơn, 150 builder; Lotus Hacks >1.000 dev, >200 dự án |
| Viblo, TopDev, ITviec, Dạy Nhau Học, Tôi đi code dạo | Cộng đồng/nội dung | Chia sẻ kỹ thuật, tuyển dụng |
| Xu hướng 2026 | – | Dev VN chuyển từ outsourcing sang "AI building"; dự án hướng ngành: sản xuất, logistics, TMĐT, nông nghiệp |

## 4b. Kỹ thuật agentic & pháp lý số tại VN (từ repo của chủ kho, mục 23, 2026-10-12)

- **Engineering agentic viết bằng tiếng Việt**: 19 repo của `seeker19110`/`donghanhcungban` (xboss, projects-template, X-Agents, dhcb, Dhcb-Tools, Sales-Hunter…) có CLAUDE.md, ADR, TRAPS.md, hook, skill, commit toàn tiếng Việt — bằng chứng rằng harness tiếng Việt chạy được với Claude Code/Codex/Hermes; 7 skill tiếng Việt cho kỹ sư Revit/AutoCAD (`Dhcb-Tools/skills`), 112 SKILL.md trong Hermes-Agents (vendor + tự viết).
- **AI cho AEC/BIM**: Dhcb-Tools (Revit/AutoCAD MCP + IDS/BCF), xboss (quản lý tiến độ MEP/ACMV) — nhánh ứng dụng theo ngành ít thấy trong các awesome list.
- **Pháp lý (theo docs nội bộ của các repo, chưa xác minh văn bản gốc):** NĐ 13/2023 bảo vệ dữ liệu cá nhân + DPIA (dhcb `security-audit-20260927.md`); **NĐ 217/2026** BIM bắt buộc công trình cấp II từ 1/7/2026; **NĐ 207/2026** nhật ký thi công điện tử, dấu hoàn công; TT 09/2024; NĐ 70/2025 hoá đơn điện tử; NĐ 06/2021 → 35/2023 quản lý chất lượng công trình. Thanh toán: **SePay** (webhook chuyển khoản VietQR) dùng trong dhcb.
- Model VN nên theo dõi thêm: nhóm Hermes/Antigravity dùng Gemini 3.x làm model chính cho tiếng Việt (quan sát trong config, chưa có benchmark).
- **Repo VN về video-as-code và đội agent (tìm thấy khi kiểm bài đăng "điền form nhận 4 thứ", mục 22 §9i, 2/11/2026):** `HaiTLU/video-studio` (kho sản xuất video của Trung tâm Đào tạo ngắn hạn ĐH Thăng Long: 52 skill tiếng Việt, bảng đối chiếu nguồn/giấy phép từng skill, **không có LICENSE**), `hdduytran/one-studio-skill` (plugin video trọn gói, TTS tiếng Việt ZeroTTS, không LICENSE), `Freedombuiders/AIOS-Lite` (MIT, "hệ điều hành cho đội agent" có 8 bài học tiếng Việt), `lelongc/tools` (kho cá nhân giữ nguyên văn danh sách 20 repo video). Mẫu chung: viết tiếng Việt toàn bộ, vendor skill mở rồi ghi nguồn, nhưng hai trong bốn kho chưa khai license của chính mình.
- **`blogminhquy/javis-os` (mục 02 §4f, đọc mã 2/11/2026):** trợ lý tự host tiếng Việt nhiều sao nhất của VN mà kho đọc được (537★, 205 fork, MIT), 1.531 commit trong 4 tháng gần như toàn bộ do agent viết (4.116 trailer Co-Authored-By), nối Zalo/Pancake POS/Meta Ads qua MCP cho chủ shop; mã và comment tiếng Việt không dấu kèm GLOSSARY cho người đọc nước ngoài; README 12 ngôn ngữ có workflow kiểm dịch. Điểm cần đọc trước khi dùng: nhánh `bypassPermissions` khi không có allowlist, plugin Python chạy trong process, cập nhật bằng `git pull` không tag.
- **`duongbirken2510/AI-Money` (mục 21 §10g, đọc mã 3/11/2026):** thực nghiệm "AI tự kiếm tiền nuôi server" trong 20 ngày bằng Python thuần + SQLite + VietQR/SePay/Casso. Webhook ngân hàng làm đúng (HMAC, fail-closed). Nhưng có bot Facebook điều khiển Chrome qua CDP để đăng nhóm và trả lời bình luận, kèm skill viết rõ mục đích lách Admin Assist; thu số điện thoại và ngày sinh mà không thấy chính sách bảo mật; không có LICENSE.

## 4c. Repo & model tiếng Việt đã xác minh (2026-10-12)

> Số sao/lượt tải/tháng đọc trực tiếp trên GitHub và Hugging Face ngày 12/10/2026. Với model, **lượt tải trên HF** phản ánh mức dùng thật tốt hơn số sao GitHub.

| Repo / model | ★ · HF tải/tháng | License | Hoạt động gần nhất | Vì sao đáng dùng | Lưu ý |
|---|---|---|---|---|---|
| **VinAIResearch/PhoBERT** | 809★ · phobert-base ~66k + base-v2 ~65k | base/large MIT; **base-v2 AGPL-3.0** | 8/2026 (chỉ sửa README) | Encoder RoBERTa tiếng Việt chuẩn (EMNLP 2020 Findings); là nền của bi-encoder BKAI | Bản v2 AGPL; input cần tách từ trước (theo README, chưa tự kiểm) |
| **bkai-foundation-models/vietnamese-bi-encoder** (HF) | **~485k tải/tháng** | Apache-2.0 | 2024 (arXiv 2403.01616) | Model tiếng Việt được tải nhiều nhất trong đợt kiểm; embedding cho RAG, MRR@10 80,73 trên Zalo Legal 2021 | Huấn luyện phần lớn trên MS MARCO/SQuAD dịch máy; chỉ test trên dữ liệu pháp luật |
| **AITeamVN/Vietnamese_Embedding** (HF) | ~21,7k tải/tháng | Apache-2.0 | 5/2025 | BGE-M3 tinh chỉnh 300k bộ ba tiếng Việt, ngữ cảnh 2.048 token; MRR@10 0,818 so với BKAI 0,795 | Điểm tự báo cáo, một benchmark pháp luật duy nhất |
| **VinAIResearch/PhoWhisper** | 259★ · large ~8,2k | BSD-3-Clause | 11/2024 | Whisper tinh chỉnh 844 giờ đa giọng vùng miền; WER 4,67 trên VIVOS (ICLR 2024 Tiny Papers) | Repo chỉ trỏ tới model, không cập nhật từ 11/2024 |
| **pnnbao97/VieNeu-TTS** | 2,8k★ | Apache-2.0 | 12/10/2026 | TTS tiếng Việt hoạt động mạnh nhất (737 commit); v3 Turbo 48 kHz, 25 giọng, chạy CPU qua GGUF/ONNX, clone giọng tức thì | Một người phát triển; **v4 đóng, chỉ có API** |
| **nguyenthienhy/F5-TTS-Vietnamese** | 174★ · ~5,4k | Code MIT; **weights CC-BY-NC-SA-4.0** | 4/2025 | Pipeline fine-tune F5-TTS + weights ~1.000 giờ (ViVoice, VLSP 2021–23) | Weights cấm thương mại; repo ngừng từ 4/2025 |
| **thinhlpg/vixtts-demo** (viXTTS) | 518★ · ~0,8k | Code MPL-2.0; weights Coqui Public Model License | 4/2025 | XTTS-v2 tinh chỉnh tiếng Việt; 202 fork | README tự ghi "not actively maintained"; CPML **không thương mại** (chưa xác minh điều khoản) |
| **DAMO-NLP-SG/SeaLLMs** | 176★ · v3-7B-Chat ~1k | "SeaLLMs Terms of Use" (riêng) | 7/2024 | LLM Đông Nam Á của Alibaba DAMO; tiếng Việt được đánh giá trên M3Exam, Flores, Sea-bench (arXiv 2407.19672) | Ngừng từ giữa 2024; điều khoản riêng |
| **ZaloAI-Jaist/VMLU** | 83★ | MIT (README ghi "TBU") | 5/2024 | Benchmark kiểu MMLU cho LLM tiếng Việt (Zalo AI × JAIST): 10.880 câu, 58 môn | Leaderboard đóng băng từ 5/2024 |

**Nhận xét:** nhiều repo nền tảng đã **đóng băng** nhưng vẫn được dùng rất nhiều: VietAI/ViT5 (78★, commit cuối 2/2023), BARTpho (105★, 7/2024), pyvi (279★, 9/2024), trong khi PhoBERT + bi-encoder BKAI có hơn 600k lượt tải mỗi tháng. Với RAG tiếng Việt, cặp **bi-encoder BKAI / Vietnamese_Embedding + Qwen/Gemma đa ngôn ngữ** là lựa chọn thực dụng. Với TTS thương mại, cần chọn **VieNeu-TTS v3** (Apache-2.0), vì F5-TTS-Vietnamese và viXTTS đều có weights cấm thương mại, còn Audio8 (mục 14) không hỗ trợ tiếng Việt.

**Công cụ dev-agent do người Việt làm (17/10/2026):** `Manto-X/Agent_Board` (MIT, Python stdlib, mới tinh 17/10) — blackboard file + "gậy tiếp sức" `BATON.json` điều phối Claude/Codex/Antigravity desktop, zero-install, cầu chì 2 hiệp chống ping-pong. Hồ sơ đầy đủ + đọc cổng thật (baton là *quy ước* không phải lock, installer `curl | python3`) ở [mục 01](../01-ai-coding-agents/README.md) §3h.

**Bộ làm video AI cho kênh cá nhân của CuongIT (21/10/2026):** `Cuongyd196/auto-compare-video` (220★, HyperFrames), `Cuongyd196/remotion-cuongit-template` (208★, Remotion), `Cuongyd196/auto-video-gen` (184★, bản sao có ghi credit của `hoquanghai/Auto-Create-Video`, 322★) và app TTS `Cuongyd196/cit-voice-studio` (119★, đóng mã, chạy VieNeu-TTS v3 Turbo). Mỗi repo video kèm một skill cho Claude Code/Antigravity; agent tự viết kịch bản. Lưu ý trước khi dùng: repo Remotion không có LICENSE và commit font Segoe UI của Microsoft, LICENSE của auto-video-gen thay tên tác giả gốc, bộ cài CIT Voice Studio không ký số. Hồ sơ ở [mục 19](../19-agentic-video-media/README.md) §1f.

**Nội dung SEO/GEO tiếng Việt (25/10/2026):** infographic "SEO không thiếu việc, nhưng AI đang thay đổi cuộc chơi" của Danh Nolan (danhnolan.com) chia 5 cấp SEO × 7 mảng việc theo mức AI tự động hóa. Bài kiểm đối chiếu với tài liệu Google ở [mục 08](../08-awesome-lists-learning/README.md) §2h: khung "tác vụ, không phải vai trò" hợp lý, nhưng ảnh thiếu phần đo lường khi click giảm và phần kiểm soát crawler/snippet, và không nói ranh giới scaled content abuse.

**Công cụ sáng tạo do người Việt làm (13/10/2026):** `letuandat131/whiteboard-animation-vi` (~56★, mã gốc CC0-1.0) biến ảnh tĩnh thành video vẽ bảng trắng bằng app Gradio chạy cục bộ, tách nền bằng ISNet. Hồ sơ và kiểm ảnh ở [mục 22](../22-motion-design-animation/README.md) §9d. Lưu ý: giao diện tiếng Anh, ảnh bàn tay và tranh demo chưa có giấy phép.

## 4d. Nâng cấp 31/10/2026: rà repo lớn

> Hai việc. (1) Đọc lại số sao, license, trạng thái của 15 repo GitHub đã có trong mục 18 (GitHub search API và `meta_all` ngày 31/10/2026; với underthesea thì clone để đọc lịch sử LICENSE). (2) Tìm repo AI/dev Việt Nam còn thiếu: 16 truy vấn GitHub ("vietnamese llm/tts/asr/ocr/dataset/nlp/rag/whisper/legal/agent", topic `vietnamese`, "tiếng việt", repo tạo sau 1/10/2025). Hệ sinh thái nhỏ: ngoài VieNeu-TTS, không repo AI tiếng Việt mới nào vượt 1k★. Chọn **7 repo**, clone `--filter=blob:none`, đọc LICENSE, manifest, script cài, mã nạp model. **Không chạy script nào.** Số sao đọc 31/10/2026.

### 4d.1 Repo cũ: điều đã đổi

| Repo | Thay đổi | Hệ quả |
|---|---|---|
| `undertheseanlp/underthesea` | **Đổi license GPL-3.0 → Apache-2.0** (commit `d9c9ad3`, 7/2/2026); 1,8k★, v9.5.0, commit 29/10/2026 | Catalog đang ghi GPL-3.0 là sai. Nay nhúng được vào sản phẩm đóng mà không phải mở mã |
| `VinAIResearch/PhoGPT` | 794★; GitHub nhận **BSD-3-Clause** cho mã (catalog ghi "custom"); push cuối **12/11/2024** | Đóng băng gần 2 năm; điều khoản weights cần đọc riêng trên HF |
| `vncorenlp/VnCoreNLP` | 679★; push cuối **12/2/2023**; GitHub `NOASSERTION` | Đóng băng; dùng underthesea (nay Apache-2.0) thay thế |
| `vndee/awsome-vietnamese-nlp` | 320★; push cuối 28/10/2025 | Danh sách một năm chưa cập nhật, thiếu các model 2025–2026 |
| `VinAIResearch/PhoWhisper` · `nguyenthienhy/F5-TTS-Vietnamese` · `thinhlpg/vixtts-demo` · `ZaloAI-Jaist/VMLU` | Không đổi từ 11/2024 · 4/2025 · 4/2025 · 5/2024 | Đã ghi đóng băng ở §4c; nay có thay thế mới ở 4d.2 (ASR, TTS) |
| `pnnbao97/VieNeu-TTS` | 2,8k → **3,1k**★, 943 fork, commit 30/10/2026 | Vẫn là repo AI tiếng Việt lớn nhất và hoạt động mạnh nhất |
| `Viet-Mistral/Vistral-7B-Chat` | Không tồn tại trên GitHub (đây là model trên Hugging Face) | Trường `repo` trong catalog trỏ sai nền tảng |
| `DAMO-NLP-SG/SeaLLMs` | Repo còn (ls-remote có HEAD) nhưng search API không trả kết quả | Chưa đọc được số sao mới |

### 4d.2 Bảng nhanh 7 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `thanglequoc/vietnamese-provinces-database` | Dữ liệu cho dev | 1,8k · MIT | 22/9/2026 | 34 tỉnh, 3.321 xã/phường sau sáp nhập; SQL cho 6 CSDL, JSON, Redis, Elasticsearch, GIS, mã bưu chính | Ranh giới GIS lấy từ bản đồ của nhà xuất bản |
| `th1nhhdk/local_ai_ocr` | OCR cục bộ | 888 · Apache-2.0 | 5/7/2026 | App PySide6 chạy DeepSeek-OCR-2 trên máy: ảnh/PDF → Markdown/Word | `trust_remote_code` với repo model bên thứ ba |
| `duydo/elasticsearch-analysis-vietnamese` | Tìm kiếm | 565 · Apache-2.0 | 30/10/2026 | Plugin `vi_analyzer` cho Elasticsearch 9.x, dùng bộ tách từ của Cốc Cốc | Cần build thư viện C++ |
| `tronghieuit/v-tts` | TTS | 385 · **CC-BY-NC-4.0** | 23/7/2026 | TTS 74,8M tham số, 5 giọng, clone giọng zero-shot, app `.exe` | Cấm thương mại; GitHub báo NOASSERTION |
| `zeroweight-ai/ZeroTTS` | TTS | 308 · MIT (code + weights) | 17/9/2026 | TTS zero-shot 202M tham số, ONNX trên CPU, không cần PyTorch | Benchmark không so với VieNeu-TTS |
| `VietnamAIHub/Vietnamese_LLMs` | Dữ liệu instruction | 285 · Apache-2.0 | 18/10/2026 | Bộ instruction tiếng Việt dịch máy và LLaMA-2 tinh chỉnh (2023) | Nội dung từ 2023, commit 10/2026 chỉ là CI |
| `ggroup-ai-lab/gipformer` | ASR | 156 · **không có LICENSE** | 17/9/2026 | Zipformer RNN-T 68M tham số, mạnh ở cuộc gọi tổng đài | README ghi MIT nhưng repo không có file |

### 4d.3 Hồ sơ ngắn

- **vietnamese-provinces-database.** 612 commit từ 11/2021, Thang Le Quoc 605 commit. Theo dõi từng nghị quyết sắp xếp đơn vị hành chính; bản v5.2.0 theo **388/NQ-UBTVQH16, hiệu lực 20/9/2026** (theo bảng trong README, chưa đối chiếu văn bản gốc). Dữ liệu tỉnh/xã sinh từ API của Tổng cục Thống kê bằng script Go có trong repo, nên tái tạo được; thêm bảng vùng, loại đơn vị, tên tiếng Anh, slug. Bản phát hành tải từ CDN riêng `vn-provinces-ds.thanglequoc.xyz`. Có `AGENTS.md` và cấu hình OpenCode để agent bảo trì. ⚠️ Ranh giới GIS "derived from" bản đồ `sapnhap.bando.com.vn` của NXB Tài nguyên Môi trường và Bản đồ; README cấp MIT cho toàn bộ, nhưng quyền phân phối lại dữ liệu bản đồ gốc **(chưa xác minh)**. 0/14 action ghim SHA. Dùng: tải zip đúng phiên bản theo bảng Download, đừng lấy nhánh `master`.
- **local_ai_ocr.** Một người viết (52 commit, 11/2025–7/2026), giao diện tiếng Việt tự bật khi máy có Cốc Cốc hoặc Zalo. `env_setup_linux.sh` tải Python standalone, PyTorch cu130, wheel flash-attn từ repo cá nhân `mjun0812`, rồi `huggingface-cli download Dogacel/Universal-DeepSeek-OCR-2` (6,67 GB). ⚠️ README ghi "không liên lạc đi đâu", nhưng `transformers_service.py` nạp model bằng ID Hub với **`trust_remote_code=True`**, không ghim `revision`, không đặt `HF_HUB_OFFLINE`: khi có mạng, mỗi lần nạp vẫn hỏi Hub, và mã Python của repo model **bên thứ ba** (không phải `deepseek-ai`) sẽ được chạy. Muốn dùng cho tài liệu nhạy cảm: đặt `HF_HUB_OFFLINE=1` sau khi tải, đọc mã trong thư mục model, hoặc chuyển sang model chính chủ. Không có CI.
- **elasticsearch-analysis-vietnamese.** Plugin lâu năm (từ 3/2014, 283 commit, v9.3.0), bọc bộ tách từ C++ của Cốc Cốc; trả token như "cộng hòa", "xã hội" thay vì từng âm tiết. Hữu ích cho RAG lai (BM25 + embedding BKAI ở §4c) với tài liệu tiếng Việt. Cần build `coccoc-tokenizer` và đặt từ điển ở `/usr/local/share/tokenizer/dicts`; license của thư viện Cốc Cốc cần kiểm riêng **(chưa xác minh)**. Commit 7/2026 thêm một file "Arcade architecture analysis" do tác giả ẩn danh viết, không ảnh hưởng mã.
- **v-tts.** 22 commit của một người (12/2025–7/2026). File LICENSE là **CC-BY-NC-4.0** (GitHub không nhận dạng nên báo NOASSERTION): cấm dùng thương mại, giống F5-TTS-Vietnamese và viXTTS ở §4c. Bản `.exe` 394 MB không ký số, lần đầu chạy tải model ~100 MB từ Hugging Face. Trong `dist/` còn con trỏ LFS tên `ValtecTTS.exe`, gợi ý dự án từng mang tên khác; nguồn gốc dữ liệu huấn luyện không ghi **(chưa xác minh)**.
- **ZeroTTS.** 63 commit (15/8–17/9/2026), bản PyPI `zerotts` 0.1.5. Code và weights **MIT**; `NOTICE` và `LICENSES/` liệt kê đúng phần bên thứ ba (decoder MOSS-Audio-Tokenizer Apache-2.0, quy tắc chuẩn hoá số của `soe-vinorm` MIT). Suy luận chỉ cần `onnxruntime`, không PyTorch; weights ~900 MB tải từ Hub, có tuỳ chọn `--revision` để ghim. ⚠️ Câu "chính xác nhất trong các TTS tiếng Việt mở" dựa trên benchmark ZeroBench-TTS tự làm (WER 1,03%), chỉ so với OmniVoice, XTTS-v2-vietnamese, viXTTS; **không có VieNeu-TTS**, repo phổ biến nhất. Bộ benchmark là CC-BY-NC-4.0. Repo đứng yên từ 17/9.
- **Vietnamese_LLMs (VietnamAIHub).** Ví dụ "trông mới nhưng cũ": GitHub báo push 18/10/2026, nhưng 7 commit từ 8/2026 chỉ là workflow CI, font và sửa README; model và dữ liệu (LLaMA-2 7B/13B, Alpaca 52k, Dolly dịch bằng GPT) đều từ 2023. Link "checkpoint" trong README còn trỏ tới tìm kiếm `taiwan-llama`. Dữ liệu dịch bằng API OpenAI có thể vướng điều khoản dùng output để huấn luyện model cạnh tranh **(chưa xác minh)**. Chỉ dùng làm tư liệu lịch sử.
- **gipformer (G-Group).** 12 commit, chỉ có script suy luận (`infer_onnx.py`, `infer_pytorch.py`) và 18 file âm thanh mẫu; model trên HF `g-group-ai-lab/gipformer1.5-68M-rnnt`. Bảng WER so với 13 model (PhoWhisper, Qwen3-ASR, Parakeet…): tốt nhất trên 4 tập tổng đài **riêng tư** và 4 tập miền công khai do chính nhóm phát hành; trên vivos/Common Voice/VLSP thì `hynt/Zipformer-30M-RNNT-6000h` (30M) tốt hơn. ❌ README gắn badge "License: MIT" và link `LICENSE`, nhưng repo **không có file LICENSE**: về mặt pháp lý chưa được cấp quyền. Hợp làm ứng viên ASR nhẹ thay PhoWhisper (đóng băng) sau khi nhóm bổ sung license.

### 4d.4 Mẫu chung rút ra

1. **License tiếng Việt hay "lệch nhãn"**: underthesea đổi sang Apache-2.0 mà catalog chưa biết; v-tts là CC-BY-NC nhưng GitHub báo NOASSERTION; gipformer ghi MIT mà không có file. Đọc file LICENSE và lịch sử của nó.
2. **TTS tiếng Việt cho thương mại giờ có hai lựa chọn mở**: VieNeu-TTS v3 (Apache-2.0) và ZeroTTS (MIT, ONNX/CPU). F5-TTS-Vietnamese, viXTTS, v-tts đều cấm thương mại.
3. **App "offline" vẫn có thể chạy mã tải về**: `trust_remote_code=True` với repo model không ghim là đường cho mã lạ chạy trên máy. Ghim `revision` và đặt `HF_HUB_OFFLINE=1`.
4. **Ngày push không phản ánh nội dung**: Vietnamese_LLMs có push 10/2026 nhưng nội dung từ 2023. Kiểm commit chạm vào mã/dữ liệu, không chỉ ngày.
5. **Benchmark tự làm bỏ sót đối thủ mạnh** (ZeroTTS không so VieNeu-TTS; gipformer mạnh nhất trên tập riêng tư). Với tiếng Việt, vẫn thiếu một leaderboard ASR/TTS độc lập; VMLU cho LLM đã đóng băng từ 5/2024.

**Nguồn §4d:** GitHub search API 31/10/2026 (`repo:` cho repo cũ, 16 truy vấn) · `git ls-remote` cho `DAMO-NLP-SG/SeaLLMs`, `Viet-Mistral/Vistral-7B-Chat` · clone `undertheseanlp/underthesea` (LICENSE, `git log -- LICENSE`) · clone `--filter=blob:none` 7 repo mới, đọc: vietnamese-provinces-database (LICENSE, README (bảng nghị quyết, Download, GIS, FAQ), AGENTS.md, workflows), local_ai_ocr (LICENSE, README, `env_setup_linux.sh`, `requirements.txt`, `src/{transformers_service,lang_handler,config}.py`), elasticsearch-analysis-vietnamese (README, git log, tags), v-tts (LICENSE, README, `dist/`, `src/`), ZeroTTS (LICENSE, NOTICE, LICENSES/, README (Install, Benchmarks, License), `src/zerotts/{hub,cli}.py`), Vietnamese_LLMs (LICENSE, README, git log), gipformer (README, cây file) · https://huggingface.co/g-group-ai-lab/gipformer1.5-68M-rnnt · https://huggingface.co/zeroweight-ai/ZeroTTS · https://sapnhap.bando.com.vn (link trong README, chưa mở)

## 4e. Hồ sơ mhfed/vn-law-check: skill audit pháp lý website và mobile app theo luật Việt Nam 2025–2026 (link người dùng gửi, đọc mã 3/11/2026)

> Đọc mã tại `5847e324337faab6886b6aedfd4e9bea4e0f2fea` (v1.3.0, 2/11/2026). Clone đủ lịch sử: 18 commit, toàn bộ trong ngày 2/11/2026, một tác giả. Số sao lấy từ GitHub search API ngày 3/11/2026. **Không chạy, cài hay build mã của repo**; `tests/run.sh` và `scan.sh` chỉ được đọc. Điều khoản luật đối chiếu với tóm tắt của EY và Luật Việt An, **chưa đọc toàn văn** (thuvienphapluat trả 403).

| Thuộc tính | Giá trị |
|---|---|
| Repo / URL | https://github.com/mhfed/vn-law-check |
| Mô tả 1 dòng | Bộ checklist + skill cho coding agent (Claude Code, Cursor, Copilot, Windsurf, Cline, Codex): quét code hoặc URL để phân loại site, rồi audit theo luật dữ liệu cá nhân, TMĐT, an ninh mạng, người tiêu dùng, quảng cáo, giao dịch điện tử và AI của Việt Nam, có dẫn Điều/khoản |
| Loại | checklist / agent skill + Claude plugin marketplace |
| License | MIT cho mã và cấu trúc. GitHub hiện `NOASSERTION` vì file `LICENSE` có thêm đoạn ghi chú sau văn bản MIT. Dòng copyright ghi "Contributors to vn-web-compliance-audit", là tên cũ của dự án. Văn bản pháp luật được dẫn là tài liệu công khai, không thuộc phạm vi license |
| Phiên bản đã đọc | `5847e324337faab6886b6aedfd4e9bea4e0f2fea` (plugin.json `1.3.0`) |
| Kiểm chứng | 2026-11-03; code-read: README, LICENSE, SKILL.md, AGENTS.md, 10 file `references/`, `sources/legal-references.md`, `scripts/scan.sh`, `scripts/fetch-site.sh`, `install.sh`, `tools/sync.sh`, `tests/run.sh` + 8 fixture `EXPECTED`, `.github/workflows/check.yml`, `.claude-plugin/marketplace.json`, `plugin.json`. Chưa chạy test |
| ★ (ngày) | 126★, 29 fork (2026-11-03, GitHub search API). Repo tạo 2/11/2026. Topic: `claude-plugin`, `agent-skills`, `cursor-rules`, `legal-tech`, `vietnam` |
| Tác giả | `mhfed`: dev web/TypeScript cá nhân. Các repo khác đều dưới 10★ (`next-query-sync`, `react-shadcn-shopping-cart`, `gom`…). README tự nhận "Mình là dev, không phải luật sư". Web search 3/11/2026 chưa thấy bài viết hay thảo luận bên ngoài về repo |

**Cấu trúc thật (đối chiếu với README)**

- **Một nguồn, nhiều bản copy.** Nguồn gốc là `AGENTS.md`, `SKILL.md`, `references/`, `sources/`, `examples/`, `scripts/`. `tools/sync.sh` sinh ra `CLAUDE.md`, `.windsurfrules`, `.clinerules`, `.github/copilot-instructions.md`, `.cursor/rules/*.mdc` (thêm frontmatter) và bản trong `plugins/vn-law-check/` (copy file thật, vì thư mục plugin của Claude không nhận symlink). CI chạy `sync.sh --check` và báo lỗi khi bản copy bị lệch so với nguồn.
- **Triage trước khi audit** (`references/00-triage.md`). `scan.sh` grep 10 nhóm tín hiệu (FORM, TRACKING, COMMERCE, AUTH, MARKETPLACE, AI, PERMISSIONS, SDK_TRACKING, ADS_SDK, FOREIGN_HOST), nhận diện Flutter/React Native/Expo/Android/iOS, rồi in `LEVEL=0..3 AI= FOREIGN_HOST= APP=` kèm bằng chứng `file:dòng:đoạn khớp`. Site mức 0 chỉ nhận 1 dòng kết luận, không phải bảng checklist dài. Regex có mẫu cho JSX đã compile (`jsx("form"`) để bắt form trong bundle React/Next. Script chạy được trên bash 3.2 của macOS vì không dùng `declare -A`.
- **Quét theo URL** (`fetch-site.sh`): tải trang chủ, tối đa 15 trang cùng gốc có tên gợi ý chính sách/giỏ hàng/đăng nhập và tối đa 20 file JS, rồi quét như code. Header phản hồi được dùng để đoán hosting (Vercel, Cloudflare, CloudFront…).
- **Test**: 8 fixture (static-blog, landing-form, shop, marketplace, ai-chat, spa-url phục vụ qua `python3 -m http.server`, rn-app, flutter-shop), mỗi fixture có `EXPECTED` dạng `LEVEL=… AI=… APP=…`.
- **Cách ghi chưa chắc chắn**: điều khoản nào chưa đối chiếu toàn văn thì ghi `CHƯA XÁC MINH` ngay tại chỗ, và SKILL.md cấm agent tự điền số điều hay mức phạt cho các mục đó. Mỗi phát hiện xếp 🔴/🟡/🟢/⚪. Báo cáo phải đóng bằng phần giới hạn và khuyến nghị tham vấn luật sư.
- **Không có telemetry.** Mạng chỉ dùng trong `fetch-site.sh` (GET tới site đang quét, UA `vn-law-check (+github…)`) và `install.sh` (`git clone` nhánh `main`).

**Vì sao đáng tham khảo**

- Đây là bộ rule compliance theo **luật Việt Nam mới** đầu tiên cho coding agent mà kho tìm được. Các bộ privacy lớn hơn vẫn dẫn luật cũ: `mukul975/Privacy-Data-Protection-Skills` (328★, Apache-2.0, đọc HEAD `9b2ef9e` ngày 16/3/2026) vẫn ghi "Decree 13/2023/ND-CP" trong nhiều skill APAC, trong khi NĐ 13 hết hiệu lực từ 01/01/2026.
- Mẫu đáng học cho mọi skill "audit theo luật": **triage bằng máy có bằng chứng** → chỉ mở checklist áp dụng được → mỗi dòng có Điều/khoản → chỗ chưa kiểm ghi rõ và cấm agent bịa. Cách này khác GESF (mục 09 §2b), nơi công cụ tự chấm điểm "100%".
- Thời hạn xử lý quyền chủ thể dữ liệu ghi theo **Điều 5 NĐ 356/2025**: phản hồi 2 ngày làm việc; xem/sửa 10 ngày; rút đồng ý/hạn chế/phản đối 15 ngày; xóa 20 ngày. Hai bản tóm tắt độc lập (EY, Luật Việt An) cho cùng các mốc này, kèm mốc 15/20/30 ngày khi phải phối hợp bên thứ ba. Mốc "72 giờ" chung là của NĐ 13/2023 cũ. Chỗ này lệch với X-Templates (xem dưới).
- Tách nguồn khỏi bản copy cho từng công cụ và có CI chặn lệch là cách phân phối một bộ rule cho 6 agent mà không phải sửa tay 6 chỗ.

**Hạn chế / rủi ro (tự kiểm 3/11/2026)**

- ⚠️ **README ghi "còn 32 chỗ CHƯA XÁC MINH", nhưng tại HEAD đếm được 43 dòng** trong `references/`. 11 dòng thêm đến từ `09-mobile-app.md`, mới thêm ở v1.3.0 (43 − 11 = 32), nên con số trong README đã cũ sau đợt thêm mobile.
- ⚠️ Bảng mức trong `00-triage.md` ghi mức 3 = "Toàn bộ `01`–`08`" và "không áp đủ 8 checklist", chưa tính `09-mobile-app`. Bảng mô tả mức 3 là "có tài khoản, **hoặc** xử lý dữ liệu lớn, **hoặc** là nền tảng", nhưng `scan.sh` chỉ xếp mức 3 khi có **cả** AUTH **và** MARKETPLACE. Một SaaS có đăng nhập mà không có từ khóa người bán sẽ bị xếp mức 1 hoặc 2.
- ⚠️ `fetch-site.sh` lọc link cùng gốc bằng so khớp tiền tố (`[[ "$href" == "$origin"* ]]`), nên `https://shop.vn.example.com/...` vẫn lọt qua khi quét `https://shop.vn`. Thêm vào đó `curl -L` đi theo redirect sang miền khác. Tuyên bố "không gửi request đi đâu khác" vì vậy chỉ đúng với site bình thường **(suy từ mã, chưa chạy thử)**.
- Grep heuristic: chữ "thanh toán" trong bài blog cũng bị tính là COMMERCE, và tài liệu tự nói phải xem lại bằng chứng. Quét qua URL không thấy được phía server (chatbot gọi AI ở backend, nơi lưu dữ liệu).
- Tuổi đời một ngày, một tác giả không phải luật sư, chưa có issue hay PR từ bên ngoài. Phần lớn số điều lấy từ tóm tắt của công ty luật và báo chí. Mức phạt NĐ 330/2026 và toàn bộ khung phạt TMĐT, quảng cáo, AI còn `CHƯA XÁC MINH`.
- Cài bằng `curl … | bash` sẽ clone `main` không ghim tag. `install.sh` chèn khối có marker vào `AGENTS.md`/`CLAUDE.md` của dự án (không ghi đè, chạy lại không chèn trùng) nhưng xóa và tạo lại `.vn-law-check/` mỗi lần chạy.

**So với lựa chọn cùng loại (GitHub search API 3/11/2026)**

| Repo | ★ · license | Phạm vi | Khác biệt |
|---|---|---|---|
| **mhfed/vn-law-check** | 126 · MIT (+ghi chú) | Luật VN 2025–2026, web + mobile | Triage bằng `scan.sh` + fixture CI. Đánh dấu `CHƯA XÁC MINH` tại chỗ |
| `waldo-van-der-code/deutsches-recht-mit-claude` | 44 · MIT (`4c5e72d`, 20/10/2026) | DSGVO/BFSG/Widerruf của Đức | Mẫu gần nhất: 4 skill thuần Markdown, `/legal-audit` quét code hoặc URL. Không có script quét hay test |
| `mukul975/Privacy-Data-Protection-Skills` | 328 · Apache-2.0 (`9b2ef9e`, 16/3/2026) | 282+ skill GDPR/CCPA/PIPL/DPDP… | Rộng nhưng phần Việt Nam còn dẫn NĐ 13/2023 đã hết hiệu lực |
| `Sushegaad/Claude-Skills-Governance-Risk-and-Compliance` | 1.031 · MIT | ISO 27001, SOC 2, GDPR… | Hướng dẫn GRC tổng quát, không theo luật VN **(chỉ đọc mô tả)** |
| `greenarmor/GESF` (mục 09 §2b) | 48 · MIT | GDPR/OWASP/CIS dạng control JSON | CLI tự chấm điểm, không có checklist VN |

**Tích hợp**

- Dùng làm **bước rà soát ban đầu** trước khi phát hành site hoặc app có người dùng Việt Nam. Không dùng làm bằng chứng tuân thủ gửi ra ngoài. Ghim commit hoặc tag khi cài (`git clone` rồi checkout `5847e32`) thay vì `curl | bash` vào `main`.
- Dự án đã có khung compliance (X-Templates `framework/16-compliance-privacy/vietnam-data-law.md`) nên đối chiếu từng mốc thời hạn và số điều, chưa nên nhúng nguyên bộ. Phần đáng lấy là triage và kỷ luật `CHƯA XÁC MINH`.
- Khi quét URL của site người khác: chỉ dùng kết quả để báo riêng cho chủ site, đúng như README dặn.

**Liên quan:** mục 09 §2b (GESF), mục 20 (Claude plugin marketplace, SKILL.md), mục 04 (AGENTS.md), §4b (pháp lý số tại VN, nhận định NĐ 13/2023 lấy từ docs nội bộ đã cũ), mục 23.

**Nguồn §4e:** clone đủ lịch sử `mhfed/vn-law-check` HEAD `5847e324337faab6886b6aedfd4e9bea4e0f2fea` (3/11/2026) · GitHub search API 3/11/2026 (`repo:mhfed/vn-law-check`, `user:mhfed`, 3 truy vấn chủ đề compliance/GDPR skill) · clone `--depth 1 --filter=blob:none`: `waldo-van-der-code/deutsches-recht-mit-claude` `4c5e72d`, `mukul975/Privacy-Data-Protection-Skills` `9b2ef9e` (grep "Decree 13/2023") · https://www.ey.com/vi_vn/technical/tax/tax-and-law-updates/nghi-dinh-so-356-2025-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-va-bien-phap-thi-hanh-luat-bao-ve-du-lieu-ca-nhan · https://luatvietan.vn/diem-moi-cua-nghi-dinh-356-2025-so-voi-nghi-dinh-13-2023-ve-huong-dan-bao-ve-du-lieu-ca-nhan.html · https://english.luatvietnam.vn/legal-updates/the-latest-law-on-personal-data-protection-and-the-guiding-documents-892-106778-article.html

## 5. Gợi ý bổ sung tiếp

- Thêm link GitHub cụ thể của từng model/toolkit (số sao, ngày cập nhật) khi có.
- Theo dõi: Hugging Face `vinai`, `VietAI`, `Vi-VLM`, `GreenNode`; GitHub topic `vietnamese-nlp`.

## 5b. Nâng trần 2/11/2026: benchmark tiếng Việt chạy được và cổng kiểm văn bản tiếng Việt (yêu cầu người dùng)

> Tìm cổng đo cho model và văn bản tiếng Việt. Gồm 6 truy vấn GitHub ("vietnamese benchmark llm", "vietnamese llm evaluation", "VNHSGE", "vietnamese mteb", "SEA-HELM", "vietnamese eval") và đọc mã của ba bộ đánh giá lớn (MTEB, lm-evaluation-harness, HELM) để đếm task tiếng Việt. Số sao lấy từ GitHub search API ngày 2/11/2026. **Không chạy mã nào của các repo.** Hệ sinh thái nhỏ: phần lớn benchmark tiếng Việt riêng lẻ trên GitHub có dưới 5★ (VLegal-Bench, V-MTEB của haisonle001, ViLegalREB…), nên không thêm.

**Trần hiện tại**

- Benchmark LLM duy nhất là VMLU (§4c), đóng băng từ 5/2024. Embedding tiếng Việt (§4c) chỉ có điểm **tự báo cáo** trên một tập pháp luật.
- §4d.4 ý 5 đã ghi: thiếu leaderboard độc lập. TTS và ASR chỉ có benchmark tự làm.
- Chưa có **cổng máy cho văn bản tiếng Việt** do agent sinh (Unicode NFC, kiểu đặt dấu, câu dịch máy), dù các repo của chủ kho viết toàn bằng tiếng Việt (§4b).

**Bảng repo mới**

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `embeddings-benchmark/mteb` (benchmark **VN-MTEB**) | Cổng máy | 3,5k · Apache-2.0 | 2/11/2026 | Benchmark `VN-MTEB (vie, v1)` gồm **50 task**: 24 retrieval, 12 classification, 5 clustering, 3 pair-classification, 3 reranking, 3 STS. Tham chiếu EACL 2026 Findings. Đã khai báo sẵn model tiếng Việt trong `vi_vn_models.py`: bi-encoder BKAI, AITeamVN/Vietnamese_Embedding (§4c), 4 model GreenNode, halong_embedding, sup-SimCSE PhoBERT | Tên task (`MSMARCO-VN`, `FiQA2018-VN`, `Banking77VNClassification`…) cho thấy phần lớn được dịch từ tập tiếng Anh, có thể lệch tiếng Việt tự nhiên. Cách dịch **(chưa xác minh)** |
| `aisingapore/SEA-HELM` | Cổng máy | 42 · LICENSE là MIT, `pyproject.toml` ghi Apache-2.0 | 5/8/2026 | Bộ đánh giá LLM Đông Nam Á của AI Singapore (v1.3.0), làm nền cho leaderboard SEA-LION. Khoảng **20 nhóm task có cấu hình `vi`**: NLU, NLG, NLR, an toàn (toxicity, nội dung văn hoá), IFEval, MT-Bench, long-context, vision. Điểm tính trên 8 lượt chạy, có khoảng tin cậy | ❌ License trong file và trong manifest mâu thuẫn. Python ghim 3.12, phụ thuộc flashinfer bản cu129 (cần GPU NVIDIA). Ít sao |
| `Xdao85/VNHSGE` | Dữ liệu benchmark | 31 · **không có LICENSE** | 30/10/2026 | Đề thi tốt nghiệp THPT: 9 môn, 19.000 câu trắc nghiệm + 300 câu tự luận Văn, có ảnh, song ngữ (arXiv 2305.12199). Ngày 30/10/2026 thêm bộ train/test cho 5 môn; `Dataset/NOTES.md` ghi lại mọi chỗ sửa tay | Không có LICENSE nên chưa được cấp quyền dùng. Một phần lấy từ sách đề thi thử có bản quyền (theo NOTES). Đề công khai 2019–2023 nhiều khả năng đã nằm trong dữ liệu huấn luyện của model (nhiễm dữ liệu) |
| `jangtrinh/design-os-vietnamese` | Cổng máy (lint văn bản) | 10 · **PolyForm Shield 1.0.0** (không phải license OSI) | 1/11/2026 | Linter offline `shared/scripts/validate_copy.py` (1.745 dòng): chuẩn hoá NFC, kiểu dấu cũ/mới (`hoà`/`hòa`), câu dịch máy, luật theo ngành. `check_i18n_parity.py` kiểm khớp khoá và plural ICU giữa en/vi. Có 16 skill cho Claude Code/Codex/Gemini, CI chạy unittest | PolyForm Shield cấm dùng trong sản phẩm cạnh tranh với tác giả. ⚠️ README ghi "489 golden evaluation pairs" nhưng đếm được **575 dòng** trong `evals/*/pairs.jsonl`. Luật pháp lý trong rule chưa đối chiếu văn bản gốc. Tác giả cũng là upstream của `design-os-3d-blender` (mục 23 §6.1) |

**Cổng có sẵn trong công cụ kho đã có (không thêm vào catalog):**

- `EleutherAI/lm-evaluation-harness` (mục 07) có task tiếng Việt chạy ngay. Đếm file theo nhóm: `global_mmlu` vi (64), `mmlu_prox` (33), `include` (18), `mlqa` (13), `global_piqa` (4), `okapi` (5), cùng `belebele` `vie_Latn`, `xcopa`, `xnli`, `xquad`.
- `stanford-crfm/helm` (mục 07 đã loại vì vào chế độ bảo trì từ 1/6/2026) chứa bộ **MELT** cho tiếng Việt, 21 scenario: ViMMRC, Zalo QA, VSEC (sửa chính tả), VLSP/VSFC (cảm xúc), ViHSD/ViCTSD (độc hại), PhoMT, VietNews, kèm metric thiên kiến và độc hại. ⚠️ "VHELM" trong HELM là đánh giá **vision-language**, không phải tiếng Việt.

**Stack nâng trần**

1. **RAG tiếng Việt**: chạy phần retrieval của VN-MTEB cho bi-encoder BKAI và Vietnamese_Embedding (§4c) trên cùng cấu hình, thay cho MRR tự báo cáo. Ghép BM25 qua `elasticsearch-analysis-vietnamese` (§4d), rồi đo lại.
2. **Chọn LLM**: dùng task `vi` của lm-evaluation-harness (global_mmlu vi, belebele) làm cổng nhanh trong CI. VMLU (§4c) và VNHSGE đo kiến thức phổ thông. SEA-HELM dùng khi cần đánh giá rộng, có an toàn và văn hoá.
3. **Văn bản agent sinh**: chuẩn hoá NFC, thống nhất một kiểu đặt dấu và kiểm khớp khoá i18n en/vi trước khi merge nội dung UI. Lấy ý tưởng từ design-os-vietnamese; nếu sản phẩm có thể cạnh tranh với tác giả thì tự viết lại, đừng nhúng mã.
4. **Chống nhiễm dữ liệu**: giữ một tập test riêng gồm đề hoặc văn bản ra đời **sau** mốc dữ liệu của model, và công bố phương pháp (bài học từ gipformer, §4d).

**Nguồn §5b:** GitHub search API 2/11/2026 (6 truy vấn chủ đề; `repo:` cho 6 repo) · clone `--filter=blob:none`: embeddings-benchmark/mteb (HEAD `da9f201` 2/11/2026: LICENSE, `mteb/benchmarks/benchmarks/benchmarks.py` khối `VN_MTEB`, `mteb/models/model_implementations/vi_vn_models.py`), aisingapore/SEA-HELM (`9be3986` 5/8/2026: LICENSE, README.md, pyproject.toml, `seahelm_tasks/**` khoá `vi:`), Xdao85/VNHSGE (`04c845d` 30/10/2026: README.md, `Dataset/NOTES.md`, cây file), jangtrinh/design-os-vietnamese (`63dc654` 1/11/2026: LICENSE, README.md, `shared/scripts/validate_copy.py`, `evals/*/pairs.jsonl`, `.github/workflows/ci.yml`), EleutherAI/lm-evaluation-harness (`d6de816` 14/9/2026: cây `lm_eval/tasks`), stanford-crfm/helm (`63754d0` 5/6/2026: `run_entries_melt.conf`, `melt_*` scenario, `docs/vhelm.md`) · https://aclanthology.org/2026.findings-eacl.86/ · https://arxiv.org/abs/2305.12199 · https://leaderboard.sea-lion.ai/

## 5c. Vietnamese domain evaluation

> Mở rộng ngày 2/11/2026. §5b đã có VMLU/VN-MTEB/SEA-HELM và linter tiếng Việt; mục tiêu tiếp theo là **đúng domain, bền trước biến thể ngôn ngữ, hiển thị đúng trong sản phẩm**. Không coi một điểm leaderboard là đủ để chọn model cho mọi ứng dụng tiếng Việt.

### 5c.1 Retrieval theo domain và phương ngữ

| Nguồn | Cơ chế / giá trị | Trạng thái kiểm và giới hạn |
|---|---|---|
| [ViRE — longstnguyen/ViRE](https://github.com/longstnguyen/ViRE/tree/60ea7155134eaa426ab1d0a82d2bbbf327d1b470) | Benchmark retrieval đa domain; [paper EACL 2026](https://aclanthology.org/2026.findings-eacl.110/) mô tả sáu domain, mười dataset và so lexical/dense/sparse/late-interaction/hybrid cùng giao thức | 7★ · code MIT · HEAD `60ea715` (2026-10-17), đọc 2/11/2026. Đọc README, LICENSE và mã eval; quyền dữ liệu nguồn phải kiểm từng dataset, không suy ra từ code MIT; chưa tái lập điểm |
| [VialectBench](https://vialectbench.github.io/) + [paper](https://arxiv.org/abs/2608.10414) | So cặp câu chuẩn/phương ngữ giữ nguyên ý và nhãn; đo giảm điểm và đổi từ đúng sang sai | Đã đọc trang/paper metadata 2/11/2026; link “Code” trên trang dẫn tới tổ chức chỉ thấy website công khai, chưa xác minh có harness và tập dữ liệu đầy đủ. Chỉ dùng thiết kế phép đo và ví dụ công khai; không gọi là bộ eval đã chạy được |
| VMLU / SEA-HELM / VN-MTEB (§5b) | Năng lực tổng quát, văn hóa/an toàn và embedding retrieval | Dùng làm baseline; [paper VMLU](https://aclanthology.org/2025.acl-long.563/) cho thấy thiết kế prompt ảnh hưởng kết quả, nên luôn ghi template/chat format và revision |

**ViRE (Long S. T. Nguyen, Tho T. Quan):** khác bảng xếp hạng model đơn lẻ ở chỗ giữ giao thức so retrieval xuyên domain. Nên lấy tập giống dữ liệu sản phẩm và so BM25, embedding, hybrid rồi reranker trong cùng corpus/chunking; không chuyển kết quả trên bộ giáo dục thành lời khuyên chắc chắn cho pháp lý/y tế. Liên kết cổng nDCG/Recall và chunking ở mục 10, kiểm dữ liệu ở mục 15, chống nhiễm tập test ở mục 24. Đọc [`cli.py`](https://github.com/longstnguyen/ViRE/blob/60ea7155134eaa426ab1d0a82d2bbbf327d1b470/src/vi_retrieval_eval/cli.py) và [`metrics.py`](https://github.com/longstnguyen/ViRE/blob/60ea7155134eaa426ab1d0a82d2bbbf327d1b470/src/vi_retrieval_eval/metrics.py): quickstart lấy mẫu cả query và candidate corpus; metric loại gold index ngoài miền và có heuristic đổi chỉ số 1-based. Vì vậy phải báo kích thước candidate pool, kiểm coverage/qrels và chuẩn hóa ID tường minh trước khi so hệ thống; điểm trên corpus lấy mẫu không đại diện chỉ mục production đầy đủ.

### 5c.2 Chuẩn Unicode và bản địa hóa

| Lớp | Quy tắc tham khảo | Cổng nên có |
|---|---|---|
| Nội dung lưu/truy vấn | [UAX #15 — Unicode Normalization Forms](https://www.unicode.org/reports/tr15/) | Kiểm cặp NFC/NFD tiếng Việt cho tìm kiếm, khóa và so khớp; lưu bản gốc khi cần audit. NFKC là compatibility normalization, không tự thay NFC hay bỏ dấu |
| Ngày, số, tiền, plural | [UTS #35 / CLDR](https://www.unicode.org/reports/tr35/) | Test `vi-VN`, `en-US` và timezone do người dùng chọn; không ghép chuỗi số/ngày bằng tay. Việc tiếng Việt ít biến thể plural không cho phép bỏ placeholder ở locale khác |
| Catalog dịch và UI | i18next/Lingui/Weblate ở [mục 06 §7u](../06-ui-ux-design/README.md#i18n-lifecycle-2026-11-02) | Kiểm key thiếu/thừa, placeholder, glossary; pseudo-localization, font dấu Việt và overflow; người có chuyên môn duyệt thuật ngữ |
| Giọng nói | WER/CER + task outcome ở [mục 14 §5e](../14-voice-multimodal/README.md#5e-voice-reliability) | Cùng câu chuẩn/phương ngữ, số tiền, tên riêng, địa chỉ; báo từng nhóm giọng/điều kiện ồn, không chỉ điểm gộp |

UAX #15 được đọc ở bản revision 58 (12/8/2026); CLDR và runtime được ghim phiên bản khi dự án đích chạy. Cổng NFC không sửa được câu sai nghĩa; cổng linter tiếng Việt (§5b) không thay người chấm nội dung chuyên ngành.

### 5c.3 Thang đánh giá cho sản phẩm tiếng Việt

1. Chọn use case và hậu quả sai: gia sư, tìm tài liệu, OCR biểu mẫu hay điều khiển công cụ; gán owner/rubric riêng, giữ tập test ngoài dữ liệu tune.
2. Báo baseline công khai và tập giữ riêng theo domain; chia kết quả theo vùng/ngôn ngữ trộn, độ dài, dấu và trường quan trọng; dùng confidence interval hoặc số lượng mẫu thay vì chỉ một tỷ lệ.
3. Lưu model revision, prompt, retrieval corpus/chunking, normalizer, rubric và người chấm. Nhận định pháp lý ở §4b/§7 của mục 23 vẫn là dữ liệu từ docs nội bộ **(chưa xác minh)** cho đến khi đối chiếu văn bản gốc.
4. Dùng replay để CI phát hiện thay đổi giao thức và ca đã biết; lấy mẫu chạy live định kỳ để phát hiện provider/model drift. Replay không chứng minh chất lượng trả lời của model hiện tại.
5. Chỉ phát hành khi task outcome, an toàn và bản địa hóa đều qua cổng; liên kết kết quả với commit sản phẩm để không tái dùng báo cáo cũ sau khi đổi model/prompt.

**Nguồn §5c:** GitHub metadata/clone ViRE ngày 2/11/2026 (LICENSE, README, mã eval) và permalink trên; paper EACL 2026, VMLU ACL 2025, VialectBench (trang công bố; harness đầy đủ chưa xác minh), Unicode UAX #15 và UTS #35. Không tải dữ liệu người dùng và không chạy benchmark.

## 5d. Hồ sơ jangtrinh/design-os-vietnamese: 16 skill viết tiếng Việt theo ngành, linter tất định và kho tri thức có neo SHA-256 (link người dùng gửi, đọc mã 3/11/2026)

> §5b chỉ có một dòng bảng. Đây là hồ sơ đầy đủ, đọc lại tại `63dc65459628c72bf44691ded75c195d69f9e1d7` (1/11/2026). Upstream **không có commit mới** kể từ lần đọc 2/11. Clone `--filter=blob:none`, 63 commit từ 26/10/2026. **Không chạy mã** (`validate_copy.py`, `verify_ukmc.py`, test).

### 5d.1 Hồ sơ nhanh

| Thuộc tính | Giá trị (3/11/2026) |
|---|---|
| Repo | https://github.com/jangtrinh/design-os-vietnamese · **10★, 0 fork**, 0 issue mở (GitHub search API) |
| Tác giả | Jang Trịnh (`jangtrinh`), một người: 62/63 commit. Cũng là upstream của `design-os-3d-blender` (mục 23 §6.1). 36 dòng trailer Co-Authored-By |
| License | **PolyForm Shield 1.0.0** (GitHub hiển thị `NOASSERTION`): source-available, **cấm dùng trong sản phẩm cạnh tranh** với tác giả. Không phải license OSI, nên catalog ghi `open_source: false` |
| Nội dung | **16 skill** cho Claude Code, Codex, Gemini CLI, Antigravity: landing, e-commerce, tài chính, bảo hiểm, y tế, giáo dục, pháp lý–hợp đồng, nhân sự, chính phủ–dịch vụ công, bất động sản–xây dựng, du lịch, truyền thông–PR, an ninh mạng, tech writing, business comms, design system UX. Có `shared/references/` dùng chung (register-matrix 31 đối tượng, banned-phrases, compliance, locale-formatting) và mỗi skill có một bản copy |
| Cổng máy | `shared/scripts/validate_copy.py` (1.745 dòng, chỉ dùng thư viện chuẩn) với 23 mã rule kiểu `LAW001`, `PROD004`, `SPAM001`, `PLAIN001–007`… Thêm `plain_tone.py`, `check_i18n_parity.py`, `check_font_coverage.py` và `writing_context.py`. CI chạy `self_check.py`, `verify_ukmc.py`, `unittest` và pre-commit |
| Kho tri thức | 18 module "UKMC.v1" trong `knowledge/`. Mỗi đoạn có neo `<!-- ease:source uri=… sha256=… -->` trỏ tới nguồn đã đóng băng trong `knowledge/_evidence/vn-design-os-261026/sources/` (văn bản tải từ vbpl.vn, hethongphapluat.com, hoatieu.vn) |

### 5d.2 Điểm đáng học

- **Kiểm hiệu lực văn bản bằng dữ liệu máy đọc.** Báo cáo `plans/reports/knowledge-261028-2016-legal-validity-and-rule-variant-tables.md` (28–29/10) lấy trạng thái từ trường schema.org `legislationLegalForce` trên trang vbpl.vn (InForce, NotInForce, PartiallyInForce) và đóng băng thành dòng 1 của mỗi file nguồn. Đợt này đã **gỡ nhận định cũ coi NĐ 13/2023 là văn bản đang hiệu lực** (`state.json`, `retired_claim_ids`) và chuyển sang Luật 91/2025 + NĐ 356/2025, kèm NĐ 330/2026 về xử phạt. Đây là cách làm chặt hơn hẳn cách "tóm tắt từ blog luật".
- **Đếm nguồn độc lập theo nhà xuất bản, không theo file.** Báo cáo tự ghi: hai file của cùng một nơi chỉ là một nguồn. Kết quả: 3 nhà xuất bản bên ngoài, 0 trước đợt này.
- **Reviewer độc lập khác model** (`review.json`: `passed: true`, 29/10/2026). Rule có "negation guard": "không phải số 1" không bị bắt là quảng cáo bậc nhất. Muốn giữ claim bậc nhất thì phải ghi chú `<!-- proof: … -->`.

### 5d.3 Lệch giữa README, cổng và nội dung (tự kiểm)

- ⚠️ **Module TMĐT vẫn theo khung cũ.** `shared/references/compliance.md` §4 (footer bắt buộc, mã `LND004`) và `knowledge/ecommerce-retail-and-consumer-law.md` dẫn **NĐ 52/2013 + NĐ 85/2021**, không nhắc **Luật TMĐT 122/2025** (hiệu lực 01/07/2026) và NĐ 248/2026. Grep `122/2025|248/2026` trong repo không có kết quả. Đợt kiểm hiệu lực 28/10 không có TMĐT trong bảng, và nguồn của module này là corpus do dự án tự viết (`06-realestate-ecommerce-…-corpus.md`). Theo vn-law-check (§4e), website đăng ký theo khung cũ còn hoạt động được tới 30/06/2027. Nội dung footer có đổi hay không **(chưa xác minh)**.
- ⚠️ **README chỉ nêu cổng dễ hơn.** README ghi 18 module "STOP_SUFFICIENT"; `verify_ukmc.py` đúng là trả kết quả đó. Nhưng cổng chặt hơn của chính dự án (`kb gate`) vẫn là **DEEPEN** (§14 của báo cáo), vì mới bão hòa 1/3 vòng và còn câu hỏi mở: điều khoản nào của Luật KDBĐS 29/2023 đã hết hiệu lực, nghị định nào thay NĐ 15/2018, từ điển. `state.json`: `status: RUNNING`, vòng 13.
- ⚠️ README ghi "489 golden evaluation pairs" nhưng `evals/*/pairs.jsonl` (17 file) có **575 dòng**, đúng như §5b đã ghi. Chưa sửa.
- `register-matrix.md` và `compliance.md` được copy vào từng skill. Sửa ở `shared/` mà không đồng bộ thì các bản copy lệch nhau, và repo không có cổng chặn lệch kiểu `sync.sh --check` của vn-law-check **(chưa thấy, chưa kiểm hết `self_check.py`)**.

### 5d.4 So với cùng loại

| Repo | ★ (3/11) | License | Khác |
|---|---|---|---|
| **jangtrinh/design-os-vietnamese** | 10 | PolyForm Shield | Viết tiếng Việt theo ngành, linter tất định, tri thức có neo SHA-256 + reviewer độc lập |
| `mhfed/vn-law-check` (§4e) | 126 | MIT (+ghi chú) | Audit pháp lý website/app, không viết copy. Đã theo Luật TMĐT 122/2025 |
| antislop (mục 06 §7i) | 8k | MIT | Lọc "AI slop" cho UI và văn bản tiếng Anh, không có luật VN |
| X-Templates `framework/16-compliance-privacy` | – | – | Khung yêu cầu, không phải linter |

### 5d.5 Dùng thế nào

- Lấy **ý tưởng** linter (NFC, kiểu dấu, câu dịch máy, claim bậc nhất có proof, giờ gửi tin quảng cáo) và cách neo nguồn bằng hash. Nếu sản phẩm của bạn có thể cạnh tranh với tác giả thì đừng nhúng mã (PolyForm Shield).
- Với nội dung TMĐT, đối chiếu thêm Luật 122/2025 và NĐ 248/2026 trước khi tin rule `LND004`. Với dữ liệu cá nhân thì module đã cập nhật theo luật mới.
- Đọc `plans/reports/…legal-validity…md` §14 để biết những phần nào còn mở trước khi dùng các module tương ứng.

**Nguồn §5d:** link người dùng gửi 3/11/2026 · clone https://github.com/jangtrinh/design-os-vietnamese HEAD `63dc65459628c72bf44691ded75c195d69f9e1d7` (README.md, LICENSE, `shared/references/{compliance,register-matrix,banned-phrases}.md`, `shared/scripts/*.py`, `knowledge/ecommerce-retail-and-consumer-law.md`, `knowledge/_evidence/vn-design-os-261026/{state,review}.json`, `plans/reports/knowledge-261028-2016-legal-validity-and-rule-variant-tables.md`, `.github/workflows/*`, `evals/*/pairs.jsonl`; grep `122/2025|248/2026|52/2013|85/2021`) · GitHub search API `repo:jangtrinh/design-os-vietnamese` 3/11/2026.

<a id="factory-vietnam-product-2026-11-04"></a>

## 5e. Nâng trần 4/11/2026: tiếng Việt phải đi qua hợp đồng sản phẩm và dữ liệu nghiệp vụ

**Trần và khoảng trống.** Mục này có mô hình/NLP, dữ liệu địa giới, benchmark và skill pháp lý; mục 14 có giọng nói, mục 26 có OCR. Xưởng còn cần kiểm **người dùng Việt hoàn thành tác vụ thật**: đăng ký, tìm kiếm, địa chỉ, ngày/tiền, tải tài liệu và hỗ trợ. Điểm benchmark ngôn ngữ cao không chứng minh biểu mẫu, hóa đơn hay luồng phục hồi tài khoản đúng.

### 5e.1 libphonenumber: chuẩn hóa và kiểm số điện thoại, tách khỏi xác minh chủ thể

| Thuộc tính | Kết quả đọc 4/11/2026 |
|---|---|
| Repo / tác giả | `google/libphonenumber`; thư viện gốc Java/C++/JavaScript của Google và cộng đồng; không phải dự án chỉ cho Việt Nam |
| License · phiên bản | Apache-2.0; HEAD `c9b437b1251b59a71efbd054999ae26f624b0079`; không thu thập sao; wrapper ngôn ngữ khác có vòng phát hành/license riêng |
| Mã đã đọc | `PhoneNumberUtil.isValidNumber` tìm region rồi gọi `isValidNumberForRegion`; nhánh region kiểm country calling code, metadata và type pattern |
| Giới hạn quan trọng | “Valid” là dải/mẫu số phù hợp metadata, **không biết số đang được cấp hay ai sở hữu**. FAQ yêu cầu bước xác minh riêng nếu cần chứng minh reachability; short number nằm ở `ShortNumberInfo` |
| CI | `java-unit-test.yml` chạy Maven tests và Ant JUnit; không đồng nghĩa mọi wrapper JS/Python có cùng metadata hôm nay; chưa chạy thư viện trong đợt này |
| Tích hợp | Parse với region phù hợp khi thiếu mã quốc gia; lưu dạng chuẩn hóa để đối chiếu, hiển thị dạng phù hợp người dùng; không tự đổi quốc gia chỉ theo vị trí IP |

[Implementation và callsite]( https://github.com/google/libphonenumber/blob/c9b437b1251b59a71efbd054999ae26f624b0079/java/libphonenumber/src/com/google/i18n/phonenumbers/PhoneNumberUtil.java ) · [FAQ possible/valid/reachable]( https://github.com/google/libphonenumber/blob/c9b437b1251b59a71efbd054999ae26f624b0079/FAQ.md ) · [các giả định hay sai]( https://github.com/google/libphonenumber/blob/c9b437b1251b59a71efbd054999ae26f624b0079/FALSEHOODS.md ) · [license]( https://github.com/google/libphonenumber/blob/c9b437b1251b59a71efbd054999ae26f624b0079/LICENSE ) · [CI]( https://github.com/google/libphonenumber/blob/c9b437b1251b59a71efbd054999ae26f624b0079/.github/workflows/java-unit-test.yml ).

### 5e.2 So lựa chọn theo tác vụ của sản phẩm Việt Nam

| Tác vụ | Lựa chọn / baseline | Cổng nghiệm thu ở dự án dùng |
|---|---|---|
| Số điện thoại | libphonenumber; regex hẹp nếu chỉ kiểm cú pháp; input mask để hỗ trợ nhập; OTP qua provider khi cần xác minh | Phân biệt parse, valid pattern và verified ownership. Ca có `+84`, số nội địa, khoảng trắng, số nước ngoài, máy bàn, short number và metadata đổi |
| Tên/địa chỉ | Dữ liệu địa giới đã có §4d + lưu version nguồn; form văn bản linh hoạt khi không có mã phù hợp | Không suy tên người từ hai trường first/last bắt buộc; giữ địa chỉ lịch sử theo thời điểm giao dịch, có ánh xạ địa giới mới/cũ, không ghi đè dữ liệu cũ chỉ vì danh mục mới |
| Dịch giao diện | Lingui/Weblate (mục 13) hoặc tập message nhỏ được review; NLP/model ở §1–§3 cho tác vụ riêng | Key thiếu, placeholder đổi kiểu, plural/date/currency, Unicode và layout dài; screenshot/luồng người dùng với nội dung tiếng Việt thật |
| Tìm kiếm/RAG | Baseline có/không dấu; PhoBERT/embedding/ViRE đã có §3, §5b–§5c | Corpus truy vấn miền ứng dụng, alias/viết tắt, tên riêng và không dấu; đo theo nhóm truy vấn, không lấy một điểm retrieval làm điểm đúng câu trả lời |
| Pháp lý và dữ liệu cá nhân | `vn-law-check`, DESIGN:OS Vietnamese (§4e, §5d) để triage có bằng chứng; người có trách nhiệm đối chiếu văn bản gốc | Ghi văn bản/hiệu lực/phạm vi và điều chưa xác minh; checklist của skill không phải ý kiến pháp lý hay chứng nhận tuân thủ |

### 5e.3 Pipeline nghiệm thu cho một sản phẩm phục vụ người Việt

1. Chọn vài luồng tạo giá trị cụ thể, persona và thiết bị; mỗi luồng giữ input mẫu đã ẩn danh, kết quả mong đợi và người chịu trách nhiệm nội dung.
2. Đóng băng version của message catalog, thư viện locale/phone và dữ liệu địa giới. Không trộn ngày snapshot với ngày pháp lý có hiệu lực; nguồn dữ liệu hành chính và quyền phân phối phải được xem riêng.
3. Test tất định các ranh giới: Unicode tổ hợp/tách dấu, dấu nháy/tên dài, số/tiền/ngày, locale/timezone, biểu mẫu và thông báo lỗi. Chuẩn hóa để tìm kiếm không được làm mất bản gốc cần hiển thị/chứng từ.
4. Chạy kiểm frontend/backend cùng contract; giữ ví dụ không hợp lệ và thông báo có thể sửa được. Mask, parser và server phải không bất đồng đến mức người dùng được gửi rồi bị từ chối không rõ lý do.
5. Với LLM/ASR/OCR, phân nhóm miền ứng dụng và vùng giọng/loại tài liệu như §5b–§5c và mục 14/26; giữ ca có chi phí lỗi cao, tỷ lệ từ chối và đường chuyển người thật.
6. Nghiệm thu accessibility/E2E (mục 30), đo completion/drop-off có sự đồng ý phù hợp (mục 28), review lại khi danh mục địa giới, cách đánh số hoặc văn bản nguồn đổi. Ngưỡng chất lượng phải do sản phẩm đặt; đợt này không có số đo người dùng mới.

**Đã nâng sâu:** từ danh sách công cụ/cộng đồng tiếng Việt sang hợp đồng đầu vào, phiên bản dữ liệu và luồng nghiệm thu sản phẩm. libphonenumber không tự xử lý tên/địa chỉ hay xác minh pháp lý; các nhánh đó có baseline riêng.

**Nguồn §5e:** implementation/LICENSE/CI/FAQ/`FALSEHOODS.md` upstream đã ghim; các hồ sơ địa giới, benchmark, pháp lý hiện có trong mục này và localization mục 13. Chưa gọi OTP, không dùng dữ liệu khách hàng thật, không chạy upstream.

## 6. Nguồn

- https://www.emergentmind.com/topics/phogpt · https://arxiv.org/html/2509.26189v2 · https://arxiv.org/html/2608.25478 · https://ai.stanford.edu/blog/crossing-linguistic-horizon/ · https://aisean.org/resources/ · https://huggingface.co/Vi-VLM/Vistral-V-7B · https://github.com/vndee/awsome-vietnamese-nlp
- https://pypi.org/project/underthesea/ · https://github.com/undertheseanlp/underthesea · https://aclanthology.org/N18-5012/
- https://www.sotatek.com/newsroom/sotatek-contributes-to-vigen-vietnams-first-open-source-vietnamese-language-dataset-for-ai/ · https://technode.global/2026/06/18/vietnams-developers-are-moving-from-outsourcing-to-ai-building/ · https://morsoftware.com/news/codex-community-hackathon-hanoi-2026 · https://www.vietnam.vn/en/khoi-dong-cuoc-thi-vietnam-ai-open-hackathon-2026 · https://www.vietnam.vn/en/lam-chu-ai-va-phat-trien-phan-mem-nguon-mo-an-toan · https://www.openhackathons.org/s/siteevent/a0CUP00004VRMiz2AH/se000492
- Repo/model đã xác minh (12/10/2026): https://github.com/VinAIResearch/PhoBERT · https://huggingface.co/vinai/phobert-base · https://huggingface.co/vinai/phobert-base-v2 · https://github.com/VinAIResearch/PhoWhisper · https://huggingface.co/vinai/PhoWhisper-large · https://github.com/DAMO-NLP-SG/SeaLLMs · https://huggingface.co/SeaLLMs/SeaLLMs-v3-7B-Chat · https://github.com/pnnbao97/VieNeu-TTS · https://github.com/nguyenthienhy/F5-TTS-Vietnamese · https://huggingface.co/hynt/F5-TTS-Vietnamese-ViVoice · https://github.com/thinhlpg/vixtts-demo · https://huggingface.co/capleaf/viXTTS · https://huggingface.co/bkai-foundation-models/vietnamese-bi-encoder · https://huggingface.co/AITeamVN/Vietnamese_Embedding · https://github.com/ZaloAI-Jaist/VMLU · https://github.com/VinAIResearch/BARTpho · https://github.com/vietai/ViT5 · https://github.com/trungtv/pyvi
