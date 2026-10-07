# M-VAVE FM1 & M-UPGRADE Analysis & MIDI SysEx Protocol Documentation

This document contains technical research, hardware details, and reverse-engineering results for the **M-VAVE FM1** synthesizer (powered by the **JieLi AC791N** processor) and the `M-UPGRADE-FM1.app` (macOS) utility.

---

## 1. Hardware & Device Ecosystem Overview

### 1.1. Target Device & Processor
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

### 1.2. Hardware PCB Characteristics & Recovery Vector
* **No Debug Ports / Jumpers:** The M-VAVE FM1 PCB contains **no exposed debug headers** (JTAG, SWD, or UART debug pads).
* **No Recovery Buttons:** There are **no hidden jumper pins or physical recovery buttons** on the board for forcing bootloader / DFU mode.
* **Firmware Update Vectors:**
  * **Standard User-Mode Flashing:** MIDI SysEx over USB is the official, application-level firmware update channel available on the device.
  * **Unbrick & Hardware Recovery (JieLi Mask-ROM / UBOOT mode):** The JieLi AC791N SoC boot ROM can be forced into its mask-ROM USB download mode (`UBOOT1.00`) through the external USB-C port using a dedicated **RP2040-based hardware dongle** (or vendor JieLi USB Updater). This dongle bit-bangs the hardware boot key (`0x16EF` at ~50 kHz) over USB D+/D- lines at power-up, allowing SPI flash recovery and unbricking without opening the enclosure (see [ip2k/mvave-fm1-open-firmware](https://github.com/ip2k/mvave-fm1-open-firmware)).

### 1.3. Device Disassembly & Case Opening Instructions
To open the physical enclosure of the M-VAVE FM1:
1. **Remove Bottom Screws:** Unscrew **6 self-tapping screws** from the bottom casing.
   * **Hidden Screw:** 5 screws are visible on the bottom surface; **1 screw is hidden in the center under the product sticker**.
   * **Rubber Feet:** The rubber feet do **NOT** need to be unglued or peeled off (no screws are hidden under the rubber pads).
2. **Separate Housing Latches:** After removing all 6 screws, carefully unclip the internal **plastic retaining latches/snaps** running along the bottom enclosure seam to separate the case halves.

* **Teardown & Internal PCB Photos:**
  * High-resolution disassembly photos of the PCB and internal components are available locally in the [photos/](photos/) directory.
  * Teardown photo discussion and community analysis can also be viewed on [Reddit r/synthdiy](https://www.reddit.com/r/synthdiy/comments/1vgotwe/comment/p3gk1ko/).

---

## 2. Core Technical Findings

### 2.1. Does the firmware update occur over MIDI?
**Yes, the firmware update occurs entirely over the MIDI SysEx protocol.**

The application does not use dedicated USB DFU/CDC emulation or direct low-level raw flash access during standard operation. The entire process (from handshake to streaming every byte of firmware and preset data) is executed via **USB MIDI SysEx messages** using the **RtMidi** library on top of macOS **CoreMIDI**.

### 2.2. Where is the firmware file stored?
**The firmware binary is embedded directly inside the native executable file.**

There are no external `.bin` or `.hex` files in the resources directory. Inside the executable file [M-UPGRADE-FM1](M-UPGRADE-FM1.app/Contents/MacOS/M-UPGRADE-FM1), the firmware image is embedded:
* **Internal Resource Name:** `usb_hid_ota.bin` (offset `0xEEDDC`).
* **Container Format:** Signatures `@JMUA` (offset `0xF3BB8`) and `JLUFW` (offset `0xF3CDC`).

### 2.3. Is Signature Verification implemented?
**Asymmetric cryptographic signature verification (RSA/ECDSA/AES) is NOT implemented.**

Security checks include:
1. **Container Header & Signature Validation:** Verification of `@JMUA` / `JLUFW` signatures, target device type, and version strings.
2. **Size Boundaries Validation:** `Embedded firmware too small: %1 bytes (min %2)`.
3. **Checksums (CRC/Byte Checksums):** Every block transmitted via SysEx is accompanied by a byte checksum.

---

## 3. M-UPGRADE-FM1 Application Architecture

* **UI Framework:** Qt6 (`MainView`, `SelectFile`, `LoadingWidget`).
* **MIDI Stack:** RtMidi (`RtMidiIn`, `RtMidiOut`, `MidiInCore`, `MidiOutCore`).
* **OTA Update Worker Modules:**
  * `OtaUpgradeWorker`: Background worker managing the two-step firmware flashing process.
  * `PresetUpdateWorker`: Background worker handling preset bank uploads.
  * `OtaFormat`: Utility class responsible for packing (`pack`), parsing (`parse`, `tryParse`), and building metadata frames (`buildMetaSequence`).

---

## 4. MIDI SysEx Commands & Interaction Scenarios

### 4.1. Handshake & Device Detection Trace
* **Purpose:** Query connected devices for FM1 identity and status.
* **Captured MIDI Log Trace:**

```text
To USB Composite Device    SysEx 10 bytes:  F0 00 32 45 00 00 00 40 7F F7
From USB Composite Device  SysEx 41 bytes:  F0 00 32 45 58 01 00 00 23 4D 5A 44 XX XX XX XX XX 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 40 06 F7
```

> **Parameter Query Fuzzing Note:**  
> Exhaustive read scanning across all Parameter IDs (`0x00` through `0x7F` with command `0x7F`) confirmed that the M-VAVE FM1 synthesizer responds **exclusively to Parameter ID `0x40` (64)**. Queries sent to all other Parameter IDs produce no response.

* **Detailed Trace Breakdown:**

  * **Outgoing Request Frame (`10 bytes`):**
    * `F0`: SysEx Start.
    * `00 32 45`: Manufacturer Header Prefix (`_s_arrSysexHead`).
    * `00`: Channel / Device Broadcast ID (`0x00`).
    * `00 00 00`: Parameter Address (`0x000000`).
    * `40`: Parameter / Status Item (`0x40` = 64).
    * `7F`: Command Value (`0x7F` = 127 = Get Value / Status Query).
    * `F7`: SysEx End.

  * **Incoming Response Frame (`41 bytes`):**
    * `F0 00 32 45`: Header Prefix.
    * `58`: Reply Command Type (`0x58` ACK / Parameter Response).
    * `01`: Device Subtype / Protocol Version.
    * `00 00`: Echo Address (`0x0000`).
    * `23 4D 5A 44 XX ...`: Serial Number & Device ID payload (contains ASCII bytes `4D 5A 44` -> `MZD` prefix; serial masked for privacy).
    * `40`: Echo Parameter ID (`0x40`).
    * `06`: Response Status / Checksum byte.
    * `F7`: SysEx End.

### 4.2. Step 1: Verification & Pre-check
* **Purpose:** Transmit firmware metadata (version, length, checksum).
* **App Log:** `Sending upgrade mode command (first step - verification)`
* **Flow:** `OtaFormat::buildMetaSequence` constructs the metadata frame. The synthesizer verifies the metadata and enters bootloader/OTA mode.

### 4.3. Step 2: Start Upgrade Mode
* **Purpose:** Trigger memory erase and Flash overwrite sequence on the microcontroller.
* **App Log:** `Sending upgrade mode command (second step - upgrade)`
* **Flow:** Upon ACK from device, launches the data chunk streaming thread.

### 4.4. OTA Data Chunk Streaming
* **Purpose:** Stream binary firmware payload to Flash memory.
* **Flow:** Slices binary data into chunks. Each chunk is packaged via `OtaFormat::pack` using 8-bit to 7-bit MIDI encoding (`u8ToMidi`).
* **Delivery Control:** After sending each chunk, checks device status (`Failed to get lower device request` on timeout).

### 4.5. Preset Update
* **Purpose:** Upload user patch banks to RAM / non-volatile memory.
* **Logic:** Executed in "hot" mode without rebooting the synthesizer via `PresetUpdateWorker`.
* **App Log:** `Starting preset update, size=%1 bytes, device=%2`

---

## 5. OtaFormat SysEx Frame Layout

Every SysEx message follows this layout:

```
[F0] [Manufacturer ID / Head] [Cmd Type] [Seq ID / Address] [Payload Data] [CRC / Checksum] [F7]
```

* **`F0`**: Start of SysEx frame.
* **`Header`**: Prefix ID (`_s_arrSysexHead`), specifying manufacturer and device model IDs (`00 32 45`).
* **`Cmd Type`**:
  * `0x01` — Handshake & Metadata Verification.
  * `0x02` — Start Upgrade Mode.
  * `0x03` — OTA Firmware Data Chunk.
  * `0x04` — Preset Bank Data.
  * `0x58` — Device Response / Status ACK.
* **`Payload Data`**: 7-bit encoded MIDI bytes (MSB packing).
* **`F7`**: End of SysEx frame.

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

## 9. Python Flashing Utility (`fm1_flasher.py`)

A standalone CLI tool [fm1_flasher.py](fm1_flasher.py) implements this protocol. Project environment is managed via [`uv`](https://github.com/astral-sh/uv) (configured in [`pyproject.toml`](pyproject.toml)).

> [!WARNING]
> **UNTESTED UTILITY DISCLAIMER:**  
> The Python flasher script ([fm1_flasher.py](fm1_flasher.py)) was developed strictly by reverse-engineering the native `M-UPGRADE-FM1.app` macOS application binary. **This script HAS NOT been tested on physical M-VAVE FM1 hardware.** Use with caution and at your own risk.

### Features:
* **Automatic Firmware Extraction:** Extracts embedded firmware from `M-UPGRADE-FM1.app` at offset `0xF3BB8` if no input file is supplied.
* **Custom Firmware Flashing:** Accepts custom `.bin` / `.ufw` binaries via `--file`.
* **Preset Uploading:** Uploads patch banks via `--preset`.

### Example Commands:
```bash
# List available MIDI ports
uv run fm1-flasher --list

# Flash using embedded firmware
uv run fm1-flasher

# Flash custom firmware file
uv run fm1-flasher --file my_firmware.ufw
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

## 11. Custom & Alternative Firmwares

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

> [!TIP]
> **Community Flashing Experience & Safe Upgrade Practice:**  
> While not an absolute hard rule, there is a prominent community recommendation to avoid flashing one custom firmware directly over another. To minimize bricking risks, some users suggest rolling back to the official stock firmware (v15) via M-VAVE's official updater first, and only then flashing the next custom firmware build.

---

## 12. External References & Resources

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



