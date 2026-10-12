# 11 · Browser Agents, Computer Use & Agent Sandboxes

> Agent thao tác trình duyệt/máy tính và hạ tầng chạy code an toàn cho agent.

## 1. Browser agents / automation cho LLM

| Dự án | Repo | License | ★ (2026) | Cách hoạt động | Ghi chú |
|---|---|---|---|---|---|
| **Browser Use** | browser-use/browser-use | MIT | ~114k (9/2026) | Agent Python điều khiển Playwright, DOM + vision | Lớn nhất; có cloud |
| **agent-browser** (Vercel Labs) | vercel-labs/agent-browser | – | ~29.5k | CLI Rust cho agent điều khiển trình duyệt | Mới, tăng nhanh |
| **Stagehand** (Browserbase) | browserbase/stagehand | MIT | ~25.6k | SDK `act/extract/observe`, v4 dùng CDP trực tiếp (không Playwright) | Tích hợp Claude Code, Codex, Mastra |
| **Skyvern** | Skyvern-AI/skyvern | AGPL-3.0 | – | Vision + LLM, workflow form | |
| **Playwright MCP** | microsoft/playwright-mcp | Apache-2.0 | – | MCP server, làm việc trên accessibility tree (không screenshot) | Server MCP phổ biến nhất nhóm browser |
| **Steel / Browserbase / Hyperbrowser** | – | – | – | Browser-as-a-service cho agent | Hạ tầng |
| **Expect / Passmark** | – | – | – | AI testing trên browser | QA |

**Nhận định:** DOM/accessibility-tree rẻ và ổn định hơn vision; vision cần cho canvas/ứng dụng lạ. Chọn Browser Use để thử nhanh, Stagehand khi cần SDK có kiểm soát trong TypeScript.

## 2. Computer use (điều khiển máy tính)

| Nhà cung cấp / dự án | Ghi chú |
|---|---|
| Anthropic Computer Use (tool `computer_20xx`) | API tool chính thức; reference implementation + quickstart container |
| OpenAI Operator / CUA (Computer-Using Agent) | Sản phẩm trong ChatGPT + API `computer-use-preview` |
| Open Interpreter, UI-TARS (ByteDance), OS-Copilot | Mã mở, kiểm soát desktop |
| Benchmark | OSWorld, WebArena, Mind2Web, AgentDojo (bảo mật) |

## 3. Sandbox chạy code cho agent

| Nền tảng | Mã mở? | Cách cô lập | Cold start | Điểm nổi bật | Giá tham khảo |
|---|---|---|---|---|---|
| **E2B** | Apache-2.0 (SDK + infra) | Firecracker microVM, kernel riêng | ~0.5s (đo độc lập, nhanh nhất) | SDK đơn giản, nhiều template | ~$0.0504/vCPU-giờ |
| **Modal** | SDK mở, nền tảng đóng | gVisor (user-space kernel), tùy chọn VM | nhanh | **Có GPU** trong sandbox, serverless Python | ~$0.071/vCPU-giờ |
| **Daytona** | Từng mở; một nguồn nói đóng từ 6/2026 **(chưa xác minh)** | Container (tùy chọn VM) | Claim 90ms, đo được ~0.75s | Snapshot/fork stateful | |
| **Fly Machines** | Nền tảng | Firecracker | | Máy ảo nhanh, giá theo giây | |
| **Vercel Sandbox / Cloudflare Sandbox** | Nền tảng | microVM / isolate | | Gắn hệ sinh thái | |
| **microsandbox** | mã mở | microVM | | Self-host | |

**Chọn:** cần kernel riêng & mở → E2B; cần GPU → Modal; cần snapshot/fork → Daytona; tự host → microsandbox/Firecracker. Nghiên cứu bảo mật: arXiv 2606.08433 (so sánh engine: attack surface, CVE, patch cadence).

## 4. Nguồn

- https://gist.github.com/kevinmichaelchen/9d77b8a681238cc45297dff969686175 · https://www.firecrawl.dev/blog/best-browser-agents · https://scrapfly.io/blog/posts/stagehand-vs-browser-use · https://agentscamp.com/guides/comparisons/browser-agents-compared-2026 · https://bug0.com/blog/expect-vs-agent-browser-vs-stagehand-vs-passmark · https://github.com/browserbase/stagehand · https://kanopylabs.com/blog/stagehand-vs-browserbase-vs-steel-browser-ai
- https://www.superagent.sh/blog/ai-code-sandbox-benchmark-2026 · https://blog.logrocket.com/comparing-ai-agent-sandbox-platforms-e2b-modal-daytona-and-more/ · https://devtoollab.com/blog/best-ai-code-execution-sandboxes · https://bex.co/blog/2026/09/25/four-companies-one-sandbox-market-agent-code-execution · https://www.developersdigest.tech/blog/ai-agent-code-sandbox-comparison-2026 · https://www.beri.net/article/e2b-vs-modal-vs-daytona-agent-sandbox-pricing-isolation-2026 · https://particula.tech/blog/modal-vs-e2b-vs-daytona-vs-vercel-sandbox-ai-code-execution · https://arxiv.org/pdf/2606.08433
