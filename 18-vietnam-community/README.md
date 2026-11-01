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

## 5. Gợi ý bổ sung tiếp

- Thêm link GitHub cụ thể của từng model/toolkit (số sao, ngày cập nhật) khi có.
- Theo dõi: Hugging Face `vinai`, `VietAI`, `Vi-VLM`, `GreenNode`; GitHub topic `vietnamese-nlp`.

## 6. Nguồn

- https://www.emergentmind.com/topics/phogpt · https://arxiv.org/html/2509.26189v2 · https://arxiv.org/html/2608.25478 · https://ai.stanford.edu/blog/crossing-linguistic-horizon/ · https://aisean.org/resources/ · https://huggingface.co/Vi-VLM/Vistral-V-7B · https://github.com/vndee/awsome-vietnamese-nlp
- https://pypi.org/project/underthesea/ · https://github.com/undertheseanlp/underthesea · https://aclanthology.org/N18-5012/
- https://www.sotatek.com/newsroom/sotatek-contributes-to-vigen-vietnams-first-open-source-vietnamese-language-dataset-for-ai/ · https://technode.global/2026/06/18/vietnams-developers-are-moving-from-outsourcing-to-ai-building/ · https://morsoftware.com/news/codex-community-hackathon-hanoi-2026 · https://www.vietnam.vn/en/khoi-dong-cuoc-thi-vietnam-ai-open-hackathon-2026 · https://www.vietnam.vn/en/lam-chu-ai-va-phat-trien-phan-mem-nguon-mo-an-toan · https://www.openhackathons.org/s/siteevent/a0CUP00004VRMiz2AH/se000492
- Repo/model đã xác minh (12/10/2026): https://github.com/VinAIResearch/PhoBERT · https://huggingface.co/vinai/phobert-base · https://huggingface.co/vinai/phobert-base-v2 · https://github.com/VinAIResearch/PhoWhisper · https://huggingface.co/vinai/PhoWhisper-large · https://github.com/DAMO-NLP-SG/SeaLLMs · https://huggingface.co/SeaLLMs/SeaLLMs-v3-7B-Chat · https://github.com/pnnbao97/VieNeu-TTS · https://github.com/nguyenthienhy/F5-TTS-Vietnamese · https://huggingface.co/hynt/F5-TTS-Vietnamese-ViVoice · https://github.com/thinhlpg/vixtts-demo · https://huggingface.co/capleaf/viXTTS · https://huggingface.co/bkai-foundation-models/vietnamese-bi-encoder · https://huggingface.co/AITeamVN/Vietnamese_Embedding · https://github.com/ZaloAI-Jaist/VMLU · https://github.com/VinAIResearch/BARTpho · https://github.com/vietai/ViT5 · https://github.com/trungtv/pyvi
