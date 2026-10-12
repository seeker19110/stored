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

## 5. Gợi ý bổ sung tiếp

- Thêm link GitHub cụ thể của từng model/toolkit (số sao, ngày cập nhật) khi có.
- Theo dõi: Hugging Face `vinai`, `VietAI`, `Vi-VLM`, `GreenNode`; GitHub topic `vietnamese-nlp`.

## 6. Nguồn

- https://www.emergentmind.com/topics/phogpt · https://arxiv.org/html/2509.26189v2 · https://arxiv.org/html/2608.25478 · https://ai.stanford.edu/blog/crossing-linguistic-horizon/ · https://aisean.org/resources/ · https://huggingface.co/Vi-VLM/Vistral-V-7B · https://github.com/vndee/awsome-vietnamese-nlp
- https://pypi.org/project/underthesea/ · https://github.com/undertheseanlp/underthesea · https://aclanthology.org/N18-5012/
- https://www.sotatek.com/newsroom/sotatek-contributes-to-vigen-vietnams-first-open-source-vietnamese-language-dataset-for-ai/ · https://technode.global/2026/06/18/vietnams-developers-are-moving-from-outsourcing-to-ai-building/ · https://morsoftware.com/news/codex-community-hackathon-hanoi-2026 · https://www.vietnam.vn/en/khoi-dong-cuoc-thi-vietnam-ai-open-hackathon-2026 · https://www.vietnam.vn/en/lam-chu-ai-va-phat-trien-phan-mem-nguon-mo-an-toan · https://www.openhackathons.org/s/siteevent/a0CUP00004VRMiz2AH/se000492
- Repo/model đã xác minh (12/10/2026): https://github.com/VinAIResearch/PhoBERT · https://huggingface.co/vinai/phobert-base · https://huggingface.co/vinai/phobert-base-v2 · https://github.com/VinAIResearch/PhoWhisper · https://huggingface.co/vinai/PhoWhisper-large · https://github.com/DAMO-NLP-SG/SeaLLMs · https://huggingface.co/SeaLLMs/SeaLLMs-v3-7B-Chat · https://github.com/pnnbao97/VieNeu-TTS · https://github.com/nguyenthienhy/F5-TTS-Vietnamese · https://huggingface.co/hynt/F5-TTS-Vietnamese-ViVoice · https://github.com/thinhlpg/vixtts-demo · https://huggingface.co/capleaf/viXTTS · https://huggingface.co/bkai-foundation-models/vietnamese-bi-encoder · https://huggingface.co/AITeamVN/Vietnamese_Embedding · https://github.com/ZaloAI-Jaist/VMLU · https://github.com/VinAIResearch/BARTpho · https://github.com/vietai/ViT5 · https://github.com/trungtv/pyvi
