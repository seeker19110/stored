# 25 · Model Adaptation & Post-training

> Từ một model nền đến phiên bản chuyên biệt có thể kiểm chứng: chọn đúng phương pháp, đóng băng dữ liệu, huấn luyện, đánh giá, xuất và triển khai. Khảo sát 2/11/2026; đọc README, LICENSE, CI và các đường mã nêu trong từng hồ sơ. Không cài, build hay chạy training của repo ngoài; mọi nhận xét về tốc độ, VRAM và chất lượng ở đây không phải phép đo tại kho này.

## 1. Phạm vi và ranh giới

Mục này giải quyết **thay đổi tham số hoặc cách hậu huấn luyện model**. [Mục 17](../17-prompt-engineering/README.md) quản lý prompt; [mục 10](../10-local-llm-rag-memory/README.md) quản lý truy xuất/bộ nhớ/inference; [mục 24](../24-ai-data-engineering/README.md) quản lý đầu vào và nhãn; [mục 07](../07-eval-observability/README.md) quản lý đánh giá; serving quy mô thuộc [mục 10](../10-local-llm-rag-memory/README.md).

| Lớp | Thay đổi gì | Câu hỏi quyết định |
|---|---|---|
| Prompt / context | Chỉ dẫn và ví dụ lúc gọi | Có thể giải bằng chỉ dẫn rõ và context đủ hay chưa? |
| RAG | Thông tin được truy xuất | Tri thức có cập nhật, cần dẫn nguồn hay phân quyền từng tài liệu không? |
| SFT | Học từ cặp đầu vào–đáp án / hội thoại mẫu | Có cần hành vi, định dạng hoặc kỹ năng lặp lại mà prompt chưa đạt không? |
| LoRA / QLoRA | Cách cập nhật một tập tham số nhỏ; QLoRA giữ base đã lượng tử hoá | Tài nguyên, kiến trúc và đường xuất có hỗ trợ không? Đây không phải mục tiêu học riêng. |
| Preference tuning / DPO | Học lựa chọn tốt hơn từ cặp chosen–rejected | Cặp đáp án có cùng prompt, khác biệt có ý nghĩa và nhãn đáng tin không? |
| RL với reward | Học bằng rollout và tín hiệu thưởng | Reward có đo đúng kết quả, kiểm được gian lận và đủ ngân sách rollout không? |
| Continued pretraining / full tuning | Học tiếp miền hoặc cập nhật nhiều tham số | Lợi ích dự kiến có đủ bù chi phí, rủi ro quên kiến thức và gánh vận hành không? |

Fine-tune không tự tạo cơ chế trích nguồn, xoá dữ liệu theo yêu cầu hay cập nhật tri thức tức thời. Hệ thống có thể ghép RAG với model đã tune; cần đo đóng góp từng phần bằng baseline tách biệt.

## 2. Chọn công cụ theo nhu cầu

| Nhu cầu | Điểm bắt đầu | Khi cân nhắc lựa chọn khác | Điều phải kiểm trước |
|---|---|---|---|
| Thêm adapter vào pipeline Transformers đang có | PEFT | TRL nếu cần trainer SFT/DPO/GRPO | Model revision, target modules, tokenizer và adapter format |
| Nghiên cứu SFT/preference/RL bằng Python | TRL | verl khi rollout/training phân tán thành nút thắt | Loss masking, reference model, reward và phần cứng được CI phủ |
| Thử nghiệm local với UI, xuất GGUF/định dạng khác | Unsloth | PEFT/TRL cho pipeline nhỏ ít thành phần | License core/Studio riêng, hỗ trợ model/backend và bản export thực |
| Pipeline cấu hình, distributed training | Axolotl | LlamaFactory cho WebUI và nhiều stage trong một sản phẩm | Lưu config đã resolve, checkpoint/restart, tương thích kernel |
| Nhóm cần CLI/WebUI chung cho nhiều model/stage | LlamaFactory | TRL/PEFT nếu cần sửa vòng học sâu | Template hội thoại, schema dataset, stage và dependency pin |
| RL post-training đa GPU, nhiều worker rollout/reward | verl | TRL cho baseline nhỏ dễ kiểm | Ray/resource pool, rollout engine, reward sandbox và replay |

Ba lựa chọn cùng dòng không mặc nhiên thay thế nhau: **PEFT là lớp adapter**, **TRL là lớp thuật toán/trainer**, còn Unsloth/Axolotl/LlamaFactory đóng gói nhiều lớp. So sánh từng đường chạy và từng cấu hình, không cộng số sao thành điểm chất lượng.

