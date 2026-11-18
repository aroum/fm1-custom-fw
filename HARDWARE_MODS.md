# M-VAVE FM-1 Hardware Mods, Add-ons & DIY Enhancements

Community hardware modifications, 3D-printable enclosures, ergonomic upgrades, and electrical expansions for the **M-VAVE FM-1** synthesizer.

---

## Hardware Modifications & Add-ons

1. **[FM-1 Bonus Box by pfkellogg](https://github.com/pfkellogg/fm1-bonus-box):**
   ESP32-S3 external companion module featuring a rotary preset browser with round color TFT, sustain pedal input, Wi-Fi bank manager, USB-MIDI host, and a sing-on-pitch voice trainer.

2. **[fm1-sustain-footswitch by pfkellogg](https://github.com/pfkellogg/fm1-sustain-footswitch):**
   Arduino-based adapter converting a standard 1/4" sustain pedal into MIDI CC64 over the FM-1's 3.5 mm TRS MIDI input (includes full schematics).

3. **[fm1-midi-voice-tuner by pfkellogg](https://github.com/pfkellogg/fm1-midi-voice-tuner):**
   Passive TRS MIDI splitter box with built-in microphone and OLED pitch display guiding singers on whether they match the FM-1's current note.

4. **[fm1-cartridge by Andre Rezemini (andrerezemini)](https://github.com/andrerezemini/fm1-cartridge) ([Reddit Build Thread](https://www.reddit.com/r/MVaveFM1/comments/1xdl20u/i_built_an_esp32s3_cartridge_for_the_mvave_fm1/)):**
   * **License:** Open Source.
   * **Concept:** Custom DIY hardware expansion cartridge built on an ESP32-S3 microcontroller, interfacing with the FM-1 to enable portable cartridge swapping and fast flash deployment of Clipper, Melodee, and Felucca firmwares in the field.

5. **[fm1buddy by konsumer](https://github.com/konsumer/fm1buddy) ([Web Installer](https://konsumer.js.org/fm1buddy/)):**
   * **License:** Open Source.
   * **Concept:** Multi-hardware companion firmware runner for M5Stack Cardputer, LilyGO T-Deck, and standard ESP32-S3 / RP2040 microcontrollers.
   * **Features:** Acts as a standalone hardware bridge between the FM-1 and external controllers over USB Host, offering hardware MIDI patch selection, live sequence transport, voice editing, and chord transposition.

6. **[FM-1 MIDI Breakout Box by zack-attack](https://github.com/zack-attack/fm1-midi-box):**
   * **Concept:** Active DIN-5 to 3.5 mm TRS Type-A MIDI breakout and power injection hub.
   * **Features:** Optoisolated 5-pin DIN MIDI IN/OUT/THRU, built-in USB-C power filtering (reduces ground loop audio hum during concurrent USB charging), and an optional rechargeable 18650 Li-Ion battery sled.

7. **[FM-1 Hardware DIN MIDI Out Mod (by ehn96)](https://github.com/ehn96/dinghy/releases/tag/v0.3.0):**
   Hardware mod to add a real 3.3V DIN-5 MIDI Out port to the FM-1 hardware, verified with Dinghy v0.3.0 (which outputs hardware MIDI out on pin 39, recommends 74LVC1G07 buffer) and discussed on [Reddit r/MVaveFM1](https://www.reddit.com/r/MVaveFM1/comments/1xltvxw/of_course_i_made_a_firmware/).

8. **[TNFM (Teensy 4.1 + FM-1 Hardware Mod) by FloatingSignifiers](https://www.reddit.com/r/synthdiy/comments/1xo5zou/progress_update_on_the_tnfm_teensy41fm1_mod/):**
   * **Concept:** Ambitious hardware coprocessor / processor replacement mod physically embedding a high-speed **PJRC Teensy 4.1** (ARM Cortex-M7 @ 600 MHz) directly inside the M-VAVE FM-1 enclosure.
   * **Modifications & Architecture:**
     * Tracing and cutting PCB traces around output filter caps (C98, C99, C100, C102) to disconnect the internal DAC from the stock AC7911B processor and route audio generation to the Teensy.
     * Tapping internal 3.7V battery power via the switched battery rail directly to the Teensy `VIN` (with `VIN–VUSB` trace cut for safe simultaneous USB programming).
     * Wiring the FM-1 panel controls, encoders, keys, and display to the Teensy to build a DAWless pocket tracker / Yamaha QY70-style sequencing groovebox on top of Teensy Audio Library / custom DSP.

9. **[Custom Knob Caps & Encoder Toppers (3D Prints & Replacements)](https://www.reddit.com/r/MVaveFM1/comments/1xysqec/some_more_knobcaps/):**
   * **Problem:** Stock FM-1 potentiometer shafts are small, bare knurled metal posts that feel cramped and difficult to turn precisely in live performance.
   * **Hardware Specs:** Standard 6 mm 18-tooth knurled shaft (`WH148 AG3` type; do not use D-shaft).
   * **Dimensions & Solutions:** Tight clearances require outer diameter caps between 8.5 mm and 10 mm for edge knobs, and up to 11–13 mm for center controls. Community members share 3D printable STL models (Printables) and recommend compact aluminum/plastic slip-on toppers (AliExpress, Thonk) requiring no soldering.

---

*Related documents: [README.md](README.md) (Custom Firmwares Catalog) | [REVERSE_ENGINEERING.md](REVERSE_ENGINEERING.md) (Hardware & OTA Protocol Reference) | [OFFICIAL_FIRMWARE.md](OFFICIAL_FIRMWARE.md) (Stock Firmware Reference).*
