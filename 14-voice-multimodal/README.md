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

## 6. Nguồn

- https://micdrop.dev/blog/open-source-voice-agent-frameworks · https://livekit.com/blog/best-open-source-voice-and-video-ai-agent-frameworks · https://www.forasoft.com/blog/article/pipecat-vs-livekit-agents · https://github.com/pipecat-ai/pipecat · https://techsy.io/en/blog/best-open-source-voice-agent-frameworks · https://grokipedia.com/page/List_of_open-source_voice_AI_frameworks
- https://ocdevel.com/blog/20250720-tts · https://pinggy.io/blog/best_open_source_self_hosted_text_to_speech_models/ · https://www.tryspeakeasy.io/blog/open-source-text-to-speech-2026 · https://localaimaster.com/blog/best-local-tts-models · https://www.spheron.network/blog/deploy-open-source-tts-gpu-cloud-2026/
- https://github.com/QwenLM/Qwen3-VL · https://github.com/LLaVA-VL/LLaVA-NeXT · https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-2
- https://en.wikipedia.org/wiki/ComfyUI · https://en.wikipedia.org/wiki/Automatic1111 · https://github.com/lllyasviel/Fooocus · https://insiderllm.com/guides/comfyui-vs-automatic1111-vs-fooocus/ · https://meetrix.io/blogs/fooocus-vs-automatic1111-vs-comfyui/
- Audio8 TTS (2026-10-12): https://github.com/edge0-ai/audio8_tts (clone đầy đủ) · https://huggingface.co/Audio8/Audio8-TTS-Preview-0.6b · https://huggingface.co/Audio8/Audio8-TTS-Preview-0.1b · https://audio8-ai.github.io/Audio8_TTS/ · https://deepinfra.com/Audio8/Audio8-TTS-Preview-0.6b · https://github.com/john-rocky/coreai-model-zoo/pull/47 · https://github.com/0xShug0/audio.cpp/blob/main/docs/community_models/audio8_tts.md · https://hackernoon.com/audio8-tts-preview-06b-compact-multilingual-voice-cloning · https://creativeaishow.com/audio8-tts-preview-the-free-0-6b-ai-voice-cloning-model-that-runs-on-your-cpu/ · https://huggingface.co/fishaudio/s2-pro/blob/main/LICENSE.md · https://fish.audio/fr/blog/what-we-mean-by-open-source-for-s2/