## 3. Hồ sơ đọc mã

<a id="peft"></a>

### 3.1. PEFT — adapter là artifact có hợp đồng

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [huggingface/peft](https://github.com/huggingface/peft) |
| Bằng chứng đọc | `d672982142a705f47696db2dd2218805517509cd` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 21,866 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Thêm adapter/LoRA vào model nền; tích hợp Transformers, Diffusers và Accelerate. |
| Đường mã đã đọc | `LoraModel` cùng `PeftModel.save_pretrained()` / `from_pretrained()`: lưu adapter/config, có `selected_adapters`, `safe_serialization=True`, tuỳ chọn lưu embedding. |
| CI đã đọc | Workflow `tests.yml` có bộ test và kiểm chất lượng; sự hiện diện của workflow không chứng minh model tuỳ chọn đã được kiểm trên phần cứng của người dùng. |
| Tích hợp | Dùng PEFT trong dự án huấn luyện; manifest phải ghim base revision, tokenizer revision, adapter config và hash artifact. Kiểm tải lại adapter trong tiến trình inference sạch. |
| Hạn chế / rủi ro | Một adapter không mang đầy đủ base model. `target_modules`, phần embedding bổ sung và phiên bản thư viện ảnh hưởng tính tương thích; checkpoint adapter và model đã merge cần hai kết quả eval riêng. |
| Bài học kiến trúc | Đơn vị phát hành là **base + adapter + tokenizer + config**, không chỉ một thư mục trọng số. License Apache của thư viện không cấp thêm quyền cho base/weights/dataset. |
| Thay thế / liên quan | TRL (trainer), Axolotl/LlamaFactory (đóng gói pipeline), mục 24 và mục 07. |

**Nguồn hồ sơ:** [README](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/README.md) · [LICENSE](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/LICENSE) · [save/load artifact](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/src/peft/peft_model.py) · [LoRA](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/src/peft/tuners/lora/model.py) · [CI](https://github.com/huggingface/peft/blob/d672982142a705f47696db2dd2218805517509cd/.github/workflows/tests.yml).

<a id="trl"></a>

### 3.2. TRL — SFT, preference và RL dùng chung nền trainer

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [huggingface/trl](https://github.com/huggingface/trl) |
| Bằng chứng đọc | `c734c60d85766aff4542a00643a2ca7e4a3c72ac` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 19,657 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Các trainer SFT, DPO, GRPO trên hệ Transformers; ghép PEFT và backend phân tán khi phù hợp. |
| Đường mã đã đọc | `sft_trainer.py` phân biệt dataset language-modeling với prompt–completion và hội thoại, kiểm `assistant_only_loss` / `completion_only_loss`; đã đọc đường DPO và GRPO để phân biệt preference pair với rollout/reward. |
| CI đã đọc | Workflow `tests.yml` định nghĩa nhiều job/nhóm test; không suy từ test Python sang tương đương số học của mọi GPU/backend. |
| Tích hợp | Cố định trainer/config, render vài mẫu thành token và mask trước training; giữ log reward riêng với metric chất lượng held-out; ghim phiên bản Transformers/PEFT theo đường chạy. |
| Hạn chế / rủi ro | Tối ưu loss sai vị trí có thể dạy model lặp lại user/system prompt. Một cờ assistant-only không thay việc kiểm template hỗ trợ mask. Reward tăng không bảo đảm task success hoặc an toàn tăng. |
| Bài học kiến trúc | Trình bày rõ **schema dữ liệu → template → token/mask → loss**. Kiểm lớp trung gian này trước khi tăng số GPU hay độ phức tạp thuật toán. |
| Thay thế / liên quan | PEFT cho adapter; verl cho RL phân tán; Axolotl/LlamaFactory cho cấu hình; mục 17 và mục 24. |

**Nguồn hồ sơ:** [README](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/README.md) · [LICENSE](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/LICENSE) · [SFT và masking](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/trl/trainer/sft_trainer.py) · [DPO](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/trl/trainer/dpo_trainer.py) · [GRPO](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/trl/trainer/grpo_trainer.py) · [CI](https://github.com/huggingface/trl/blob/c734c60d85766aff4542a00643a2ca7e4a3c72ac/.github/workflows/tests.yml).

<a id="unsloth"></a>

### 3.3. Unsloth — core training và Studio/CLI có license khác nhau

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [unslothai/unsloth](https://github.com/unslothai/unsloth) |
| Bằng chứng đọc | `63a3896459a9d57396cb1a61b3041b678387870b` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 78,950 ★ (GitHub REST API); Core Apache-2.0; Studio AGPL-3.0-only; CLI AGPLv3 |
| Giá trị cốt lõi | Hiện là bộ công cụ có ứng dụng desktop/UI chạy và huấn luyện model, lõi Python tối ưu đường model/adapter, nhiều đường export. Không còn nên mô tả toàn repo chỉ là thư viện fine-tuning. |
| Đường mã đã đọc | `FastLlamaModel.from_pretrained()` có nhánh lượng tử hoá; `get_peft_model()` ghép adapter và gradient checkpointing. Studio có helper tạo train/eval split bằng seed cố định. |
| CI đã đọc | `studio-backend-ci.yml` định nghĩa kiểm backend; ngoài ra tree có workflow cho từng nền tảng. Chưa chạy các job, export hay đo VRAM. |
| Tích hợp | Chọn rõ dùng core Python hay Studio. Giữ một cấu hình/model nhỏ làm baseline, lưu dependency/backend chính xác rồi kiểm artifact ở runtime đích. |
| Hạn chế / rủi ro | README nêu tăng tốc/giảm VRAM là tuyên bố của nhà phát triển, không phải kết quả tái lập tại đây. Split theo seed của Studio là tiện ích, không tự chặn dữ liệu cùng tài liệu/khách hàng lọt sang hai tập. |
| License thật | README §License ghi hai lớp; `LICENSE` gốc tách `unsloth/*`/tests/scripts là Apache và `studio/*`, `unsloth_cli/*` là AGPLv3; header của `eval_dataset.py` ghi rõ AGPL-3.0-only. Khi nhúng/sửa/triển khai Studio cần đọc nghĩa vụ tương ứng; không lấy nhãn Apache ở gốc áp cho toàn repo. |
| Bài học kiến trúc | UI thuận tiện vẫn cần export một manifest training và dataset split độc lập; tách license theo component thay vì một cờ “open source” duy nhất. |
| Thay thế / liên quan | PEFT/TRL cho pipeline thư viện; Axolotl/LlamaFactory cho cấu hình; mục 10, 24 và 26. |

**Nguồn hồ sơ:** [README và license scope](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/README.md) · [core LICENSE](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/LICENSE) · [Studio LICENSE](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/studio/LICENSE.AGPL-3.0) · [loader/adapter](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/unsloth/models/llama.py) · [split eval](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/studio/backend/core/training/eval_dataset.py) · [CI](https://github.com/unslothai/unsloth/blob/63a3896459a9d57396cb1a61b3041b678387870b/.github/workflows/studio-backend-ci.yml).

<a id="axolotl"></a>

### 3.4. Axolotl — cấu hình có thể phát lại và checkpoint có thể phục hồi

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) |
| Bằng chứng đọc | `da7d6b8138d6c0bcf7815ffb2475845dd40718d5` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 12,654 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Pipeline fine-tuning đa model, cấu hình và tích hợp phân tán/kernel; phù hợp nhóm muốn chuẩn hoá một recipe training. |
| Đường mã đã đọc | `train.py` tách setup model/reference/trainer, xác định checkpoint trước `trainer.train(resume_from_checkpoint=...)`, lưu tokenizer/config, model card và trọng số qua các nhánh backend. |
| CI đã đọc | `tests.yml` là bộ kiểm nhiều job; tree còn có workflow CPU/distributed/GPU. Chưa xác minh kết quả chạy và coverage của cấu hình riêng. |
| Tích hợp | Lưu YAML gốc cùng config đã resolve, dataset revision, seed và checkpoint. Kiểm resume một lần trong dự án tích hợp trước khi giao job dài; kiểm artifact sau bước save/merge. |
| Hạn chế / rủi ro | Resume checkpoint chứa optimizer/scheduler khác với chỉ nạp adapter. Cấu hình nhiều backend tạo ma trận tương thích lớn; không lấy ví dụ của model này áp sang model khác. |
| Bài học kiến trúc | Recipe là artifact có phiên bản; quá trình phục hồi cần kiểm được, không chỉ có đường chạy từ đầu. |
| Thay thế / liên quan | LlamaFactory cho CLI/WebUI chung, TRL/PEFT khi cần kiểm soát code trainer, verl cho RL rollout quy mô lớn; mục 13 và 24. |

**Nguồn hồ sơ:** [README](https://github.com/axolotl-ai-cloud/axolotl/blob/da7d6b8138d6c0bcf7815ffb2475845dd40718d5/README.md) · [LICENSE](https://github.com/axolotl-ai-cloud/axolotl/blob/da7d6b8138d6c0bcf7815ffb2475845dd40718d5/LICENSE) · [setup/train/save/resume](https://github.com/axolotl-ai-cloud/axolotl/blob/da7d6b8138d6c0bcf7815ffb2475845dd40718d5/src/axolotl/train.py) · [CI](https://github.com/axolotl-ai-cloud/axolotl/blob/da7d6b8138d6c0bcf7815ffb2475845dd40718d5/.github/workflows/tests.yml).

<a id="llamafactory"></a>

### 3.5. LlamaFactory — nhiều stage nhưng mỗi stage có điều kiện riêng

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) |
| Bằng chứng đọc | `9997aa078b4da35e04bb492a8a27d45141f4b80b` · commit 2026-10-31 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 75,845 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Cổng CLI/WebUI và recipe chung cho nhiều LLM/VLM, các stage pretraining, SFT, reward model, PPO, DPO, KTO trong đường cấu hình đã đọc. |
| Đường mã đã đọc | `FinetuningArguments` kiểm `stage`, phương pháp `lora/oft/freeze/full`, một số tổ hợp không hợp lệ và yêu cầu reward model cho PPO. `train/sft/workflow.py` tách dataset/model/collator/trainer và các pha train/eval/save. |
| CI đã đọc | `tests.yml` tạo matrix Python 3.11–3.13 trên Linux/Windows/macOS, cài PyTorch CPU, kiểm style/license/build/test; workflow CUDA/NPU ở file khác. Đây không phải bằng chứng mọi model đều huấn luyện được trên CPU. |
| Tích hợp | Chọn template/schema dataset trước khi dùng UI; xuất cấu hình ra file có revision. Kiểm input/output trên mẫu có tool call, Unicode tiếng Việt và hội thoại nhiều lượt theo nhu cầu. |
| Hạn chế / rủi ro | Danh sách “hỗ trợ model” không nói đủ khả năng của từng stage/backend. Không suy tính năng của v1 trainer sang đường legacy hoặc ngược lại. License trọng số và dữ liệu phải kiểm riêng. |
| Bài học kiến trúc | Chặn tổ hợp không hợp lệ bằng cấu hình có kiểu trước khi cấp tài nguyên; UI cần tạo được recipe tái lập để review và dùng CI. |
| Thay thế / liên quan | Axolotl, TRL/PEFT, Unsloth; mục 18 cho tập kiểm tiếng Việt và mục 24 cho dataset contract. |

**Nguồn hồ sơ:** [README](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/README.md) · [LICENSE](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/LICENSE) · [ràng buộc stage](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/src/llamafactory/hparams/finetuning_args.py) · [SFT workflow](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/src/llamafactory/train/sft/workflow.py) · [CI](https://github.com/hiyouga/LlamaFactory/blob/9997aa078b4da35e04bb492a8a27d45141f4b80b/.github/workflows/tests.yml).

<a id="verl"></a>

### 3.6. verl / HybridFlow — tách rollout, reward và cập nhật policy

| Thuộc tính | Giá trị |
|---|---|
| Repo / tác giả | [verl-project/verl](https://github.com/verl-project/verl) |
| Bằng chứng đọc | `6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3` · commit 2026-11-02 · chưa archive khi đọc 2/11/2026 |
| ★ · license (2/11/2026) | 24,102 ★ (GitHub REST API); Apache-2.0 |
| Giá trị cốt lõi | Hệ RL post-training với điều phối worker phân tán; hướng nghiên cứu HybridFlow có controller kết hợp để ánh xạ training/generation lên phần cứng. |
| Đường mã đã đọc | `RayPPOTrainer` điều phối actor/rollout, critic, reference/reward và resource pool; tính advantage/KL, validation dataloader và ghi mẫu rollout. Dataset RL xử lý prompt/tokenization trong lớp riêng. |
| CI đã đọc | `cpu_unit_tests.yml` là lớp kiểm CPU; tree còn có GPU/NPU và nhiều workflow E2E theo rollout engine. Không coi test CPU là xác nhận hiệu quả của một cụm RL. |
| Tích hợp | Bắt đầu bằng baseline nhỏ có reward kiểm được; đặt trần số rollout/token/thời gian/chi phí, ghi revision của actor và reward, cấu hình pool tài nguyên, checkpoint và log validation. |
| Hạn chế / rủi ro | Thêm rollout engine làm tăng chi phí bộ nhớ và đồng bộ; reward có thể bị khai thác hoặc sai nhãn. Khi reward chấm code/tool, phải cách ly executor như mục 11/12; đây không phải chức năng được bảo đảm chỉ nhờ chọn framework. |
| Bài học kiến trúc | Tách metric “policy tối ưu reward” khỏi “người dùng hoàn thành việc”, giữ validation không tham gia reward và lưu trace đủ để điều tra. |
| Thay thế / liên quan | TRL cho baseline SFT/GRPO/DPO ít lớp; PEFT cho adapter; Axolotl/LlamaFactory cho recipe; mục 07, 11, 12, 21 và 24. |

**Nguồn hồ sơ:** [README](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/README.md) · [LICENSE](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/LICENSE) · [trainer/resource/reward](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/verl/trainer/ppo/ray_trainer.py) · [RL dataset](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/verl/utils/dataset/rl_dataset.py) · [CI](https://github.com/verl-project/verl/blob/6879e1ab07b9cfd0b4b27c31ca4e7afcad1466b3/.github/workflows/cpu_unit_tests.yml).

## 4. Chuẩn và hồ sơ cần mang theo model

Các tài liệu dưới đây là nguồn gốc phương pháp và khung báo cáo; chúng không phải chứng nhận rằng một model đã đạt chất lượng hay an toàn.

| Nguồn gốc | Ý nghĩa thực dụng | Điều không được suy rộng |
|---|---|---|
| [LoRA](https://arxiv.org/abs/2106.09685) | Cố định base và học cập nhật low-rank; báo rank, alpha, dropout, modules, embeddings được lưu | Ít tham số trainable không có nghĩa tổng VRAM chỉ bằng kích thước adapter |
| [QLoRA](https://arxiv.org/abs/2305.14314) | Backprop qua base lượng tử hoá vào adapter; ghi quantization và optimizer | Kết quả phần cứng trong paper không là bảo đảm cho mọi model/context/batch |
| [DPO](https://arxiv.org/abs/2305.18290) | Học từ preference pair với objective cụ thể | Chosen/rejected không phải sự thật tuyệt đối; DPO không thay quy trình xây nhãn |
| [HybridFlow](https://arxiv.org/abs/2409.19256) | Thiết kế orchestration training/generation phân tán | Throughput paper phụ thuộc cấu hình; không dự báo tốc độ cụm khác |
| [LlamaFactory paper (ACL 2024)](https://arxiv.org/abs/2403.13372) | Nguồn thiết kế framework thống nhất nhiều phương pháp/model qua CLI/WebUI | Paper 2024 không đại diện toàn bộ feature/compatibility của HEAD 2026 |
| [Model Cards](https://arxiv.org/abs/1810.03993) | Ghi intended use, ngoài phạm vi, dữ liệu, cách đo, kết quả theo nhóm và hạn chế | Có model card không đồng nghĩa được kiểm toán độc lập |
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | Giải thích nguồn, thành phần, thu thập và cách dùng dữ liệu training | License công cụ xử lý không cấp quyền cho nội dung dataset |

**Manifest phát hành nên có:** base/tokenizer revision; dataset/split hash; code/trainer/dependency revision; config đã resolve và seed; precision/quantization/adapter target; phần cứng thực chạy; checkpoint đầu ra/hash; metric baseline–candidate; license code/base/adapter/dataset; runtime đích và kết quả kiểm artifact sau export. Artifact này thuộc dự án tích hợp, kho `stored` chỉ giữ hồ sơ và tiêu chí tham khảo.

## 5. Cổng chất lượng từ dữ liệu đến runtime

| Cổng | Bằng chứng phải lưu ở dự án tích hợp | Chặn phát hành khi |
|---|---|---|
| Baseline | Cùng tập kiểm cho base + prompt, base + RAG và candidate tune; mục tiêu định trước | Chưa biết lỗi cần sửa nằm ở truy xuất, prompt hay hành vi |
| Dữ liệu và quyền | Dataset card, đồng ý/quyền sử dụng, hash/lineage, leakage report theo tài liệu/người/nguồn | Không rõ quyền dùng, PII ngoài mục đích hoặc train–test trùng nhóm |
| Token và loss | Vài mẫu đã render, token/mask, phần bị truncation, test Unicode/tool-call | Mask học user/system sai mục tiêu, đáp án bị cắt hoặc template lệch inference |
| Tài nguyên | Peak allocated/reserved GPU memory, batch/context, tokens thực, thời gian/chi phí trong cấu hình chạy thật | Vượt ngân sách hoặc chỉ ước VRAM từ số tham số |
| Tiến trình | Loss/NaN, checkpoint, log validation, thử resume có kiểm soát | Không thể phục hồi; chọn checkpoint theo tập test cuối |
| Held-out | Task success/định dạng/groundedness nếu dùng RAG, regression kiến thức chung và nhóm tiếng Việt | Candidate không đạt ngưỡng đã định hoặc giảm nhóm quan trọng |
| Preference / reward | Nguồn nhãn, agreement, kiểm reward hacking, judge model/prompt revision | Reward tăng nhưng human/task eval không cải thiện hoặc giữ được |
| Xuất artifact | Load lại trong tiến trình sạch, đúng tokenizer/template, eval sau merge/quantization | File export hợp lệ nhưng hành vi khác candidate đã chấp nhận |
| Serving | Độ trễ/throughput/VRAM theo workload, rate limit/rollback; đối chiếu mục 10 | Chưa có đường rollback hoặc ngân sách inference không đáp ứng |

Không có trần VRAM phổ quát cho “model 7B/8B”. Trọng số, activation theo độ dài context, gradient/optimizer, precision, checkpointing, batch và cách phân tán đều góp phần. Cổng ở trên yêu cầu đo cấu hình cụ thể; số do README công bố chỉ là ứng viên cần tái lập. Loss thấp không đủ chứng minh chất lượng hội thoại, an toàn, tri thức hay độ tin cậy của tool call.

## 6. Stack tham khảo và bài học ghép kho

1. [Mục 17](../17-prompt-engineering/README.md) cố định prompt/schema; [mục 10](../10-local-llm-rag-memory/README.md) thử baseline truy xuất trước khi quyết định tune.
2. [Mục 24](../24-ai-data-engineering/README.md) đóng băng dữ liệu, nhóm split và nhãn; [mục 18](../18-vietnam-community/README.md) cung cấp hướng tìm eval tiếng Việt phù hợp tác vụ.
3. Chọn PEFT + TRL nếu cần pipeline thư viện; Unsloth/Axolotl/LlamaFactory nếu giá trị chính là đóng gói; verl khi quy mô RL tạo nhu cầu orchestration cụ thể.
4. [Mục 07](../07-eval-observability/README.md) giữ held-out, trace và regression; [mục 12](../12-ai-security-guardrails/README.md) kiểm nguồn model/data và reward executor.
5. Chỉ bàn giao artifact đã kiểm sau export cho runtime [mục 10](../10-local-llm-rag-memory/README.md) kèm card/manifest và đường quay về base.

**Trần được nâng:** kho có đường đi từ recipe dữ liệu đến adapter/model đã kiểm, tránh lấy “hỗ trợ LoRA” hay một biểu đồ benchmark làm lý do duy nhất để tích hợp. Chưa chạy phép đo độc lập, chưa kiểm license từng model/dataset và chưa xác minh mọi backend được quảng bá **(chưa xác minh)**.

## 7. Nguồn và cách cập nhật

Nguồn GitHub trong từng hồ sơ ghim full commit SHA đã clone; số sao và `archived` đọc bằng GitHub REST ngày 2/11/2026. Commit date là ngày của `HEAD` đã đọc, khác `pushed_at` (có thể là nhánh khác). README/CI là bằng chứng về thiết kế và định nghĩa kiểm, không phải kết quả thực thi tại kho này. Nguồn ngoài repo gồm các paper gốc ở §4; không dùng bài SEO để quyết định tính tương thích hay license.

Khi cập nhật: đọc lại license từng component, release/changelog, trainer/schema/template và đường save/load; giữ bằng chứng cấu hình cụ thể nếu báo tốc độ/VRAM; đối chiếu model card và rerun eval ở dự án tích hợp. Chỉ bổ sung con số benchmark khi có hardware, dataset/split, config, revision và giới hạn của phép đo.
