# 14 · Voice Agents, Speech & Multimodal (Vision, Image Generation)

> Agent giọng nói thời gian thực, STT/TTS mã mở, model thị giác-ngôn ngữ và công cụ sinh ảnh. Số sao ước lượng giữa–cuối 2026.

## 1. Framework voice agent realtime

| Dự án | Repo | License | ★ | Định vị | Ghi chú |
|---|---|---|---|---|---|
| **Pipecat** (Daily) | pipecat-ai/pipecat | BSD-2 | ~15–16k | Pipeline Python cho voice/multimodal agent | Mặc định tốt cho backend Python |
| **LiveKit Agents** | livekit/agents | Apache-2.0 (model turn-detection license riêng) | ~11–15k | WebRTC, telephony, nhiều client SDK | Cloud tùy chọn |
| **TEN Framework** | TEN-framework/ten-framework | Apache-2.0 | ~11k | Realtime multimodal agent, Agora | |
| Vocode | vocodedev/vocode-core | MIT | ~4k | Ngừng cập nhật cuối 2024 | Legacy |
| OpenAI Realtime API / Gemini Live / Anthropic voice | (đóng) | – | – | Speech-to-speech end-to-end | |
| Dograh, Vapi, Retell | – | – | – | Nền tảng thương mại | |

## 2. Speech-to-text (STT)

| Dự án | Repo | Ghi chú |
|---|---|---|
| **Whisper** | openai/whisper | Model STT mở phổ biến nhất (MIT) |
| **faster-whisper** | SYSTRAN/faster-whisper | CTranslate2, nhanh 4× |
| **whisper.cpp** | ggml-org/whisper.cpp | C/C++, edge/Apple Silicon |
| WhisperX, Deepgram/AssemblyAI (đóng) | – | Diarization / cloud |

## 3. Text-to-speech (TTS)

| Model | License | Thế mạnh | Hạn chế |
|---|---|---|---|
| **Kokoro (82M)** | Apache-2.0 | Nhẹ, nhanh, Elo ~1060 (8/2026) | Không clone giọng, voicepack cố định |
| **Chatterbox** (Resemble) | MIT | Zero-shot clone ~5s audio, 23 ngôn ngữ, Elo ~1020 | Watermark output |
| **F5-TTS** | Code MIT / weights CC-BY-NC | Clone chất lượng cao | Không thương mại hóa weights |
| **Audio8 TTS** 0.6B / 0.1B (Edge0) | 0.6B: Apache-2.0 · 0.1B: **Audio8 Community License** (trần doanh thu US$2M) | Clone zero-shot, 11 ngôn ngữ, ONNX INT4 chạy CPU ~1 GiB, adapter SGLang Omni; xem §3b | Preview, không watermark, chưa có đánh giá độc lập |
| **Fish Audio S2 Pro** | Fish Audio Research License (cấm thương mại nếu không có hợp đồng) | DualAR 4,6B, kiến trúc gốc mà Audio8 dựa theo | "Open weights, not open source" (chính Fish Audio nói) |
| CosyVoice3 (Alibaba), VoxCPM2 (OpenBMB), Higgs Audio v2 (Boson AI) | xem model card từng bản | Mốc so sánh trong bảng benchmark của Audio8 (1,5B / 2,3B / 4,7B) | License VoxCPM2/Higgs **chưa xác minh** trong kho |
| Fish Speech (bản cũ), Orpheus, Coqui XTTS (ngừng) | – | | |

### 3b. Case study: Audio8 TTS (Edge0-AI) – TTS clone giọng cỡ nhỏ (link từ người dùng, 2026-10-12)

> Nguồn: https://github.com/edge0-ai/audio8_tts. Đã clone đầy đủ lịch sử (73 commit): README, NOTICE, LICENSE, `audio8_tts_*.py`, `onnx_runtime*/`, `sglang_omni/`. Cùng với đó là model card Hugging Face (0.6B, 0.1B), các bản port của bên thứ ba và các bài viết bên ngoài.

