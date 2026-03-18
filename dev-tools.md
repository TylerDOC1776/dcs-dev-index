---
title: Dev Tools
nav_order: 5
---

Tools for building, editing, and debugging DCS content outside the mission editor.

---

### [pydcs](https://github.com/pydcs/dcs)
**Release:** [v0.13.0](https://github.com/pydcs/dcs/releases/tag/v0.13.0)
Python library for programmatically creating and modifying DCS `.miz` files. Supports unit/group/waypoint creation, payload assignment, trigger scripting, and data export. Used as the backend by DCS Liberation and Retribution.

---

### [DCS-BIOS](https://github.com/DCS-Skunkworks/dcs-bios)
**Release:** [v0.11.2](https://github.com/DCS-Skunkworks/dcs-bios/releases/tag/v0.11.2)
Export hook that exposes cockpit control states over serial/UDP for hardware cockpit builders. The standard for DIY pit integration with Arduino or ESP32.

- **Docs:** https://dcs-bios.readthedocs.io/

---

### [DCS-BIOS Arduino Library](https://github.com/DCS-Skunkworks/dcs-bios-arduino-library)
**Release:** [0.3.12](https://github.com/DCS-Skunkworks/dcs-bios-arduino-library/releases/tag/0.3.12)
Arduino library for communicating with DCS-BIOS to drive physical switches, encoders, buttons, and displays in a hardware cockpit.

---

### [VEAF Mission Creation Tools](https://github.com/VEAF/VEAF-mission-converter)
**Release:** [20250329](https://github.com/VEAF/VEAF-mission-converter/releases/tag/20250329)
Build toolchain for team-based mission development. Extracts a `.miz` to a version-controllable source tree and rebuilds for deployment. Designed for multi-developer workflows using Git.

---

## No Release Tracking

**[OvGME](https://wiki.hoggitworld.com/view/OVGME)** — Mod manager. Replaces and backs up game files for clean enable/disable of mods. Supports repository URLs for one-click updates. Standard tool for managing mods on both client and server.

**[Skatezilla DCS Updater](https://forum.dcs.world/topic/134493-the-dcs-updater-launcher-gui-utility-version-20-2023/)** — GUI dashboard for managing DCS installations. Multi-threaded launch, graphics preset editing outside DCS, and VR/2D launch profiles.

**[Hoggit SSE Docs](https://wiki.hoggitworld.com/view/Simulator_Scripting_Engine_Documentation)** — Community reference for the DCS Scripting Engine API. Primary resource for any Lua mission scripting work.
