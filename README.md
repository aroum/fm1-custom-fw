# M-VAVE FM1 & M-UPGRADE Analysis & MIDI SysEx Protocol Documentation

This document contains technical research, hardware details, and reverse-engineering results for the **M-VAVE FM1** synthesizer (powered by the **JieLi AC791N** processor) and the `M-UPGRADE-FM1.app` (macOS) utility.

---

## 1. Custom & Alternative Firmwares

Community-developed custom firmwares, mods, and experimental firmware projects for the M-VAVE FM-1:

1. **[Felucca by hugelton](https://github.com/hugelton/Felucca) ([Web Installer](https://hugelton.github.io/Felucca/) | [Web Editor](https://hugelton.github.io/Felucca/webapp/editor/)):**
   * **License:** Open Source (GPL-3.0-only).
   * **Synthesizer Engines:** 9 distinct sound engines including **ANALOG** (virtual analog, 2 osc, PWM, resonant LPF), **DIGITAL** (4-op FM, 8 algorithms, feedback), **PHASE** (phase distortion), **LOFI** (chiptune, 4-bit wave RAM), **SAMPLE** (multisampled instruments + user slots), **VOICE** (formant/vocal osc), **TRIO** (3 osc with ring mod/sync), **WHEEL** (tonewheel organ with drawbars & rotary speaker), and **GRAIN** (granular textures).
   * **Architecture & Features:** 4 tracks (3 synth parts + 1 GM drum track, 8 shared voices), 64-step sequencer per track with chords/ties/slides and live loop recording, per-track SLICER (16-step tempo-synced gate/stutter), effects (distortion, chorus, delay, reverb sends, master limiter), scales & white-key quantization, and web editor.
   * **Installation:** Direct web installer via WebMIDI in Chrome/Edge over standard USB-C cable (no extra hardware needed; stock updater restores official firmware).

2. **[baud girl Custom Firmware Mod](https://baudgirl.com/):**
   * **License:** Closed Source.
   * **Features:** Comprehensive overhaul and reimagining of the stock firmware ergonomics and controls. Adds Virtual Analog (VA) synthesizer engines and a 64-step sequencer.
   * **Installation:** Web-based browser installer in a couple of clicks via WebMIDI.

3. **[Lunar Modulator by ip2k](https://github.com/ip2k/lunar-modulator):**
   * **License:** Open Source (MIT).
   * **Status:** Research / bench stage.
   * **Features:** *Intergalactic Modulation Station* — alternative firmware based on Mutable Instruments synthesizer engines, a Movy-style sequencer, and an in-browser virtual FM-1 emulator/simulator.

4. **[Groove OS](https://www.groove-os.com/) ([Web Emulator](https://www.groove-os.com/emu)):**
   * **License:** Commercial / Proprietary ($29).
   * **Concept:** Transforms the FM-1 into a standalone multitrack groovebox without needing any external equipment.
   * **Features:** Up to 8 independent tracks (drums, bass, chords, leads) with independent loop lengths (1 to 8 bars) for evolving polyrhythmic structures, dual sound engine (native 6-op FM + Virtual Analog with ladder filter), up to 20 voices of polyphony (12 FM + 8 VA, max 6 for drums), 64-step sequencer with parameter locks (p-locks), live stage view, curated sound packs, and DX7 SysEx patch reception.
   * **Installation:** Browser-based USB installer via WebMIDI in Chrome/Edge (~2 minutes).

5. **[SLOOP by isod89](https://github.com/isod89/sloop-fm1) ([Web Installer](https://isod89.github.io/sloop-fm1/) | [Web Editor](https://isod89.github.io/sloop-fm1/webapp/editor/)):**
   * **License:** Open Source (GPL-3.0). Based on Felucca by Hügelton Instruments.
   * **Concept:** Live performance groovebox firmware designed for any music style without mandatory presets or fixed patterns.
   * **Features:** 4 tracks (3 synth tracks + 1 drum machine with 16 sounds across the white keys), 9 synthesis engines, 68 sounds, 37 drum kits, custom sample support, and live-playable song mode. Features USB stereo audio input (class-compliant recording directly into DAWs without drivers), 3.5 mm TRS MIDI IN keyboard input, MIDI clock in/sync, button and note LED illumination modes for dark environments, sample chopping/fitting, and a web editor with full backup/restore.
   * **Installation:** Browser-based installer via WebMIDI in Chrome/Edge, with easy rollback to M-VAVE stock V15.

6. **[FoMni-1 by charlesvestal](https://github.com/charlesvestal/fm1-fomni) ([Web Installer](https://charlesvestal.github.io/fm1-fomni/)):**
   * **License:** Open Source (GPL-3.0).
   * **Concept:** Suzuki Omnichord-inspired chord harp firmware for the FM-1.
   * **Features:** Strum chords across the white keys like a harp strumplate, select chord roots and types on the black keys, integrated rhythmic accompaniment and arpeggiator modes.
   * **Installation:** Browser WebMIDI installer via USB.

7. **[ChoralRoot FM-1 by Quixotic7](https://github.com/Quixotic7/ChoralRootFM1) ([Web Installer](https://quixotic7.github.io/ChoralRootFM1/) | [Web Emulator](https://quixotic7.github.io/ChoralRootFM1/emu/)):**
   * **License:** Open Source (GPL-3.0). Based on Felucca (engines/platform) and ChoralRoot (Monome grid chord engine).
   * **Concept:** Telepathic Orchid / Monome-style chord performance instrument.
   * **Features:** Two-handed chord shaping (one hand selects roots, the other shapes voicings), custom key modes, performance bass line, built-in looper, full color UI, and browser sound emulator.
   * **Installation:** Browser WebMIDI installer via USB.

8. **[Melodee by keremimo](https://github.com/keremimo/melodee) ([Web Installer](https://keremimo.github.io/melodee/) | [Web Editor](https://keremimo.github.io/melodee/webapp/editor/)):**
   * **License:** Open Source (GPL-3.0-only). Modified build based on Felucca.
   * **Features:** Adds a native **Casio CZ-1** phase-distortion engine with 64 original CZ-1 factory preset tones, 8 device CZ banks with `.syx` import/export, 38 dedicated editing pages, full backup/restore before flashing, and WebMIDI management.
   * **Installation:** Browser WebMIDI installer with built-in backup before installation.

9. **[FM1 Quest by hericdk](https://github.com/hericdk/fm1-quest) ([Web Installer](https://hericdk.github.io/fm1-quest/webapp/installer/)):**
   * **License:** Open Source (GPL-3.0-only). Built upon the SLOOP groovebox core.
   * **Concept:** Fantasy RPG sidescroller interface for the groovebox: tracks are represented as party heroes, sequence steps are attacks, BPM drives party walk speed, scales dictate biomes, and recording loops triggers boss fights.
   * **Installation:** Browser WebMIDI installer via USB.

> [!TIP]
> **Community Flashing Experience & Safe Upgrade Practice:**  
> While not an absolute hard rule, there is a prominent community recommendation to avoid flashing one custom firmware directly over another. To minimize bricking risks, some users suggest rolling back to the official stock firmware (v15) via M-VAVE's official updater first, and only then flashing the next custom firmware build.

---

## 2. Hardware & Device Ecosystem Overview

### 2.1. Target Device & Processor
* **Target Device:** **M-VAVE FM1** (FM Synthesizer / MIDI Controller).
* **Processor SoC:** **JieLi AC791N** (WL82 series, 32-bit RISC core).
* **Official Development Board:** **JL_AC79_DevKit V1.0** (AC791N evaluation kit).
  * [JL_AC79_DevKit V1.0 Official Documentation](https://doc.zh-jieli.com/AC79/zh-cn/release_v1.0.3/board_description/board_overview/index.html)
  * Note: In retail/marketplace listings, this devboard has been found available for purchase primarily on **Taobao**.
  
  ![JL_AC79_DevKit V1.0](photos/devboard.webp)

* **Synthesizer Product Page:** [Cuvave / M-VAVE FM-1 Product Page](http://www.cuvave.com/product?id=fm-1)
* **Latest Available Synthesizer Firmware:** [FM-1.fwsc (v15 2026-07-30)](https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/firmware/FM-1.fwsc)
* **Firmware v15 Entropy Analysis:** ([Source Issue #1](https://github.com/aroum/fm1-custom-fw/issues/1))
  
  ![Firmware v15 Entropy Analysis](photos/firmware_entropy.png)

* **M-VAVE Ecosystem:** Many other M-VAVE audio products (MIDI foot controllers, audio interfaces, and digital pedals) use the same JieLi AC791N / AC69xx processor platform and share similar OTA firmware architectures.

### 2.2. Hardware PCB Characteristics & Recovery Vector
* **No Debug Ports / Jumpers:** The M-VAVE FM1 PCB contains **no exposed debug headers** (JTAG, SWD, or UART debug pads).
* **No Recovery Buttons:** There are **no hidden jumper pins or physical recovery buttons** on the board for forcing bootloader / DFU mode.
* **Firmware Update Vectors:**
  * **Standard User-Mode Flashing:** MIDI SysEx over USB is the official, application-level firmware update channel available on the device.
  * **Unbrick & Hardware Recovery (JieLi Mask-ROM / UBOOT mode):** The JieLi AC791N SoC boot ROM can be forced into its mask-ROM USB download mode (`UBOOT1.00`) through the external USB-C port using a dedicated **RP2040-based hardware dongle** (or vendor JieLi USB Updater). This dongle bit-bangs the hardware boot key (`0x16EF` at ~50 kHz) over USB D+/D- lines at power-up, allowing SPI flash recovery and unbricking without opening the enclosure (see [ip2k/mvave-fm1-open-firmware](https://github.com/ip2k/mvave-fm1-open-firmware)).

### 2.3. Device Disassembly & Case Opening Instructions
To open the physical enclosure of the M-VAVE FM1:
1. **Remove Bottom Screws:** Unscrew **6 self-tapping screws** from the bottom casing.
   * **Hidden Screw:** 5 screws are visible on the bottom surface; **1 screw is hidden in the center under the product sticker**.
   * **Rubber Feet:** The rubber feet do **NOT** need to be unglued or peeled off (no screws are hidden under the rubber pads).
2. **Separate Housing Latches:** After removing all 6 screws, carefully unclip the internal **plastic retaining latches/snaps** running along the bottom enclosure seam to separate the case halves.

* **Teardown & Internal PCB Photos:**
  * High-resolution disassembly photos of the PCB and internal components are available locally in the [photos/](photos/) directory.
  * Teardown photo discussion and community analysis can also be viewed on [Reddit r/synthdiy](https://www.reddit.com/r/synthdiy/comments/1vgotwe/comment/p3gk1ko/).


---

## 3. Core Technical Findings

### 3.1. Does the firmware update occur over MIDI?
**Yes, the firmware update occurs entirely over the MIDI SysEx protocol.**

The application does not use dedicated USB DFU/CDC emulation or direct low-level raw flash access during standard operation. The entire process (from handshake to streaming every byte of firmware and preset data) is executed via **USB MIDI SysEx messages** using the **RtMidi** library on top of macOS **CoreMIDI**.

### 3.2. Where is the firmware file stored?
**The firmware binary is embedded directly inside the native executable file.**

There are no external `.bin` or `.hex` files in the resources directory. Inside the executable file [M-UPGRADE-FM1](M-UPGRADE-FM1.app/Contents/MacOS/M-UPGRADE-FM1), the firmware image is stored as an embedded Qt resource package:
* **Qt Resource Length Prefix:** `0x47EB4` (`0x000ABC14` = 704,052 bytes).
* **Package Span:** `0x47EB8` – `0xF3CEC` (704,052 bytes). Contains stock V14 (`FM-1_014`).
* **Container Signatures:** `@JMUA` (offset `0xF3BB8`), `JLUFW` (offset `0xF3CDC`), and target CPU tag `AC791N` at `+0x424`.

### 3.3. Is Signature Verification implemented?
**Asymmetric cryptographic signature verification (RSA/ECDSA/AES) is NOT implemented.**

Security checks include:
1. **Container Header & Signature Validation:** Verification of `@JMUA` / `JLUFW` signatures, target device type, and version strings.
2. **Size Boundaries Validation:** `Embedded firmware too small: %1 bytes (min %2)`.
3. **Checksums (CRC/Byte Checksums):** Every block transmitted via SysEx is accompanied by a byte checksum.

---

## 4. M-UPGRADE-FM1 Application Architecture

* **UI Framework:** Qt6 (`MainView`, `SelectFile`, `LoadingWidget`).
* **MIDI Stack:** RtMidi (`RtMidiIn`, `RtMidiOut`, `MidiInCore`, `MidiOutCore`).
* **OTA Update Worker Modules:**
  * `OtaUpgradeWorker`: Background worker managing the two-step firmware flashing process.
  * `PresetUpdateWorker`: Background worker handling preset bank uploads.
  * `OtaFormat`: Utility class responsible for packing (`pack`), parsing (`parse`, `tryParse`), and building metadata frames (`buildMetaSequence`).

---

## 5. MIDI SysEx Commands & Verified OTA Protocol

### 5.1. Handshake & Device Detection Trace
* **Purpose:** Query connected devices for FM1 identity and status.
* **Handshake Query (Host → Device):** `F0 00 32 45 00 00 00 40 7F F7`
* **Incoming Response Frame (41 bytes wire, 34 bytes unpacked):**
  `F0 00 32 45 58 01 00 00 23 4D 5A 44 XX XX XX ... 40 [chk] F7`
  * Unpacks (7-bit LSB-first) on channel `00 59 11` to a 34-byte ID block containing model identity (`FM-1_015` or `FM-1_014`).
* **Parameter Query Fuzzing Note:** Exhaustive read scanning confirmed that the M-VAVE FM1 synthesizer responds **exclusively to Parameter ID `0x40` (64)**. Queries sent to all other Parameter IDs produce no response.

### 5.2. Verified Two-Step Session Flow (Device-Pull Protocol)
Analysis of the hardware verifier (`AL-255/FM-1-RE`, `docs/io/11-ota-protocol.md`, Issue #2) confirms that the firmware update is a **device-pull** architecture rather than host-push:

1. **Step 1: Verification Mode**
   * Host sends enter-upgrade command: `F0 22 24 35 7F F7`.
   * The device begins *pulling* file chunks via read requests. After entry reads pass verification, the device writes a JieLi `UPDATA_PARM` boot record and soft-resets into the OTA loader.
   * Device re-enumerates as USB device `4D4A:4155` (`ota-FM-1`).

2. **Step 2: OTA Flash Upgrade Mode**
   * Host sends handshake query and `F0 22 24 35 7F F7` again to the OTA loader.
   * The device pulls the complete image with read requests (header reads, entry-list reads descending from the top, then bulk data ascending).
   * Upon reaching completion, the device requests address `0xF0000000` (length 8); host replies with `"success\0"` on channel `00 32 41 01`. The device then reboots into the new firmware.

### 5.3. Wire Framing: Read-Request and Data-Response
All payload data between the host and device is framed as:
```text
F0 00 32 41 41 [f1:4][addr:4][len:4] [pack7(data)...] F7
```
* **Header:** `00 32 41 41` (7-bit wire packing of internal channel `00 59 30`).
* **Fields:** `f1`, `addr`, and `len` are 32-bit little-endian integers encoded as 4×7-bit groups (`b0 | b1<<7 | b2<<14 | b3<<21`).
  * `len` encodes `(length << 4) | flashtype`.
  * In requests (Device → Host): `f1 = 0`.
  * In responses (Host → Device): `f1 = length >> 4`.
* **Data Encoding:** Continuous **8→7 LSB-first bitstream** (7 wire bytes per 8 data bytes). The payload contains `length` data bytes plus 1 checksum byte:
  ```python
  checksum = ~(flashtype + sum(data) + sum(addr_LE4) + sum(len_LE3)) & 0xFF
  ```


---

## 6. Memory Map, Bootloader & Custom Firmware Development

### 6.1. Bootloader Layout & Memory Offsets
In JieLi microcontrollers (AC791N / WL82 series):
1. **Mask ROM (ROM0):** Hardwired ROM initiating chip reset.
2. **UBOOT (Bootloader):** Located at SPI Flash physical address **`0x00000000`** (size 16 KB – 64 KB).
3. **Partition Table & Header (`app_dir_head` / `isd_config.ini`):** Partition table and pin definitions (Power Pin, UART, SD).
4. **App Code Offset (`app.bin`):** User application code starts at Flash offset **`0x4000`** (16 KB) or **`0x10000`** (64 KB) as specified by `isd_config.ini`.

### 6.2. Custom Firmware Support & CRITICAL Bootloader Re-entry Requirement

**Flashing custom firmware via this protocol is fully supported, BUT requires strict adherence to bootloader re-entry logic:**

> [!CAUTION]
> **CRITICAL BOOTLOADER RE-ENTRY REQUIREMENT:**  
> Because the M-VAVE FM1 PCB lacks physical recovery buttons or debug pads, **any custom firmware MUST retain or implement a mechanism to enter the bootloader / OTA mode** (e.g. by listening for the SysEx verification/upgrade commands `0x01` / `0x02` or handling a button combination during startup).  
> **If custom firmware is flashed without a bootloader entry handler, the device will be permanently soft-locked against future MIDI updates or rollback to stock firmware.**

**Requirements for compiling custom firmware:**
1. **Toolchain:** Official JieLi GCC toolchain targeting **Pi32v2 / q32s** architecture.
2. **Linker Script:** Code must be linked at the target partition offset (`origin Flash: 0x4000` / `0x10000`).
3. **Bootloader Handler:** Include the SysEx parser / OTA transition handler in the custom application code.
4. **Container Packaging (`isd_tools`):** Package output binaries using `isd_download` / `fw_pack` into a UFW container with `@JMUA` / `JLUFW` headers.
5. **Flashing:** The resulting UFW file can be transmitted via `M-UPGRADE-FM1` or the custom Python script ([fm1_flasher.py](fm1_flasher.py)).

---

## 7. Binary References & Offsets

Binary offsets extracted from analysis:

1. **Native Application Binary:**
   * Binary Path: [M-UPGRADE-FM1](M-UPGRADE-FM1.app/Contents/MacOS/M-UPGRADE-FM1)
   * **Offset `0xEEDDC`**: Resource path string `usb_hid_ota.bin`.
   * **Offset `0xF14AD`**: Bootloader configuration block `isd_config.ini`, `app_dir_head`, `uboot`, `POWER_PIN`.
   * **Offset `0xF3BB8`**: Container signature `@JMUA`.
   * **Offset `0xF3CDC`**: JieLi firmware container magic `JLUFW`.
   * **Offset `0x14C010`**: SysEx header data symbol `_s_arrSysexHead`.

2. **Supported Hardware & UBOOT Documentation:**
   * JieLi Chip Series List (WL82 / AC791N): [README.md:L84](jl-uboot-tool/README.md#L84)
   * UBOOT Architecture: [what-is-uboot.md](jl-uboot-tool/docs/what-is-uboot.md)

---

## 8. Firmware Size Boundaries

Firmware size is constrained by three factors:

### 8.1. SPI Flash Capacity
AC791N chips feature **4 MB (32 Mbit)** or **8 MB (64 Mbit)** internal/external SPI Flash.
* **Layout:**
  * **UBOOT (Bootloader):** First `16 KB` – `64 KB` (`0x00000000` – `0x00010000`).
  * **VM / Flash DB (Settings):** Final `16 KB` – `64 KB` of Flash.
  * **User App Partition:** Remaining space between UBOOT and VM.
* **Maximum Image Size:** For 4 MB Flash, the maximum compiled image size is approximately **~3.9 MB**.

### 8.2. Application Boundary Validation
* **Lower Limit:** `Embedded firmware too small: %1 bytes (min %2)` (requires valid `@JMUA` header and >64 KB size).
* **Upper Limit:** Protocol size field is 32-bit (up to 4 GB payload support).

### 8.3. Execution Model (XIP)
Code runs via **XIP (Execute-In-Place)** directly from SPI Flash via the MCU hardware cache. SRAM size limits dynamically allocated memory (`.bss` / `.data`), but does not restrict binary code size in Flash.

---

## 9. Python Firmware Utility (`fm1_flasher.py`)

A standalone CLI tool [fm1_flasher.py](fm1_flasher.py) provides firmware extraction and experimental protocol tooling. Project environment is managed via [`uv`](https://github.com/astral-sh/uv) (configured in [`pyproject.toml`](pyproject.toml)).

> [!WARNING]
> **FLASHING STATUS & PROTOCOL DISCLAIMER (Issue #2):**  
> Direct firmware flashing implemented in [fm1_flasher.py](fm1_flasher.py) is **experimental and non-functional** on physical hardware because it assumes a host-push packet structure, whereas the actual synthesizer hardware runs a **device-pull protocol** with 8→7 LSB-first bitstream encoding (documented in Section 5).  
> **For verified, byte-exact firmware flashing on physical hardware, use `tools/fm1_ota.py` from [AL-255/FM-1-RE](https://github.com/AL-255/FM-1-RE).**

### Features:
* **Firmware Extraction (`--extract`):** Fully functional. Carves the exact 704,052-byte `.fwsc` package (`0x47EB8`–`0xF3CEC`, stock V14) from the macOS `M-UPGRADE-FM1` binary by resolving the big-endian Qt resource length prefix and verifying the `AC791N` marker.
* **MIDI Port Discovery (`--list`):** Scans and enumerates available MIDI inputs and outputs.
* **Experimental Flash Tooling (`--file`):** Research skeleton for protocol analysis.

### Example Commands:
```bash
# List available MIDI ports
uv run fm1-flasher --list

# Extract embedded .fwsc firmware from macOS updater app
uv run fm1-flasher --extract FM-1_014.fwsc --app M-UPGRADE-FM1.app/Contents/MacOS/M-UPGRADE-FM1

# Flashing on physical hardware (use AL-255's verified tool):
python3 tools/fm1_ota.py flash FM-1.fwsc
```

---

## 10. Firmware Disassembly & Reverse Engineering

Reverse-engineering JieLi microcontrollers (AC791N / WL82 / AC69x series) requires specialized tools due to JieLi's proprietary 32-bit RISC processor architectures (**Pi32**, **Pi32v2**, **q32s**).

### 10.1. Disassembly Tools & Ghidra Plugin

* **Ghidra Processor Module ([ghidra-jieli](https://github.com/kagaimiq/ghidra-jieli)):**
  An open-source Ghidra processor module targeting JieLi CPU architectures:
  * `pi32`: Functional disassembly support for older JieLi chips.
  * `pi32v2`: Processor definition for **AC791N (WL82 series)**. Enables Ghidra to parse function boundaries, construct control flow graphs (CFG), and trace MMIO register addresses (`JL_PORTA`, `JL_PORTB`, `JL_PORTC`).
  * `q32s`: Processor definition for BD19/BD29 series.

* **JieLi Official Toolchain (`pi32v2-elf-objdump`):**
  Provides 100% accurate instruction decoding from the vendor SDK, used in combination with Ghidra for verifying complex instruction groups.

---

## 11. External References & Resources

Useful open-source tools, documentation, and SDK repositories:

1. **[AL-255/FM-1-RE Repository](https://github.com/AL-255/FM-1-RE):**
   Reverse-engineering repository for M-VAVE FM-1 firmware. It reveals that the stock FM-1 firmware itself utilizes a Dexed/msfa-derived 6-operator FM synthesis engine, and contains V13/V14 disassembly function maps, XIP flash offset analyses, as well as an experimental custom firmware build.
2. **[ip2k/mvave-fm1-open-firmware Repository](https://github.com/ip2k/mvave-fm1-open-firmware):**
   Research project towards an open-source firmware for the M-VAVE FM-1. Includes specification, reference implementation, and simulation testbench for an **RP2040-based `USB_KEY` hardware recovery dongle** (`dongle/` directory) that forces the JieLi AC791N SoC into mask-ROM USB download mode (`UBOOT1.00`) via the external USB-C port, enabling low-level flash backup and unbricking.
3. **[ghidra-jieli Repository](https://github.com/kagaimiq/ghidra-jieli):**
   Ghidra processor extension for disassembling and decompiling JieLi `pi32`, `pi32v2`, and `q32s` CPU binaries.
4. **[jl-uboot-tool Repository](https://github.com/kagaimiq/jl-uboot-tool):**
   Utility for interacting with JieLi UBOOT bootloaders over USB Mass Storage / SCSI pass-through.
5. **[jl-misctools Repository](https://github.com/kagaimiq/jl-misctools):**
   Utilities for inspecting and converting JieLi firmware containers, key files, and UI resources.
6. **[JieLi USB Boot Key Activation (jielie docs)](https://kagaimiq.github.io/jielie/isp/usb/usb-key.html):**
   Documentation on triggering JieLi hardware USB boot loader mode via D+/D- signal patterns and ISP keys.
7. **[JieLi SoC Forum Thread (esp8266.ru)](https://esp8266.ru/forum/threads/jl-soc.5500/):**
   Community research thread discussing JieLi SoCs, SDKs, toolchains, flash recovery, and hardware boot modes.
8. **[JieLi AC79 Official Peripheral Documentation](https://doc.zh-jieli.com/AC79/zh-cn/release_v1.0.3/module_example/peripherals/sd.html):**
   Official documentation covering AC79xx series peripheral hardware modules (SD controller, GPIO, UART, SPI, I2S).
9. **[JieLi AC79 AIoT SDK (Gitee Repository)](https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK):**
   Official C SDK codebase for AC79 series (WL82 / AC791N) microcontrollers, containing board support packages (BSP), linker scripts, and hardware register headers.
10. **[M-VAVE SMK-37 PRO Reverse Engineering Gist (by probonopd)](https://gist.github.com/probonopd/18b3ed65a69d0229eb630c47d7e316dc):**
    Research notes on unpacking `.fwsc` firmware files for the M-VAVE SMK-37 PRO (DX7 FM MIDI keyboard) and identifying the underlying JieLi AC791N platform structure using `jl-misctools`.
11. **[FM-1 Online Editor](https://fm1-editor.com/):**
    Web-based configuration and patch editor for the M-VAVE FM1 synthesizer.
12. **[OpenPatch.es (Yamaha DX7 Patch Utility)](https://openpatch.es/):**
    Web utility for DX7 FM patches allowing WAV upload to recover/match patches, live auditioning, sequencing, modifying, mutating, and exporting patch sets as `.syx` files.
13. **[FM-1 Pulses by mene311](https://github.com/mene311/fm1-pulses) ([Web App](https://mene311.github.io/fm1-pulses/)):**
    Browser-based generative MIDI sequencer and pattern generator for the M-VAVE FM-1 (Web MIDI API / PWA, runs on desktop/mobile). Generates reproducible 64-step banks with parameter drift and can freeze them directly into the hardware pattern slots over SysEx (supported on Baud Girl / FM-1+VA firmware), or broadcast live MIDI notes in real time.
14. **[SLOOP FM-1 Simulator by Chance Roth](https://github.com/chancethemaker/sloop-fm1-sim) ([Web Simulator](https://chancethemaker.github.io/sloop-fm1-sim)):**
    Self-contained in-browser interactive simulator of the SLOOP / Felucca firmware for the FM-1, allowing testing controls, sound engines, and workflow directly in the browser without physical hardware.




