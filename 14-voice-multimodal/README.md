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
| Fish Speech, Orpheus, Coqui XTTS (ngừng) | – | | |

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