| Thuộc tính | Giá trị (đọc 2026-10-12) |
|---|---|
| Repo / tên | `Edge0-AI/Audio8_TTS` (1,6k★, 161 fork, 8 issue + 1 PR mở). README vẫn trỏ badge và star-history về `Audio8-AI/Audio8_TTS`; trên Hugging Face, model nằm ở `Edge0/…`, `Audio8/…`, lệnh cài lại ghi `AutoArk-AI/…` → **3 tên tổ chức** cho cùng một dự án. Email commit thuộc domain `autoark.ai` |
| Tuổi | Commit đầu 27/7/2026, cuối 1/9/2026; 0.1B ra 19/8/2026 |
| Lịch sử commit | Một phần commit có tác giả `Your Name <you@example.com>`, `root@pytorch-training-…svc.cluster.local` và `Codex <codex@localhost>`; một PR huấn luyện 0.1B bị revert ngay trong ngày → quy trình phát hành còn non |
| Mã nguồn | ~2,6k dòng Python: infer, chuẩn bị codec, SFT (`torchrun`), runtime ONNX (CLI + web/HTTP + giọng đăng ký sẵn), adapter SGLang Omni (API `/v1/audio/speech` kiểu OpenAI, SSE streaming) |
| Kiến trúc | **DualAR** theo Fish Audio S2 Pro: slow AR 24 lớp (1 token ngữ nghĩa mỗi frame) + fast AR 4 lớp (10 codebook × 4.096); codec 44,1 kHz (~21,5 frame/s) đóng gói trong checkpoint; 601M tham số không kể codec. Bản 0.1B thay slow AR bằng **Falcon-H1** (lai Mamba2 + attention): main ~170M + codec decoder ~120M (HF ghi 0.2B) |
| Triển khai | GPU: SGLang Omni, RTF 0,116, p50 0,691 s trên 1×H20 (tác giả tự đo). CPU: ONNX INT4 ~1 GiB trên Apple M2. Cộng đồng đã port sang audio.cpp, Core AI (coreai-model-zoo #47) và có API trên DeepInfra |
| Benchmark (tự công bố) | Seed-TTS EN WER **1,506** (tốt nhất bảng), ZH CER 0,950; nhưng **SIM** (độ giống giọng) thấp nhất bảng (63,2 so với 72–75 của CosyVoice3/VoxCPM2), hard-ZH CER 11,5 kém hẳn CosyVoice3 (5,83). Tác giả tự ghi: normalizer khác nhau nên chỉ là "reference comparisons" |

**Mâu thuẫn và rủi ro**

- **License:** README và NOTICE ghi "Code and model weights in this repository are released under Apache 2.0", nhưng weights **0.1B** trên Hugging Face dùng *Audio8 Community License v1.0*: miễn phí cho phi thương mại và cho đơn vị doanh thu dưới **US$2M/năm** (tính cả công ty mẹ/con), trên mức đó phải mua license. Kiến trúc lấy cảm hứng từ Fish S2 Pro, mà weights Fish dùng Research License cấm thương mại. Audio8 chỉ ghi "inspired by"; kho chưa kiểm được codec bundled có nguồn gốc từ đâu **(chưa xác minh)**.
- **Lạm dụng:** clone giọng zero-shot nhưng **không có watermark**, chỉ khuyến nghị xin đồng ý và công bố là audio tổng hợp. Chatterbox (§3) watermark output; nên tự thêm watermark hoặc log nguồn khi đưa vào sản phẩm.
- **Chất lượng:** câu vào nên ≤150 ký tự; transcript tham chiếu phải khớp audio; Transformers 5.x sinh code toàn 0; một bài nghe thử không chính thức chê "okay, robotic"; bản port audio.cpp ghi đường clone 0.6B chưa được đánh giá bằng ASR.
- **Tiếng Việt: không hỗ trợ** (11 ngôn ngữ khuyến nghị không có vi). Cho tiếng Việt xem mục 18 (ViGen…).

**Bài học:** (1) tách **slow AR ngữ nghĩa / fast AR codebook** giúp model nhỏ vẫn đạt WER thấp, nhưng độ giống giọng (SIM) là thứ mất đi khi thu nhỏ → luôn đọc cả WER **lẫn** SIM; (2) gói kèm runtime ONNX INT4 + giọng đăng ký sẵn là mẫu tốt để chạy TTS offline trên CPU cho voice agent (Pipecat/LiveKit §1, Personal Jarvis mục 01 §3c); (3) kiểm tra license **theo từng checkpoint**, không theo README.

## 4. Vision-language model (VLM) mã mở

| Model | Repo | ★ | Ghi chú |
|---|---|---|---|
| **Qwen3-VL** (Alibaba) | QwenLM/Qwen3-VL | ~20k | Apache-2.0; 2B/7B, 72B sắp mở |
| LLaVA-NeXT / LLaVA-OneVision-2 | LLaVA-VL/LLaVA-NeXT · EvolvingLMMs-Lab/LLaVA-OneVision-2 | ~4.7k / ~1.2k | Framework huấn luyện mở (4/2026) |
| InternVL | OpenGVLab/InternVL | – | |
| Gemma 3 / Llama 4 / Pixtral | – | – | Open-weight đa phương thức |

## 5. Sinh ảnh / video

| Công cụ | Repo | ★ | Trạng thái |
|---|---|---|---|
| **ComfyUI** | comfyanonymous/ComfyUI | ~122–136k | Node-based, hỗ trợ model mới nhanh nhất (Flux, video); **đã thắng** |
| AUTOMATIC1111 WebUI | AUTOMATIC1111/stable-diffusion-webui | ~164k | Release cuối v1.10.1 (7/2024), dừng phát triển |
| Forge / Forge Neo | lllyasviel/stable-diffusion-webui-forge | – | Khuyến nghị thay A1111 |
| Fooocus | lllyasviel/Fooocus | ~53k | LTS, chỉ sửa lỗi |
| Flux (Black Forest Labs), SDXL, Wan/HunyuanVideo | – | – | Model |
| **Wan 2.2 / LTX-2** | Wan-Video/Wan2.2 · Lightricks/LTX-2 | – | Model video mở X-Studio chọn cho xưởng video (mục 23 §3.2); OpenMontage bundle Wan (mục 19) |

### 5b. 3D & tài liệu (từ repo của chủ kho, mục 23)

- **Ảnh/văn bản → 3D** (research `design-os-3d-blender`, 28/7/2026, gắn `[UNVERIFIED]`): Microsoft **TRELLIS.2** (MIT, PBR native), TripoSG/SR/SF, Direct3D-S2, Step1X-3D, **Hunyuan3D 2.1** (license hạn chế lãnh thổ EU/UK/KR, kể cả output), PartCrafter, HoloPart, **UniRig**/MagicArticulate (rigging); marketplace in 3D.
- **Agent điều khiển Blender**: `ahujasid/blender-mcp` (~24,6k★ theo docs nội bộ) hoặc headless `blender -b -P`; mẫu sentinel `AGENT_OK/AGENT_FAIL` + verify ladder rẻ→đắt (assert số → preview 0,2s → render) vì exit code của Blender sai cả hai chiều.
- **Scan tài liệu di động** (X-Scanner, Flutter): OpenCV edge detection + perspective warp, OCR on-device (ML Kit) — `docs/research/2026-10-11-scanner-product-suggestions.md`.

## 5c. Nâng cấp 31/10/2026: rà repo lớn

> Cách làm: đọc lại sao, license, trạng thái của 17 repo GitHub đã có trong mục 14 (GitHub API, 31/10/2026). Tìm repo còn thiếu bằng 12 truy vấn GitHub search (`text to speech`, `tts`, `speech recognition`, `voice agent`, topic `text-to-speech`/`speech-recognition`/`multimodal`, `vision language model`, `image generation`, `ocr`, và `created:>2025-10-01` cho repo mới). Lọc bỏ repo đã có trong `data/projects.json`, chọn **6 repo**, clone `--filter=blob:none` rồi đọc LICENSE, README, manifest, CI, file telemetry và host mạng trong mã. **Không cài, không chạy script của repo.** Số liệu đọc 31/10/2026.

### 5c.1 Trạng thái repo cũ

| Repo | Thay đổi | Hệ quả |
|---|---|---|
| `hexgrad/kokoro` | Push cuối **6/8/2025** (9,8k★) | Repo code đứng yên hơn 1 năm; model Kokoro-82M vẫn được dùng qua wrapper như `remsky/Kokoro-FastAPI` (5,6k★, push 31/10/2026) và backend của LocalAI |
| `QwenLM/Qwen3-VL` | Push cuối **30/1/2026** | Dòng "72B sắp mở" ở §4 không còn cập nhật; theo dõi model card Hugging Face thay vì repo |
| `AUTOMATIC1111/stable-diffusion-webui` | Push cuối 2/3/2026, 165,2k★ | Đúng như §5 ghi "dừng phát triển" |
| `lllyasviel/Fooocus` | Push cuối 1/12/2025 | Hết giai đoạn LTS trên thực tế |
| `black-forest-labs/flux2` | Push cuối 12/3/2026 (2,8k★) | Repo tham chiếu, ít cập nhật |
| `Comfy-Org/ComfyUI` | **144,4k★** (bảng §5 ghi ~122–136k, repo cũ `comfyanonymous/ComfyUI`) | Đã chuyển sang tổ chức Comfy-Org; cập nhật tên repo |
| `Edge0-AI/Audio8_TTS` | 1,6k → **2,1k** | Hồ sơ §3b vẫn đúng |
| `openai/whisper` · `ggml-org/whisper.cpp` · `SYSTRAN/faster-whisper` | 111,7k · 54,8k · 26,4k | Catalog bổ sung sao còn thiếu |
| `resemble-ai/chatterbox` | 27,5k, push cuối 21/7/2026 | Hơn 3 tháng không push |
| `TEN-framework/ten-framework` · `fishaudio/fish-speech` | GitHub báo `NOASSERTION` | Không đổi license: TEN có điều khoản bổ sung trên Apache-2.0 **(chưa xác minh)**, Fish dùng Research License (đã ghi §3) |
| VoxCPM2 (§3) | License "chưa xác minh" | Nay đã đọc: **Apache-2.0 cho cả code và weights** theo README và LICENSE của `OpenBMB/VoxCPM` (xem dưới) |

### 5c.2 Bảng nhanh 6 repo mới

| Repo | Nhóm | ★ · license | Commit cuối | Một dòng | Cờ |
|---|---|---|---|---|---|
| `debpalash/VoiceStudio` | App giọng nói | 96,8k · **AGPL-3.0 + CLA** | 1/11/2026 | Clone, thiết kế giọng, lồng tiếng video, đọc chính tả; desktop + mobile | Sao tăng bất thường; bán license thương mại |
| `jamiepine/voicebox` | App giọng nói | 59,1k · MIT | 7/10/2026 | "ElevenLabs + WisprFlow" chạy local, 8 engine TTS, MCP `voicebox_speak` | Bảo trì bằng agent Capy; không có bản Linux dựng sẵn |
| `microsoft/VibeVoice` | ASR + TTS | 55,1k · MIT | 8/10/2026 | ASR 60 phút một lượt (ai nói, lúc nào), streaming ASR, TTS realtime 0,5B | Code TTS dài từng bị gỡ vì lạm dụng; không CI |
| `RVC-Boss/GPT-SoVITS` | Clone giọng | 64,4k · MIT | 31/10/2026 | Huấn luyện TTS từ ~1 phút giọng, WebUI | Tag cuối 6/6/2025; nhịp chậm |
| `OpenBMB/VoxCPM` | TTS | 40,9k · Apache-2.0 | 8/10/2026 | VoxCPM2 2B, 30 ngôn ngữ **có tiếng Việt**, 48 kHz, thiết kế giọng | Benchmark tự công bố |
| `cjpais/Handy` | STT desktop | 35,9k · MIT | 27/10/2026 | Giữ phím, nói, chữ dán vào app đang mở; Whisper/Parakeet offline | Tải model từ `blob.handy.computer` |

### 5c.3 Hồ sơ ngắn

- **VoiceStudio.** Repo tạo 10/4/2026; trong ~7 tháng có 6.378 commit, 155 tác giả, **40% commit có trailer Claude**, 96,8k★: tốc độ tăng sao này cao bất thường so với mọi repo TTS khác trong đợt **(chưa xác minh nguồn sao)**. Biến môi trường còn tên cũ `OMNIVOICE_*`, submodule `omnivoice-gallery`. `LICENSE-NOTICE.md`: AGPL-3.0, người đóng góp ký CLA trao quyền cho Yupcha Softwares Private Limited, công ty bán license thương mại và bản Pro. Telemetry PostHog có trong mã (`backend/core/analytics.py`), **tắt mặc định**, chỉ gửi trường trong allowlist, không gửi traceback ✅; tắt cứng bằng `OMNIVOICE_ANALYTICS_DISABLED=1`. Có workflow `scam-guard` tự xoá các bình luận dụ dán lệnh `irm … | iex` trong issue. Cài theo README là `curl -fsSL https://voicestudio.sh/install | sh` (chạy script từ xa).
- **Voicebox.** Tauri + Python backend, 813 commit từ 25/1/2026, tag cuối v0.5.0 (25/4/2026). README ghi dự án được "Capy Captain" (agent của capy.ai, nhà tài trợ) điều phối hằng ngày: một repo lớn bảo trì chủ yếu bằng agent. 8 engine TTS (Qwen3-TTS, LuxTTS, Chatterbox, HumeAI TADA, Kokoro…), Whisper cho đọc chính tả, MCP server cho agent nói bằng giọng đã clone. Có `RESPONSIBLE_USE.md` nhưng không có watermark trong mã **(chưa xác minh hết engine)**. Cài: tải DMG/MSI hoặc `docker compose up`.
- **VibeVoice (Microsoft).** 161 commit, không có workflow CI. Ghi chú 5/9/2025 trong README: code TTS dài (1,5B) bị **gỡ vì bị dùng sai mục đích**, Playground để "Disabled". Từ 2026 dự án chuyển sang ASR: VibeVoice-ASR 7B (60 phút một lượt, hơn 50 ngôn ngữ, hotword), bản streaming (9/2026), bản BitNet chạy CPU qua `microsoft/VibeASR.cpp`. Commit 7/10/2026 "Remove remote audio URL fetching from streaming ASR" bỏ khả năng tải URL từ xa. Cài: `pip install -e .` từ clone hoặc qua Transformers (`microsoft/VibeVoice-ASR-HF`).
- **GPT-SoVITS.** 1.066 commit, MIT, chủ yếu một tác giả (621 commit). Bản mới nhất v2Pro (6/6/2025); chỉ 20 commit từ 1/7/2026. `install.sh` tải model từ Hugging Face hoặc ModelScope; README hỗ trợ zh/en/ja/ko/yue, **không có tiếng Việt**. Không có CI kiểm thử, chỉ build Windows và Docker. Cài: `bash install.sh --device CU128 --source HF`.
- **VoxCPM (OpenBMB).** 182 commit, Apache-2.0; README nói rõ **weights và code đều Apache-2.0, dùng thương mại được** ✅ (khác Fish S2 Pro, F5-TTS weights ở §3). VoxCPM2: 2B, 30 ngôn ngữ trong đó có tiếng Việt, 48 kHz, voice design. Bảng benchmark là tự đo. Phục vụ nhanh qua `nano-vllm-voxcpm`. Đây là ứng viên TTS clone giọng tiếng Việt có license thoáng nhất trong kho, nên đánh giá cùng mục 18 (VieNeu-TTS). Cài: `pip install voxcpm`.
- **Handy.** Tauri (Rust + React), 902 commit, 178 tác giả, 9 workflow (có Playwright). STT hoàn toàn offline sau khi tải model (Whisper, Parakeet V3), VAD Silero. Mạng: model tải từ `blob.handy.computer`, cập nhật từ GitHub Releases; xử lý hậu kỳ bằng LLM là tuỳ chọn và gọi OpenAI/OpenRouter. Không thấy telemetry. Cài: `brew install --cask handy` (cask cộng đồng) hoặc tải từ Releases.

Đã cân nhắc nhưng chưa thêm: `k2-fsa/OmniVoice` (16,1k, TTS 600+ ngôn ngữ, tạo 3/2026), `index-tts/index-tts` (24,8k, `NOASSERTION`), `m-bain/whisperX` (25,0k), `modelscope/FunASR` (20,9k), `k2-fsa/sherpa-onnx` (15,6k), `KittenML/KittenTTS` (16,7k), `kyutai-labs/pocket-tts` (10,2k), `QwenLM/Qwen3-TTS` (14,1k, push cuối 17/3/2026), `livekit/livekit` (22,0k), `supertone-oss-archive/supertonic` (13,8k, **đã archive**).

### 5c.4 Mẫu chung rút ra

1. **Weights mới là chỗ quyết định license.** VoxCPM ghi rõ weights Apache-2.0; ngược lại F5-TTS, Fish, Audio8 0.1B (§3, §3b) tách license weights. Luôn kiểm model card từng checkpoint.
2. **Clone giọng kéo theo trách nhiệm**: Microsoft gỡ hẳn code TTS; Voicebox, VoiceStudio chỉ có văn bản "responsible use". Sản phẩm dùng clone giọng nên tự thêm watermark hoặc nhật ký nguồn.
3. **App voice local vẫn có đường mạng**: tải model từ CDN riêng (Handy), PostHog tuỳ chọn (VoiceStudio), LLM cloud cho hậu kỳ (Handy, Voicebox). Telemetry tắt mặc định kèm allowlist trường như VoiceStudio là mẫu tốt.
4. **Repo lớn được bảo trì bằng agent** đã thành phổ biến (VoiceStudio 40% commit có Claude, Voicebox do Capy điều phối). Số commit cao không còn là thước đo công sức con người.
5. **Cài bằng `curl … | sh`** vẫn là đường chính ở app desktop (VoiceStudio); scam-guard của VoiceStudio cho thấy lệnh dán vào shell cũng là kênh phát tán malware.

**Nguồn §5c:** GitHub search API 31/10/2026 (12 truy vấn + `repo:` cho 17 repo cũ và 6 repo mới) · clone `--filter=blob:none`, đọc: VoiceStudio (LICENSE, LICENSE-NOTICE.md, README.md, backend/core/analytics.py, .gitmodules, .github/workflows/scam-guard.yml), voicebox (LICENSE, README.md, RESPONSIBLE_USE.md, backend/, app/src/), VibeVoice (LICENSE, README.md, lịch sử commit), GPT-SoVITS (LICENSE, README.md, install.sh), VoxCPM (LICENSE, README.md, pyproject.toml), Handy (LICENSE, README.md, src-tauri/src/, src-tauri/tauri.conf.json) · https://github.com/debpalash/VoiceStudio · https://github.com/jamiepine/voicebox · https://github.com/microsoft/VibeVoice · https://github.com/RVC-Boss/GPT-SoVITS · https://github.com/OpenBMB/VoxCPM · https://github.com/cjpais/Handy · https://huggingface.co/openbmb/VoxCPM2

## 5d. Nâng trần 2/11/2026: đo chất lượng giọng nói (WER, MOS, eval voice agent) và watermark (yêu cầu người dùng)

> Mục 14 đã có framework, model STT/TTS và app giọng nói, nhưng chưa có công cụ nào để **đo** chúng. Đợt này thêm lớp đo và lớp gắn nhãn đầu ra. Số liệu đọc bằng GitHub search API ngày 2/11/2026. Clone `--depth 1 --filter=blob:none` 7 repo, đọc LICENSE, README, `pyproject.toml`, `.env.example` và file chính. **Không cài, không chạy.**

### 5d.1 Trần hiện tại

- Chọn model theo **benchmark tự công bố**: Elo của Kokoro/Chatterbox (§3), bảng của Audio8 (§3b), VoxCPM (§5c). Kho chưa có công cụ nào để dự án tự đo lại trên dữ liệu của mình, nhất là tiếng Việt.
- STT chưa có cổng **WER/CER**, TTS chưa có điểm **MOS** tự động, voice agent (Pipecat, LiveKit §1) chưa có eval hội thoại nhiều lượt.
- §5c.4 khuyên "tự thêm watermark" cho clone giọng nhưng chưa chỉ công cụ nào. Chỉ Chatterbox có watermark sẵn (§3).

### 5d.2 Bảng repo mới

| Repo | Lớp | ★ · license (2/11/2026) | Commit cuối | Vì sao nâng trần | Rủi ro |
|---|---|---|---|---|---|
| `jitsi/jiwer` | Cổng máy (STT) | 942 · Apache-2.0 | 16/4/2026 | Thư viện Python chuẩn để tính WER, MER, WIL, WIP, CER bằng RapidFuzz; v4.0.0. Đủ nhỏ để chạy trong CI trên bộ audio mẫu của dự án | Kết quả phụ thuộc bước chuẩn hoá văn bản (dấu, số, viết hoa). Với tiếng Việt phải tự định nghĩa và ghi rõ chuẩn hoá thanh điệu và số |
| `huggingface/open_asr_leaderboard` | Chuẩn đo (ASR) | 278 · Apache-2.0 | 30/10/2026 | Mã của Open ASR Leaderboard: bộ test công khai (short-form, long-form, multilingual FLEURS/MCV/MLS), chạy trên Hugging Face Jobs cùng phần cứng để tái lập, có cả tập riêng tư. Là thước đo trung lập để so Whisper, Parakeet, VibeVoice-ASR | Normalizer chủ yếu cho tiếng Anh (`EnglishTextNormalizer`); với nhánh multilingual dùng `BasicMultilingualTextNormalizer`. Kết quả tiếng Việt **(chưa xác minh có công bố)** |
| `Picovoice/speech-to-text-benchmark` | Cổng máy (STT) | 698 · Apache-2.0 | 7/10/2026 | Khung nhỏ đo WER và độ trễ trên LibriSpeech, TED-LIUM, Common Voice, MLS, VoxPopuli, FLEURS…; có engine Whisper, whisper.cpp streaming, Moonshine, Vosk, Nemotron cùng các API cloud | **Benchmark của nhà bán**: có engine Cheetah/Leopard của chính Picovoice. Dùng khung đo, đừng dùng bảng kết quả |
| `sarulab-speech/UTMOSv2` | Cổng máy (TTS) | 377 · MIT | 2/4/2026 | Dự đoán MOS độ tự nhiên, hạng 1 ở 7/16 chỉ số của VoiceMOS Challenge 2024 Track 1 (SLT 2024). Dùng để chặn hồi quy chất lượng TTS khi đổi model hay voicepack | Huấn luyện cho giọng tổng hợp chất lượng cao, phần lớn tiếng Anh/Nhật. Với tiếng Việt chỉ nên so tương đối giữa hai phiên bản, không coi là điểm tuyệt đối **(chưa xác minh)** |
| `ServiceNow/eva` | Cổng máy (voice agent) | 235 · MIT | 29/10/2026 | Eval hội thoại nói nhiều lượt theo kiểu bot đối thoại với bot: **EVA-A** (làm đúng việc) và **EVA-X** (tự nhiên, ngắn, hợp hội thoại nói). 213 kịch bản doanh nghiệp, bộ nhiễu (tiếng ồn, giọng vùng miền, mạng chập chờn), kết quả cho 12 hệ thống | Cần key ElevenLabs/OpenAI/Google/AWS cho người dùng giả và giám khảo LLM, nên tốn phí. Kịch bản tiếng Anh |
| `OpenBMB/UltraEval-Audio` | Cổng máy (tổng hợp) | 328 · Apache-2.0 | 28/10/2026 | Gom 34 benchmark (giọng nói, âm thanh, y tế, âm nhạc; 10 ngôn ngữ) cho cả hiểu và sinh giọng, kèm lệnh tái lập kết quả của các model phổ biến (ACL 2026 demo) | Khung lớn, tự cài phụ thuộc riêng cho từng model. README đủ tiếng Anh, có bản tiếng Trung |
| `facebookresearch/audioseal` | Đầu bảng (watermark) | 802 · MIT (cả weights từ 4/2024) | 2/11/2026 | Watermark âm thanh theo từng đoạn: dò được vị trí đoạn bị chèn, chạy streaming từ v0.2. Đã nằm trong **danh sách soft-binding của C2PA** (`com.aiwatermark.audioseal.1`, xem mục 19 §3d) | Watermark có thể bị tấn công gỡ. Chỉ là một lớp, phải đi kèm manifest C2PA |

**Đã xem nhưng không thêm:** `SpeechColab/Leaderboard` (558★, không có LICENSE, push cuối 3/2025) · `tarepan/SpeechMOS` (368★, MIT, đứng yên từ 10/2023) · `boson-ai/EmergentTTS-Eval-public` (237★, Apache-2.0, push cuối 12/2025).

### 5d.3 Stack nâng trần

1. **Cổng WER/CER cho STT (nửa ngày).** Chuẩn bị 50–200 câu audio tiếng Việt thật của sản phẩm kèm transcript chuẩn. Tính bằng `jiwer` sau một bước chuẩn hoá cố định, chặn PR khi WER tăng quá ngưỡng. Áp cho Whisper, faster-whisper (§2), PhoWhisper (mục 18) và VibeVoice-ASR (§5c).
2. **So model bằng khung trung lập (1 ngày).** Dùng harness của Open ASR Leaderboard hoặc Picovoice với dữ liệu của mình. Không tin bảng số của nhà bán, kể cả bảng của Picovoice.
3. **MOS tự động cho TTS (1 ngày).** Chấm UTMOSv2 trên bộ câu cố định mỗi khi đổi model hay giọng (Kokoro, VoxCPM2, VieNeu…). Chỉ so tương đối, và định kỳ cho người nghe thật duyệt lại.
4. **Eval voice agent (2–3 ngày).** Chạy EVA (EVA-A/EVA-X và bộ nhiễu) cho agent dựng bằng Pipecat hoặc LiveKit (§1) trước khi lên production. Tự viết kịch bản tiếng Việt theo cùng khung.
5. **Gắn nhãn giọng clone.** Chèn AudioSeal vào đầu ra TTS clone giọng (VoxCPM, GPT-SoVITS, Voicebox ở §5c), ký manifest C2PA (mục 19 §3d), lưu nhật ký người đồng ý cho giọng.

**Nguồn §5d:** GitHub search API 2/11/2026 (`repo:` cho 7 repo; 6 truy vấn `word error rate`, `MOS prediction`, `TTS evaluation`, `ASR benchmark leaderboard`, `voice agent evaluation`, `audioseal OR videoseal`) · clone `--depth 1 --filter=blob:none` 2/11/2026: jitsi/jiwer (HEAD 2227002, 16/4/2026; README.md, LICENSE, pyproject.toml), huggingface/open_asr_leaderboard (edd6842, 30/10/2026; README.md, LICENSE, normalizer/normalizer.py), Picovoice/speech-to-text-benchmark (aea7914, 7/10/2026; README.md, LICENSE, engine.py), sarulab-speech/UTMOSv2 (cc2700d, 2/4/2026; README.md, LICENSE), ServiceNow/eva (236f4ea, 29/10/2026; README.md, LICENSE, .env.example), OpenBMB/UltraEval-Audio (c0be484, 28/10/2026; README.md, LICENSE), facebookresearch/audioseal (98f56cd, 2/11/2026; README.md, LICENSE) · danh sách soft-binding C2PA: github.com/c2pa-org/specifications `softbinding-alg-list/softbinding-algorithm-list.json` (HEAD 66ee450)

## 5e. Voice reliability

> Mở rộng khảo sát ngày 2/11/2026. §5d đã đo WER/MOS và tác vụ hội thoại; phần này đánh giá **đường truyền, lượt nói và quyền thu âm**. Đọc LICENSE, CI và mã nguồn tại commit ghim dưới đây; không cài hay chạy mã ngoài. Các ngưỡng vận hành phải lấy từ yêu cầu của sản phẩm, chưa có kết quả chạy tiếng Việt trong khảo sát này.

### 5e.1 Hai thành phần dưới framework

| Repo | ★ · license (2/11/2026) | Commit đọc | Cơ chế đáng học | Giới hạn / điều kiện |
|---|---|---|---|---|
| [snakers4/silero-vad](https://github.com/snakers4/silero-vad/tree/066409f3d9db45a30d21dfcbf9147826ffdd7052) | 10,581 · MIT | 2026-10-22 · `066409f` | VAD để tách đoạn tiếng nói trước STT, có ONNX/TorchScript và trạng thái streaming | VAD không xác định người nói, không đo hiểu đúng ý hay sự đồng ý; cần kiểm tiếng ồn/giọng vùng miền trên dữ liệu đích |
| [aiortc/aiortc](https://github.com/aiortc/aiortc/tree/d6a003fcb6511675318b4494e5b225b78abd2af2) | 5,124 · BSD-3-Clause | 2026-11-01 · `d6a003f` | WebRTC/ORTC Python asyncio, media track, RTP/RTCP và data channel | Là transport thấp tầng; không cung cấp sẵn signaling production, quản lý lượt nói hay chính sách lưu âm thanh |

**Silero VAD (Silero Team).** [Mã wrapper ONNX](https://github.com/snakers4/silero-vad/blob/066409f3d9db45a30d21dfcbf9147826ffdd7052/src/silero_vad/utils_vad.py) quy định khung 512 mẫu ở 16 kHz và 256 mẫu ở 8 kHz, có `reset_states()` khi cấu hình stream đổi. Vì vậy không dùng chung trạng thái model giữa các phiên độc lập nếu wrapper đang giữ state. README có đường cài qua Torch Hub; triển khai cần ghim revision và checksum model. So với WebRTC VAD hoặc VAD sẵn trong Pipecat/LiveKit (§1), Silero là lựa chọn model có thể tách riêng để thử cùng một audio corpus; chưa có phép đo chung trong khảo sát này.

**aiortc (Jeremy Lainé và cộng đồng).** [RTCPeerConnection](https://github.com/aiortc/aiortc/blob/d6a003fcb6511675318b4494e5b225b78abd2af2/src/aiortc/rtcpeerconnection.py) cung cấp trạng thái kết nối và `close()` để dọn sender/receiver/transport. [CI upstream](https://github.com/aiortc/aiortc/blob/d6a003fcb6511675318b4494e5b225b78abd2af2/.github/workflows/tests.yml) có test nhưng khảo sát này không chạy và không suy ra chất lượng mạng production. Chọn aiortc khi cần kiểm soát transport Python; chọn Pipecat khi muốn pipeline processor, LiveKit khi cần room/participant và hạ tầng realtime đã đóng gói. Không tự thay framework hoàn chỉnh bằng một thư viện transport chỉ vì API nhỏ hơn.

### 5e.2 Ma trận lỗi cần đo riêng

| Ranh giới | Tình huống kiểm | Bằng chứng phải lưu |
|---|---|---|
| Thu âm → VAD | Im lặng, nhạc/ồn, nói nhỏ, giọng Bắc/Trung/Nam, ngắt giữa câu | False start, bỏ mất tiếng đầu/cuối, thời gian chốt lượt; phiên bản VAD và normalizer |
| STT → LLM → TTS | Cùng câu hỏi bằng transcript chuẩn và bằng audio | Chênh lệch hoàn thành tác vụ; WER thấp vẫn có thể sai số tiền/tên riêng |
| Lượt nói | Người dùng chen ngang khi TTS phát và khi tool đang chạy | Thời gian tới lúc ngừng audio, không phát tiếp đoạn TTS cũ; hủy audio không mặc nhiên hủy tác vụ ghi |
| Transport | Mất mạng, reconnect, gói tới chậm/lặp, đóng tab | Session/turn ID, thứ tự sự kiện, dọn tài nguyên; tool có side effect dùng khóa chống chạy trùng |
| Quyền và dữ liệu | Từ chối/rút quyền microphone, bật/tắt ghi âm, xoá phiên | Trạng thái UI khớp capture thật; thời hạn lưu, nơi gửi audio, quyền tái dùng giọng tách khỏi quyền microphone |

**Chuẩn gốc:** [Media Capture and Streams của W3C](https://www.w3.org/TR/2025/CRD-mediacapture-streams-20251009/) yêu cầu xin quyền và chỉ báo capture; đây không phải bằng chứng người dùng đã đồng ý lưu lâu dài hay clone giọng. [SEA-HELM Audio](https://arxiv.org/abs/2610.19869) (preprint, 10/2026) minh họa phép đo chênh lệch text→speech, nhưng năm ngôn ngữ trong abstract **không có tiếng Việt**; không chuyển số điểm của paper thành kết quả tiếng Việt.

### 5e.3 Stack và cổng phát hành

1. Chốt policy microphone/recording/clone giọng; đưa lý do và khả năng rút quyền vào giao diện, giữ audio thô tách khỏi trace ứng dụng.
2. Ghim transport + VAD + STT/TTS/model revision; đo từng đoạn `end_of_user_speech → transcript_final → first_llm_token → first_audio` và toàn tuyến bằng p50/p95, không cộng trung bình để suy ra p95.
3. Kết hợp WER/CER (§5d) với độ đúng các trường quan trọng, lượt nói và kết quả tool; tách phiên bị lỗi mạng khỏi câu trả lời sai.
4. Thử interruption/reconnect bằng dữ liệu có đồng ý; tác vụ ghi chỉ xác nhận một lần qua executor (mục 03/21), không replay tool chỉ vì phải phát lại audio.
5. Gắn metadata nguồn giọng/watermark khi phù hợp (§5d và mục 19); watermark không thay hồ sơ quyền sử dụng giọng.

**Nguồn §5e:** GitHub metadata/HEAD 2/11/2026 và các permalink trên; clone chỉ đọc LICENSE, README, CI, `utils_vad.py`, `rtcpeerconnection.py`; W3C Media Capture and Streams; SEA-HELM Audio (preprint). Không có benchmark chạy mới.

## 5f. Hồ sơ kornia/kornia: thư viện thị giác máy tính khả vi trên PyTorch, đang chuyển sang làm đặc tả thực thi được (ảnh README người dùng gửi, đọc mã 3/11/2026)

> Ảnh là phần đầu README: logo Kornia "Open Source and Computer Vision, Powered by PyTorch"; badge pypi 0.9.0, downloads 120M, G-Star 98, license Apache 2.0; khối "Direction" (reference implementation và executable specification); mục "When to use Kornia" (1.200+ operator, tham số theo lô, minimal solver và RANSAC theo lô). Đã clone `--filter=blob:none` đủ lịch sử, HEAD `a733fe3b6248652b0a509d002cf452b2167965f0` (2/11/2026). **Không cài, không chạy test.**

### 5f.1 Kiểm ảnh

| Ô trong ảnh | Kết quả | Đối chiếu (3/11/2026) |
|---|---|---|
| "pypi package 0.9.0" | ✅ | PyPI `kornia` 0.9.0, Python ≥ 3.11; phụ thuộc `torch>=2.5.1`, `numpy`, `kornia_rs` (phần Rust). `main` đang là `0.9.1.dev` |
| "license Apache 2.0" | ✅ | `LICENSE` Apache-2.0, cộng thêm file `COPYRIGHT` |
| "downloads 120M" | ⚠️ khó kiểm | Có vẻ là tổng tích lũy. pypistats (không tính mirror) cho **2,18 triệu/tháng**; `ROADMAP.md` tự ghi "~3M downloads/month" |
| "1,200+ public operators" | ⚠️ chưa xác minh | Đếm `__all__` trong các `__init__.py` được **712 tên**. Đây là cận dưới, vì không phải module con nào cũng khai `__all__`. Con số 1.200 có thể tính cả lớp augmentation, model và alias |
| "From Kornia 0.9.1, a `sigma` tensor … validated on the device" | ⚠️ chưa phát hành | README trên `main` đang mô tả bản 0.9.1 chưa ra. Người dùng 0.9.0 chưa có hành vi này |
| ★ | ✅ | 12.188★, 1.494 fork, 144 issue+PR mở (GitHub search API) |

### 5f.2 Điều đáng học (đọc mã)

- **"Đặc tả thực thi được" thay vì thêm API.** `ROADMAP.md` (23/10/2026) nói rõ lỗi nguy hiểm nhất của mã hình học là sai **quy ước**: `align_corners`, tâm hay góc pixel, (x,y) hay (row,col), tọa độ chuẩn hóa hay pixel, chiều quay, chuẩn hóa homography. Code vẫn chạy nhưng sai về toán, và "this is exactly the error class LLMs reproduce". Lộ trình ba bước: **ghi rõ** (mỗi op có khối Convention trong docs và test `test_convention_*`; hiện có **1.413 test** như vậy) → **sửa và deprecate trong một cửa sổ chung** → **đóng băng** một tập "Tier A" có bảo đảm autograd, gradcheck, compile, dtype/device. Tier A **mới là đề xuất**, chưa áp dụng.
- **Conformance corpus** (dự kiến): bộ vector vàng trung lập với framework, kèm tolerance và metadata quy ước, để các port sang JAX, Rust/Triton, bản vendor **và mã do LLM sinh ra** có thể tự kiểm. Đây là mẫu tốt cho mọi thư viện có lỗi khó thấy.
- **Chính sách AI rõ ràng**: `AI_POLICY.md` và `CONTRIBUTING.md` không phân loại đóng góp theo mức dùng AI, chỉ yêu cầu nói rõ AI đã giúp gì và "care". Từ 1/8/2026 có 1.456 commit, trong đó **999 có trailer Co-Authored-By Claude**. Maintainer chính Dmytro Mishkin có 431 commit trong kỳ. Repo có `AGENTS.md` và `CLAUDE.md`. PR im lặng 15 ngày bị gắn nhãn stale nhưng **không bị đóng**.
- **Phát hành**: `pypi-release.yml` dùng trusted publishing (`id-token: write`, `pypa/gh-action-pypi-publish@release/v1`). ROADMAP ghi đã đối chiếu wheel PyPI với bản build trong CI. Tuy vậy PyPI **không có provenance** cho `kornia-0.9.0-py3-none-any.whl`. CI có workflow riêng cho typecheck, import-surface, test gói PyPI định kỳ, upstream probe và tutorial. Action **ghim theo tag** (`actions/checkout@v7`, `setup-pixi@v0.11.2`), không theo SHA.
- Không thấy telemetry (grep `telemetry|posthog|sentry_sdk` trong `kornia/`).

### 5f.3 Rủi ro và cách dùng

- Phiên bản 0.x, và lộ trình đã báo trước một **cửa sổ sửa quy ước** (box, camera, augmentation) có cảnh báo deprecation ít nhất một bản minor. Ghim phiên bản; đọc trang "Conventions & Pitfalls" và "stability policy" trước khi nâng.
- Ảnh và tham số phải là float trong `[0, 1]`. Đầu vào số nguyên không được hỗ trợ theo `CONTRIBUTING.md`.
- **Với agent viết mã thị giác**: bắt agent trích dẫn khối Convention của op đang dùng, và tái dùng test `test_convention_*` của Kornia làm cổng kiểm trước khi tin hàm hình học tự viết.

| Thư viện | ★ (3/11) | License | Khác Kornia |
|---|---|---|---|
| **kornia/kornia** | 12k | Apache-2.0 | Khả vi, chạy theo lô trên GPU; hình học epipolar, camera, RANSAC; đang xây đặc tả |
| `pytorch/vision` (torchvision) | – | BSD-3-Clause | Transform cơ bản (resize, crop, flip, jitter); mỗi lần gọi một tham số **(theo README Kornia)** |
| OpenCV | – | Apache-2.0 | Rộng nhất nhưng chạy trên CPU hoặc CUDA riêng, không khả vi |
| `albumentations` | – | MIT (bản gốc) | Augmentation trên CPU bằng numpy **(không đọc mã)** |

**Nguồn §5f:** ảnh README người dùng gửi 3/11/2026 · clone https://github.com/kornia/kornia HEAD `a733fe3b6248652b0a509d002cf452b2167965f0` (README.md, ROADMAP.md, AI_POLICY.md, CONTRIBUTING.md, LICENSE, pyproject.toml, `.github/workflows/{pypi-release,tests}.yml`; đếm `def test_convention_`, `gradcheck`, `__all__`; `git shortlog --since=2026-08-01`) · https://pypi.org/pypi/kornia/json · PyPI integrity API (0.9.0: không có provenance) · https://pypistats.org/api/packages/kornia/recent (2.176.424/tháng) · GitHub search API `repo:kornia/kornia` 3/11/2026.

## 5g. Nâng sâu 4/11/2026: từ ghi âm yêu cầu đến transcript kiểm chứng được

**Trần hiện tại:** mục này đã có ASR/TTS, đo WER và voice reliability. Với xưởng phần mềm, ghi âm phỏng vấn khách hàng, dựng phụ đề demo và voice UI cần thêm provenance của transcript, timestamp, speaker và quyền dữ liệu. Transcript do ASR không tự thành yêu cầu đã được khách hàng xác nhận; tóm tắt phải dẫn về đoạn ghi âm và giữ phần không nghe rõ.

<a id="factory-2026-11-04-whisperx"></a>

### WhisperX: forced alignment và diarization là các bước có lỗi riêng

| Thuộc tính | Kết quả đọc |
|---|---|
| Repo · SHA | `m-bain/whisperX` · `5d3678b8535698a2826a5db9eb3e4105aef85dd9` |
| License | Code BSD-2-Clause; weights ASR, alignment và diarization có license/điều kiện riêng. Không suy BSD của wrapper sang tất cả model |
| Đường xử lý | `whisperx/transcribe.py`: ASR → alignment nếu không tắt → diarization nếu bật → gán speaker theo word → writer. `alignment.py` có model mặc định theo ngôn ngữ, gồm tiếng Việt |
| Phụ thuộc | `DiarizationPipeline` tải `pyannote/speaker-diarization-community-1` qua `Pipeline.from_pretrained`, có tham số token/cache; README yêu cầu chấp nhận điều khoản model. Tải model/cache không chứng minh audio đã rời máy; cũng không được suy toàn bộ pipeline offline khi chưa kiểm egress |
| Giới hạn | README tự nêu speech chồng lấn xử lý kém, diarization không hoàn hảo, từ ngoài dictionary alignment có thể thiếu timing. Nhãn SPEAKER không xác thực danh tính con người |
| CI | `.github/workflows/tests.yml` dùng uv chạy pytest theo ma trận Python; chưa chạy inference, đo WER hay GPU trong đợt này |

**Phạm vi kiểm (2026-11-04):** đọc tài liệu, LICENSE, mã đường gọi và workflow tại SHA dưới đây; không cài/chạy upstream. Các cổng nghiệm thu là đề xuất cho repo tích hợp, chưa phải kết quả chạy của kho. Số sao không thu thập trong đợt này.

| Lựa chọn | Vai trò | Điều kiện lựa chọn |
|---|---|---|
| Whisper / faster-whisper | ASR văn bản/segment; faster-whisper dùng CTranslate2 | Baseline cho chất lượng, latency và bộ nhớ cùng model/corpus |
| whisper.cpp | ASR tối ưu triển khai cục bộ theo nền tảng | Kiểm feature/model format/hardware trên thiết bị đích |
| WhisperX | Ghép ASR với alignment và speaker diarization | Cần phụ đề có word timing hoặc phân đoạn hội thoại; chấp nhận thêm model và lỗi ghép |
| LiveKit / Pipecat | Pipeline voice tương tác theo thời gian thực | Đo barge-in, timeout, mất gói, khôi phục kết nối; không thay bộ chép lời batch |

**Stack cho xưởng:** ghi nhận quyền thu âm và mục đích → mã hóa/giới hạn lưu giữ → chốt audio hash và model revisions → ASR/align/diarize → người nghe kiểm lại đoạn có giá trị pháp lý/nghiệp vụ → liên kết yêu cầu/ADR tới timestamp → xóa dữ liệu theo policy. Nếu cần bí mật, prefetch model qua đường được phép rồi kiểm pipeline trong môi trường egress bị chặn; đo thay vì tin nhãn local.

**Cổng nghiệm thu:** corpus tách tiếng Việt vùng miền, code-switching, số tiền/tên riêng, nhiễu và nhiều người nói; đo WER/CER cùng lỗi entity quan trọng, sai số timestamp và speaker attribution. Fixture audio im lặng, quá ngắn, không có speech, chồng lấn phải có trạng thái rõ, không sinh transcript bịa thành yêu cầu. Chỉ xuất artifact đã lọc PII theo scope; review thủ công các quyết định quan trọng. Benchmark tốc độ quảng cáo upstream chưa được tái lập tại kho.

**Nguồn §5g:** [LICENSE](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/LICENSE) · [README/limits](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/README.md) · [pipeline callsite](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/whisperx/transcribe.py) · [language alignment](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/whisperx/alignment.py) · [diarization load](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/whisperx/diarize.py) · [CI](https://github.com/m-bain/whisperX/blob/5d3678b8535698a2826a5db9eb3e4105aef85dd9/.github/workflows/tests.yml).

## 6. Nguồn

- https://micdrop.dev/blog/open-source-voice-agent-frameworks · https://livekit.com/blog/best-open-source-voice-and-video-ai-agent-frameworks · https://www.forasoft.com/blog/article/pipecat-vs-livekit-agents · https://github.com/pipecat-ai/pipecat · https://techsy.io/en/blog/best-open-source-voice-agent-frameworks · https://grokipedia.com/page/List_of_open-source_voice_AI_frameworks
- https://ocdevel.com/blog/20250720-tts · https://pinggy.io/blog/best_open_source_self_hosted_text_to_speech_models/ · https://www.tryspeakeasy.io/blog/open-source-text-to-speech-2026 · https://localaimaster.com/blog/best-local-tts-models · https://www.spheron.network/blog/deploy-open-source-tts-gpu-cloud-2026/
- https://github.com/QwenLM/Qwen3-VL · https://github.com/LLaVA-VL/LLaVA-NeXT · https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-2
- https://en.wikipedia.org/wiki/ComfyUI · https://en.wikipedia.org/wiki/Automatic1111 · https://github.com/lllyasviel/Fooocus · https://insiderllm.com/guides/comfyui-vs-automatic1111-vs-fooocus/ · https://meetrix.io/blogs/fooocus-vs-automatic1111-vs-comfyui/
- Audio8 TTS (2026-10-12): https://github.com/edge0-ai/audio8_tts (clone đầy đủ) · https://huggingface.co/Audio8/Audio8-TTS-Preview-0.6b · https://huggingface.co/Audio8/Audio8-TTS-Preview-0.1b · https://audio8-ai.github.io/Audio8_TTS/ · https://deepinfra.com/Audio8/Audio8-TTS-Preview-0.6b · https://github.com/john-rocky/coreai-model-zoo/pull/47 · https://github.com/0xShug0/audio.cpp/blob/main/docs/community_models/audio8_tts.md · https://hackernoon.com/audio8-tts-preview-06b-compact-multilingual-voice-cloning · https://creativeaishow.com/audio8-tts-preview-the-free-0-6b-ai-voice-cloning-model-that-runs-on-your-cpu/ · https://huggingface.co/fishaudio/s2-pro/blob/main/LICENSE.md · https://fish.audio/fr/blog/what-we-mean-by-open-source-for-s2/
