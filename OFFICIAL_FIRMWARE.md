# M-VAVE FM-1 Official Stock Firmware, SDK & Recovery Reference

This document covers the official **M-VAVE FM-1** stock firmware releases, the open-source vendor SDK, official updater utilities, and safe rollback / recovery procedures.

---

## 1. Official Stock Firmware Releases

* **Latest Official Stock Firmware:** **[FM-1.fwsc](https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/firmware/FM-1.fwsc)** (718 KB, SHA-256 verified)
  * **Engine & Polyphony:** 8-part multitimbral synthesis engine (MIDI channels 1–8) with expanded 20-voice shared polyphony.
  * **Sequencing:** Upgraded 64-step sequencer & live arrangement matrix (8 tracks × 8 columns).
  * **Effects Chain:** True-stereo global FX chain (Filter, Reverb, Delay, Distortion, Chorus, Phaser).
  * **Voice Controls:** Independent per-voice tuning ($\pm 100$ cents), pan, and glide.
  * **Interface:** Customizable 240×240 TFT display RGB color themes.
  * **Patch Management:** Standard Yamaha DX7 `.syx` bank import and export.
* **Firmware Versions:**
  * **V16 / Latest:** Latest factory release fixing sequencer edge cases and expanded multi-timbral MIDI routing.
  * **V15:** Previous widely deployed stable factory release. Contains the baseline oscillator detune and reverb model.

---

## 2. Official Open Source Repository & Web Workbench

* **Official Open Source SDK:** **[m-vave/fm1_open](https://github.com/m-vave/fm1_open)**
  * **License:** GNU General Public License v3.0 (GPL-3.0).
  * **Contents:** Complete hardware C drivers for JieLi AC791N SoC (display, I2S DAC, silicone keys, rotary encoders), 8 tracks, 8 sample slots, 16 demo FX, and build scripts.
* **Online Web Workbench:** **[open.m-vave.com/fm1-workbench](https://open.m-vave.com/fm1-workbench)**
  * **Features:** In-browser WebAssembly hardware simulation, preset testing, and direct WebUSB / WebMIDI firmware flashing.
* **Official Community Announcement:**
  * **[M-VAVE Official Forum Topic #4](https://forum.m-vave.com/topic/4)** *(Note: manufacturer forum topic #4 was subsequently removed by manufacturer, archived copies preserved in community mirrors).*

---

## 3. Official Flasher Utilities

* **M-UPGRADE-FM1.app (macOS):**
  * Bundled directly in this repository: [`M-UPGRADE-FM1.app`](M-UPGRADE-FM1.app)
  * Decompiled source & resource breakdown: [MVAVE-M-UPGRADE-decompiled](https://github.com/entitymar/MVAVE-M-UPGRADE-decompiled)
* **Windows Flasher:**
  * Official M-VAVE M-UPGRADE utility executable for Windows (distributed via M-VAVE software download portal).

---

## 4. Safe Rollback & Transit Guidelines

> [!TIP]
> **Community Safe Flashing Practice:**
> While not an absolute hard rule, there is a prominent community recommendation to avoid flashing one custom firmware directly over another. To minimize bricking risks, some users suggest rolling back to the official stock firmware (V15/V16) via M-VAVE's official updater first, and only then flashing the next custom firmware build.
> 
> Alternatively, you can use **[TransitFM1](https://quixotic7.github.io/TransitFM1/)** — a dedicated lightweight bridge firmware by Quixotic7 designed with crash-guarded boot stubs and stock V15 identity emulation to safely transition between custom builds without wear on protected boot sectors.

---

## 5. Stock Firmware Patchers & Binary Mods

Modifications that directly enhance or repurpose the official factory firmware:

| # | Name, Author, License & Links | Description & Features |
|---|-------------------------------|------------------------|
| 1 | **FM-1 Firmware Patcher by Christian Zietz (czietz)**<br>[GitHub](https://github.com/czietz/fm1-firmware-patcher)<br>**License:** Open Source (Unlicense / Public Domain). | **Target:** Stock official **V15** firmware (`FM-1.fwsc`).<br>**Modifications & Bug Fixes:**<br>* Fixes the oscillator detune calculation in the stock synth engine to accurately match Dexed / Yamaha DX7 behavior.<br>* Disables unhandled MIDI aftertouch messages that cause unwanted heavy vibrato.<br>* Modifies the UI colorway: changes the main oscilloscope display to dark blue and the FX selection cursor to green (as visual confirmation of patched firmware).<br>**Usage:** Python patcher script applying precise binary offsets (`python patch_firmware.py FM-1.fwsc FM-1-fixed.fwsc`). Flashed via M-VAVE's M-UPGRADE utility. |
| 2 | **FM-1 Macropad Patch by smememe**<br>[GitHub](https://github.com/smememe/fm1-macropad-patch) \| [Web Patcher](https://smememe.github.io/fm1-macropad-patch/)<br>**License:** Open Source (MIT). | **Target:** Stock official **V15** firmware (`FM-1.fwsc`).<br>**Concept & Modifications:** Binary patch that transforms the FM-1 into a 55-input MIDI macro pad controller. Modifies the firmware so every physical button, piano key, and rotary knob sends a USB-MIDI note message while turning off all LEDs. Combined with desktop hotkey software, it converts the synthesizer into an external macro pad.<br>**Usage:** Apply patch directly in the browser via WebAssembly/WebMIDI or via Python script (`python3 fm1patch.py FM-1.fwsc`). Flashed via standard update tools. |

---

*Related documents: [README.md](README.md) (Custom Firmwares Catalog) | [REVERSE_ENGINEERING.md](REVERSE_ENGINEERING.md) (Hardware & OTA Protocol Reference) | [RESOURCES.md](RESOURCES.md) (Tools & Utilities).*
