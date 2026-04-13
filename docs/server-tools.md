# Server Tools

Tools for running and managing DCS dedicated servers.

---

### [DCSServerBot](https://github.com/Special-K-s-Flightsim-Bots/DCSServerBot)
**Release:** [v3.0.4.22](https://github.com/Special-K-s-Flightsim-Bots/DCSServerBot/releases/tag/v3.0.4.22)
Full-featured server admin bot with Discord integration. Handles server monitoring, per-player statistics, mission rotation, slot blocking, and bans. Integrates with SRS, LotAtc, Olympus, SkyEye, Tacview, and DCS-gRPC. Scales from single-server hobby setups to large multi-server deployments.

- **Docs:** https://special-k-s-flightsim-bots.github.io/DCSServerBot/

---

### [DCS-gRPC](https://github.com/DCS-gRPC/rust-server)
**Release:** [0.8.1](https://github.com/DCS-gRPC/rust-server/releases/tag/0.8.1)
gRPC server for DCS. Runs as a Lua hook inside the server and exposes real-time mission state and control over gRPC. Foundation for external tools and bots that need live interaction with a running server.

---

### [DCS-SRS](https://github.com/ciribob/DCS-SimpleRadioStandalone)
**Release:** [2.3.6.0](https://github.com/ciribob/DCS-SimpleRadioStandalone/releases/tag/2.3.6.0)
SimpleRadio Standalone. De facto VOIP radio system for DCS multiplayer. Integrates with in-cockpit radio frequencies for full-fidelity modules; manual tuning for FC3 aircraft. Required on virtually every serious multiplayer server.

- **Website:** http://dcssimpleradio.com/

---

### [dcs-bullseye](https://github.com/TylerDOC1776/dcs-bullseye)
**Release:** [2026-03-27](https://github.com/TylerDOC1776/dcs-bullseye)
DCS server management stack — Discord bot, FastAPI REST orchestrator, and Windows agent. Long-running actions run as async Jobs; real-time state exposed via SSE/WebSocket.

---

## Paid / No Release Tracking

**[LotAtc](https://www.lotatc.com/)** — GCI/ATC radar client for DCS servers. Provides a terrain-masked radar picture with BRAA tools and precision approach management. Standard on servers running a dedicated GCI role. Integrates with DCSServerBot.

**[Tacview](https://www.tacview.net/)** — ACMI-style flight data recorder and debrief tool. Records all unit positions and events in real time for post-mission playback and analysis. Free tier available; premium adds live telemetry and advanced features.
