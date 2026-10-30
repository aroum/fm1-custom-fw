# M-VAVE FM1 Resource Hub, Custom Firmwares & MIDI SysEx Protocol Documentation

A curated directory and reference hub for the **M-VAVE FM1** synthesizer (powered by the **JieLi AC791N** processor) — gathering community custom firmwares, documentation, tools, MIDI SysEx protocol details, and the `M-UPGRADE-FM1.app` (macOS) updater.

> [!NOTE]
> **Device Compatibility Notice & SMK-37 Resources:**  
> This repository strictly curates custom firmwares and tools specifically targeted at the **M-VAVE FM-1** synthesizer.  
> Resources and ports for the **M-VAVE SMK-37 / SMK-37 Pro** keyboard controller:
>
> * **[M-VAVE SMK-37 Custom Firmware Hub](https://genkigenki.github.io/smk37/):** Directory and browser-based installer for SMK-37 firmwares and FM-1 ports.
> * **[fm1-to-smk37 Port Kit by genkigenki](https://github.com/genkigenki/fm1-to-smk37):** Board port patches and documentation for adapting FM-1 firmwares to SMK-37 hardware.

> [!IMPORTANT]
> **Official Stock Firmware & Open Source SDK (M-VAVE):**  
> * **Latest Stock Firmware:** **[FM-1.fwsc (Version V16, 2026-10-21)](https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/firmware/FM-1.fwsc)** (718 KB, SHA-256 verified) — major official release introducing an **8-part multitimbral engine** (MIDI channels 1–8), expanded **20-voice shared polyphony**, an upgraded **64-step sequencer & live arrangement matrix** (8 tracks × 8 columns), an upgraded **true-stereo global FX chain** (Filter, Reverb, Delay, Distortion, Chorus, Phaser), independent per-voice tuning ($\pm 100$ cents) / pan / glide, customizable TFT display RGB color themes, and DX7 standard `.syx` bank import/export.
> * **Previous Official Releases:** V15 (2026-07-30, detune/reverb fixes), V14 (initial factory release).
> * **Official Open Source Repository:** **[m-vave/fm1_open](https://github.com/m-vave/fm1_open)** (GPL-3.0, 8 tracks, 8 sample slots, 16 demo FX, hardware C drivers, and WebAssembly simulator).
> * **Online Web Workbench:** **[open.m-vave.com/fm1-workbench](https://open.m-vave.com/fm1-workbench)** — provides in-browser WebAssembly simulation, testing, and direct USB firmware flashing.
> * **Announcement & Discussion:** **[M-VAVE Official Forum Topic #4](https://forum.m-vave.com/topic/4)**.

---

## 1. Custom & Alternative Firmwares

Community-developed custom firmwares, mods, and experimental firmware projects for the M-VAVE FM-1, clearly divided into sound/groovebox instruments, modular builders, games and non-audio ports, and stock binary patchers:

### 1.1. Sound, Synthesizer & Groovebox Firmwares (Music & Audio)

Community musical firmwares organized by architectural family and lineage — the **Felucca** multi-engine platform, the **SLOOP** live groovebox ecosystem, the **FoMni** chord harp branch, and standalone independent engines:

#### 1.1.1. Felucca Ecosystem (Multi-Engine Platform & Direct Forks)

Firmwares built upon or directly forked from the foundational open-source multi-engine **Felucca** synthesizer core by Hügelton Instruments:

1. **[Felucca by hugelton](https://github.com/hugelton/Felucca) ([Web Installer](https://hugelton.github.io/Felucca/) | [Web Editor](https://hugelton.github.io/Felucca/webapp/editor/) | [Build Guide](https://github.com/hugelton/Felucca/blob/main/BUILDING.md)):**

* **License:** Open Source (GPL-3.0-only).
* **Polyphony & Voice Budget:** Up to 14 voices total — 8 dynamically shared synth voices across tracks 1–3 (`NVOICE 8` pool) plus 6 dedicated percussion voices on track 4 (`NDRUM 6`). Per-engine maximum voice caps: FM6 (up to 6 voices), PHYS (3 voices, SYMP 2 voices), GRAIN (3 voices), and VOICE (formant, 4 voices).
* **Synthesizer Engines:** 9 distinct sound engines including **ANALOG** (virtual analog, 2 osc, PWM, resonant LPF), **DIGITAL** (4-op FM, 8 algorithms, feedback), **PHASE** (phase distortion), **LOFI** (chiptune, 4-bit wave RAM), **SAMPLE** (multisampled instruments + user slots), **VOICE** (formant/vocal osc), **TRIO** (3 osc with ring mod/sync), **WHEEL** (tonewheel organ with drawbars & rotary speaker), and **GRAIN** (granular textures).
* **Architecture & Features:** 4 tracks (3 synth parts + 1 GM drum track), 64-step sequencer per track with chords/ties/slides and live loop recording, per-track SLICER (16-step tempo-synced gate/stutter), effects (distortion, chorus, delay, reverb sends, master limiter), scales & white-key quantization, and web editor.
* **Documentation:** [Felucca BUILDING.md Guide](https://github.com/hugelton/Felucca/blob/main/BUILDING.md) — complete build guide for compiling Felucca-family firmwares from source using the JieLi `pi32v2` toolchain.
* **Video Guides & Demos:** [Complete Guide (v0.9)](https://www.youtube.com/watch?v=UzgbDjsFEpY) | [Engine Tour & Sequencing](https://www.youtube.com/watch?v=EzFknmhtKZk) | [Live Performance Jam](https://www.youtube.com/watch?v=XEK4VhsYwCE).

2. **[Felucca [Salt] by Chance Roth (ChanceTheMaker)](https://github.com/ChanceTheMaker/Felucca) ([Web Installer](https://chancethemaker.github.io/Felucca/webapp/installer/) | [Web Studio](https://chancethemaker.github.io/Felucca/webapp/editor/)):**
    * **License:** Open Source (GPL-3.0-only). Enhanced fork of Felucca by Leo Kuroshita (Hügelton Instruments).
    * **Polyphony:** 8 dynamically shared synth voices across 3 tracks plus 6 dedicated drum voices (up to 14 voices total).
    * **Concept:** Multi-engine synthesizer firmware with hardware-inspired browser Studio, hardware TRS MIDI expansion, rich display palettes, and standalone in-browser sound generation.
    * **Features:**
      * **Studio & In-Browser Synthesizer:** Browser Studio can act as an online synthesizer without physical hardware (nine engines, 54 presets, live oscilloscope waveform, 12 hardware themes like Stage Red, Matrix, Vintage DX, Model D, Vaporwave, and on-screen keyboard).
      * **Hardware TRS MIDI Input:** Full expression handling on 3.5 mm TRS MIDI IN alongside USB (sustain pedal, pitch bend, mod-wheel vibrato, MIDI panic/reset).
      * **Flexible Clock Sources:** Internal, USB, or TRS clock sync and MIDI Start/Stop/Continue.
      * **Display Themes & Typography:** 20 on-device screen palettes (including 8 light palettes and light/dark high contrast modes), selectable Terminus Regular/Bold typography.
      * **Preset Management:** Persistent favorite stars, All/Favorites browsing filtering, and live MIDI event/chord monitor.

3. **[Melodee by keremimo](https://github.com/keremimo/melodee) ([Web Installer](https://keremimo.github.io/melodee/) | [Web Editor](https://keremimo.github.io/melodee/webapp/editor/)):**

* **License:** Open Source (GPL-3.0-only). Modified build based on Felucca.
* **Polyphony:** Per-engine voice limits: 16 voices for Casio CZ-1, 8 voices for Prophet-5, 8 voices for DX-7 / FM-6, and faithful hardware-accurate voice count for SID chip emulation (3 voices per chip), plus rhythm accompaniment.
* **Features:**
  * **Prophet-5 Engine:** Native **Sequential Prophet-5 Rev 4** engine replacing ANALOG — two oscillators with hard sync, Poly-Mod, LFO/noise wheel modulation, selectable SSI (Rev 1/2) and Curtis (Rev 3) 4-pole low-pass filters, separate filter/amp envelopes, Vintage knob, glide, unison, and 5 voices per track. Includes **all 200 programs** of Sequential's v1.03 factory bank (128 native user slots P001–P128), 16 device parameter pages, and `.syx` program/bank import and export in the web editor.
  * **Casio CZ-1 Phase Distortion:** Authentic CZ-1 engine with 64 original CZ-1 factory preset tones, 8 CZ device banks with `.syx` import/export, and 38 dedicated editing pages.
  * **FM6 & Microtonal Scales:** 64 DX7/FM6 slots with direct SysEx bank dump support, 70 microtonal tunings across equal divisions, just intonation, historical temperaments, and maqam models.
  * **Advanced Sequencing:** Single unified note editor (`SEQ > NOTES`), reversible timing quantization (`QNT`), and 1,024 recorded notes across 32 pattern banks.

4. **[ChoralRoot FM-1 by Quixotic7](https://github.com/Quixotic7/ChoralRootFM1) ([Web Installer](https://quixotic7.github.io/ChoralRootFM1/) | [Web Emulator](https://quixotic7.github.io/ChoralRootFM1/emu/)):**

* **License:** Open Source (GPL-3.0). Based on Felucca (engines/platform) and ChoralRoot (Monome grid chord engine).
* **Polyphony:** Dynamic multi-voice chord voicing engine + separate dedicated performance bass layer leveraging dual-core rendering.
* **Concept:** Telepathic Orchid / Monome-style chord performance instrument.
* **Features:** Two-handed chord shaping (one hand selects roots, the other shapes voicings), custom key modes, performance bass line, built-in looper, full color UI, and browser sound emulator.
* **Community Remix / Mod:** [Choralroot-remix on r/MVaveFM1](https://www.reddit.com/r/MVaveFM1/comments/1x3qrqx/choralrootremix/) by Creative_One919 — extended remix incorporating Melodee's 6-voice Prophet-5 engine with 200 factory presets, DUELL-inspired Morph engine, dedicated BASS engine with multi-core rendering, "Rosen" random preset cycling, "Swag voicing" mode, synced BPM gate, and sidechain volume.

5. **[X0X by Charles Vestal](https://github.com/charlesvestal/fm1-x0x) ([Web Installer](https://charlesvestal.github.io/fm1-x0x/install/) | [Web Emulator](https://charlesvestal.github.io/fm1-x0x/emu/) | [Manual](https://charlesvestal.github.io/fm1-x0x/manual/)):**
    * **License:** Open Source (GPL-3.0). Based on Felucca.
    * **Polyphony & Engines:** Two monophonic TB-303 synthesizers (303A & 303B), 11-voice TR-909 drum machine, 11-voice TR-808 drum machine, and 1 breakbeat slice player running simultaneously.
    * **Concept:** Propellerhead ReBirth-inspired techno/acid groovebox machine.
    * **Features:** TR-909, TR-808, two TB-303 synths with an integrated acid line generator, and a breakbeat player all playing simultaneously; includes automation, shared reverb and tape delay sends, and a master compressor.

6. **[GHOULBOX 2.0 by Jason Persinger](https://github.com/jasonpersinger/ghoulbox-fm1-dungeon-synth) ([Website & Browser Emulator](https://ghoulbox.messy.quest) | [Web Installer](https://ghoulbox.messy.quest/webapp/installer/)):**
    * **License:** Open Source (GPL-3.0). Based on Felucca.
    * **Polyphony:** 12 voices of polyphony (expanded from 8) with dedicated drone latching.
    * **Concept:** Dungeon synth, dark ambient, and fantasy music groovebox firmware.
    * **Features:** Cathedral-sized HALL reverb, worn-cassette TAPE / CRKL stage, dedicated hurdy-gurdy engine (GURDY with crank clicks and buzzing trompette), drone latching, historical/just temperaments, and 36+ dungeon sounds (crypt pads, monk choirs, lutes, organs) with an old-school RPG UI and skull boot screen.
    * **Interactive Browser Version:** Complete in-browser emulation playable on an interactive virtual FM-1 via keyboard or mouse at [ghoulbox.messy.quest](https://ghoulbox.messy.quest) without flashing hardware first.

7. **[Jangada by zednaked](https://github.com/zednaked/jangada) ([Web Installer](https://zednaked.github.io/jangada/) | [Web Studio](https://zednaked.github.io/jangada/webapp/studio/)):**
    * **License:** Open Source (GPL-3.0). Based on Felucca.
    * **Polyphony:** 8 shared voices across 4 tracks with `TENS` voice detune spreading (±12 cents) and drone holding.
    * **Concept:** Dark, industrial, Brazilian-accented groovebox firmware.
    * **Features:** 10 sound engines (including 6-op FM and superwave analog), 4 tracks, modulation matrix, ratchets, drone holding/evolving modes, and dedicated custom drum kits.

8. **[REDACTED by DJ Redacted](https://fm1-redacted-installer.xrhetor.chatgpt.site/):**
    * **License:** Open Source (GPL-3.0). Built on Felucca by Hügelton Instruments.
    * **Polyphony:** 4-track layered groovebox architecture with dynamic voice allocation.
    * **Concept:** Experimental dark, fractured lo-fi four-track groovebox firmware (`PULSE` · `VOLTAGE` · `STATIC` · `GHOST`).
    * **Features:**
      * **Four Track Engines:** Four distinct sound layers chosen via `ALGORITHM`.
      * **Real-Time Track Shapers:** Four top knobs mapped to dynamic performance parameters: `FRACTURE`, `STATIC`, `CHANCE`, and `MUTATE`.
      * **Startup Artwork:** Custom broken vinyl record splash screen.

9. **[Hortator by DEADACTIVE](https://github.com/DeadActive/hortator) ([Web Emulator & Player](https://deadactive.github.io/hortator/)):**
    * **License:** Open Source (GPL-3.0). Built on Felucca.
    * **Polyphony:** 8 dedicated percussion tracks running simultaneous drum synthesis (Plaits, 808/909, 2-op FM, physical membrane models).
    * **Concept:** 8-track drum machine firmware.
    * **Features:** TR-808, TR-909 and Mutable Instruments Plaits drum models, user samples, Mutable Instruments Grids generative rhythm algorithm, pumping master compressor, and acoustic resonators.

10. **[April OS by beashoko](https://github.com/beashoko/april-os) ([Web Installer](https://beashoko.github.io/april-os/)):**
    * **License:** Open Source (MIT). Based on Felucca.
    * **Polyphony:** 8 tracks of sample playback and live sequencing.
    * **Concept:** Dedicated sampling-focused groovebox firmware.
    * **Features:** 32 sample slots (up to 3 seconds each), 8-track sequencer, built-in sample slice and loop editor, direct audio recording using a connected smartphone or computer microphone.

11. **[WaveLoop FM-1 by ELI7VH](https://github.com/ELI7VH/Felucca) ([Web Installer](https://eli7vh.github.io/Felucca/)):**
    * **License:** Open Source (GPL-3.0). Based on Felucca.
    * **Polyphony:** 8 shared synth voices across 3 tracks plus dedicated drum track (Felucca core).
    * **Concept:** Performance firmware specifically mapped for external control via Arturia MiniLab 3.
    * **Features:** Dedicated track fader mappings, follow-the-track encoder integration, DJ filter mode, and momentary punch-in FX pad triggers.

12. **[Rainbow mode by joshbartlettband-web](https://github.com/joshbartlettband-web/felucca-rainbow) ([Web Installer & Emulator](https://joshbartlettband-web.github.io/felucca-rainbow/)):**
    * **License:** Open Source (GPL-3.0). Based on Felucca.
    * **Polyphony:** 8 shared voices across tracks + drum voice layer.
    * **Concept:** Children's musical exploration instrument with rainbow color-coded keys, 40 animal sound effects and rhythms, safe volume limiter, and access to the complete Felucca engine via secret key combination.

13. **[fm1-chord by math0ne](https://github.com/math0ne/fm1-chord):**
    * **License:** Open Source (GPL-3.0). Built on Felucca.
    * **Polyphony:** Multi-voice polyphonic chord generator and arpeggiator engine.
    * **Concept:** Chord composition tool, chord sequencer, rhythm accompanist, and ear-training aid.

14. **[DUELL by balinthcom](https://github.com/oscillr/DUELL) ([Web Emulator](https://oscillr.github.io/DUELL/emu/)):**
    * **License:** Open Source (GPL-3.0). Built on Felucca by Hügelton Instruments.
    * **Polyphony:** Bi-timbral 2-part synthesizer (Part 1 and Part 2) with independent per-part polyphony, unison stereo detune stack, and LAYER/SPLIT/STEREO routing.
    * **Concept:** Multi-morphing bi-timbral synthesizer firmware for the FM-1: two full simultaneous sound parts, each with its own synthesis engine, patches, effects, EQ, and arpeggiator.
    * **Features:**
      * **Bi-Timbral Modes:** LAYER, SPLIT (keyboard zone), and STEREO (dual mono, part 1 hard-left and part 2 hard-right with isolated audio engines).
      * **Patch Morphing:** Smooth glide between two states of any patch with SMART randomization and per-patch morph amount.
      * **Per-Part Engine Architecture:** Independent arpeggiators, secondary envelopes and LFOs, 8-slot modulation matrix, dedicated EQ, sidechain ducking triggered via MIDI, and ping-pong delay.
      * **Factory Sound Bank:** ~100 sounds across 12 synthesis engines, 16 multi-setups, and 16 patterns.
      * **MIDI Implementation:** Discrete MIDI channel per part, program change, bank select, and clock sync.
    * **Status:** Available to play via in-browser WebAssembly emulator; hardware flashing in ongoing development.

15. **[MAKU (幕間機) by okumurari2](https://github.com/okumurari2/maku) ([Web Emulator](https://okumurari2.github.io/maku/) | [Releases](https://github.com/okumurari2/maku/releases)):**
    * **License:** Open Source (GPL-3.0-only). Built on Felucca by Hügelton Instruments.
    * **Polyphony:** 4 simultaneous voice layers (Pulse kick, Floor drone, Haze shimmer, Voice arpeggiated phrase).
    * **Concept:** Always-on generative ambient machine firmware designed for DJ intermissions and generative soundscapes: power on and an evolving, random, in-key sonic world is immediately playing.
    * **Features:**
      * **Four Continuous Parts:** Pulse (kick/rhythm, DRUM engine), Floor (drone, PHYS physical modeling), Haze (shimmer/textures, GRAIN granular engine), and Voice (arpeggiated melodic phrase, PHYS engine).
      * **Dynamic Generative Evolution:** Every boot generates a unique scale, tempo (70–90 BPM), sounds, and macro states. Holding HOME regenerates a new world.
      * **Taste Memory ("Likes"):** Tapping REC saves preferred worlds (up to 16). Future generated worlds increasingly draw inspiration and mutate from saved favorites.
      * **Verb-Based Interface:** Action buttons perform timed organic changes — FX (sinks depth), SCL (cascades higher intervals), ENV (swells chords), LFO (wobbles filter/pitch), EDIT (lifts brightness/sharpness), GLO (scrambles phrases), and PLAY (toggles DRIFT value wandering).

16. **[Polly by Charles Vestal](https://github.com/charlesvestal/fm1-polly) ([Web Installer & Emulator](https://charlesvestal.github.io/fm1-polly/)):**
    * **License:** Open Source (GPL-3.0). Built on Felucca by Leo Kuroshita / Hügelton Instruments.
    * **Polyphony:** Dynamic multi-voice polyphony driven by the Sonivox EAS General MIDI sound engine across 8 accompaniment and melody tracks.
    * **Concept:** Yamaha QY70-inspired 8-track pocket accompaniment arranger and auto-accompaniment workstation for the FM-1.
    * **Features:**
      * **8-Track Arranger Architecture:** Dedicated parts for Drums, Percussion, Bass, and 5 Chord accompaniment tracks powered by the Sonivox EAS General MIDI sound engine.
      * **Interactive Chord Recognition & Follower:** Play chord shapes on the keyboard (or via MIDI IN) to drive realistic live auto-accompaniment transformations.
      * **Style Engine & QY70 Import:** Built-in accompaniment styles with variation switching, fill-ins, intro/outro, and direct import compatibility for Yamaha QY-format style patterns.
      * **In-Browser WebAssembly Simulator:** Full hardware simulation with screen rendering and audio playback running directly in the browser at [charlesvestal.github.io/fm1-polly](https://charlesvestal.github.io/fm1-polly/).

17. **[TRIBE (fm1-tribe) by Alexandre Piel (apiel)](https://github.com/apiel/fm1-tribe) ([Site & Web Installer](https://apiel.github.io/fm1-tribe/)):**
    * **License:** Open Source (GPL-3.0-only). Fork of X0X (Charles Vestal) and built on Felucca (Leo Kuroshita / Hügelton Instruments) with kicks and scatter effects from zicBox.
    * **Polyphony:** 10 simultaneous polyphonic and percussion tracks across 25 assignable engines (dual kicks, 909/808 drums, 303 bass).
    * **Concept:** Ten-track groovebox firmware where any synthesis or drum engine plays on any track.
    * **Features:**
      * **10 Tracks & 25 Engines:** Freely assignable tracks running two dedicated kick models (`KICK W`, `KICK P`), Roland TR-909 and TR-808 drum voice models (9W9 / 8W8 ports), and TB-303 bassline synthesis (schwung-303 port).
      * **16 Clips per Track:** Launch clips at pattern boundaries or instantly; supports 16, 32, or 64 steps, 6 playback clock rates, 4 playback directions, and shuffle/swing.
      * **Live Performance Scatter FX:** Momentary performance effects triggered directly from keys while playing (beat loops, reverse, rhythmic gating, bitcrush, distortion, ring modulation, and resonant filters).
      * **Dual Master FX & Compressor:** Reverb, delay, drive, distortion, fuzz, wavefolder, bitcrusher, decimator, or ring modulator fed by per-track sends, plus an always-on master compressor.
      * **In-Browser Emulator:** Real firmware compiled to WebAssembly running directly in the browser at [apiel.github.io/fm1-tribe](https://apiel.github.io/fm1-tribe/#emulator).

18. **[Golana by Gadlele](https://github.com/Gadlele/Golana) ([Website & Web Installer](https://gadlele.github.io/Golana/) | [Releases](https://github.com/Gadlele/Golana/releases)):**
    * **License:** Open Source (GPL-3.0). Built on Felucca by Leo Kuroshita / Hügelton Instruments.
    * **Polyphony:** 4-voice polyphonic / unison / mono / legato engine.
    * **Concept:** Korg microKORG-inspired analog-modeling synthesizer firmware for the FM-1 featuring the classic MATRIX editing workflow.
    * **Features:**
      * **MicroKORG Synth Architecture:** 4-voice polyphonic / unison / mono / legato engine with 2 oscillators per voice (saw, pulse with PWM, tri with wavefold, sine with cross-mod from OSC 2, noise, and ring modulation), dual LFOs, and 4 assignable virtual modulation patch routings.
      * **Resonant Multi-Mode Filter:** 24 dB/oct LPF, 12 dB/oct LPF, BPF, HPF, and an aggressive screaming MS-20-style resonant low-pass filter model.
      * **Matrix Interface & Waveform Drawing:** On-device 240 × 240 graphics rendering real-time waveforms for OSC 1/2, dynamic filter response curves, envelope graphs, and live LFO waveforms calculated directly from parameter values.
      * **FX Chain & 16-Step Sequencer:** Integrated arpeggiator, 16-step sequencer with ties/slides per program, modulation FX (chorus, flanger, ensemble, phaser, metal distortion), tempo-synced delay, and reverb with flexible FX routing orders.

19. **[FANTASMA / Pelucco by Gadlele](https://github.com/Gadlele/Pelucco) ([Web Emulator / Artifact](https://claude.ai/artifact/RLDaXqXDuzzfyJZ8ibS5Gk)):**
    * **License:** Open Source (GPL-3.0). Built on Felucca by Leo Kuroshita / Hügelton Instruments.
    * **Polyphony:** 12-voice polyphony (8 melodic/chops voices + 4 drum/ambient voices) across 4 dedicated roles.
    * **Concept:** Generative ambient and drone synthesizer firmware for the FM-1 with dedicated chord-strum and generative "haunted" modes.
    * **Features:**
      * **"Haunted" Generative Ambient Engine:** Pressing `OCT+` on the fourth SEQ page triggers self-generating, evolving ambient music across three independent channels across randomized musical scales (major, minor, dorian, mixolydian, pentatonic, phrygian, lydian) even with the transport stopped; `OCT-` halts the generator.
      * **BELL Generative Loops:** 4 drifting loops of 13/17/23/29 steps (`DENS`, `EVOLVE`, `RANGE`, `SEED`) snapped to the scale on the BELL engine.
      * **Dedicated Ambient Role Split:** 4 channels configured for ambient roles: Pads (automatic chord generator), Lead (key-locked for live manual jamming over drones), FM Bells (generative chime echoes), and Continuous Noise (sea/wind textures).
      * **OMNI Strum Mode:** Omnichord-style performance mode where black keys trigger chords following the active root scale while white keys act as a harp strum plate.
      * **USB Rescue Boot:** Built-in safe recovery mode (`OCT-` held on power-on or two crash loops in a row) launching a minimal updater screen reporting as `FM-1_000` to guarantee web flashing and recover without bricking.
      * **Custom Ambient UI & Reverb:** Expansive long-decay `AMBI` reverb engine, custom ghost splash screen, and high-visibility neon "ECTO" color theme.

20. **[Skiff by illuminus5](https://github.com/illuminus5/skiff) ([Web Installer](https://illuminus5.github.io/skiff/webapp/installer/) | [Web Editor](https://illuminus5.github.io/skiff/webapp/editor/) | [Learn / 19-Chapter Manual](https://illuminus5.github.io/skiff/learn/)):**
    * **License:** Open Source (GPL-3.0). Fork of Felucca by Leo Kuroshita / Hügelton Instruments.
    * **Polyphony:** 6 polyphonic tracks with up to 12 shared voices on dual-core CPU.
    * **Concept:** 6-track groovebox firmware for the FM-1 with 14 synthesis engines and deep parameter-locking sequencer.
    * **Features:**
      * **6 Tracks & 14 Engines:** Expanded polyphonic tracks hosting virtual analog, FM, wavetable, physical modeling, drums, and noise generators.
      * **Advanced 64-Step Sequencer:** Per-step parameter locks (p-locks), microtiming, ratchets, and trig conditions (probability / iteration logic).
      * **Dual Effects & Mod Matrix:** Flexible send effects and real-time knob modulation assignments.
      * **Web Tooling:** Dedicated browser WebMIDI installer and companion web editor for patch and pattern management.

21. **[Felucca 8 Patterns by echoe](https://github.com/echoe/Felucca_8_patterns) ([Releases](https://github.com/echoe/Felucca_8_patterns/releases/tag/1.5.1_and_sequences)):**
    * **License:** Open Source (GPL-3.0). Fork of Felucca 1.5.1.
    * **Concept:** Pattern-chaining and arrangement expansion fork of Felucca.
    * **Features:**
      * **8 Chainable Patterns per Track:** Extends Felucca with 8 independent pattern slots per track that can be chained into song sequences.
      * **Optimized Flash Footprint:** Sample playback assets removed to maximize flash space and code budget for sequence memory and pattern chaining.

22. **[LCD-4 by devrvega](https://github.com/devrvega/LCD-4) ([Website & Hub](https://devrvega.github.io/LCD-4/) | [Web Emulator](https://devrvega.github.io/LCD-4/emu/) | [Web Installer](https://devrvega.github.io/LCD-4/install/) | [Manual](https://devrvega.github.io/LCD-4/manual/)):**
    * **License:** Open Source (GPL-3.0). Built on Felucca by Hügelton Instruments, by way of X0X, AMB-1, and IND-1.
    * **Polyphony:** 12-voice polyphony (8 melodic/synth voices + 4 drum voices) across 4 dedicated tracks.
    * **Concept:** Four-track pocket groovebox inspired by pocket calculator synths (Teenage Engineering Pocket Operator style) and vintage Game & Watch LCD games, featuring custom animated LCD game scenes for every sound engine.
    * **Features:**
      * **Four Dedicated Tracks:**
        * **Drums:** 4 kits of 11 parts selectable on black keys (TR-808, TR-909, Arcade console with pulse kicks/zaps/coin, and Vintage Rhythm Box CR-78/606). White keys act as 16-step sequencer lanes as on X0X, featuring Pip the drummer animating on screen.
        * **Basses:** Circuit-modelled Acid (TB-303 with accents/slides and bubbling lab animation), Mono (SH-101), Fat (Minimoog), Boom (808 sub), FM Bass (DX7), and Reese.
        * **Keys:** Poly (Juno-60 with chorus), Brass (Prophet-5 / OB-Xa), E.Piano (DX7), Organ (Korg M1 house organ), Strings (Solina string ensemble), and Bells.
        * **Leads:** Sync, Scream (Korg MS-20), Arcade (NES/Game Boy chip channels with tracker FX), and Arp. (Any synth track can load any sound).
      * **Sequencing & Performance:** 16 patterns with pattern chaining up to 64 steps, 16 chords with chord progression chaining, parameter locks (p-locks), ratchets, slides, swing, 16 punch-in effects, and live/step recording.

23. **[Caravel by bonszaimusic](https://github.com/bonszaimusic/caravel) ([Web Installer & Studio](https://bonszaimusic.github.io/caravel/webapp/installer/)):**
     * **License:** Open Source (GPL-3.0). Based on Felucca 1.6.1 by Leo Kuroshita / Hügelton Instruments.
     * **Concept:** Multi-engine synthesizer and groovebox featuring custom CrispyZebra waveforms, drum voices, expanded sample pack, and companion web studio.

24. **[PIGEON by The Shrimp Blimp](https://github.com/TheShrimpBlimp/pigeon) ([Website](https://theshrimpblimp.com/pigeon/) | [Signed Final Beta](https://github.com/TheShrimpBlimp/pigeon/releases/tag/v0.5.0-beta.1) | [Web Installer](https://theshrimpblimp.github.io/pigeon-website/webapp/installer/) | [Web Sample Tool](https://theshrimpblimp.github.io/pigeon-website/webapp/pigeon/) | [Web Emulator](https://theshrimpblimp.github.io/pigeon-website/webapp/emu/)):**
    * **License:** Open Source (GPL-3.0-only). Based on Felucca 1.5.1 by Hügelton Instruments, with recovery safeguards adapted from ChoralRoot FM-1.
    * **Concept:** Performance sampler with two song tracks, a 16-pad drum kit, chopping, sequencing and digital USB audio sampling. Current release: **0.5.0-beta.1 — THE FINAL BETA**.
    * **Features:**
      * **Samples & Voices:** 500 KiB usable shared storage; indexed mono MP3/IMA ADPCM songs and ADPCM drum hits. Up to 32 chops per song, eight shared song voices and four additional drum voices.
      * **USB Sampling:** Record to the selected song or drum pad, with threshold start, seconds/bar limits, meter/clipping indication, unsaved-take audition, trim, retry/discard and confirmed save. Input is mono PCM16 at 22.05 kHz; USB audio output can also be recorded on a computer.
      * **Chops & Library:** Per-chop playback point, reverse, cents, gain and loop crossfade; FIFO queues, undo/redo, selected-chop retention and bank reclamation. Browser chop collections assemble reusable sounds into songs or kits. Scratch decks are excluded from 0.5.
      * **Sequencer & Effects:** Grid/piano roll, 1–64 steps and four notes per step, independent note length/nudge, probability, conditions, Euclidean tools, A–D patterns and a 16-section arrangement; mixer, filter, delay, chorus, reverb, distortion and compression.
      * **Web & Accessibility:** Local sample editor, complete-session backups, screen-reader support, browser emulator and WAV/MP3 emulator recording.
    * **Provenance:** GitHub builds and attests the package through Firmware Hub's shared workflow; the maintainer reports hardware checks complete. Back up before installing; see the release's compatibility notes.

25. **[NOIZ DEMONS by SPIKE the Percussionist](https://github.com/SPIKE-the-Percussionist/noiz_demons) ([Releases](https://github.com/SPIKE-the-Percussionist/noiz_demons/releases) | [Live Firmware Jam](https://youtube.com/watch?v=o4zknplU5RE)):**
    * **License:** Open Source. Built on Felucca by Hügelton Instruments.
    * **Concept:** Ritualistic noise and sound generator firmware where parameter randomization is framed as occult summoning.
    * **Features:** Generating a sound summons one of 30 demons of the Ars Goetia, rendering the demon's sigil across the 240 × 240 color screen while its demonic rank algorithmically drives the wildness and distortion of the sound synthesis engine.

26. **[Tuna by delirioux](https://github.com/delirioux/tuna) ([Website & Web Emulator](https://delirioux.github.io/tuna/)):**
    * **License:** Open Source. Built on Felucca by Hügelton Instruments.
    * **Concept:** Generative music synthesizer and composition engine.
    * **Features:** Interactive composer profiles algorithmically generate and evolve musical tracks in real time, with macro controls allowing the performer to steer tonal palettes, tempo, and arrangement.

27. **[X0X-RMX by Mr-Roboto](https://github.com/Mr-Roboto/fm1-x0x-rmx) ([Website](https://mr-roboto.github.io/fm1-x0x-rmx/) | [Web Installer](https://mr-roboto.github.io/fm1-x0x-rmx/install/) | [Web Emulator](https://mr-roboto.github.io/fm1-x0x-rmx/emu/) | [Releases](https://github.com/Mr-Roboto/fm1-x0x-rmx/releases)):**
    * **License:** Open Source (GPL-3.0). Independent fork of X0X by Charles Vestal (built on Felucca).
    * **Polyphony & Engines:** Dual monophonic TB-303 synthesizers, dual TR-909 / TR-808 drum engines, and breakbeat slice playback.
    * **Concept:** Enhanced ReBirth-style acid and techno groovebox machine expanding the dual drum machines (TR-909 / TR-808), dual TB-303 synthesizers, and breakbeat engine.
    * **Features:**
      * **ORB-Inspired Remix Engine:** 256 step-remapping patterns available independently for the 909, 808, 303A, and 303B lanes.
      * **Enhanced TB-3PO Bassline Generator:** 22 musical scales, motif-based melodic phrase generation, rhythmic call-and-response phrasing, expressive accents/slides, and controlled parameter mutation.
      * **Grids MAP/EUCLID Drum Generation:** Generative Euclidean rhythm and drum patterns with density fill, offset, and chaos probability controls.
      * **Experimental 303 Morph Waveform:** Continuous real-time waveform morphing between Sharkfin, Trapezoid, and Notch-Trapezoid responses.
      * **Performance & Display Polish:** Pattern chaining, saved startup pattern combinations, and six selectable LCD color schemes.

28. **[DUB-1 by sbegueria](https://github.com/sbegueria/fm1-dub) ([Homepage](https://sbegueria.github.io/fm1-dub/) | [Web Installer](https://sbegueria.github.io/fm1-dub/install/) | [Web Emulator](https://sbegueria.github.io/fm1-dub/emu/) | [Manual](https://sbegueria.github.io/fm1-dub/manual/)):**
    * **License:** Open Source (GPL-3.0). Fork of AMB-1 by Charles Vestal (built on Felucca by Hügelton Instruments).
    * **Polyphony:** Multi-voice chord-memory stabs (open 7th, 9th) layered over 4 polymetric FM ping loops, sub-bass, and drum voices.
    * **Concept:** Berlin-style generative dub techno machine ("4 AM in Berlin"): power on and it immediately self-generates deep, evolving dub techno arrangements.
    * **Features:**
      * **Generative Dub Structure:** Chord stabs sent into tape delay, 4 FM ping loops running at independent polymeter lengths, tuned deep sub-bass under a ducking kick, rhythmic shaker, off-beat hi-hat, rimshot, sparse claps, and authentic vinyl crackle.
      * **Self-Arranging 8-Bar Phrases:** Automatically generates evolving arrangements with kick drops, breakdowns, builds, and fills.
      * **Generative & Custom Chord Memory:** Weighted random walks over musical scales that naturally resolve home, voiced as classic Roland/Basic Channel chord-memory stabs, plus 8 user-programmable progression slots.
      * **Performance Dub Controls & Echo Ripples:** Dedicated `REC` dub-hold button to freeze and loop the tape delay buffer infinitely while reverb continues ringing out and dry beats ride over top; real-time echo ripple animations visualising delay throws and loop positions on screen.

29. **[Unholy Union by Sparky (actuallysparky)](https://github.com/actuallysparky/FM-1-Unholy-Union-generative-drone-firmware) ([Releases](https://github.com/actuallysparky/FM-1-Unholy-Union-generative-drone-firmware/releases)):**
    * **License:** Open Source (GPL-3.0). Built on Felucca and Jangada.
    * **Concept:** Generative ambient and drone firmware featuring church-themed visuals and atmospheric harmonics.
    * **Features:** A single key press algorithmically generates and rolls a pad, an ambient sequence, a chord arpeggio, and a live-playable lead voice all locked to a shared harmonic key. Includes cathedral reverb algorithms, slow parameter drift, and church-inspired screen aesthetics.

30. **[Tessera by Rastapopolix](https://github.com/Rastapopolix/tessera) ([Project Page & Web Installer](https://rastapopolix.github.io/tessera/) | [Releases](https://github.com/Rastapopolix/tessera/releases)):**
    * **License:** Open Source (GPL-3.0). Formerly Melodee (Tess); a fork of Melodee by keremimo, itself built on Felucca by Leo Kuroshita (Hügelton Instruments).
    * **Concept:** Generative sequencer firmware: four tracks that write, evolve, and arrange music with you, from short loops to slowly changing ambient pieces.
    * **Features:**
      * **13 Algorithmic Note Generators:** Turing machine shift register, Euclid, Markov chain transitions, Morph phrase mutation, Atlas drum maps, Bounce/Fall, Awake, Poly, Quad, Constellation, Series, Chord progressions, and Answer (which dynamically replies to phrases you play).
      * **Generative Progression & Structure:** Evolve, Form (AABA-style sections), Tweak, and Energy pages dynamically shape and arrange musical phrases over time.
      * **Modulation Matrix & Cords:** 16 modulation cords from any source to any destination, slow organic modulation sources (`TIDE`, `SWARM`), and a dedicated modulation matrix.
      * **Sequencer & I/O:** Per-step ratchets and nudge, unified musical key for the whole project, MIDI clock out, and multi-channel MIDI output (dedicated MIDI channel per track).
      * **Sound Engines:** Authentic 6-operator FM (FM6), TRIO, and DRUM engines (808, 909, SID drum kit).

31. **[REGGAE-OS by Kemar Pennant (KemstheSage)](https://github.com/KemstheSage/reggae-os):**
    * **License:** Open Source (GPL-3.0). Derivative of Felucca 1.6.1.
    * **Concept:** Dub and roots reggae performance firmware transforming the FM-1 into a portable reggae sound system.
    * **Features:** Dedicated reggae tonewheel organ and deep sub-bass sound engines, intuitive four-knob dub shaping, and an animated retro sound system UI on the color display.

32. **[Glitchbox by Erik de Vos](https://github.com/erikdevos/glitchbox):**
    * **License:** Open Source (GPL-3.0). Fork of Felucca 1.5.1.
    * **Concept:** Harsh, experimental glitch synthesizer and live performance noise box.
    * **Features:** Self-chopping glitch synthesizer engine, a crushed bit-reduced synthesized drum kit, and live punch-in performance effects (beat rolls, rhythmic gating, pitch sweeps, and bitcrush filters) — 100% synthesized in real time without sample playback dependencies.

33. **[FM-1 T1 by Tensor-Programming](https://github.com/tensor-programming/fm1-t1):**
    * **License:** Open Source (GPL-3.0). Fork of Felucca 1.6.
    * **Concept:** Torso T-1 style generative algorithmic sequencer firmware for the FM-1.
    * **Features:** Six tracks running algorithmic generative cycles inspired by the Torso T-1 hardware sequencer, featuring Euclidean rhythm generation, pitch mapping, velocity accentuation, and simultaneous MIDI output routing across five tracks.

34. **[Patricktronics by gaumondp](https://github.com/gaumondp/patricktronics):**
    * **License:** Open Source (GPL-3.0). Derivative of Felucca.
    * **Concept:** Self-evolving ambient looping synthesizer inspired by Robert Fripp and Brian Eno's tape-delay Frippertronics setup.
    * **Features:** Locks a musical palette of up to five notes played through an FM sound engine, while a bounded random generator continuously rearranges the sequence note order, octave, and timing over time into an endless, evolving ambient soundscape.

35. **[FMini-1 by Guilherme Ruppert](https://github.com/ruppert/fmini-1) ([Web Installer & Manual](https://ruppert.github.io/fmini-1/)):**
    * **License:** Open Source (GPL-3.0-only). Built upon Felucca by Leo Kuroshita / Hügelton Instruments.
    * **Polyphony:** Monophonic (1 voice with 3-oscillator architecture, low-note priority, and authentic analog drift simulation).
    * **Concept:** Minimoog Model D style analog modeling synthesizer firmware for the M-VAVE FM-1.
    * **Features:** Triple-oscillator bank (LO to 2' range, 6 selectable waveforms including triangle, saw-triangle, reverse sawtooth, pulse, and wide/narrow square; independent detuning on OSC 2 & 3; noise generator with white and pink noise), 4-pole 24 dB/oct resonant ladder low-pass filter with per-stage nonlinear saturation and self-oscillation, dual Minimoog-style exponential contour generators (Filter ADS and Loudness ADS with release switch), LFO modulation (triangle/square) routable to pitch or cutoff, 100 factory presets across 5 categories + 32 user memory slots, dedicated arpeggiator with HOLD latch, 16-step sequencer (REC/PLAY), per-preset FX (reverb, tape delay, stereo chorus, overdrive), 50 assignable MIDI CC parameters with MIDI learn, USB and 3.5 mm TRS MIDI IN, and a custom 240×240 vintage Minimoog-inspired graphical UI with animated real-time filter response curves and ADSR envelopes.

36. **[Clipper by isod89](https://isod89.github.io/clipper-fm1/) ([Web Installer](https://isod89.github.io/clipper-fm1/webapp/installer/) | [Web Editor](https://isod89.github.io/clipper-fm1/webapp/editor/)):**
    * **License:** Open Source (GPL-3.0-only). Built upon Felucca by Leo Kuroshita / Hügelton Instruments.
    * **Polyphony:** 8 voices standard (12 or 16 voices optional compile target rendered across both CPU cores) with glide, polyphonic unison (2 or 4 voices per note), and dual-sound layer/split/multi-timbral support.
    * **Concept:** Deep polyphonic synthesizer firmware turning the FM-1 into an expansive multi-engine sound design powerhouse.
    * **Features:**
      * **23 Synthesis Engines & 407 Sounds:** Expansive multi-engine library (virtual analog, 6-op FM, wavetable, wave sequencing, vector crossfading, physical modeling, Casio CZ phase distortion, Roland Juno, granular, and sample playback).
      * **Modulation & Sequencing:** 12-slot modulation matrix, 3 LFOs, looping auxiliary envelopes, 4 performance macros (BRITE, TIMBR, MOTN, SPACE), and a 4-lane MOD SEQ modulation sequencer. Step sequencer with chord recording and 15-mode arpeggiator including a Turing machine generative looper (`TURNG`) and SPICE/DICE variations.
      * **Zero-Delay-Feedback Filters & FX:** 8 filter topologies (Moog ladder, MS-20, diode ladder, SEM, SVF, notch, BP, HP), per-sound insert FX (drive, fuzz, fold, crush, phaser, flanger, Juno chorus), stereo tempo-synced delays, Dattorro hall and shimmer reverbs, 3-band master EQ, and bus look-ahead limiter.
      * **Microtonal & MPE Support:** Full Scala (`.scl`) scale import alongside 14 historical/ethnic temperaments, MPE (per-note pitch bend, pressure, slide), and USB class-compliant stereo audio streaming directly into DAWs.

37. **[Felucca Wavetable Odeath Mod by gybe808-dotcom](https://github.com/gybe808-dotcom/FeluccaWavetableOdeathMod) ([Web Installer](https://gybe808-dotcom.github.io/FeluccaWavetableOdeathMod/)):**
    * **License:** Open Source (GPL-3.0). Built upon Felucca by Leo Kuroshita / Hügelton Instruments.
    * **Concept:** Community wavetable expansion modification for Felucca integrating custom wavetable banks and wave interpolation.

38. **[AmbWave by mentalcells](https://github.com/mentalcells/ambwave) ([Web Demo & Emulator](https://mentalcells.github.io/ambwave/try/)):**
    * **License:** Open Source (GPL-3.0). Built upon Felucca (formerly known as Hasake).
    * **Concept:** Ambient performance instrument: hold chords, layer atmospheric textures and sparse generative notes, and morph acoustic scenes via four rotary encoders.

39. **[fm1-studio-tess by jamesusmusic](https://github.com/jamesusmusic/fm1-studio-tess):**
    * **License:** Open Source (GPL-3.0). Merges Melodee's sound engine with Tess's generative sequencing algorithms.
    * **Concept:** Studio performance firmware utilizing dual JieLi `pi32v2` cores for polyphonic rendering alongside algorithmic generative polyrhythmic step sequencing.

40. **[Gnomad Synth V1 by Kyle Palaniuk](https://github.com/kpalaniuk/gnomad-firmware) ([Website & How-to](https://gnomad.cc) | [Releases](https://github.com/kpalaniuk/gnomad-firmware/releases) | [Install Guide](https://github.com/kpalaniuk/gnomad-firmware/blob/main/INSTALL.md)):**
    * **License:** Open Source (GPL-3.0). Built on Felucca.
    * **Concept:** Kid- and beginner-friendly firmware. EASY mode picks sounds by picture (10 pictures, 57 sounds, no reading needed), four colour-coded knobs named on screen with no shift layer, a singing Gnome, five ready-made grooves, loop recording with click and count-in, and hold PLAY to restart on the next bar. Hold HOME + SAVE to switch to Advanced: four tracks, step sequencer, effects, MIDI over USB and TRS.

41. **[Araminta by Wulgaren](https://github.com/Wulgaren/Araminta) ([Web Installer](https://wulgaren.github.io/Araminta/webapp/installer/) | [Web Editor](https://wulgaren.github.io/Araminta/webapp/editor/)):**
    * **License:** Open Source (GPL-3.0). Rebuilt on Felucca 1.5.1.
    * **Concept:** Modular-effects groovebox for the FM-1 with reorderable dynamic DSP signal routing.
    * **Features:** Introduces a per-track effects list that users can reorder, chain, or bypass on the fly, paired with expanded polyphony and an in-browser WebMIDI editor.

42. **[ESTAMPIE by ocean](https://github.com/ocean/estampie) ([Web App & Installer](https://fm-1.drewr.dev/estampie/webapp/installer/)):**
    * **License:** Open Source (GPL-3.0). Built on GHOULBOX and Felucca.
    * **Concept:** Medieval acoustic groovebox featuring authentic period instruments, modal tunings, and historical sonorities.
    * **Features:** Dedicated acoustic models and samples of lutes, hurdy-gurdies, shawms, portative organs, and historical frame drums, with authentic medieval temperaments and drone latching.

43. **[Mini-Tone by eldontyrellcorp](https://github.com/eldontyrellcorp/Mini-Tone):**
    * **License:** Open Source (GPL-3.0). Built on Felucca 1.5.
    * **Concept:** 6-track groovebox with Elektron-inspired sound engines and sequencing.
    * **Features:** 6 independent tracks hosting SID, Mutable Instruments Braids, and TB-303 synthesis machines, combined with ping-pong and alternating step sequencing.

44. **[Felucca MPE by Stanley Gurvich (EmeraldMoonLabs)](https://github.com/stanleygurvich/FeluccaMPE):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** MPE (MIDI Polyphonic Expression) performance expansion fork for Felucca.
    * **Features:** Adds per-note MPE pitch bend, pressure, and timbre modulation from external MPE controllers (LinnStrument, Seaboard, Erae Touch), alongside Voice LFO (VLFO) and DRIFT algorithms for living, breathing polyphonic chord textures.

45. **[TamaMPE by tamabotmusic](https://github.com/tamabotmusic/TamaMPE):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Expressive MPE synthesizer firmware for the M-VAVE FM-1.
    * **Features:** Combines 6-operator FM (FM6) and Sequential Prophet-5 style analog synthesis with MPE responsiveness, stereo spatialization, and expressive per-voice modulations.

46. **[Blue Hare by TristanoSuriani](https://github.com/TristanoSuriani/fel-tracker):**
    * **License:** Open Source (GPL-3.0). Deep rewrite of Felucca 1.4.1 into a 16-engine synthesizer.
    * **Concept:** Multi-engine synthesis workstation with vintage computer chips, vocal synthesis, and a 14-segment retro display.
    * **Features:** 16 distinct synth engines including Commodore 64 SID emulation, Oberheim OB-Xa polyphonic engine, rave/trance leads, LPC speech modeling, and synthesized drum kits; generative techno rhythm player on ARP and classic retro LED styling.

47. **[CRT-4 by devrvega](https://github.com/devrvega/CRT-4) ([Web Installer](https://devrvega.github.io/CRT-4/install/) | [Web Emulator](https://devrvega.github.io/CRT-4/emu/)):**
    * **License:** Open Source (GPL-3.0). Built on the Felucca HAL.
    * **Concept:** 4-track retro chiptune groovebox emulating the sound chips of 9 legendary gaming consoles and vintage computers.
    * **Features:** Emulates NES, Game Boy, Sega Master System, Sega Genesis / Mega Drive, PC Engine / TurboGrafx-16, and more. Track 1 is dedicated to period-accurate chiptune percussion, while tracks 2–4 play polyphonic chip voices selected from 16 custom sounds per machine. Includes full in-browser WebAssembly emulator and WebMIDI installer.

48. **[sardab by jrdntnnr](https://github.com/jrdntnnr/sardab) ([Web Installer](https://jrdntnnr.github.io/sardab/)):**
    * **License:** Open Source (GPL-3.0). Built upon GHOULBOX and Felucca 1.6 with elements from SLOOP, JIANT, and Melodee.
    * **Concept:** Desert dungeon-synth firmware and Eastern acoustic groovebox for the M-VAVE FM-1.
    * **Features:** Traditional microtonal *maqam* tunings, Arabic rhythm generators, physical modeling of Middle Eastern instruments (*oud* and *ney*), and resonant stone chamber reverbs.

49. **[Simorgh by runestone74](https://github.com/runestone74/Simorgh):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Persian traditional music synthesizer firmware for the FM-1.
    * **Features:** Physical modeling of the Persian hammered dulcimer (*santur*) in the PHYS engine, authentic Persian *dastgah* scale presets, and a custom mythical Simorgh boot splash.

50. **[Oktowave by PierreArnaudGUYOT](https://github.com/PierreArnaudGUYOT/FM1-Oktowave-Firmware) ([Web Installer](https://pierrearnaudguyot.github.io/FM1-Oktowave-Firmware/)):**
    * **License:** Open Source (GPL-3.0). Fork of Felucca 1.6.1.
    * **Concept:** Adds fixed-point WAVELET synthesis to the Felucca platform.
    * **Features:** Integrates engines A and B from the Wavelet Synthesizer, 108 curated factory presets, and a dedicated browser installer.

51. **[Yanfei by izumoe](https://github.com/izumoe/yanfei) ([Web Installer & Emulator](https://izumoe.github.io/yanfei/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** 12-engine synthesizer and 4-track music tracker on the Felucca platform.
    * **Features:** 12 synthesis engines (including retro chip voices), 96 factory presets, integrated 4-track tracker sequence interface, and an interactive browser environment.

52. **[Felucca-opx by thomasgregorymarsden-code](https://github.com/thomasgregorymarsden-code/Felucca-opx) ([Web Installer](https://thomasgregorymarsden-code.github.io/Felucca-opx/) | [Web Emulator](https://thomasgregorymarsden-code.github.io/Felucca-opx/webapp/try/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Adds a Korg Opsix-style altered FM operator engine to Felucca.
    * **Features:** Expanded FM operator modes with non-linear waveshaping, ring modulation, and operator filter modes, complete with browser emulator and installer.

53. **[Acultur8 X0X by keyboy250](https://github.com/keyboy250/fm1-x0x-acultur8) ([Web Emulator & Lab](https://keyboy250.github.io/fm1-x0x-acultur8/)):**
    * **License:** Open Source (GPL-3.0). Built on X0X and Felucca.
    * **Concept:** Experimental sample-slicing groovebox variant for the FM-1.
    * **Features:** Real-time playback of tempo-synced slice banks from WAV files and marker cues, paired with an interactive browser-based sound laboratory.

54. **[Cesari by briwil](https://github.com/briwil/Felucca) ([Web Installer](https://briwil.github.io/Felucca/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Felucca modification enabling multi-track drum kits across any channel.
    * **Features:** Assign full TR-808 (from X0X) and TR-606 (from 6W6) drum kits to any track, with independent per-drum sound parameter editing.

55. **[ChoralRoot J-6 by EremanSim](https://github.com/EremanSim/ChoralRootj-6) ([Web Installer](https://eremansim.github.io/ChoralRootj-6/webapp/installer/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Port of ChoralRoot chord-machine firmware incorporating the Roland Aira Compact J-6 chord set and progression library.

56. **[more chords! by rosen-wav](https://github.com/rosen-wav/more-chords-M-VAVE-FM-1-Custom-Firmware) ([Web Installer](https://rosen-wav.github.io/more-chords-M-VAVE-FM-1-Custom-Firmware/site/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Deep ChoralRoot remix and chord performance firmware.
    * **Features:** 7 new custom synthesis engines (PROPHET, GRAIN, SWARM, CLUSTER, CLOUD, BASS, MORPH), advanced step sequencer, and algorithmic chord generator.

57. **[fm1-amy / X0X AMY by Dan Ellis (dpwe)](https://github.com/dpwe/fm1-amy):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Ports the AMY (Additive Music synthesizer librarY) polyphonic Juno-60 engine to the M-VAVE FM-1.
    * **Features:** 6-voice polyphonic synthesizer running 128 factory Roland Juno-60 patches on the X0X firmware hardware platform.

58. **[OrganVave-1 by ruppert](https://github.com/ruppert/organvave-1):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Dedicated Hammond B3 tonewheel organ emulation with virtual drawbars and Leslie rotating speaker simulation, ported from setBfree.

59. **[Haunted FM-1 by davidpryan](https://github.com/davidpryan/haunted-fm1) ([Web Installer & Emulator](https://davidpryan.github.io/haunted-fm1/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Suite of 5 generative ambient and hauntological firmwares: Midnight Route, Voicemail, Untrue Step, Half-Light, and Worn Tape.
    * **Features:** Tape saturation, lo-fi wow/flutter, generative harmony walkers, and nostalgic ambient textures.

60. **[FM-PLAITS by Narti-Live](https://github.com/Narti-Live/fm1-fm-plaits) ([Web Installer](https://narti-live.github.io/fm1-fm-plaits/)):**
    * **License:** Open Source (GPL-3.0). Built on FM1 Open.
    * **Concept:** 16 Mutable Instruments Plaits-inspired macro-oscillator models with an algorithmic generative melody sequencer.

61. **[Tessera (Melodee Tess) by Rastapopolix](https://github.com/Rastapopolix/melodee-tess) ([Web Installer](https://rastapopolix.github.io/melodee-tess/webapp/installer/) | [Web Emulator](https://rastapopolix.github.io/melodee-tess/webapp/sim/)):**
    * **License:** Open Source (GPL-3.0). Fork of Melodee.
    * **Concept:** Algorithmic generative composition firmware with 13 procedural generators, structural song forms (verse/chorus), and an extensive modulation matrix.

62. **[1971 by synthi](https://github.com/synthi/fm1-1971):**
    * **License:** Open Source (GPL-3.0). Fork of Melodee 1.3.5.
    * **Concept:** Generative ambient synthesizer firmware focusing on vintage drift, meditation soundscapes, and warmth.

63. **[Haave by thebrodi](https://github.com/thebrodi/fm1-haave) ([Web Emulator](https://thebrodi.github.io/fm1-haave/try/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Ambient meditation firmware featuring self-evolving chord progressions and live keyboard layer toggles.

64. **[Modular One by bunglesociety](https://github.com/bunglesociety/modular-one) ([Web Installer](https://bunglesociety.github.io/modular-one/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Film score synthesizer running the Modular Town plugin's soft FM synthesis engine, 3 synth tracks, cinematic effects, and an onboard MIDI player.

65. **[MEOW-1 by JB-Interactive](https://github.com/JB-Interactive/Felucca-Meow):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Expressive cat-vocalization synthesizer (meow, purr, hiss) and 4-track feline band based on Felucca.

66. **[NCC (Novation Circuit Companion) by fenderberg](https://github.com/fenderberg/fm1-nc-companion) ([Web Emulator](https://fenderberg.github.io/fm1-nc-companion/webapp/try/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** 2-part multitimbral synthesizer tailored as an expansion sound module for the Novation Circuit Tracks, with CC macro maps and quick patch recall.

67. **[Golana DZ Edition by dzwerg](https://github.com/dzwerg/Golana-DZ):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Enhanced Golana synthesizer with a 64-step sequencer, 32 program banks, song mode, and polyphonic USB-MIDI output.

68. **[Elixir by Dan Majka (dmajka)](https://github.com/dmajka/elixir) ([Website & Web Installer](https://dmajka.github.io/elixir/) | [Web Emulator / Try It](https://dmajka.github.io/elixir/try/) | [Kit Library & Manager](https://dmajka.github.io/elixir/library/) | [Manual](https://dmajka.github.io/elixir/manual/)):**
    * **License:** Open Source (GPL-3.0-only). Built upon the Felucca hardware abstraction layer, USB stack, and reverb. Formerly known as *Kettle* (up to v0.13).
    * **Polyphony & Architecture:** 6 voices across 7 tracks (3 drum parts, snare/clap, cymbal, closed and open hi-hats), with fixed-point DSP rewrite (tested to match original float calculations within 0.1 dB and 0.99–1.00 correlation).
    * **Concept:** Port and substantial expansion of the **Erica Synths LXR-02** digital drum synthesizer and groovebox for the M-VAVE FM-1.
    * **Sound Engines & Synthesis:**
      * Every drum voice features dedicated oscillator, FM modulation, transient shaper, multi-mode filter, envelopes, and LFO.
      * Drum voices 1–3 can route into a port of **Mutable Instruments Rings** physical modeling resonators (modal, string, FM).
      * Per-voice waveshapers (5 curves), bit reducer, tilt EQ, random-per-hit variations, choke groups, and cross-modulation between voices.
      * Complete compatibility with hardware Erica Synths LXR-02 `.SND` kits and project folders over USB.
    * **Sequencing & Generative Engines:**
      * 32 patterns of 4 bars (up to 64 steps) with parameter locks on any step, flams, shifts, rolls, ratchets, and step probability.
      * Polymetric sequencing: independent per-track lengths, clock divisions (/4 to x4), and playback directions (forward, reverse, ping-pong, random, random walk).
      * Integrated generative pattern generators: Euclidean rhythms (with dual pulses combined via boolean logic: OR, XOR, AND, SUB), Turing machine, Cellular automata, and Emilie Gillet's Mutable Instruments Grids drum mapping.
      * **Cross-Track Links:** Conditional track modulation (e.g., when kick hits, closed-hat probability ducks by -60%).
    * **Performance Mode (PERF) & Effects:**
      * **16-Key PERF Mode:** Transforms the 16 white keys into momentary performance controls (rolls, fills, beat repeat, delay freeze, reverb throws, tape stop, filter sweeps, drill, half-time, sidechain pump, comb, crush, reverse).
      * **FX Bus & Master Reverb:** Overdrive (tube, fold, rat), ring modulator, compressor, delay, phaser, flanger, and Felucca's room/spring/hall stereo reverbs.

69. **[PALEOTONE by fantasmoslam](https://github.com/fantasmoslam/Paleotone) ([Web Installer](https://fantasmoslam.github.io/Paleotone/webapp/installer/) | [Web Emulator](https://fantasmoslam.github.io/Paleotone/webapp/emu/) | [USB Second-Screen App](https://fantasmoslam.github.io/Paleotone/webapp/screen/) | [Manual](https://fantasmoslam.github.io/Paleotone/manual/)):**
    * **License:** Open Source (GPL-3.0-only). Built on GHOULBOX 2.3.2 by Jason Persinger and Felucca 1.4.1 by Hügelton Instruments. Formerly known as *DINOBOX*.
    * **Polyphony:** 12 voices of polyphony across 4 tracks with drone latching.
    * **Concept:** Generative ambient dinosaur and prehistoric soundscape synthesizer and groovebox featuring prehistoric creatures, war drums, jungle pads, and volcanic rumbles.
    * **Features:**
      * **1993 Park-Operations Terminal UI:** Share Tech Mono pixel typography, phosphor green and amber CRT glass palette with scanlines, electrical fence posts, Dilophosaurus boot splash, and T. rex icons.
      * **SAURUS Creature Voice Engine (Engine 15):** Synthesized prehistoric throat modeling with adjustable CALL shapes (BELLOW, ROAR, BARK, HOOT, TRILL, CHIRP, MOAN, HISS, SNORT), animal SIZE (sauropod formants), SWOOP pitch glide, GROWL roughness, breath noise, and mouth openness. Includes 20 distinct creature profiles (Tyrant Roar, Brachio Call, Raptor Chat, Ptero Shriek, Titan Ape, Sea Monster, etc.).
      * **ROAR Hurdy-Gurdy & EPOCH Generative Composer:** Evolved hurdy-gurdy engine with drone and call controls, plus algorithmic generative progression composer (EPOCH) across four tracks.
      * **Prehistoric Sound Library & TRIBE Drums:** 119 original sounds across Analog, Voice, Wheel, Phys, Trio, and Lofi engines; custom synthesized prehistoric percussion kit (BOOM, SKIN, CLAP, SEEDS, RATTL, LOG, BONE, ROCK) and environmental samples (storm, lithophone, jungle ambience).
      * **USB Second-Screen Companion:** Web-based display companion over USB-C translating MIDI and video render slices to mirror and control the synthesizer screen on an external smartphone, tablet, or cyberdeck monitor.

70. **[BB1 by Texas Radio & The Big Beat](https://github.com/TexasRADIO/bb1-firmware) ([Web Installer](https://thebigbeat.app/fm1/install/) | [Web Emulator](https://thebigbeat.app/fm1/emulator/) | [Guide](https://thebigbeat.app/fm1/guide/)):**
    * **License:** Open Source (GPL-3.0-only). Felucca-family firmware.
    * **Polyphony & Engines:** Two independent drum machines (KIT A + KIT B) running simultaneously: a live-synthesised 808 plus seven sampled machines—LinnDrum, Linn LM-1, DrumTraks, DMX, Drumulator, Simmons and Rhythm King. **Dillo** is a monophonic bass synth with nine presets, including Square Acid; a shared three-head tape echo and spring reverb. Drum B renders on the FM-1's second core.
    * **Concept:** A two-beat rhythm machine: stack two drum machines from different eras and let the bass ride on top.
    * **Features:**
      * **Library (BB1 1.5):** 67 songs / 233 song sections, 21 eras / 168 sections, 138 classic preset rhythms from four vintage rhythm boxes, and 205 ACID phrases in 27 Dillo banks.
      * **On the beat:** kit and pattern changes queue for the next bar, with the screen showing NEXT until they land.
      * **Performance:** REC + FX dub throw, live tempo/swing/A-B balance/transpose, and four knobs that always follow the screen.
      * **Install:** one-click browser installer handles firmware and the separate sound library over USB-MIDI, checking the existing sounds before writing. Official-firmware return uses M-VAVE's updater; keep backups and follow the guide.
      * **Browser player:** the released BB1 engine and all eight machines in the browser. The guide documents known limits, including the first tempo-edit jump; browser checks do not establish hardware timing.

#### 1.1.2. SLOOP Ecosystem (Groovebox Core & Derived Firmwares)

Firmwares centered around the **SLOOP** 4-track live groovebox workflow and its DX7/sampling expansion forks:

1. **[SLOOP by isod89](https://github.com/isod89/sloop-fm1) ([Web Installer](https://isod89.github.io/sloop-fm1/) | [Web Editor](https://isod89.github.io/sloop-fm1/webapp/editor/)):**

* **License:** Open Source (GPL-3.0). Based on Felucca by Hügelton Instruments.
* **Polyphony:** Up to 14 voices total — 8 dynamically shared synth voices across 3 tracks (`NVOICE 8`) plus 6 dedicated drum voices on track 4 (`NDRUM 6`) with dual-core audio rendering.
* **Concept:** Live performance groovebox firmware designed for any music style without mandatory presets or fixed patterns.
* **Features:** 4 tracks (3 synth tracks + 1 drum machine with 16 sounds across the white keys), 9 synthesis engines, 68 sounds, 37 drum kits, custom sample support, and live-playable song mode. Features USB stereo audio input (class-compliant recording directly into DAWs without drivers), 3.5 mm TRS MIDI IN keyboard input, MIDI clock in/sync, button and note LED illumination modes for dark environments, sample chopping/fitting, and a web editor with full backup/restore (including portable project dumps and loads directly from mobile phones over USB-C WebMIDI).

2. **[sloopDX by zvenson](https://github.com/zvenson/dxsloop) ([Website & Web Installer](https://dx7.designburgapps.com/) | [Web Editor](https://dx7.designburgapps.com/webapp/editor/) | [Cheat Sheet PDF](https://dx7.designburgapps.com/sloopdx-cheat-sheet.pdf)):**
    * **License:** Open Source (GPL-3.0-only). Built upon SLOOP (isod89), Felucca (Leo Kuroshita), and the `msfa` 6-operator DX7 core of Dexed (Apache-2.0).
    * **Polyphony:** Shared 8-voice polyphonic budget across 3 synth parts (Dexed 6-op FM) + 1 dedicated FM drum machine.
    * **Concept:** SLOOP's live groovebox workflow merged with an authentic Yamaha DX7 engine and a fully programmable FM drum machine.
    * **Features:**
      * **6-Operator FM Engine:** Complete 32-algorithm DX7 engine ported directly from Dexed's `msfa` (99% sample-identical to Dexed), featuring full envelope scaling, keyboard level/rate scaling, LFO, and feedback.
      * **Cutoff & Resonance Filter:** Dedicated resonant low-pass filter (CUT and RESO on Knobs 1 & 2) placed behind every DX7 voice, modulatable via envelope and LFO.
      * **On-Device Voice Editing:** Full voice programming on the FM-1 hardware with parameter lists, visual operator box diagrams, and operator solo/mute auditioning, backed by a companion web editor.
      * **256 Sysex Voices:** 8 banks of 32 voices loaded directly from standard DX7 `.syx` bulk dumps (4104 bytes), supplemented with 20 factory modern patches (DEEP SUB, 808 SUB, REESE).
      * **Programmable 16×8 FM Drums:** 16 distinct FM drum sounds across 5 kits (`DX KIT`, `808 FM`, `ELECTRO`, `METAL`, `MY KIT`). Each sound provides 8 on-device macro controls (TUNE, DECAY, SWEEP, BRIGHT, NOISE, LEVEL, PAN, CHOKE) plus a dedicated reverb send, parameter locks per step, kit randomization dice, and kit export/import via `.syx`.
      * **OMNI Chord Harp Mode:** Turn any synth track into an Omnichord-like instrument (black keys trigger chords like F, C, G, Dm, Am, Em, G7, E7, D7, Bb, A7, while white keys act as 16 strum strings; bass tracks can follow chords via `FLW`).
      * **Sequencer & Effects:** Up to 128 steps per track (256 steps shared dynamically across tracks), dedicated per-effect pages (SENDS, DIST with soft/hard/fuzz/crush, CHORUS, DELAY, REVERB), USB audio streaming, and live punch-in FX.

3. **[FM1 Move by Nicodesy06](https://github.com/Nicodesy06/FM1-MOVE) ([Web Simulator](https://nicodesy06.github.io/FM1-MOVE/sim/) | [Device Installer & Manager](https://nicodesy06.github.io/FM1-MOVE/device/) | [Manual / Quick Start](https://nicodesy06.github.io/FM1-MOVE/manual/) | [Source Branch](https://github.com/Nicodesy06/FM1-MOVE/tree/fm1-move/dev)):**
    * **License:** Open Source (GPL-3.0). Built upon SLOOP 2.5 by isod89.
    * **Polyphony:** 8 independent tracks with an 8-voice polyphony budget.
    * **Concept:** Eight-track groovebox firmware for the FM-1 inspired by the Ableton Move workflow, featuring a custom 240 × 240 UI designed for live performance.
    * **Features:**
      * **8 Independent Tracks:** Flexible track assignments (any combination of synth tracks or drum kits).
      * **Clips & Scenes:** Performance-oriented clips and scene launcher replacing traditional linear song arrangers.
      * **Browser Simulator:** Firmware compiled to WebAssembly running directly on a simulated device panel in the browser.
      * **Device Page:** In-browser WebMIDI tool to install/backup firmware, manage presets, kits, FM6 banks, and samples.
      * **Status:** Verified in host simulation and builds cleanly for the JieLi AC791N target compiler (experimental / hardware verification in progress).

4. **[FM1 Quest by hericdk](https://github.com/hericdk/fm1-quest) ([Web Installer](https://hericdk.github.io/fm1-quest/webapp/installer/) | [Web Emulator](https://hericdk.github.io/fm1-quest/emulator/)):**
    * **License:** Open Source (GPL-3.0-only). Built upon the SLOOP groovebox core.
    * **Polyphony:** 8 shared synth voices across 3 tracks + 6 drum voices (up to 14 voices total).
    * **Concept:** Fantasy RPG sidescroller interface for the groovebox: tracks are represented as party heroes, sequence steps are attacks, BPM drives party walk speed, scales dictate biomes, and recording loops triggers boss fights.

5. **[JIANT FM by juanjiant-bit](https://github.com/juanjiant-bit/JIANT) ([Online Emulator](https://juanjiant-bit.github.io/JIANT/) | [Web Installer](https://juanjiant-bit.github.io/JIANT/webapp/installer/) | [Web Editor](https://juanjiant-bit.github.io/JIANT/webapp/editor/)):**
    * **License:** Open Source (GPL-3.0-only). Built upon Felucca 1.1.5.1 and SLOOP.
    * **Polyphony:** 6 multi-engine tracks with dynamic voice allocation and dual-core processing.
    * **Concept:** Bio-synthetic groovebox & performance synthesizer OS for the FM-1 with a high-contrast "thermal camera" UI theme (ironbow gradient palette and Chakra Petch typography). Treat each sound engine as an organic bio-organism reacting dynamically in real time.
    * **Features:**
      * **6 Multi-Engine Tracks (T1–T6):** Flexible pattern sequencing with compressed song sections (storing 8 songs × 4 sections within the FM-1's flash boundary).
      * **8 Distinct Sound Engines:** ANALOG, FM6 (6-op DX7), PHASE, LOFI (bytebeat/floatbeat), VOICE (formants), WHEEL (tonewheel), NOISE, and DRUM-X (bio-percussion).
      * **Bus Slicer (SL BUS):** 16-step mix-bus stutter/repeater and pitch-slicing processor (can be routed post-effects or pre-effects tail).
      * **Technical Visualizer:** Live display curves for envelopes, LFOs, distortion, delay, reverb, and thermal isotherm spectrum.
      * **Live Performance Navigation:** Quick page-jumping by turning the `PRESETS` encoder while holding page navigation buttons.

6. **[ORBIT by dspaudio](https://github.com/dspaudio/orbit) ([Web Installer](https://dspaudio.github.io/orbit/) | [Web Emulator](https://dspaudio.github.io/orbit-web-emu/)):**
    * **License:** Open Source (GPL-3.0). Based on SLOOP.
    * **Concept:** Groovebox with visual aesthetic and screen interfaces inspired by the Teenage Engineering OP-1.
    * **Features:** Integrated sample manipulation tools and an event tape mechanism for dynamically shifting and rearranging what the 4 tracks play.

7. **[NoteSorcery by catacombius](https://github.com/catacombius/NoteSorcery):**
    * **License:** Open Source (GPL-3.0). Built on SLOOP.
    * **Concept:** OP-1-style 8-track groovebox firmware.
    * **Features:** Live USB audio sampling, project export straight to Ableton Live sets, companion Android controller application.

8. **[SLOOP ALG by shaw-core](https://github.com/shaw-core/Sloop_ALG02):**
    * **License:** Open Source (GPL-3.0-only). Based on SLOOP.
    * **Concept:** Experimental synthesis expansion fork adding Karplus-Strong string synthesis, plucked physical models, additive synthesis, DX7, and VA engines.

9. **[FM80S by Floydus (y6zkcqnf5r-hue)](https://github.com/y6zkcqnf5r-hue/fm1-fm80s):**
    * **License:** Open Source (GPL-3.0). Based on SLOOP 2.5 and Felucca.
    * **Concept:** Synthwave-oriented synth-looper firmware for live loop stacking, step sequencing, and song assembly with planned 8-track expansion.

10. **[SLOOP DX7 Banks by majnikool](https://github.com/majnikool/sloop-fm1):**
    * **License:** Open Source (GPL-3.0). Built on SLOOP by isod89.
    * **Concept:** SLOOP expansion fork supporting up to 12 DX7 voice banks grouped by sound category.
    * **Features:**
      * **12 Categorized DX7 Banks:** Direct flash storage and instant switching across 12 full DX7 voice banks (384 presets) categorized by instrument types (Keys, Bass, Leads, Pads, Strings, Brass, Percussion, FX).
      * **Fast Preset Navigation:** Instant preset category selection without overwriting SLOOP sequencer project states.

11. **[SLOOP Floyd FM by René Bohne](https://github.com/renebohne/sloop-fm1):**
    * **License:** Open Source (GPL-3.0). Fork of SLOOP by isod89.
    * **Concept:** SLOOP fork integrating Floyd Steinberg's 4-operator FM synthesis algorithms and real-time visual envelope feedback.
    * **Features:**
      * **Floyd Steinberg 4-OP FM Engine:** Adds dedicated 4-operator FM sound algorithms with custom modulation matrices and operator wave shaping.
      * **Live Envelope & Scope Display:** Real-time on-device oscilloscope rendering active voice output and ADSR envelope curve response directly on the 240 × 240 screen.

12. **[SLICE64-FM by jeymadcat-ops](https://jeymadcat-ops.github.io/SLICE64-FM-web/):**
    * **License:** Open Source (GPL-3.0). Built upon SLOOP / Felucca core.
    * **Concept:** 64-slice sample chopper, beat-slicing, and FM groovebox firmware for the FM-1.
    * **Features:** Deep 64-slice sample mapping across pads/keys, auto-transient detection, slice reversal, pitch pitching per slice, and integrated FM synth accompaniment.

13. **[winampFM by hericdk](https://github.com/hericdk/winampFM) ([Website & 3D Web Simulator](https://hericdk.github.io/winampFM/)):**
    * **License:** Open Source (GPL-3.0-only). Built upon SLOOP 2.6 (isod89) and Felucca (Leo Kuroshita / Hügelton Instruments).
    * **Concept:** Winamp 2.x-inspired performance synthesizer & groovebox firmware turning the FM-1 interface into classic Winamp windows (main player, equalizer sliders, playlist, and pixel-art visualizers).
    * **Features:**
      * **Winamp 2.x Main Screen & Playlist:** Main home screen styled as Winamp 2.x with time counter, audio spectrum analyzer, BPM, sound marquee, and track buttons. Sound presets browse like a Winamp playlist.
      * **Reel-to-Reel Tape Looping:** Tape deck recording screen with live input VU meter, tape counter, note display, and pass counts. Arming REC starts recording; pressing REC again calculates and locks the loop BPM automatically.
      * **Equalizer Sliders FX & PARTY Mode:** Effects grouped into Winamp equalizer slider bands (SEND, SPACE, MASTER, PARTY, TRACK) controlled via the 4 knobs. Dedicated PARTY performance staging (SOLO, DUEL, TRIAD, AUTOTURN stage cycling, KEEP lead holding, YOYO cross-track stepping).
      * **28 Full-Screen Pixel-Art Visualizers:** Pressing HOME twice unlocks 28 reactive full-screen visualizers responding to played notes, loops, and knobs (Milkdrop-style oscilloscope, spectrum bars, starfield shooter, 80s neon night drive, polygonal chords, doomscrolling feed, dancing raccoon, and lofi study).
      * **Expanded Sound Library & Tapes Carousel:** 157 total sounds (including 153 SLOOP 2.6 sounds plus Brazilian acoustic instruments: Cavaquinho, Berimbau, Agogô Bell, Sanfona, and Brasil drum kits), with a PS1-style 3D cassette tape preview carousel.
      * **Web 3D Simulator & Recorder:** Includes an interactive in-browser 3D model simulator running the real firmware via WebAssembly with audio playback and a Win98-style screen & sound recorder widget.

14. **[No Man Sky FM by hericdk](https://github.com/hericdk/nomanskyFM) ([Website & Web Installer](https://hericdk.github.io/nomanskyFM/) | [3D Web Simulator](https://hericdk.github.io/nomanskyFM/#simulator)):**
     * **License:** Open Source (GPL-3.0). Built upon SLOOP 2.7.1 (isod89) and Felucca (Leo Kuroshita / Hügelton Instruments).
     * **Concept:** Space exploration RPG adventure and live performance groovebox firmware for the FM-1: fly between procedurally generated planetary systems using the rotary knobs while the other hand performs and arranges the live soundtrack.
     * **Features:**
       * **Spaceflight & Planet Exploration:** Pilot a spacecraft across star systems with KNOB 1 (turn/steer) and KNOB 2 (velocity/thrust); land on planetary surfaces, mine mineral resources, fight sentinel robots, warp between stars, and call in your starship via OCT- hold commands.
       * **Interactive Cockpit & Camera Zoom:** KNOB 3 cycles 4 camera perspectives: wide orbit, near flyby, close-up chase, and internal cockpit cabin view.
       * **Live Soundtrack Engine:** Integrated SLOOP 2.7.1 groovebox core allows live sequencing, synth solos, and beat jamming simultaneously while piloting the spacecraft.
       * **Web 3D Simulator & Installer:** Includes an interactive in-browser 3D model simulator running the firmware via WebAssembly with sound output, plus one-click browser WebMIDI installation directly from the project site.

15. **[MYCELIUM by Mandalars](https://github.com/megagott/mycelium-fm1) ([Website](https://www.mandalars.org/mandalars/fm1/) | [Releases](https://github.com/megagott/mycelium-fm1/releases)):**
     * **License:** Open Source (GPL-3.0). Built upon Felucca and SLOOP.
     * **Concept:** Psychedelic dance music groovebox firmware dedicated to Forest, Psytrance, Goa, and Hitech production on the FM-1.
     * **Features:** Custom-crafted punchy trance drum kits, alien psychedelic icons and animations, fast rolling 16th-note bassline tools, and four factory demo arrangements.

16. **[GR!MM by GRiMMBIENT](https://github.com/GRiMMBIENT/grimm) ([Browser Demo](https://grimmbient.github.io/grimm/) | [Web Sound & Sample Editor](https://grimmbient.github.io/grimm/editor.html) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1xapljs/grmm_firmware_for_dark_ambient_v20_coming_soon/)):**
     * **License:** Open Source (GPL-3.0). Built upon Felucca and SLOOP.
     * **Concept:** Dark ambient, dungeon synth, and deathdream groovebox firmware transforming the FM-1 into an atmospheric sound generator.
     * **Features:**
       * **4 Independent Tracks:** Each track hosts its own sound engine and can be latched and played simultaneously directly from the home screen.
       * **Diverse Sound Sources:** 7 selectable sound engines including a full 6-operator FM engine alongside custom sample playback with authentic tape-warble modulation.
       * **Atmospheric Signal Chain:** Onboard effect suite featuring TAPE saturation, GRAIN granulator, DELAY, and SPACE (infinite reverb and audio freeze mode).
       * **Sequencing & Performance:** 64-step sequencer, one-key chords, dedicated song mode, PERFORM live-tweak page, and autosave.
       * **Web Companion:** Browser-based editor for sculpting sounds, loading custom WAV samples, and managing backups over WebMIDI, plus an in-browser WebAssembly demo.

17. **[TheReFmB1rth by AlexanderSeel](https://github.com/AlexanderSeel/TheReFmB1rth) ([Releases](https://github.com/AlexanderSeel/TheReFmB1rth/releases)):**
     * **License:** Open Source (GPL-3.0). Built upon Felucca and SLOOP core.
     * **Concept:** Four-machine acid groovebox inspired by Propellerhead ReBirth RB-338: dual TB-303 style acid basslines alongside TR-808 and TR-909 drum machines (including 909 flam memory).
     * **Features:** 4-track mixer, sequence sections A through H chainable into complete songs, resonant filter, stereo delay, distortion, and master compression.

18. **[Kawa Tracker by Guizmoh](https://github.com/Guizmoh/Kawa-Tracker-Fm1):**
     * **License:** Open Source (GPL-3.0). Built upon SLOOP and Felucca.
     * **Concept:** 6-track pocket tracker and groovebox firmware with trilingual UI support (English, French, Spanish).
     * **Features:** 6 tracks assignable to pulse, 4-bit wave, noise, 6-operator FM, drum kits, or samples; song chaining, 32 live performance punch-in effects, and Magic generative tools for drums, melodies, and breakbeat slicing.

19. **[BREAK//174 (Fm1dnbchatgpt) by EremanSim](https://github.com/EremanSim/Fm1dnbchatgpt):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Jungle and Drum & Bass performance machine running at ~166–174 BPM.
     * **Features:** Instant Amen break generator with live roll staging, slice stutter, and reverse playback mapped across physical keys.

20. **[Loom FM-1 by Co-oscillator](https://github.com/Co-oscillator/Loom-FM-1):**
     * **License:** Open Source (GPL-3.0-only). Built upon Felucca platform.
     * **Concept:** Five-track polyphonic synthesizer, sampler, and groovebox firmware with neon color-coded UI themes.
     * **Features:** 4 polyphonic synth/sampler tracks (1–4) plus a dedicated 5th synthesized drum track (D) featuring analog and FM kits, choke groups, and per-lane mixing.

21. **[Ravel FM-1 by De-Pattern](https://github.com/De-Pattern/Ravel_FM1):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Eight-track sound-design groovebox turning the FM-1 into an ambient tape-sampling laboratory.
     * **Features:** 8 synthesizer tracks that continuously capture performance audio onto a shared virtual tape loop, with live slicing, re-triggering, and generative cross-track modulation.

22. **[Bunker Evolved by kidbee85-beep](https://github.com/kidbee85-beep/bunker-evolved) ([Simulator](https://bunker-evolved.sugarypixie10.chatgpt.site/simulator/)):**
     * **License:** Open Source (GPL-3.0). Built upon Felucca.
     * **Concept:** Generative ambient soundscape explorer featuring 4 evolving layers, 64 presets, 24 ambient acoustic worlds, and GROW generative scaling.

23. **[MASIF by thecemeterygates](https://github.com/thecemeterygates/masif-fm1) ([Website & Web Installer](https://thecemeterygates.github.io/masif-fm1/) | [Releases](https://github.com/thecemeterygates/masif-fm1/releases)):**
     * **License:** Open Source (GPL-3.0-only). Built upon zp12, SLOOP, and Felucca.
     * **Concept:** 4-track sample tracker and rack sampler firmware turning the FM-1 into a portable tracker and hardware sampling workstation.
     * **Features:**
       * **4-Track Tracker Engine:** 16 songs, 128 instruments with tables, groove controls, modulation envelopes, LFOs, sidechaining, resonant filter, overdrive, and per-instrument EQ.
       * **Sample Storage:** 24 sample slots with ~730 KB flash sample memory (~19s at 26 kHz 12-bit or up to ~108s at 13 kHz 4-bit ADPCM).
       * **Direct USB & Hardware Sampling:** On-device sampler page to record computer audio over bi-directional USB or sample MASIF's own master mix.
       * **Effects & Master Section:** Send busses for stereo chorus, delay, and reverb alongside master mixer and project management pages.
       * **Web Companion & Installer:** Companion WebMIDI browser interface to drop audio files, record live from microphone or line-in, trim/loop/fade slices, and sync pools directly to hardware flash.

24. **[Cut-A-Dor by Kid Bunka (kidbee85-beep)](https://github.com/kidbee85-beep/cut-a-dor-release) ([Browser Editor](https://cut-a-dor.sugarypixie10.chatgpt.site/dojo.html)):**
     * **License:** Open Source (GPL-3.0). Built upon the SLOOP groovebox lineage.
     * **Concept:** Dirty little beat dojo and gritty 8-track performance beat machine / sampler for the FM-1 (named as a tribute to the Matador of the crossfader).
     * **Features:** Dusty drum processing, funky pocket swing, eight recordable punch-in performance FX, and an interactive browser-based sound/pattern editor.

25. **[fm-dub by imijes](https://github.com/imijes/fm-dub) ([Web Emulator](https://imijes.github.io/fm-dub/)):**
     * **License:** Open Source (GPL-3.0). Built on SLOOP 2.5.
     * **Concept:** Dub sound-system preamp and performance dub station for the M-VAVE FM-1.
     * **Features:** Routes the master mix (and USB audio in) through band kills, a stepped high-pass filter, a dub siren generator, vintage tape echo, and a spring reverb tank, playable from 16 FX punch-in pads and a dedicated MIDI channel.

26. **[Synthesthetic by michaeljsmalley](https://github.com/michaeljsmalley/synthesthetic) ([Web Installer](https://michaeljsmalley.github.io/synthesthetic/) | [Web Emulator](https://michaeljsmalley.github.io/synthesthetic/play/)):**
     * **License:** Open Source (GPL-3.0). Built on SLOOP 2.7.1.
     * **Concept:** Visualizer groovebox that transmits live video of its on-screen visuals to a host computer over USB as a standard UVC webcam stream.
     * **Features:** Real-time audio-reactive graphics streamed directly into OBS, Zoom, or video production software without capture cards.

27. **[SPIRALFM1 by Spiralfractalplugins](https://github.com/Spiralfractalplugins/spiralfm1) ([Web Installer](https://spiralfractalplugins.github.io/spiralfm1/)):**
     * **License:** Open Source (GPL-3.0). Built on SLOOP and MYCELIUM.
     * **Concept:** Psytrance, Goa, forest, and hi-tech groovebox with 6 groove templates, 4 factory songs, and dedicated PSY FX performance pads.

28. **[shifl by schwartzworld](https://github.com/schwartzworld/shifl) ([Web Installer](https://shifl.netlify.app/webapp/installer/) | [Web Editor](https://shifl.netlify.app/webapp/editor/)):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Advanced live performance and composition sequencing firmware on the SLOOP architecture.

29. **[MerthSloop by merthsoft](https://github.com/merthsoft/sloop-fm1) ([Web Installer](https://merthsoft.github.io/sloop-fm1/)):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Enhanced SLOOP firmware featuring per-track wah and panning, note ties, custom chord progressions, refined typography, and an accompanying Android companion app.

30. **[Videodrome by Leeman1982](https://github.com/Leeman1982/sloop-fm1):**
     * **License:** Open Source (GPL-3.0). Built on SLOOP 2.8.
     * **Concept:** Vintage synthesizer tribute groovebox featuring 6 component-level models of classic synths: Minimoog Model D, Sequential Prophet-5, Roland Jupiter-8, Oberheim OB-X, Korg MS-20, and Yamaha CS-80.

31. **[LAUNCHPARTY by megagott](https://github.com/megagott/launchparty-fm1) ([Companion App](https://mandalars.org/mandalars/launchparty/)):**
     * **License:** Open Source (GPL-3.0). Sibling of MYCELIUM.
     * **Concept:** Interactive performance firmware designed for the Novation Launchpad Pro MK3, featuring playable synth sounds, interactive LED lightshows, and a browser companion.

#### 1.1.3. FoMni Family (Strumplate & Chord Instruments)

Suzuki Omnichord and Japanese Shigin accompaniment instruments featuring strumplate and chord-shaping workflows:

1. **[FoMni-1 by charlesvestal](https://github.com/charlesvestal/fm1-fomni) ([Web Installer](https://charlesvestal.github.io/fm1-fomni/)):**

* **License:** Open Source (GPL-3.0).
* **Polyphony:** Dual-voice shimmering strumplate harp + sustained chord and auto-accompaniment bass engine.
* **Concept:** Suzuki Omnichord-inspired chord harp firmware for the FM-1.
* **Features:** Strum chords across the white keys like a harp strumplate, select chord roots and types on the black keys, integrated rhythmic accompaniment and arpeggiator modes.

2. **[FuMi-1 by cartesive](https://github.com/cartesive/fumi-1) ([Web Installer & Emulator](https://cartesive.github.io/fumi-1/)):**
    * **License:** Open Source (GPL-3.0). Fork of FoMni.
    * **Concept:** Traditional Japanese Shigin accompaniment synthesizer inspired by Suikohsha's ST-50.
    * **Features:** Authentic Koto, Sho, Shakuhachi, and Taiko voices tuned to the historical ST-50 just intonation scale system.

3. **[CoralFlower by FicusFicusov](https://github.com/FicusFicusov/CoralFlower) ([Website & Web Player](https://ficusficusov.github.io/CoralFlower/) | [Releases](https://github.com/FicusFicusov/CoralFlower/releases)):**
    * **License:** Open Source (GPL-3.0).
    * **Polyphony:** Multi-voice chord engine with dedicated coupled bass voice.
    * **Concept:** Expressive chord machine inspired by the Torso Electronics T-1 / Orchid chord concepts, tailored specifically to the ergonomics of the FM-1.
    * **Features:** Single-finger chord generation with root and bass note coupling, 27 musical scales, built-in arpeggiator, looper, lush plate reverb, and an evolving pixel flower graphic that grows on the 240 × 240 screen as you play.

4. **[FM-1 Pocket Guitar by xMagElonx](https://github.com/xMagElonx/fm1-guitar) ([Web Emulator & Releases](https://fm1-tone-engine.app.workbuddy.host/guitar-fw/)):**
    * **License:** Open Source (GPL-3.0). Pure C99 guitar strumming and chord voicing layer for the FM-1.
    * **Polyphony:** Polyphonic acoustic/electric string modeling engine with per-string voice allocation and realistic micro-delay onset pick modeling (~65 ms strum spread).
    * **Concept:** Virtual acoustic and electric guitar performance instrument mapping the FM-1's 27 keys into an interactive fretboard and strumming surface.
    * **Features:**
      * **Strings & Chords Keybed Layout:** 11 black keys silently select chords while the 16 white keys act as individual strings for realistic arpeggios, fingerpicking, and automated down/up stroke strumming with velocity dynamics, chucking, and palm muting.
      * **On-Device Chord Library Editor:** Dedicated `ACTIONS -> CHORD LIBRARY` configuration page allowing users to customize and reassign all 11 black key chord slots to any root and chord quality with persistent saving across power cycles.
      * **Auto-Rhythm Looper:** Dedicated rhythm keys trigger full bars of genre strumming patterns (folk, pop, punk, reggae) that loop while held and seamlessly finish at bar boundaries upon release.
      * **5 Factory Timbres & Key Change:** Gapless on-the-fly timbre switching at measure boundaries and mid-song instant transposition.

5. **[Jambox FM-1 by RayDNoper](https://github.com/RayDNoper/fm1-fomnium):**
    * **License:** Open Source (GPL-3.0). Built upon FoMni-1.
    * **Concept:** Omnichord-style chord strumming performance firmware incorporating Yamaha DX7 voices, chord progression sequences, reggae accompaniment rhythms, and an algorithmic melody maker.

#### 1.1.4. Independent & Original Engine Firmwares

Firmwares featuring original sound engines, written-from-scratch architectures, or specialized controller frameworks:

1. **[baud girl Custom Firmware Mod](https://baudgirl.com/) ([MIDI & SysEx Guide](https://m-vave-fm1-midi-guide.up.railway.app/)):**

* **License:** Closed Source.
* **Polyphony:** 9–12 voices for FM presets with VA filter, and up to 8 voices for pure VA waveforms.
* **Features:** Comprehensive overhaul and reimagining of the stock firmware ergonomics and controls. Adds Virtual Analog (VA) synthesizer engines and a 64-step sequencer.
* **Documentation:** [FM-1 MIDI & SysEx Guide](https://m-vave-fm1-midi-guide.up.railway.app/) — exhaustive human-readable documentation of channels, SysEx structure, CC mappings for internal DSP effects, and clock synchronization.
* **Video Tutorial:** [Baud Girl FM-1+VA Comprehensive Tutorial (NatLife Sounds)](https://www.youtube.com/watch?v=jfuoEBIUsEE) — programming VA engines and the dot-matrix sequencer.

2. **[Groove OS](https://www.groove-os.com/) ([Web Emulator](https://www.groove-os.com/emu)):**

* **License:** Commercial / Proprietary ($29).
* **Concept:** Transforms the FM-1 into a standalone multitrack groovebox without needing any external equipment.
* **Features:** Up to 8 independent tracks (drums, bass, chords, leads) with independent loop lengths (1 to 8 bars) for evolving polyrhythmic structures, dual sound engine (native 6-op FM + Virtual Analog with ladder filter), up to 20 voices of polyphony (12 FM + 8 VA, max 6 for drums), 64-step sequencer with parameter locks (p-locks), live stage view, curated sound packs, and DX7 SysEx patch reception.

3. **[Bubba Machine by Erbubar23](https://github.com/Erbubar23/bubba-machine) ([Website](https://erbubar23.github.io/bubba-machine/) | [Web Emulator](https://erbubar23.github.io/bubba-machine/emulador.html) | [Manual](https://github.com/Erbubar23/bubba-machine/blob/main/docs/MANUAL.md)):**
    * **License:** Open Source (GPL-3.0-or-later). Written from scratch in C99.
    * **Polyphony:** Up to 20 voices of polyphony across 6 tracks (FM, VA, drums).
    * **Concept:** 6-track live performance groovebox firmware for the FM-1 with four gestures per button, dedicated HOME layer, and zero third-party audio dependencies (all factory kits and wavetables synthesized procedurally in C).
    * **Features:**
      * **6 Flexible Tracks:**
        * `T1` TR-Style Drum Machine: 16 instruments with independent polymeter track lengths, accent, ratchets, flam, parameter locks (P-Locks), fill-only steps, and live TR-style roll/erase while running.
        * `T2` Sampler 3.0: 8-slice loop engine reassembled bar-by-bar via algorithmic generator (`TU` programmed row vs `SUENA` played row), integrated sample recorder, take library, slice editor, and 3-band frequency waveform visualization (low/mid/high).
        * `T3` Wavetable Bass: Glide and wavetable synthesis.
        * `T4–T6` Assignable Tracks: Configurable as `SYNTH`, `MONO`, `KIT` (secondary drum machine), or `MIDI`. Per-track arpeggiator, looper, and dedicated musical scale.
      * **Polymeter & Independent Track Timing:** Each track features independent length (1–64 steps) and clock multipliers/dividers (×2 to ×1/4).
      * **Chord Grid:** 16 color-coded chords displaying scale degree and harmonic function.
      * **Live Performance & Safe Flash:** 4 chained scenes, song recording, auto-fills, 16 punch-in FX, track/instrument mutes, and crash-resilient flash saving (CRC, end commit, wear-leveling, and auto-save on stop).
    * **Status:** Firmware runs in desktop simulation and the in-browser WebAssembly emulator; hardware flasher/installer is in roadmap development.

4. **[zp12 by Sven Trogus (zvenson)](https://github.com/zvenson/zp12) ([Web Installer & Homepage](https://zp12.designburgapps.com/)):**
    * **License:** Open Source (GPL-3.0-only).
    * **Concept:** Authentic 1980s-style 12-bit sampling drum machine firmware for the FM-1.
    * **Features:**
      * **Lo-Fi 12-Bit Sound Engine:** 32 pads across 4 banks running at 26.04 kHz (or 27.5 kHz). Samples are pitched via pure playback rate skipping without interpolation for authentic gritty 80s aliasing and grain.
      * **8 Filtered Channels:** Independent channel playback where new hits cut previous ones. Channels 1–2 feature a resonant 4-pole low-pass filter closing with decay, channels 3–6 have fixed filters, and knobs act as channel faders.
      * **Performance & Sequencing:** 11 loops triggered on black keys, 4 chained songs, real-time recording with auto-correct and 16-step grid editing, classic MPC-style swing (50–71%), and 4 punch-in FX (beat repeat/roll, reverse, tape stop).
      * **Browser Sample Dropper:** In-browser tool to drop custom user WAVs onto pads and transmit them directly to flash over WebMIDI.

5. **[FiMba-1 by J. Adam Sowers (jadamsowers)](https://github.com/jadamsowers/fm1-fimba) ([Web Installer & Emulator](https://jadamsowers.github.io/fm1-fimba/)):**
    * **License:** Open Source (GPL-3.0-only).
    * **Concept:** Thumb piano / kalimba / mbira physical modeling synthesizer firmware for the FM-1.
    * **Features:**
      * **Physical Modeling Engine:** Detailed kalimba acoustic simulation running at 44.1 kHz, featuring modeled tines (material hardness, decay, tone, worn character, tuning, release), resonator bodies (box, gourd, board, buzzers, wah resonance), and built-in effects (space reverb/delay, lo-fi/tape color, chorus, filter, and granular cloud engine).
      * **Keyboard & Key Layouts:** Traditional kalimba *Tine* layout (lowest C4 tine in the center, alternating outwards across white keys) or chromatic *Keyboard* layout. Black keys configurable for thumb-roll chord accompaniment, sharps, or performance modifiers (mute, sound hole covering, freeze, octave shift).
      * **Built-in Sequencer/Arpeggiator:** Mbira pattern generator over chords and live playing.
      * **WebAssembly Browser Emulator:** Complete C sound engine and UI compiled to WebAssembly running in-browser with Web MIDI and preset saving.

6. **[Lunar Modulator by ip2k](https://github.com/ip2k/lunar-modulator):**

* **License:** Open Source (MIT).
* **Status:** Research / bench stage.
* **Features:** *Intergalactic Modulation Station* — alternative firmware based on Mutable Instruments synthesizer engines, a Movy-style sequencer, and an in-browser virtual FM-1 emulator/simulator.

7. **[AMB-1 by Charles Vestal](https://github.com/charlesvestal/fm1-amb) ([Web Installer & Emulator](https://charlesvestal.github.io/fm1-amb/) | [Manual](https://charlesvestal.github.io/fm1-amb/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Generative ambient synthesizer machine inspired by Brian Eno's *Music for Airports*.
    * **Features:** Self-generating playback immediately from power-on, unsynced tape loops of unequal lengths, gliding bass lines, and generative Euclidean percussion patterns.

8. **[CTL-1 by Charles Vestal](https://github.com/charlesvestal/fm1-ctl) ([Web Installer](https://charlesvestal.github.io/fm1-ctl/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Dedicated MIDI master controller firmware for the FM-1.
    * **Features:** Turns the FM-1's keys and knobs into a multi-channel USB/TRS MIDI controller while providing internal General MIDI sounds for standalone monitoring.

9. **[PurpleMonkey FM-1 by Quixotic7](https://github.com/Quixotic7/PurpleMonkeyFM1) ([Web Emulator](https://quixotic7.github.io/PurpleMonkeyFM1/emu/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Simplified toddler music instrument featuring a 5-note pentatonic scale, backing drum beats, and zero menus.

10. **[FM-1 B-Boy Edition by friendsmakenoise-prog](https://github.com/friendsmakenoise-prog/fm1-pocket-sampler):**
    * **License:** Open Source (No license specified in upstream repository).
    * **Concept:** Late-1990s hip-hop chop sampler firmware featuring 3 sample tracks and a dedicated FM bass/lead lane.

11. **[fm1-polyseq by NOVALENTI](https://github.com/NOVALENTI/fm1-polyseq):**
    * **License:** Open Source (No license file in repository; source code is publicly accessible).
    * **Concept:** Polyphonic 16-step sequencer and bare-metal hardware abstraction layer (HAL) written in strict C99 for the AC791N's pi32v2 CPU.

12. **[FM-106 by PattF](https://github.com/patttf/fm-106) ([Librarian & SysEx Editor](https://patttf.github.io/fm-106/Librarian.html)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Roland Juno-106 emulation firmware for the FM-1 based on an optimized port of the open-source KR-106 synthesizer engine.
    * **Features:**
      * **Full 6-Voice Polyphony:** Authentic Juno DCO sound generation hitting ~30% CPU load across both JieLi `pi32v2` cores.
      * **Oscilloscope & Real-Time Controls:** Split on-device display showing the live oscilloscope waveform alongside simultaneous filter, envelope, and oscillator parameters.
      * **Juno-106 SysEx Patch Compatibility:** Direct `.syx` patch import and management via companion web Librarian.
      * **Bank Management:** 4 banks (2 factory banks + 2 user banks) selectable via the `ALGORITHM` encoder, with on-device patch naming and saving.
      * **USB-C Audio:** Integrated class-compliant digital stereo audio output over USB-C.

13. **[ETCH by SikkenWorks](https://github.com/SikkenWorks/ETCH) ([Homepage & Web Installer](https://etch.sikkenworks.com/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** "Draw. Morph. Modulate." — waveform drawing and morphing synthesizer firmware.
    * **Features:** 8-voice polyphony, direct on-device single-cycle waveform drawing (Waves A, B, and modulating Wave C), real-time interpolation/morphing between drawn waves, wave library, motion recording, and arpeggiator with generative RIFF mode.

14. **[AMBII by MilkBoyG / JalopyMusic](https://github.com/JalopyMusic/fm1-milkboyg-ambii):**
    * **License:** Open Source (GPL-3.0). Built on Melodee and Felucca.
    * **Concept:** Alternative performance and recording interface firmware built on Melodee's real multi-engine C core.
    * **Features:** Four tracks with scoped pattern actions, drum ratchets, parameter automation graphs with undo, shared delay/reverb, and dedicated Galaxy / Dark Matter UI themes.
    * **Status:** In-browser prototype and development preview (no hardware release image yet).

15. **[MC-1 by dspaudio](https://github.com/dspaudio/mc-1) ([Web Hub & Online Player](https://dspaudio.github.io/mc-1-web/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** 4-track groovebox firmware inspired by Roland Linear Arithmetic (LA) synthesis (D-50) and MC-series grooveboxes (MC-101 / MC-303).
    * **Features:**
      * **LA Synthesis Sound Engine:** Combines PCM attack transients with synthesized sustaining partials, driving authentic late-80s digital/analog hybrid timbres.
      * **4 Tracks & Performance Sequencer:** Dedicated lanes for Drums, Bass, Chords, and Lead/Arp with step sequencing and live parameter modulation.
      * **Drum & Acid Generators:** Built-in synthesized TR-style rhythm voices and resonant 303 acid line generator.
      * **Dedicated Web Companion:** Web audio player and patch tool running at `dspaudio.github.io/mc-1-web`.

16. **[OberVave by Sven Trogus (zvenson)](https://github.com/zvenson/obervave) ([Webpage & Web Installer](https://fm1.designburgapps.com/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** 8-voice American analog polysynth emulation (Oberheim OB-Xa / OB-8 style, 1979–1984) for the M-VAVE FM-1.
    * **Features:**
      * **Classic 8-Voice Polysynth Architecture:** Dual oscillators per voice with sawtooth and pulse (PWM) waves, hard oscillator sync, cross-modulation, and white noise generator.
      * **Morphing 12/24 dB Resonant Filter:** Continuous morphing between 2-pole (12 dB/oct Oberheim SEM style) and 4-pole (24 dB/oct Curtis/CEM style) low-pass filter responses with dedicated envelope modulation.
      * **Vintage Drift & Unison:** Modeled analog voice circuit drift, polyphonic unison/detune stack, dual LFOs, and vintage chorus/delay spatial effects.
      * **On-Device Graphical Editing:** Real-time filter frequency curve rendering and envelope visualization on the 240 × 240 display.

17. **[MONK-1 by Charles Vestal](https://github.com/charlesvestal/fm1-monk) ([Web Emulator](https://charlesvestal.github.io/fm1-monk/emu/) | [Web Installer](https://charlesvestal.github.io/fm1-monk/install/) | [Manual](https://charlesvestal.github.io/fm1-monk/manual/) | [Releases](https://github.com/charlesvestal/fm1-monk/releases)):**
    * **License:** Open Source (GPL-3.0). Free of charge (donations suggested to savetibet.org).
    * **Concept:** Formant vocal synthesizer firmware turning the FM-1 into Jonathan Taylor's **MonkSynth** (homage to AudioNerdz's 2002 *Delay Lama* plug-in) with twelve singing characters (Jerry the monk, Philip the unicorn, Snider, etc.).
    * **Features:**
      * **12 Animated Singing Characters:** Each character sings with its own vocal tract size and voice; mouth animations follow vowels in real-time sprite frames on the color screen.
      * **Native Velocity & Pressure/Aftertouch:** Leverages the FM-1's stock capacitive keys without hardware modifications (via [Velo](https://github.com/charlesvestal/fm1-velocity) sensing algorithms) to control note loudness via strike velocity and vowel morphing/pitch bends via pressure aftertouch.
      * **Dedicated Vocal Controls:** Gliding legato mono voice, Choir/Unison stack (1–10 voices with detune and head size spread), vibrato rate/depth, echo delay, ADSR envelopes, and octave switching.
      * **USB MIDI & Accessibility:** Full USB-MIDI in/out with polyphonic aftertouch and vowel CC controls; integrates with the [FM-1 Screen Reader](https://charlesvestal.github.io/fm1-reader/) to speak aloud on-screen parameters and button actions for visually impaired users.

18. **[M-VAVE FM1 Open Firmware (m-vave/fm1_open)](https://github.com/m-vave/fm1_open) ([Releases / V10](https://github.com/m-vave/fm1_open/releases) | [Official Workbench](https://open.m-vave.com/fm1-workbench)):**
    * **License:** Open Source (GPL-3.0-only for application code; includes vendor binary libraries and third-party notices).
    * **Significance:** Official open-source release of the factory FM-1 firmware and SDK directly from the manufacturer (M-VAVE).
    * **Architecture & Features:**
      * **8 Tracks & 8 Sample Slots:** Full multitrack groovebox architecture with 8 audio/synth tracks, 8 sample slots, and 16 built-in demo presets/FX.
      * **Board Drivers & Audio HAL:** Direct hardware C source code for panel controls, 240 × 240 display, encoders, and audio engine rendering (`app/board/`, `app/audio_output.c`) supporting USB/Bluetooth mixing and USB recording.
      * **Complete Toolchain & WebAssembly Workbench:** Complete build scripts (`build.bat`) supporting both native firmware compilation via JieLi PI32v2 Clang 4.0.1 (`FM1_OFFICIAL_OPEN.fwsc`) and WebAssembly compilation via WASI SDK 27 for in-browser workbench simulation.

19. **[OPN-1 by putchdev](https://github.com/putchdev/opn-1) ([Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1x7edf7/mega_drive_genesis_sounds_on_the_fm1/)):**
    * **License:** Open Source.
    * **Concept:** Sega Mega Drive / Genesis sound chip recreation for the M-VAVE FM-1, accurately emulating both the Yamaha **YM2612** 6-channel FM synthesizer and the Texas Instruments **SN76489** 4-channel PSG (Programmable Sound Generator).
    * **Features:**
      * **VGM / VGZ File Player & Patch Converter:** Web companion app converts Sega Genesis/Mega Drive VGM and VGZ music rips into playable patch banks sent directly to the FM-1, or plays the tracks directly through the synthesizer hardware.
      * **Multitimbral Polyphony & Compatibility Modes:** Includes a 6-part monophonic Mega Drive accurate compatibility mode (mapped across individual MIDI channels, with special CH3 multitimbral mode) as well as a modern polyphonic mode where parts can be layered across identical or customized MIDI channels.
      * **Advanced Part Composition & Layering:** Dedicated configuration screen with per-part amplitude scaling, programmable delay stages (parts kick in after a timed delay), and note-off trigger toggles to easily layer transients, sustain bodies, and release tails combining YM2612 FM and PSG voices.
      * **MIDI & On-Device Playback:** Retains the last loaded patch set in memory for standalone play via capacitive keys, USB MIDI, and 3.5 mm TRS MIDI input.

20. **[CS-1 by twochannels](https://github.com/twochannels/CS-1) ([Website & Web Emulator](https://twochannels.github.io/CS-1/)):**
    * **License:** Open Source.
    * **Concept:** Yamaha CS-80 analog synthesizer emulation in spirit for the FM-1.
    * **Features:** 8 voices consisting of dual independent synthesizer channels, resonant high-pass and low-pass filters in series, ring modulator, expressive touch response modeling, and 22 factory tones faithfully recreated from the original 1977 CS-80 owner's manual.

21. **[Frodhes by Leonardo Mirabal](https://github.com/leonardoMirabal/frodhes) ([Website & Web Emulator](https://leonardomirabal.github.io/frodhes/) | [Releases](https://github.com/leonardoMirabal/frodhes/releases)):**
    * **License:** Open Source. Built on Dinghy.
    * **Concept:** Fender Rhodes electric piano physical modeling synthesizer without sample dependencies.
    * **Features:** 4 physical electric piano models (tines, pickups, hammer character), modeled analog signal chain featuring compressor, drive, stereo tremolo or auto-wah, phaser, chorus, stereo delay, and reverb. Includes tap tempo, MIDI clock sync, musical scale quantization, and patch presets.

22. **[Vector37 by genkigenki](https://github.com/genkigenki/Vector37) ([Web Installer](https://genkigenki.github.io/smk37/#fw-vector37) | [Web Simulator](https://genkigenki.github.io/smk37/vector37-sim/) | [Releases](https://github.com/genkigenki/Vector37/releases) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1x8eo32/vector37_update_more_sounds_a_smoother_screen_for/)):**
    * **License:** Open Source (GPL-3.0). Ported from the SMK-37 to FM-1.
    * **Concept:** Orbiting overtone vector synthesizer inspired by the Beetlecrab Vector.
    * **Features:**
      * **Orbiting Overtone Synthesis:** Four corners each hosting two overtone generators, with a central sun moving along an orbital trajectory and an orbiting moon determining crossfade and balance levels between generators, while encoders shape the active planet's synthesis characteristics.
      * **Factory & User Preset Banks:** 32 factory sounds organized into two 16-preset banks (warm strings, ambient pads, choir, vintage organ, electric piano, plucked harp, and an 8-sound drum kit), with user preset saving to a dedicated USER bank via the PATCH button.
      * **Performance & Hardware Features:** Configurable MIDI TRS OUT and USB IN routings via SETUP, plus 60 FPS display rendering optimizations.

23. **[HYP-1 by RedtailWorks](https://github.com/RustyPawz/fm1-HYP1) ([Website & Web Emulator](https://rustypawz.github.io/fm1-HYP1/)):**
    * **License:** Open Source. Forked from AMB-1 by Charles Vestal.
    * **Concept:** Hypnotic techno, acid, and drone groovebox firmware.
    * **Features:** Continuously breathing atmospheric pads, deep sub-bass drones, generative TB-303 acid line generator, and granular textures layered over a hands-on live drum step sequencer with instant bar pattern flipping and breakdown/build-up macro staging.

24. **[Tonitor by Nuno Zimas](https://github.com/nzimas/tonitor) ([Website](https://nzimas.github.io/tonitor/)):**
    * **License:** Open Source.
    * **Concept:** 6-track experimental ambient and live looping performance synthesizer.
    * **Features:** 3 distinct synthesis engines, algorithmic sound patch generator, free-length live audio loops supporting up to 10 overdubs per track, real-time granulator, multi-mode filters, and lush ambient reverb.

25. **[BEETLE by Joppe Sikken (SikkenWorks)](https://github.com/SikkenWorks/BEETLE) ([Website & Web Emulator](https://sikkenworks.github.io/BEETLE/) | [Releases](https://github.com/SikkenWorks/BEETLE/releases)):**
    * **License:** Open Source.
    * **Concept:** Classic vertical tracker firmware for the FM-1.
    * **Features:** Vertical top-to-bottom step tracking interface styled after vintage trackers, featuring dedicated columns for Note, Instrument, Chord, and Effect commands, bringing fast demoscene tracker composition workflows to the FM-1's hardware screen and buttons.

26. **[FOMAJAM by konsumer](https://github.com/konsumer/fomajam) ([Website & Web Emulator](https://konsumer.js.org/fomajam/) | [Releases](https://github.com/konsumer/fomajam/releases)):**
    * **License:** Open Source.
    * **Concept:** Classic step-grid vintage drum machine firmware for the FM-1.
    * **Features:** Faithfully synthesized drum engines inspired by iconic rhythm units: Roland TR-909, TR-808, TR-707, TR-606, Oberheim DMX, and more. Features per-voice machine assignment, step accents, pattern banks, and full browser WebAssembly simulation.

27. **[MIN-1 by Reytian](https://github.com/Reytian/fm1-min1) ([Website](https://reytian.github.io/fm1-min1/) | [Web Emulator](https://reytian.github.io/fm1-min1/emu/) | [Releases](https://github.com/Reytian/fm1-min1/releases)):**
    * **License:** Open Source.
    * **Concept:** Minimalist generative ensemble synthesizer firmware inspired by Philip Glass.
    * **Features:** Immediately begins performing intricate generative patterns upon power-up, allowing the player to seamlessly join the performance at any time. Features an EASY mode where every white key triggers harmonically fitting chords, 4 algorithmic models, and 20 built-in minimalist musical pieces.

28. **[Pocket GammaWave by ShadowTune (GammaWave Audio)](https://github.com/fvalente/GammaWave-FM1) ([Homepage](https://gammawaveaudio.com/) | [Web Simulator](https://fvalente.github.io/GammaWave-FM1/) | [Web Editor](https://fvalente.github.io/GammaWave-FM1/webapp/editor/?mock=1) | [Releases](https://github.com/fvalente/GammaWave-FM1/releases)):**
    * **License:** Open Source.
    * **Concept:** Companion pocket groovebox and industrial synthesizer for the GammaWave desktop synthesizer.
    * **Features:** Four industrial distortion modes, formant vowel and screaming resonant filters, real-time FFT audio spectrogram visualization, 4-track tape deck style interface, and an automated algorithmic song generator spanning 49 musical genres (including modern Trap, Drill, and industrial soundscapes).

29. **[TERKINSTEIN by TerkWerX](https://github.com/TerkWerX/FM1-TERKINSTEIN-Firmware) ([Releases](https://github.com/TerkWerX/FM1-TERKINSTEIN-Firmware/releases)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Dark performance synth and 4-track groovebox with a cybernetic reactive UI.
    * **Features:** 64 curated sounds, 6-operator FM engine, metallic distortion modes, fully synthesized drum kits and pads, reactive neon purple-and-green display animations, and 64-step tracks across 4 pattern banks.

30. **[Niagara Drift by Evan Yerburgh](https://github.com/evanyerburgh/niagara-drift) ([Releases](https://github.com/evanyerburgh/niagara-drift/releases)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Immersive dual-drone synthesizer with slow algorithmic parameter drift.
    * **Features:** Two continuously sounding drones with partner and sub-oscillators, resonant multi-mode filters, dual-waveform LFO, rhythmic swell generator, stereo delay and reverb, 16 pre-programmed sound scenes, and slow continuous automatic drift.

31. **[MNM-1 by sirpearson](https://github.com/sirpearson/fm-1-monomachine):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Six-track monophonic groovebox inspired by the workflow of the legendary Elektron Monomachine.
    * **Features:** One dedicated drum kit track and five monophonic synth tracks each hosting independent synthesis machines, a 64-step sequencer with parameter locks (p-locks) per step, three assignable LFOs per track, and per-track stereo delay lines.

32. **[SIDOU by Denis Sablic (dsablic)](https://github.com/dsablic/sidou) ([Releases](https://github.com/dsablic/sidou/releases)):**
    * **License:** Open Source (GPL-3.0-only for the firmware image; SIDOU's own code GPL-3.0-or-later).
    * **Concept:** A C64 SID music machine: two emulated SID chips (6581 and 8580) with a GoatTracker 2 compatible tracker.
    * **Features:** Tracker and step sequencer with parameter locks, whose songs are GoatTracker 2 `.sng` files; a live instrument playable over a song on the other chip; the chip's character (age, worn DACs, the 6581's thump, filter bleed) and CHIP SPREAD stereo; chord arpeggios; MIDI clock, CC/NRPN and MIDI learn; songs over SysEx on USB. `.sid` file playback is planned.

33. **[TripDeck by anonymousacademe](https://github.com/anonymousacademe/FM-1-TripDeck):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Psychedelic synthesizer where every screen page is an interactive full-screen animated graphic driven by the four rotary encoders.
    * **Features:** Sitar, evolving ambient pad, pipe organ, and bell FM voices; spiral echo delay, shimmer reverb, formant vowel filter, musical scale lock, integrated arpeggiator, and step sequencer.

34. **[Evander's Music Box by Mike Tsakiroglou (MikeTsak)](https://github.com/MikeTsak/Evanders-Music-Box--FM-1-LARP-firmware) ([Releases](https://github.com/MikeTsak/Evanders-Music-Box--FM-1-LARP-firmware/releases)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Roleplaying-themed firmware transforming the FM-1 into an elven bard's enchanted music box for tabletop and LARP gaming sessions.
    * **Features:** Four-track medieval workshop with a 64-step sequencer, plus an Encounter mode offering 16 instant atmospheric scene soundtracks for live games. Features custom fantasy UI and boot artwork.

35. **[LOF-1 by RedtailWorks](https://github.com/RustyPawz/fm1-HYP1) ([Website & Web Installer](https://rustypawz.github.io/fm1-HYP1/lof/) | [Web Emulator](https://rustypawz.github.io/fm1-HYP1/lof/emu/) | [Manual](https://rustypawz.github.io/fm1-HYP1/lof/manual/) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1x7pbwa/lof1_a_generative_lofi_ambiance_machine_with/)):**
    * **License:** Open Source (GPL-3.0). Built on AMB-1 (Charles Vestal) and Felucca.
    * **Concept:** Generative lo-fi ambience machine and tired jazz band groovebox: you play the lead on the capacitive keys, and an intelligent backing band listens to which chord your notes imply, dynamically following your performance with comp, bass, and drums.
    * **Features:**
      * **Interactive Lead & Tired Jazz Band:** 20 acoustic and FM instruments (Rhodes, Wurli, FM piano, upright pianos, vibes, marimba, kalimba, tenor sax, muted trumpet, clarinet, flute, ocarina, harp, music box).
      * **Comp, Bass & Call-and-Response:** Automatic chord re-voicing on changes (held, stabs, offbeats, arpeggios), walking/dub bass, and an "Answer" engine that dynamically echoes phrases or invents counter-melodies when you pause.
      * **Daydream Mode:** If left untouched, an algorithmic ghost takes over the lead melodies with configurable phrase density until any key is pressed to take back control.
      * **16-Step Drum Sequencer & Drift:** 8 drum lanes across Dusty (samples) and Tape (synthesized) kits with groove swing and automatic pattern drift.
      * **Dust Signal Chain & Old TV Display:** Authentic vinyl crackle, cassette hiss, reel-to-reel saturation, and radio static with wow/flutter and granular smear; vintage CRT scanlines with 5 color themes (Lamp, Matcha, Sakura, Midnight, Sepia).
      * **Live Performance FX Keys:** Hardware keys map to tape stop, backspin, record skip, half-time, stutter, mufflers, and throws.

36. **[ECO-1 by RedtailWorks](https://github.com/RustyPawz/fm1-HYP1/tree/main/eco1) ([Website & Web Installer](https://rustypawz.github.io/fm1-HYP1/eco/) | [Web Emulator](https://rustypawz.github.io/fm1-HYP1/eco/emu/) | [Manual](https://rustypawz.github.io/fm1-HYP1/eco/manual/)):**
    * **License:** Open Source (GPL-3.0). Fork of AMB-1 by Charles Vestal (built on Felucca by Hügelton Instruments). Experimental: tested in the simulator and browser emulator, not yet on a real FM-1.
    * **Concept:** Generative botanical ambient synthesizer turning the FM-1 into an algorithmic musical plant.
    * **Features:**
      * **Leaves & Stem:** Three virtual leaves each accumulate charge from light and water and fire a note when full (8 FM voices: Glass, Wood, Pluck, Chime, Reed, Flute, Swell, Kalimba); firings run down the stem and the other leaves answer. A stem drone underneath (Hum, Organ, Reed, Choir) on the root and a chosen interval.
      * **Sky & Weather:** Day/night cycle (30 s to 30 min) or a fixed Night or Day sky; night mellows the plant rather than silencing it. Rain showers with a synthesized rain track, wind that shakes the leaves, sings a rising whistle and opens the reverb; drought wilts the plant.
      * **Eight Plants:** Fern, Orchid, Moss, Cactus, Willow, Lotus, Ivy and Bamboo, each drawn in its own scene (forest floor, windowsill, desert, pond...) and each reacting to the weather in its own way.
      * **DAW Integration:** MIDI clock in (the day counts in bars, leaves can fire on a 1/4 to 1/16 grid), MIDI out with each leaf and the stem on its own channel plus the plant's signals (charge, water, soil, light, rain, wind) as CCs; the browser emulator outputs eight channels, each voice apart.

37. **[P6 by Jonbenderr](https://github.com/Jonbenderr/fm1-p6) ([Web Installer](https://jonbenderr.github.io/fm1-p6/install/) | [Web Emulator](https://jonbenderr.github.io/fm1-p6/emu/) | [Releases](https://github.com/Jonbenderr/fm1-p6/releases)):**
    * **License:** Open Source (GPL-3.0). Built on Dinghy by Charles Vestal.
    * **Concept:** Korg Polysix-inspired 6-voice analog polysynthesizer firmware for the M-VAVE FM-1.
    * **Features:**
      * **6-Voice Analog Architecture:** 6 voices of polyphony, 1 VCO per voice with sub-oscillator (1 or 2 octaves down), pulse width modulation (PWM), and white noise generator.
      * **Resonant 4-Pole VCF & Envelopes:** Modeled SSM2044 24 dB/oct resonant low-pass filter with keyboard tracking and dedicated ADSR envelope generator.
      * **Modulation & Vintage BBD Effects:** Modulation Generator (MG/LFO) with routing to VCO, VCF, and VCA; authentic bucket-brigade style analog Chorus, Phaser, and Ensemble spatial effects.
      * **Key & Voicing Modes:** Polyphonic, Unison (all 6 voices stacked with detune), and Chord Memory modes, plus Key Hold latching and an integrated arpeggiator with up/down/random patterns and sync.
      * **Preset Program Storage:** 32 preset program memories organized as 4 banks of 8 sounds (A-1 through D-8).

38. **[Speak37 by genkigenki](https://github.com/genkigenki/Speak37) ([Web Installer](https://genkigenki.github.io/smk37/#fw-speak37) | [Releases](https://github.com/genkigenki/Speak37/releases) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1x89f3y/speak37_a_free_talking_synth_firmware_for_the/)):**
    * **License:** Open Source (GPL-3.0). Compatible with both M-VAVE SMK-37 and FM-1.
    * **Concept:** Talking speech synthesizer and singing voice firmware for the FM-1: every keypress speaks or sings the next syllable or word of a sentence at that note's pitch, singing in multi-voice harmony when chords are played.
    * **Features:**
      * **Singing Synthesizer Engine:** 9 distinct speech voices (Classic Chip Robot, Giant, Whisper, Chipmunk, Alien, and more); chords sing in full musical harmony.
      * **Rhythm Section & Fixed-Point 808:** Built-in fixed-point Roland TR-808 rhythm generator with 16 groove styles; pressing the PLAY button automatically speaks words on the beat over drum grooves.
      * **Beatbox Drum Kit:** White and black keys double as vocal beatbox triggers (phonetic kicks, snares, hats, and vocal scratches).
      * **MOPE Mode:** An interactive sullen robot mode that actively monitors your playing, responds with melancholic spoken remarks, and plays sad algorithmic interludes when ignored.

39. **[FMEL-1 (MEL) by Antonio Altea](https://github.com/AntonioAltea/fmel-1) ([Web Installer](https://antonioaltea.github.io/fmel-1/install/) | [Web Emulator](https://antonioaltea.github.io/fmel-1/) | [Releases](https://github.com/AntonioAltea/fmel-1/releases)):**
    * **License:** Open Source (GPL-3.0). Built on Dinghy by Charles Vestal (SLOOP / Felucca lineage).
    * **Concept:** Mellotron M400 tape keyboard instrument for the FM-1 with authentic tape mechanics, dual-tape blending, and vintage analog signal processing.
    * **Features:**
      * **Four Classic M400S Tapes:** Includes authentic tape recordings of Flute (Strawberry Fields Forever), 8-Voice Choir, Cello, and Vibraphone (digitized by Bernie Kornowicz / Taijiguy).
      * **Tape Blending & Mechanics:** Seamless continuous blending between Tape A and Tape B across the keyboard, complete with authentic 8-second tape run-out physics, key release mechanical click, and half-speed tape motor playback (octave drop).
      * **LOFI Tape Aging Section:** Real-time tape degradation processing featuring wow, flutter, tape hiss, age wear, dropouts, mechanical drift, drive, and lo-fi bitcrush.
      * **Vintage FX & Sequencer:** Vibrato, Leslie rotary speaker, tape echo delay, spring/hall reverb, 2-band EQ, note HOLD latch, integrated arpeggiator, and 16-step pattern sequencer.
      * **Custom Display Art:** Features custom animated tape transport graphics and screen artwork drawn by Javi.

40. **[GRAV-1 by RedtailWorks](https://github.com/RustyPawz/fm1-HYP1/tree/main/grav1) ([Website & Web Installer](https://rustypawz.github.io/fm1-HYP1/grav/) | [Web Emulator](https://rustypawz.github.io/fm1-HYP1/grav/emu/) | [Manual](https://rustypawz.github.io/fm1-HYP1/grav/manual/)):**
    * **License:** Open Source (GPL-3.0). Built on AMB-1 by Charles Vestal and Felucca by Hügelton Instruments. Experimental: tested in the simulator and browser emulator, not yet on a real FM-1.
    * **Concept:** Generative dark, spacey ambient firmware that turns the FM-1 into a small solar system: a star and its planets play the music.
    * **Features:**
      * **Star & Planets:** A central star hissing and roaring in eight colours of noise, with up to six orbiting planets, each a voice (16 instruments) playing a short phrase around its orbit, warm and dry near the star, cold and wet far out.
      * **Gravity & Orbits:** A drum sequencer sets each planet's year (and, by Kepler's law, how close it orbits); larger planets swell smaller ones as they pass, and dust clouds, asteroids and comets drift through.
      * **Ten Systems:** Ten preset solar systems, an eclipse hold, and an orbit view that takes over the screen when left untouched.
      * **DAW Integration:** MIDI clock in drives the steps and the orbits; MIDI out sends each planet's notes on its own channel, the drums on another, and the system's signals as CCs; the browser emulator outputs eight channels, each voice apart.

41. **[MD-One by d0pe1](https://github.com/d0pe1/md-one):**
    * **License:** Open Source (GPL-3.0-only for firmware, inherited from Dinghy; standalone `dsp/` library is MIT).
    * **Concept:** Mutable Instruments-derived drone machine ("Mutable Droner") for the M-VAVE FM-1.
    * **Features:**
      * **Braids Oscillator Port:** Full port of all 48 synthesis models from Mutable Instruments Braids compiled for the JieLi `pi32v2` CPU core at 44.1 kHz.
      * **Drone Synthesis Engine:** Four always-on Braids voices with detune, tuned comb filters, slow spectral evolution, drift, and key latching to hold notes in and out.
      * **Lightweight DSP Footprint:** Highly optimized fixed-point integer DSP engine consuming ~14.5% of the AC791N audio processing budget.
      * **DAW Integration:** Designed to deliver multichannel drone soundscapes into a DAW over USB audio.
    * **Status & Installation:** Firmware core verified in desktop testing harnesses and the `fm1-emu` emulator; physical hardware release in active development.

42. **[Erik37 by genkigenki](https://github.com/genkigenki/erik37) ([Web Installer](https://genkigenki.github.io/smk37/#fw-erik37) | [Video Demo](https://youtu.be/5yUCB1-OJNE) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1x8qggc/erik37_a_grand_piano_firmware_for_the_mvave_smk37/)):**
    * **License:** Open Source (MPL-2.0; piano samples are Salamander Grand Piano V3 by Alexander Holm, CC BY 3.0). Built upon `fm1-base` (Charles Vestal) and `felucca-bsp` (Leo Kuroshita).
    * **Concept:** Acoustic concert grand piano firmware featuring dedicated dual-target builds for both the M-VAVE FM-1 (`erik37-fm1.fwsc`) and SMK-37 (Pro, Elite, MKE-P37).
    * **Sampling & Sound Engine:**
      * **Multi-Velocity Sampling:** Yamaha C5 concert grand samples (Salamander Grand Piano V3) with 18 key zones in 3 velocity layers, crossfaded in the attack and looped (~380 KB block-ADPCM at 22.05–32 kHz).
      * **20-Voice Polyphony & Key Decay:** Key-by-key decay modeled from real acoustic recordings (faster in the treble, undamped top keys), dynamic velocity-linked brightness, and mechanical damper noise on key release.
      * **Sympathetic Resonance & Three Pedals:** True undamped string resonance ringing along with held notes; sustain (with continuous half-pedal support), sostenuto, and una corda (soft pedal with adjustable tone depth).
      * **Four Tones & Four Rooms:** Tonal profiles (CONCERT, STUDIO, VINTAGE, JAZZ) paired with an 8-line Feedback Delay Network (FDN) reverb simulating dry, chamber, hall, and church acoustics with room size and stereo width controls.
    * **FM-1 Panel Integration:** Mapped for the FM-1's 27 keys (F3–G5 with velocity), Knobs 1–4 for page parameters, SELECT for page navigation, ALGORITHM for piano tones, PRESETS for 12 user preset slots, and REC/ENV/SEL acting as sustain, sostenuto, and una corda pedals.

43. **[LOOM-8 by Charles Vestal](https://github.com/charlesvestal/fm1-loom) ([Website & Web Installer](https://charlesvestal.github.io/fm1-loom/) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1xamjef/loom8_sequencing_groovebox_for_the_mvave_fm1/)):**
     * **License:** Open Source (GPL-3.0). Built on Dinghy and Felucca.
     * **Concept:** Teenage Engineering OP-XY-inspired 8-track pocket groovebox firmware for the FM-1 with dedicated color-coded tracks, generative sequencing tricks, and rich sound engines.
     * **Features:**
       * **8 Color-Coded Instrument Tracks:** Up to 8 patterns per track, up to 64 steps, 16 mute scenes, and a dedicated Conductor track for song progression, leading notes, and in-key transposition.
       * **8 Sound Engines & Drum Kit:** Includes 6 synth engines (`knit` VA supersaw/unison, `rayon` 2-op FM, `jacquard` wavetable, `bellows` rotary organ, `cane` physical model pluck/bow/reed/flute/bell/drum, `voile` formant morphing voice), a sample player with loop/reverse, a break slicer, and an 11-piece drum kit.
       * **Advanced Sequencing Tools:** Conductor track, 14 step Tricks (velocity ramps, ratchets, probability, skips, A:B conditional cycles), Weave (interleaving two patterns bar-by-bar or step-by-step), and live parameter locks (motion recording).
       * **Live Performance Throws & Players:** 12 momentary punch-in FX Throws (tape stop, beat repeat, high-pass sweep, reverse, stutters) plus dedicated note players (Arp, Strum, Hold).
       * **Effects & Master Bus:** 2 send FX (including PSXVerb PlayStation-style vintage reverb and delay), master EQ, compressor, and ducking pump. Over 85 factory presets, 16 user slots, and custom sample uploads (~200 KB, up to 32 samples).

44. **[Hersen MPC (庄赫森) by HackSnake](https://store.grandtree.art/HersenMPC/) ([FM-1 Web Manager](https://store.grandtree.art/FM1_Manager/) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1xao5xt/hacksnake%E5%BA%84%E8%B5%AB%E6%A3%AE/)):**
     * **License:** Closed Source / Freeware.
     * **Concept:** 12-bit vintage MPC-style sampling drum machine and groovebox firmware for the M-VAVE FM-1.
     * **Features:**
       * **Vintage MPC Sampling Architecture:** Bank A and Bank B (16 pads each, 32 playable channels), 64 sample slots, and 8-bit/12-bit vintage sampler character (44.1 kHz / 22.05 kHz, providing up to ~37.3 seconds of total sample flash memory across 3 blocks).
       * **Sample Chopping & Editing:** Onboard waveform trim, slice, and auto-chop (up to 16 slices per sample) with pitch tuning, envelope, and reverse playback.
       * **Sequencer & Song Mode:** MPC-style step sequencer with swing, 32 programmable sequences, and seamless song chaining.
       * **Per-Sequence Effects & Live Mixer:** Independent sequence filter, chorus, delay, and reverb; live pad mixer accessible instantly by holding SEL.
       * **Instant Boot Preview:** On-boot instant beat playback for quick previewing without loading menus.

45. **[GRAN by Hersen Zhuang (庄赫森)](https://store.grandtree.art/GRAN/) ([Sample Manager](https://store.grandtree.art/FM1_Manager/gran/samples.html) | [FM-1 Manager](https://store.grandtree.art/FM1_Manager/#fw-gran)):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Dedicated 8-voice granular synthesizer firmware for the M-VAVE FM-1.
     * **Features:** Classic, Loop, and Cloud grain synthesis models; 8 voices of polyphony, 12 factory ROM waveforms (~1 s each), 24 system presets, up to 1.48 s live sample playback buffer with browser-based sample uploading over USB WebMIDI, and a stylized cyan/magenta/sunset colorway.

46. **[SID-1 by putchdev](https://github.com/putchdev/sid-1):**
     * **License:** Open Source.
     * **Concept:** Dual Commodore 64 SID chip (MOS 6581 / 8580) synthesizer firmware for the FM-1.
     * **Features:** Authentic software modeling of two distinct SID chips providing 6 independent voices (3 voices per chip), selectable 6581 and 8580 filter non-linearities, and playable directly from capacitive keys or USB-MIDI.

47. **[Shine On by Sven Trogus (zvenson)](https://github.com/zvenson/shineon):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** 1970s analog string ensemble synthesizer (Solina / Eminent style) with top-octave divider voicing.
     * **Features:** Fully polyphonic divider organ architecture with locked-phase footages (16', 8', 4' saw and 8' pulse), six bus-level fixed formant filters (Contra Bass, Cello, Viola, Violin, Trumpet, Horn), analog-modeled triple-delay ensemble chorus, phaser, tape delay, and plate reverb.

48. **[B1 Drawbar Organ by Joppe Sikken (SikkenWorks)](https://github.com/SikkenWorks/B1-Drawbar-Organ):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Authentic tonewheel drawbar organ firmware for the FM-1.
     * **Features:** 9 virtual drawbars built from tonewheel harmonic partials (not sample playback), modeled Leslie rotating speaker, harmonic percussion (2nd/3rd), scanner vibrato/chorus, and an experimental supersaw auxiliary engine.

49. **[fm1-gator by npi3pak](https://github.com/npi3pak/fm1-gator):**
     * **License:** Open Source (MIT engine core).
     * **Concept:** Monophonic macro-oscillator synth engine based on the open-source DSP of **Mutable Instruments Plaits**.
     * **Features:** 24 distinct synthesis models across three banks (virtual analog, waveshaping, 2-op/6-op FM, formants, harmonic additive, wavetables, chords, speech, particles, noise, physical string/modal resonators, and drums) with control voltages reimagined as an interactive on-screen modulation matrix.

50. **[Mutable Dreams by Christoph Link (Kid Bunka / kidbee85-beep)](https://github.com/kidbee85-beep/mutable-dreams) ([1.1 Release](https://github.com/kidbee85-beep/mutable-dreams/releases/tag/v1.1)):**
     * **License:** Open Source (GPL-3.0-only combined distribution; original MIT/MPL-2.0 and other component notices retained).
     * **Concept:** Six freely assignable tracks for generative ambient, rhythms and basslines, combining selected Mutable Instruments algorithms with custom engines.
     * **Features:** Version 1.1 has 12 engines, 224 tones, 76 Biomes + Blank, 16 named User Biomes and 64 User Sound slots; editable 16-step phrases, a global mixer and shared granular/delay/room effects.
     * **Browser & Source:** [Playable instrument and bidirectional live editor](https://mutable-dreams.sugarypixie10.chatgpt.site/), JSON live-patch transfer, full saved-bank backup/restore, illustrated English guide and directly browsable source.

51. **[Prysm by Nicholas Pratt](https://github.com/NicholasPratt/Prysm):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Four-voice wavetable FM synthesizer firmware for the M-VAVE FM-1.
     * **Features:** 2 oscillators per voice where each oscillator is a 3-stage wavetable operator (Mod 2, Mod 1, Carrier) capable of FM, ring modulation, or hybrid blending; overdrive-enabled resonant filter, LFO, looping modulation envelope, chorus, delay, and plate reverb.

52. **[fm_lab by jsmith13](https://github.com/jsmith13/fm_lab):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Dedicated educational 6-operator FM synthesizer built for learning Yamaha DX7 frequency modulation hands-on.
     * **Features:** Strips away grooveboxes and drum machines to expose pure DX7 architecture: every parameter is instantly accessible under knobs and visible on screen with real-time feedback while audio is sounding.

53. **[Bytemania by llozd](https://github.com/llozd/bytemania):**
     * **License:** Open Source (GPL-3.0). Built upon Dinghy.
     * **Concept:** Bytebeat algorithmic synthesizer firmware running music generated entirely from one-line mathematical equations.
     * **Features:** Computes 8-bit audio formulas where played keys set the increment rate $t$ (middle C = 8 kHz classic rate) and the four rotary knobs dynamically modulate formula coefficients live during performance.

54. **[Selva1 by deabrewcontato-code](https://github.com/deabrewcontato-code/Selva1):**
     * **License:** Open Source.
     * **Concept:** Minimalist portable C synthesis engine inspired by São Paulo's urban soundscapes.
     * **Features:** 3 oscillators (A, B, C) configurable for analog waveforms, FM modulation, or noise with up to 8 overtone harmonics, detune, stereo width, and pan controls.

55. **[ZEN-1 by aceyprime](https://github.com/aceyprime/zen-1) ([Web Emulator](https://aceyprime.github.io/zen-1/emu/)):**
     * **License:** Open Source.
     * **Concept:** Generative visual ambient firmware turning the FM-1 into an animated kinetic window.
     * **Features:** Falling sakura cherry blossom petals on running water, swimming koi fish, and fireflies dancing under moonlight — where each on-screen physical motion directly generates musical notes and harmonics; knobs sculpt acoustic soundscapes and spatial depth.

56. **[AMB-1 Evolved by kidbee85-beep](https://github.com/kidbee85-beep/AMB-1-Evolved):**
     * **License:** Open Source (GPL-3.0-only). Built upon AMB-1 by Charles Vestal.
     * **Concept:** Ambient generative synthesizer expanding the AMB-1 platform.
     * **Features:** 64 presets, 32 acoustic visual themes, and 20 musical scales with Bunkai-Wolf-A1 algorithmic design.

57. **[386 DX FM1 KaraokeBot by seajaysec](https://seajaysec.github.io/386-DX-FM1-KaraokeBot/) ([Web Emulator](https://386dx.linecross.ing/emu/)):**
     * **License:** Open Source.
     * **Concept:** Cyberpunk tribute to Russian media artist Alexei Shulgin and his legendary cyber-band *386 DX*.
     * **Features:** Computerized synthetic voice singing classic rock and pop songs over raw MIDI accompaniment, bringing early cyberpunk street performance aesthetics to the FM-1 screen and speaker.

58. **[fm1-gm by jartificer](https://github.com/jartificer/fm1-gm) ([Web Demo](https://jartificer.github.io/fm1-gm/)):**
     * **License:** Open Source.
     * **Concept:** 16-channel General MIDI (GM1) sound module and playback firmware.
     * **Features:** Complete GM1 instrument set (128 melodic programs) plus General MIDI drum kit (notes 35–81) on channel 10, responding across all 16 MIDI channels with independent volume, pan, reverb, transpose, and velocity.

59. **[BOP-1 by devrvega](https://github.com/devrvega/BOP-1) ([Web Emulator](https://devrvega.github.io/BOP-1/emu/)):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Musical exploration firmware that grows with the player: from an accessible toddler sound companion (ages 3+) to beats and loops (ages 6–8), up to full subtractive synthesis (ages 9+).

60. **[kidboy by WillCMcC](https://github.com/WillCMcC/kidboy-firmware):**
     * **License:** Open Source.
     * **Concept:** Toddler-friendly toy synthesizer firmware with zero risk of misconfiguration.
     * **Features:** Four interactive activities on the preset wheel: nursery rhyme songs across all 27 keys, alphabet cards with spoken letters A–Z and ABC song, color notes, and simple animal soundboards.

61. **[Carnac OS by OrbVorgis (Owen Kirby)](https://github.com/OwenKirby/carnac-os) ([Web Installer](https://owenkirby.github.io/carnac-os/install/)):**
     * **License:** Open Source (GPL-3.0). Dual-core C architecture.
     * **Concept:** Polyphonic wavetable synthesizer and performance firmware inspired by Carnac's standing stones and forgotten Neolithic rituals.
     * **Features:** 15 morphing wavetable banks, 7 voice architectures (including STRIKE with 20 synthesized Neolithic attack sounds), 4 filter types, 3 modulation slots per patch, spring/tomb/tank reverbs, tape & BBD delays, MAQ 16/3-style step sequencer, chord sequencer, and two-layer splits/zones running across both `pi32v2` cores.

62. **[DIRGE by sinscum](https://sinscum.github.io/DIRGE/):**
     * **License:** Open Source. Built on Felucca HAL.
     * **Concept:** Darksynth, industrial noise, and drone performance firmware for the FM-1.
     * **Features:** Raw industrial drone synthesis engines, interactive noise layers, algorithm selection, built-in tape delay and drive effects, and complete MIDI CC control mapping (CC 20–27).

63. **[Monohull by markterm](https://github.com/markterm/monohull) ([Releases](https://github.com/markterm/monohull/releases)):**
     * **License:** Open Source (GPL-3.0). C99 DSP core on Felucca HAL.
     * **Concept:** Uncompromising high-fidelity analogue-modeled monophonic synthesizer firmware for the FM-1.
     * **Features:**
       * **Zero-Compromise Monophonic Voice:** Devotes the entire 240 MHz `pi32v2` single-core/dual-core budget to a single voice with no per-voice compromises; any leftover cycles dynamically scheduled for unison, chorus, delay, and reverb.
       * **Analogue-Modeled Oscillators:** Saw, pulse (PWM), triangle, and sine morphing oscillators with BLEP/BLAMP bandlimiting correction, hard sync, through-zero FM (TZFM), and dedicated sub-oscillator.
       * **5 Classic Filter Topologies:** Transistor ladder (Moog-style with TPT Newton non-linear solve), diode ladder (TB-303), OTA cascade (Roland IR3109), Sallen-Key (Korg Korg-35 via Surge model), and 12 dB state-variable filter (SVF).
       * **Dual Engine Modes:** "High" mode (oversampled oscillators, non-linear filter equations solved per-sample, antialiased drive) and "Efficient" mode (optimized solvers for maximum battery life and headroom).

64. **[MONO2K by Iñigo Hernández (InigoHernandez)](https://github.com/InigoHernandez/mono2k):**
     * **License:** Open Source (GPL-3.0). Written in C99.
     * **Concept:** Elektron Monomachine-inspired synthesizer and groovebox firmware for the M-VAVE FM-1.
     * **Features:**
       * **Six Mono Machines:** Six independent tracks, each hosting a selectable machine (SuperSaw, FM+, SID/Chiptune, Dynamic Noise, Vocal Formant, and Percussion).
       * **Deep Sequencing:** 64-step sequencer with parameter locks (p-locks), trig conditions (probability, A:B fills), microtiming, and ratchets.
       * **Lofi Bus & Effects:** Master degradation bus introducing gritty sample reduction, drive, filtered digital delay, and plate reverb.
       * **Retro-Futuristic Visuals:** Custom 1-bit dithered typography, Swiss grid layout, and PS1-era CRT aesthetics on the 240 × 240 display.

65. **[Bigorna by Nuno Zimas (nzimas)](https://github.com/nzimas/bigorna):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Industrial, power noise, and IDM rhythmic groovebox firmware inspired by the Elektron Digitone II.
     * **Features:**
       * **6-Track Industrial Sound Architecture:** Multi-operator aggressive FM and wavetable machines designed specifically for crushing industrial rhythms, metallic clangs, rhythmic noise, and distorted percussion.
       * **Non-Linear Modulation:** Chaos generators, multi-rate LFOs cross-modulating operator ratios, overdrive clipper, and resonant band-pass filtering.
       * **Polymetric Grid:** Per-track polymetric sequence lengths (1–64 steps), probability trigs, and parameter automation.

66. **[FMER by Nacsez](https://github.com/Nacsez/FMER):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** 6-operator FM and Virtual Analog 4-track performance firmware with dedicated desktop companion software.
     * **Features:**
       * **Dual Hybrid Engine:** Combines full 6-operator DX7-compatible FM synthesis with an authentic Virtual Analog engine across four independent performance tracks.
       * **Arranger & Pattern Sequencer:** Step sequencing, live motion recording, song arrangement, and real-time performance macros.
       * **FMER Companion Tool:** Desktop companion application for managing instruments, patch banks, pattern projects, and backups locally, featuring an illustrated offline handbook and guided USB firmware installer.

67. **[Ketch by risseraka](https://github.com/risseraka/fm1-tracker-ketch) ([Web Installer & Emulator](https://risseraka.github.io/fm1-tracker-ketch/install/)):**
     * **License:** Open Source (GPL-3.0). Built on Dinghy.
     * **Concept:** LSDJ-style 4-channel chiptune music tracker for the FM-1 with authentic Game Boy tracking workflows.
     * **Features:** Song, Chain, and Phrase navigation screens driving four synthesis channels running Felucca sound engines, with dedicated instrument tables and groove speed settings.

68. **[Trawler by Floydus (y6zkcqnf5r-hue)](https://github.com/y6zkcqnf5r-hue/fm1-trawler):**
     * **License:** Open Source (GPL-3.0). Built on Dinghy.
     * **Concept:** Classic vertical demoscene tracker following the LSDJ paradigm (Song, Chain, Phrase, Instrument, Table, Groove).
     * **Features:** Dedicated tabular parameter modulation, microtonal groove tables, command effect columns, and multi-pattern song arrangement.

69. **[FM2000 by jukejutsu](https://github.com/jukejutsu/FM2000):**
     * **License:** Open Source.
     * **Concept:** PlayStation *Music 2000* (MTV Music Generator) inspired song maker and arrangement workstation for the FM-1.
     * **Features:** Composes short musical riffs and arranges them directly onto a multi-track bar timeline on the device, prioritizing full linear song structure and DAW-style composition over loop-based jamming.

70. **[MIDIMON by ignis32](https://github.com/ignis32/midimonitor_fm1):**
     * **License:** Open Source (GPL-3.0). Built on `fm1-base`.
     * **Concept:** Hardware MIDI monitor, diagnostic tool, and through-router for the FM-1.
     * **Features:** Displays incoming MIDI traffic from USB-MIDI, 3.5 mm TRS MIDI, and Bluetooth LE in real time in both human-readable text and raw hex; includes configurable MIDI Thru routing between interfaces.

71. **[SEQ-4 by devrvega](https://github.com/devrvega/SEQ-4):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Master quad MIDI hardware sequencer transforming the FM-1 into four independent sequencers for external gear.
     * **Features:** Routes up to 64 MIDI channels across four virtual USB-MIDI ports (A–D) and TRS MIDI OUT; each engine runs in one of six modes (polyphonic melody, chord progression, 8-track drum grid, arpeggiator, CC motion lane, or random Euclidean generator).

72. **[WitchBox by davidpryan](https://github.com/davidpryan/witchbox):**
     * **License:** Open Source. Built on Dinghy.
     * **Concept:** 6-track groovebox designed for Burial-inspired 2-step garage, future garage, and melodic atmospheric dubstep.
     * **Features:** Algorithmic swung pattern generators, syncopated off-beat hi-hat algorithms, pitched vocal slice triggers, and crackle/rain vinyl emulation.

73. **[FRASIL by styvesgoupil](https://github.com/styvesgoupil/frasil):**
     * **License:** Open Source.
     * **Concept:** Multi-layered drone, soundscape, and textural ambient performance synthesizer.
     * **Features:** Three continuous layered drone voices with independent pitch ratios, glistening GLINT FM bell generator, tuned sub-bass foundation, and an expansive shimmer plate reverb.

74. **[Finton by justynroberts](https://github.com/justynroberts/fm1-finton) ([Web Installer](https://justynroberts.github.io/fm1-finton/)):**
     * **License:** Open Source (GPL-3.0). Built on Dinghy.
     * **Concept:** 6-track progressive house and trance machine for the M-VAVE FM-1.
     * **Features:** Algorithmic Rollwerk chord progression engine and automated LIFT breakdown/drop build sequencing.

75. **[FN ACID by Electro-Dig](https://github.com/Electro-Dig/function-acid-fw) ([Web Installer](https://fn-acid.netlify.app/)):**
     * **License:** Open Source (GPL-3.0). Built on Dinghy.
     * **Concept:** Mathematical acid groovebox where each sound track is defined by parametric functions `y(s, phi)` drawn on the LCD and evaluated in real time.

76. **[NIGHTFALL by SylarPu-X](https://github.com/SylarPu-X/nightfall-fm1) ([Web Installer](https://sylarpu-x.github.io/nightfall-fm1/update.html) | [Web Studio](https://sylarpu-x.github.io/nightfall-fm1/)):**
     * **License:** Open Source (GPL-3.0).
     * **Concept:** Cyberpunk performance synthesizer featuring 4 tracks, 64-step patterns, a 6-stage master FX chain, and dedicated browser studio.

77. **[DriftSeq by johnskiller](https://github.com/johnskiller/driftseq) ([Web Emulator](https://johnskiller.github.io/driftseq/)):**
     * **License:** Open Source.
     * **Concept:** 16-track polymetric master MIDI sequencer with an integrated General MIDI engine for auditioning arrangements.

78. **[FM-1 Ctrl by johnskiller](https://github.com/johnskiller/fm1-ctrl):**
     * **License:** Open Source.
     * **Concept:** Lightweight controller firmware mapping the FM-1's capacitive keys, rotary knobs, and buttons into a dedicated Web MIDI controller for playing browser emulators.

79. **[FM1 Betis Mode by cotrino](https://github.com/cotrino/fm1-betis-mode) ([Web Installer & Emulator](https://cotrino.github.io/fm1-betis-mode/)):**
     * **License:** Open Source. Built on FM1 Open V13.
     * **Concept:** Real Betis football club-themed firmware: stadium crowd rhythms, club dashboard visuals, and a Phrygian-dominant Spanish scale generator.

80. **[COSMOS by Gadlele](https://github.com/Gadlele/COSMOS) ([Website](https://gadlele.github.io/COSMOS/) | [Web Installer](https://gadlele.github.io/COSMOS/install/) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1xg9h4g/cosmos_let_the_planet_play_the_synth_for_you_via/)):**
     * **License:** Open Source (GPL-3.0-or-later). Built upon `fm1-base` (with Wi-Fi networking and BearSSL HTTPS stack adapted from `fm1-radio`).
     * **Polyphony:** Continuous stereo drone + 16 weather-driven atmospheric pads + 8 moon-phase star voices + planetary chord progression generator.
     * **Concept:** Generative ambient/drone synthesizer played autonomously by the sky: connects to Wi-Fi to fetch real-time atmospheric, astronomical, and space weather data based on your exact coordinates, turning the FM-1 into an evolving window on the cosmos.
     * **Features:**
       * **Astronomical Night/Day Sky UI:** On-device 240 × 240 display renders the live sky over your location (stars, moon, and visible planets rendered at real astronomical positions, obscured dynamically by daylight and cloud cover).
       * **Continuous FM Drone:** Dual stereo FM drone pairs with gentle beating, pink noise, and sub-octave oscillator; filter brightness directly modulated by the sun's altitude.
       * **16 Weather Pads (Day & Night):** Weather condition (fetched from Open-Meteo or estimated from barometric pressure/clouds) chooses the active pad on every chord cycle: NEBULA/AURORA (clear sky, saws & shimmer reverb), STRINGS/QUASAR (partly cloudy, chorus ensemble & sine grains), ORGAN/VOYAGER (overcast, drawbars & vocal formants), BACKGROUND/HORIZON (fog, harmonic veil & reverse FM), TAPE/DEEP FIELD (drizzle, saturation & wavefolding), CRYSTAL/RINGS (rain, inharmonic FM & resonators), SOLAR WIND (snow, bandpass noise), SUPERNOVA/GRAVITY (thunderstorm, brass & sub bass).
       * **Star Sequencer & 8 Moon Voices:** A scanning line sweeps the screen every 16 seconds; crossing any visible star (magnitude < 3) triggers a melodic note (height = pitch, brightness = velocity, horizontal position = stereo pan). The timbre shifts across 8 moon phases (New Moon drops, Waxing Crescent kalimba, First Quarter harp, Waxing Gibbous celesta, Full Moon chimes, Waning Gibbous glass, Last Quarter music box, Waning Crescent flute).
       * **Planetary Chords & Cosmic Tuning:** Tracks visible planets (Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn) above the horizon; plays Cousto cosmic octave frequencies and 4-chord progressions cycling every 10 seconds. Musical mode shifts from Phrygian (night) through Dorian and Mixolydian to Lydian (solar noon).
       * **Geomagnetic Storm Modes (Kp Index):** Space weather activity alters the engine: Kp ≥ 4 triggers the STARGATE 112 BPM arpeggiator; Kp ≥ 5 (geomagnetic storm) triggers PULSAR 104 BPM gated sixteenths with ring modulation.
      * **Hardware & Offline Controls:** Turning encoders in EDIT mode directly adjusts atmospheric parameters; HOME returns to live tracking. Operates offline with internal astronomical calculations and simulated weather.

81. **[MOPE-1 by slothpallas](https://github.com/slothpallas/mope-1) ([Website & Web Installer](https://slothpallas.github.io/mope-1/)):**
    * **License:** Open Source (GPL-3.0-only). Fork of FiMba-1 by J. Adam Sowers (inheriting boot, safe mode, updater, and Dattorro plate reverb from FoMni, X0X, and Felucca).
    * **Polyphony:** 6-voice wavetable synthesizer with detuned oscillators, sub-oscillator, analog drift, SVF filter, and backing band.
    * **Concept:** A melancholic wavetable synthesizer and toy-keyboard groovebox featuring an animated expressive pixel "blob" character in a rainy room, backing auto-band that strictly plays minor-key progressions, and moody synthesized lo-fi drums.
    * **Features:**
      * **Interactive "Blob" Synthesis Visualization:** The central character is a lit pixel-art jelly blob floating in a sad room with a rainy window. Turning Table/Position reshapes its body from 8 boot-generated harmonic wavetables (Sigh, Moan, Pulse, Crush, Warble, Fold, Church, Sync with anti-aliasing mipmaps); Detune causes ghost echoes to drift; Sub fattens its base; Cutoff opens or closes its eyes; Resonance shrinks its pupils into laser eyes.
      * **Live Schematic UI:** Editing parameters opens classic electronic schematics live on screen for ADSR envelopes, SVF curves, and LFOs.
      * **Minor-Key Backing Band & Gunk:** Auto-bass engine strictly resolves to relative natural minor scales; Gunk generator layers dynamic room textures (rain on glass, vinyl crackle, low rumble) that swell when playing pauses.
      * **13 Synthesized Sad Drum Styles:** Synthesized drum machine (808/gabber kick, snare, claps, hats, log drum, cowbell, sliding 808 bass) covering Grief drill, Empty city pop, Gloom gabber, Missed phonk call, Jersey cry club, Heartbreakcore, Amapia-no, Cold footwork, Dembow out, Vaporweep, Hyperflop, Funeral bossa, and Office ambivalent.
      * **Built-in Tape Looper & Arpeggiator:** Overdub loop recording up to 192 notes across 1, 2, or 4 bars with step piano roll editing on white keys, velocity, swing, and humanization.
      * **Level-Matched FX Chain:** Fry (drive, bitcrush, sample-rate reduction), 3-tap chorus, ping-pong delay, Dattorro plate reverb, and tape wow/flutter saturation.

82. **[FIZZ by Quixotic7](https://github.com/Quixotic7/FIZZ) ([Web Emulator / Preview](https://quixotic7.github.io/FIZZ/) | [Web Installer](https://quixotic7.github.io/FIZZ/install/) | [Project & Preset Manager](https://quixotic7.github.io/FIZZ/manager/) | [Playing Guide](https://quixotic7.github.io/FIZZ/guide.html)):**
    * **License:** Open Source (MPL-2.0). Engine and effects derived from ChoralRoot v0.25.1; clean-room UI rewrite with PlutoVG.
    * **Polyphony:** 8 tracks sharing 16 polyphonic FM-Tone voices (advanced Elektron Digitone-inspired FM engine with chords up to 6 notes).
    * **Concept:** Advanced FM-Tone groovebox and step sequencer inspired by the Elektron Digitone and OMX-27 Form sequencer, featuring deep parameter locks, generative rhythms, and live SysEx controller integration.
    * **Features:**
      * **FM-Tone Synthesis Engine:** Expanded FM engine featuring dedicated filter modes, unison detune, and full parameter lockability across every step.
      * **Elektron-Style Step Sequencer:** 8 tracks sharing 16 voices, track defaults with per-step overrides, conditional trigs, probability/chance, micro-timing, ratchets, and polyphonic chords up to 6 notes.
      * **Generative Engines & MIDI FX:** Integrated Euclidean rhythm generator and Mutable Instruments Grids drum mapping for algorithmic pattern generation, accompanied by creative MidiFX modulators.
      * **Dynamic Contextual SysEx UI & Accelerating Knobs:** Hardware encoders accelerate dynamically for precision vs. full sweeps; live SysEx label streaming sends real-time parameter definitions to web companions and remote controllers.
      * **Preset & Sound Pool Librarianship:** On-device 128-sound pool; web manager supports backing up projects, managing sound banks, and importing native Elektron Digitone (`.dnsnd`) and Digitone II (`.dn2pst`) FM patches.
      * **Cross-Platform Architecture:** Operates both as standalone hardware firmware and as an FM1VST core module on Mac/PC with RemoteFM1 physical hardware integration.

83. **[S1Vave by Andrew GG (AndrewGG88)](https://github.com/AndrewGG88/S1Vave) ([Website & Web Flasher](https://andrewgg.one/s1vave/) | [Browser Simulator](https://andrewgg.one/s1vave/sim/) | [The Firmware Hub](https://thefirmwarehub.com/)):**
    * **License:** Open Source (GPL-3.0-only). Derived from OberVave (zvenson), Dinghy, and Felucca base platform.
    * **Polyphony & Voicing:** 8 voices with 4 voicing modes: `MONO` (true SH-101 monosynth with legato glide), `UNISON` (8-voice stacked analog unison for massive leads and basses), `POLY` (8-voice dynamic polyphony for lush chords and pads), and `CHORD` (programmable chord memory with per-voice semitone offsets from -12 to +12).
    * **Concept:** 8-voice virtual analog tweak synthesizer modeled after the classic Roland SH-101 and AIRA Compact S-1 architecture, featuring complete sound engine parity, cascaded 4-pole self-oscillating filter, and unique oscillator drawing/chopping tools.
    * **Features:**
      * **Oscillator Core & Tweak Innovations:** PolyBLEP anti-aliased saw, square/pulse with manual/envelope/LFO pulse-width modulation (50% to 5% needle pulse), calibrated sub-oscillator with 3 octave types (`-2o.A` asymmetric growl, `-2oc`, `-1oc`), and calibrated analog pink/white noise generators.
      * **OSC DRAW & OSC CHOP:** 16-step user-drawn wavetables (`STEP` or smooth interpolated `SLOPE` with 1.0x–32.0x multiplier) and harmonic comb slicing (1.0–32.0 repetitions with 0–200 overtone depth) for metallic overtones and bell textures; built-in performance Riser/Downer transition generator.
      * **Cascaded 4-Pole Filter & Calibrated Envelopes:** 24 dB/oct state-variable low-pass filter calibrated across 20 Hz – 20 kHz with self-oscillation and bass retention, dual filter character modes (**S-1 Clean ACB** and **Warm Midnight** soft-knee drive), and hardware-measured exponential ADSR curves.
      * **LFO & Stereo Effects:** 6-waveform LFO ranging from 0.05 Hz up to ~100 Hz in Fast audio-rate mode with 31 tempo-sync divisions; 4-type stereo chorus, analog-slewing tempo-synced ping-pong delay, and 44.1 kHz Dattorro plate reverb (7 room algorithms).
      * **Dual-Track Sequencer & Factory Soundbank:** Two polyphonic tracks (A & B) sharing 256 steps with independent track lengths, clock divisions, ratchets (1–4), and probability; 64 factory presets + 35 user slots; class-compliant 44.1 kHz / 16-bit USB stereo audio and 1:1 MIDI CC control.

### 1.2. Modular Firmware Platforms & Builders


1. **[fm1-rocket-os by cmlarsen](https://github.com/cmlarsen/fm1-rocket-os):**
    * **License:** Open Source (GPL-3.0). Forked from X0X and Felucca.
    * **Concept:** Clip-launching performance firmware turning the FM-1 into an Ableton Live-style clip launcher and matrix sequencer.
    * **Status:** Work in progress.

2. **[Optimist by w0ts](https://github.com/w0ts/optimist) ([Website & Web Builder](https://w0ts.github.io/optimist/)):**
    * **License:** Open Source (GPL-3.0-only). Derived from SLOOP, Felucca, Melodee, and X0X.
    * **Status:** In active development (tested in emulator).
    * **Concept:** Modular firmware builder and platform allowing users to custom-assemble FM-1 firmware images tailored to flash and RAM budgets directly from the browser or CLI.
    * **Features:**
      * **Modular Web & CLI Builder:** Choose specific synth engines (ANALOG 2, DIGITAL, PHASE, LOFI, SAMPLE, VOICE, TRIO, WHEEL, GRAIN, FM6, SLICE, PHYS, ACID), drum kits (including 808/909 styles), effects (DUST, DUCK, DJ filter, delay, reverb), and sequencer capabilities while monitoring flash and RAM allocations live.
      * **Multi-Layer UI & Sequencer:** SLOOP-style live button-held layers, per-track patterns, scenes, snapshots, fills, microtiming, and parameter locks.
      * **In-Browser Simulator & Web Editor:** Test and audition custom firmware configurations in the browser before flashing; full SLOOP project interchangeability and web-based parameters librarian.

3. **[Dinghy by Sven Trogus (zvenson)](https://github.com/zvenson/dinghy):**
    * **License:** Open Source (GPL-3.0-only).
    * **Concept:** Minimal, clean firmware skeleton for custom developers: 4-voice sine wave synthesizer on top of working display, audio DMA, and button input drivers.

4. **[Modular-1 by morgulbrut](https://wiggismodular.github.io/Modular-1/) ([Webapp & Flasher](https://wiggismodular.github.io/Modular-1/)):**
    * **License:** Open Source (GPL-3.0). Built using Felucca HAL and tooling.
    * **Concept:** Nord Modular-inspired modular synthesizer engine and visual web patch editor for the FM-1.
    * **Features:**
      * **Browser Patch Editor:** Interactive visual web environment allowing users to construct modular signal paths, configure modules, and upload patches directly to the FM-1 hardware.
      * **Module Architecture & Matrix:** Modules feature parameter inputs (`p1` and `p2` with attenuverters) alongside an assignable modulation matrix routing global `p1`/`p2` and contextual `k1`–`k4` knob controls per module.
      * **Generative Arpeggiator:** Complex multi-page arpeggiator engine featuring dedicated melody controls (scale, root, speed), Euclidean rhythm sequencing (pulses, rotation, rate), and chaotic generative probability/octave spreading.

5. **[Hexagon Console](https://www.reddit.com/r/MVaveFM1/comments/1x5qq7z/coming_soon_hexagon_console/):**
    * **Status:** Upcoming / Teased announcement.
    * **Concept:** Console-style musical environment and custom firmware architecture for the M-VAVE FM-1.
    * **Details:** Teased within the r/MVaveFM1 community ([Coming soon: Hexagon Console](https://www.reddit.com/r/MVaveFM1/comments/1x5qq7z/coming_soon_hexagon_console/)), introducing a modular hexagonal UI paradigm and performance console interface tailored for the FM-1 hardware.

6. **[OpenIFW fm1 by rcell233](https://github.com/rcell233/OpenIFW-fm1) ([Online Demo & Web Installer](https://rcell233.github.io/OpenIFW-fm1/)):**
    * **License:** Open Source.
    * **Concept:** Open-source WebAssembly host simulation platform and web installer for FM-1 firmware developers.
    * **Features:** Executes the identical C11 firmware core (`app.c`, fixed-point DSP, display driver, and persistent storage logic) directly in the browser via WebAssembly, faithfully simulating keys, buttons, encoders, 240 × 240 RGB565 LCD, and flash memory without requiring hardware flashing.

7. **[Matryoshka by glvno](https://github.com/glvno/matryoshka) ([Web Studio & Installer](https://matry0shka.pages.dev/)):**
    * **License:** Open Source.
    * **Concept:** Recursively modular synth framework and visual web patch environment for the FM-1.
    * **Features:**
      * **Interactive Browser Canvas & Modular Routing:** Visual drag-and-drop workspace for patching synthesis modules (oscillators, physical string models, noise, filters, formant blocks) with attenuverters and modulation cables.
      * **Assemblies, Presets & Patch Library:** Prebuilt multi-module sound assemblies (Pluck, Hat, etc.), library manager with offline and hardware syncing.
      * **Integrated Hardware Emulation & Installer:** Built-in hardware emulator and one-click WebMIDI flasher with safe stock restoration workflows.

8. **[FORGE ONE & Forge Phoenix by Khantipol Kasemsant (kktp)](https://forge.kktp.net/) ([Guide & Install](https://forge.kktp.net/one/) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1xhk0yw/forge_phoenix_update_generative_groovebox/)):**
    * **License:** Open Source (GPL-3.0-only).
    * **Concept:** Standalone 4-track groovebox and live generative electronic music platform for the M-VAVE FM-1 with optional companion iPad app (*Forge Remote*).
    * **Features & Phoenix Generative Mode:**
      * **Phoenix Algorithmic Mode:** Instant generative song starter across 8 electronic styles (acid house, acid techno, electro, goa acid, dub techno, acid breaks, hard acid, acid downtempo) with 4 unique starters per style (32 starters total selectable on black keys).
      * **Live Pattern Sculpting:** `SEED` reshapes patterns, `DENSITY` adds or subtracts notes, and `EVOLVE` allows phrases to slowly drift over time.
      * **Part-Selective Regeneration & Track Lock:** Perform `NEW NOTES`, `NEW RHYTHM`, or `NEW GROOVE` to rewrite one part synchronized to the next bar boundary. Tracks can be `LOCK`ed to protect desired parts, with dedicated `FILL`, `UNDO`, and `KEEP` commands.
      * **Full Sequencer & Performance:** Kept grooves become regular 4-track patterns with full step editing, parameter locks, automation, live overdubbing, 4 project slots, and a 16-section Song Mode (each section repeating 1–16 times). `SET` mode transforms keys into momentary performance FX (filter breakdowns, build-ups).
      * **Forge Remote iPad Companion:** Optional tablet app mirroring the hardware display at crisp whole-number scale (Full and Fast modes), offering touch Pattern, Sound, Mix, and Phoenix pages to ride levels, sends, and filter envelopes in real time alongside physical hardware knobs.

9. **[fm1-dock by Joakim Eriksson](https://github.com/joakimeriksson/fm1-dock) ([Project Page & Web Console](https://joakimeriksson.github.io/fm1-dock/) | [Releases](https://github.com/joakimeriksson/fm1-dock/releases)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Multi-synth docking container and dynamic module manager for the FM-1: install once, hold HOME for 1.5 seconds to open the picker, and switch between multiple independent synthesis engines on the fly without reflashing.
    * **Features:**
      * **Flash-Resident Multi-Synth Engine Dock:** Bundles and docks full synthesis engines in flash simultaneously: CS-1 (twochannels CS-80), Scintilla (Elka Synthex), OberVave (Oberheim OB-Xa/OB-8), FM-1 SID (C64 6510/reSID engine), and SINE fallback.
      * **Fast Hot-Swapping:** Instant on-device switching via the rotary encoders/keys without computer connection; preserves deployed module presets and flash states.
      * **Wireless & Debug Tooling:** Integrated BLE-MIDI wireless support (`FM1-DOCK`), real-time WebMIDI browser console with logs, crash records, render load monitors, and fast USB module deployment in seconds.

10. **[FMLarynx by ejtb76](https://github.com/ejtb76/FMLarynx):**
    * **License:** Open Source (GPL-3.0). Built on Dinghy.
    * **Concept:** Talking formant vocal synthesizer with an integrated 303-style acid step sequencer.
    * **Features:** Routes raw analog-style sawtooth waveforms through three resonant vowel formant filters to simulate human vocal tract acoustics, combined with TB-303 accent/slide sequencing.

11. **[EXTRATONE CORE by Fabio Massimo Pasquazzi](https://github.com/fabiomassimopasquazzi/dinghy):**
    * **License:** Open Source (GPL-3.0). Built on Dinghy.
    * **Concept:** Extreme high-speed FM kick synthesizer and bassline engine designed for Extratone, Speedcore, and Terrorcore (up to 1000+ BPM).
    * **Features:** Single-voice dedicated percussion engine featuring ultra-fast pitch envelopes, AHDR amplitude modulation, 24 dB/oct resonant low-pass filter, and high-rate key retriggers.

### 1.3. Gaming, Emulators & Non-Audio Ports (Games & Experiments)

1. **[FM-1 Doom by Sven Trogus (zvenson)](https://github.com/zvenson/fm1doom) ([Web Installer](https://doom.deadlockinteractive.com/) | [Alt Web Installer](https://dx7.designburgapps.com/doom/)):**
    * **License:** Open Source (GPL-2.0-or-later / GPL-3.0; FreeDM game data under BSD-3-Clause). Based on doomgeneric, Chocolate Doom, and the sloopDX / SLOOP / Felucca platform.
    * **Concept:** Port of classic Doom (running a FreeDM arena map) on the M-VAVE FM-1 synthesizer hardware.
    * **Features:**
      * Rendered directly to the FM-1's color screen with health, armor, ammo, and automap overlay.
      * Controls mapped to physical synthesizer keys and knobs: F3/B3 or KNOB 1 to turn, A3/G3 forward/back, OCT−/OCT+ or F#3/G#3 to strafe, C5/PLAY to fire, D5/REC to open/use, E5 to run, C#5/D#5/F#5 weapon selection (fist, pistol, shotgun), ARP for automap, and FX for brightness.
      * Preserves sloopDX projects in flash without overwriting user patch data.

2. **[FM-1 NES by Keitark](https://github.com/Keitark/fm1-nes) ([App Updates Guide](https://github.com/Keitark/fm1-nes/blob/main/APP_UPDATES.md)):**
    * **License:** Open Source (Apache-2.0).
    * **Status:** Experimental / Source only (reference proof-of-concept).
    * **Concept:** Nintendo Entertainment System (NES) emulator running on the FM-1 hardware.
    * **Features:** Uses the FM-1's 27 keys as the game controller and its color screen as the television display. Developed as a worked example and educational kit for writing bare-metal FM-1 firmware from scratch.
    * **Documentation:** [FM-1 NES APP_UPDATES.md Guide](https://github.com/Keitark/fm1-nes/blob/main/APP_UPDATES.md) — developer guide detailing application-only updates (`app.bin`) that preserve the stock USB bootloader.

3. **[Mocky by Charles Vestal](https://github.com/charlesvestal/fm1-mocky) ([Web App](https://charlesvestal.github.io/fm1-mocky/)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Display testing firmware and web companion for transmitting and displaying arbitrary bitmap pictures on the FM-1's color screen over WebMIDI.

4. **[fm1-mdx by Keitark](https://github.com/Keitark/fm1-mdx):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Experimental Sharp X68000 MDX/PDX karaoke music player running a software YM2151 FM chip emulation allowing interactive part muting and live keyboard accompaniment.

5. **[GameDude by Chance The Maker](https://github.com/ChanceTheMaker/gamedude-fm1-smk) ([Web Simulator & Compiler](https://chancethemaker.github.io/gamedude-fm1-smk/)):**
    * **License:** Open Source (GPL-3.0). Built on Peanut-GB and Felucca.
    * **Concept:** Nintendo Game Boy emulator, browser-based ROM-to-firmware compiler, and interactive web simulator for the M-VAVE FM-1 and SMK-37 controller hardware.
    * **Features:**
      * **Peanut-GB Core Port:** Optimized Game Boy emulator core running at smooth framerates on the JieLi AC791N RISC CPU.
      * **Web ROM Compiler & Simulator:** Drag-and-drop any Game Boy `.gb` ROM into the browser to test it immediately in the WebAssembly simulator and generate a flashable `.fwsc` firmware image in seconds.
      * **Ergonomic Synth-Key Layout:** Physical synth keys mapped intuitively to D-pad (Up/Down/Left/Right), A/B buttons, and Start/Select, with knob controls for volume, display brightness, and color palette cycling (classic DMG pea-soup green, pocket grayscale, neon cyberpunk).
      * **Dual Device Support:** Supports both the FM-1 synthesizer and SMK-37 keyboard controller hardware.

6. **[Fart Machine One by adamcharleswilsonmusic-code](https://github.com/adamcharleswilsonmusic-code/Fart-Machine-One):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Novelty joke sample-synthesizer and sequencer firmware for the FM-1.
    * **Features:** 11 distinct pitched flatulence sample sounds, integrated 16-step sequencer, dynamic pitch modulation, and onboard stereo delay and reverb effects.

7. **[Trumpagotchi by adamcharleswilsonmusic-code](https://github.com/adamcharleswilsonmusic-code/Trumpagotchi) ([Releases](https://github.com/adamcharleswilsonmusic-code/Trumpagotchi/releases)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Virtual-pet Tamagotchi-style game and mini-instrument for the FM-1 featuring pixel-art animations.
    * **Features:** Four dedicated action keys allow feeding, praising, cleaning, and resting the pet. The white keys play a pentatonic musical instrument, and keeping the pet happy and well-rested unlocks accompanying bongo rhythm tracks.

8. **[Trireme FM-1 by ignis32](https://github.com/ignis32/trireme_fm1) ([Releases](https://github.com/ignis32/trireme_fm1/releases)):**
    * **License:** Open Source (GPL-3.0).
    * **Concept:** Transforms the FM-1 into a fully programmable USB computer keyboard and macro pad with Vial GUI configuration support.
    * **Features:** Assign any standard keyboard key, multimedia shortcut, or mouse action to each capacitive key, button, and rotary encoder; five distinct layout layers, advanced macros, on-device configuration editor, and instant USB HID compatibility.

9. **[RemoteFM1 by Quixotic7](https://github.com/Quixotic7/RemoteFM1) ([Web Demo](https://quixotic7.github.io/RemoteFM1/)):**
    * **License:** Open Source.
    * **Concept:** Thin-client bridge firmware turning the physical FM-1 into a hardware surface and LCD display for computer-based firmware emulators.
    * **Features:** Streams every capacitive keypress, button event, encoder turn, and knob value over USB to a host computer while rendering computer-sent framebuffers directly onto the 240 × 240 screen and LEDs. Allows developers and musicians to audition and live-code new firmwares at full speed on desktop or web emulators using real FM-1 controls without flashing flash memory.

10. **[FMDj by DeadActive](https://github.com/DeadActive/FMDj) ([Web Installer](https://deadactive.github.io/FMDj/webapp/lsdj-install/) | [Web Simulator](https://deadactive.github.io/FMDj/webapp/lsdj-sim/)):**
     * **License:** Open Source (GPL-3.0-only). Built upon Felucca by Leo Kuroshita / Hügelton Instruments with Peanut-GB and `minigb_apu` cores.
     * **Concept:** Game Boy music tracker emulator firmware for running Little Sound Dj (LSDj) and Drum Machina Go! (DMGo!) natively on the FM-1.
     * **Features:**
       * **Dedicated Game Boy Tracker Integration:** Runs user-provided Game Boy `.gb` ROMs with frame-accurate sound generation across all 4 Game Boy audio channels (pulse 1, pulse 2, 4-bit wave channel, noise).
       * **1.5× Scaled Color Display & Palettes:** Scaled display rendering with customizable retro palettes (DMG pea-soup green, Pocket grayscale, Light, Super Game Boy, Dark) and optional performance overlay (FPS, CPU load).
       * **Ergonomic Tracker Controls:** SELECT/ALGORITHM rotary encoders and directional keys navigate rows and screens, top keys act as A/B buttons, 16 white keys act as step triggers for DMGo!, and holding REC triggers instant battery/flash save.

11. **[Neverhood for FM-1 by snpwball](https://github.com/snpwball/fm1-neverhood) ([Web Player & Installer](https://snpwball.github.io/fm1/neverhood/)):**
     * **License:** Open Source.
     * **Concept:** Interactive claymation demo and music player tribute to The Neverhood for the M-VAVE FM-1.
     * **Features:** Renders animated claymation scenes on the 240 × 240 screen accompanied by audio synthesis and music playback.

12. **[fm1-radio by Charles Vestal](https://github.com/charlesvestal/fm1-radio) ([Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1xee57d/fm1_radio_wifi_internet_radio_with_live_fx_and/)):**
     * **License:** Open Source (GPL-3.0). Source only.
     * **Concept:** Internet radio receiver firmware with Wi-Fi streaming, Radio Garden station directory browsing, and real-time punch-in DJ audio effects.
     * **Features:** Leverages the JieLi AC791N SoC's onboard Wi-Fi to stream live internet radio stations with on-screen metadata, station browsing, and interactive live FX triggered via capacitive keys.

13. **[picovave by acidsound](https://github.com/acidsound/picovave):**
     * **License:** Open Source (MIT). Based on the `femto8` engine.
     * **Concept:** PICO-8 fantasy console emulator firmware for the M-VAVE FM-1.
     * **Features:** Runs PICO-8 game carts directly on the 240 × 240 color display with sound effects and music, supporting cartridge uploads over MIDI SysEx.

14. **[Cat Piano by thefriendlyhedgehog](https://github.com/thefriendlyhedgehog/FM-Cat1):**
     * **License:** Open Source (GPL-3.0). Derived from Fart Machine One.
     * **Concept:** Humorous feline sampler and music machine for the FM-1.
     * **Features:** Every piano key triggers an authentic pitched cat's meow across four distinct voice banks, paired with an integrated 4-track sequencer and arpeggiator.

15. **[Deal or No Deal by Kiwi3p](https://github.com/Kiwi3p/fm1-deal-or-no-deal):**
     * **License:** Open Source.
     * **Concept:** 16-bit retro arcade game adaptation of *Deal or No Deal* for the FM-1.
     * **Features:** Maps 26 mystery briefcases directly across the synthesizer keys, featuring animated pixel-art host graphics, banking decisions, and a chiptune soundtrack.

16. **[Doom E1M1 by seanohollaren](https://github.com/seanohollaren/fm1-doom) ([Web Installer](https://doom.deadlockinteractive.com/)):**
     * **License:** Open Source (GPL-2.0). Built on rp2040-doom and Felucca HAL.
     * **Concept:** Port of the first level of Doom (E1M1) running natively on the FM-1 hardware, complete with title screen, sound effects, and music.

17. **[Doom FM-1 / SMK by Chance The Maker](https://github.com/ChanceTheMaker/doom-fm1-smk) ([Web Installer & Compiler](https://chancethemaker.github.io/doom-fm1-smk/) | [Simulator](https://chancethemaker.github.io/doom-fm1-smk/simulator.html)):**
     * **License:** Open Source (GPL-2.0).
     * **Concept:** Browser firmware builder, ROM compiler, and WebMIDI installer for running Doom on the M-VAVE FM-1 and SMK-37 hardware.

18. **[Dungeon Tracker by Better-Hyena-8716](https://www.reddit.com/r/MVaveFM1/comments/1xgtupf/dungeon_tracker/):**
     * **Status:** In active development (preview announced on r/MVaveFM1).
     * **Concept:** First-person retro grid-based dungeon crawler game (*Eye of the Beholder* style) running natively on the FM-1 hardware with integrated audio tracking.

### 1.4. Stock Firmware Patchers & Binary Mods

1. **[FM-1 Firmware Patcher by Christian Zietz (czietz)](https://github.com/czietz/fm1-firmware-patcher):**
    * **License:** Open Source (Unlicense / Public Domain).
    * **Target:** Stock official **V15** firmware (`FM-1.fwsc`).
    * **Modifications & Bug Fixes:**
      * Fixes the oscillator detune calculation in the stock synth engine to accurately match Dexed / Yamaha DX7 behavior.
      * Disables unhandled MIDI aftertouch messages that cause unwanted heavy vibrato.
      * Modifies the UI colorway: changes the main oscilloscope display to dark blue and the FX selection cursor to green (as visual confirmation of patched firmware).
    * **Usage:** Python patcher script applying precise binary offsets (`python patch_firmware.py FM-1.fwsc FM-1-fixed.fwsc`). Flashed via M-VAVE's M-UPGRADE utility.

2. **[FM-1 Macropad Patch by smememe](https://github.com/smememe/fm1-macropad-patch) ([Web Patcher](https://smememe.github.io/fm1-macropad-patch/)):**
    * **License:** Open Source (MIT).
    * **Target:** Stock official **V15** firmware (`FM-1.fwsc`).
    * **Concept & Modifications:** Binary patch that transforms the FM-1 into a 55-input MIDI macro pad controller. Modifies the firmware so every physical button, piano key, and rotary knob sends a USB-MIDI note message while turning off all LEDs. Combined with desktop hotkey software, it converts the synthesizer into an external macro pad.
    * **Usage:** Apply patch directly in the browser via WebAssembly/WebMIDI or via Python script (`python3 fm1patch.py FM-1.fwsc`). Flashed via standard update tools.

> [!TIP]
> **Community Flashing Experience & Safe Upgrade Practice:**  
> While not an absolute hard rule, there is a prominent community recommendation to avoid flashing one custom firmware directly over another. To minimize bricking risks, some users suggest rolling back to the official stock firmware (v15) via M-VAVE's official updater first, and only then flashing the next custom firmware build. Alternatively, you can use **[TransitFM1](https://quixotic7.github.io/TransitFM1/)** — a dedicated lightweight bridge firmware by Quixotic7 designed with crash-guarded boot stubs and stock V15 identity emulation to safely transition between custom builds.

---

## 2. Hardware Architecture & Reverse Engineering Reference

All technical deep dives, hardware reverse engineering findings, bootloader memory maps, and protocol specifications are documented in **[REVERSE_ENGINEERING.md](REVERSE_ENGINEERING.md)**:

* **Hardware & Ecosystem Overview:** JieLi AC791N SoC specs, devboard details, PCB characteristics, and teardown instructions.
* **Device Recovery Vectors:**
  * **Plain USB Unbricking:** Soft-brick recovery directly into `WL82 UBOOT1.00` mask-ROM mode via `jl-uboot-tool` and `MvaveFM1Unbricker` without opening the casing.
  * **Hardware `USB_KEY` Mask-ROM Recovery:** Forcing mask-ROM USB download mode on frozen/hard-bricked processors using an external RP2040 dongle ([FM-1 Transporter](https://github.com/kurogedelic/FM-1-transporter)) pulsing the JieLi hardware boot key (`0x16EF` at ~50 kHz) over USB D+/D- lines, with community wiring instructions for Seeed XIAO RP2040 / Raspberry Pi Pico (Green to D6, White to D7, Black to GND).
* **Firmware Container Analysis:** Embedded `.fwsc` firmware extraction from `M-UPGRADE-FM1` (Qt resource layout, `@JMUA` / `JLUFW` signatures).
* **MIDI SysEx OTA Protocol:** Handshake, parameter query behavior, and verified two-step device-pull session flow with 8→7 LSB-first bitstream encoding.
* **Memory Map & Bootloader:** Flash partitions (UBOOT, App, VM), linker script requirements, and critical bootloader re-entry guidelines.
* **Binary References & Offsets:** Magic numbers, Qt container offsets, and symbol references.
* **Firmware Size Boundaries:** SPI flash memory budget, execution model (XIP), and partition limits.
* **Python Firmware Utility:** CLI utility ([`fm1_flasher.py`](fm1_flasher.py)) for extracting firmware images and exploring protocol exchanges.
* **Disassembly & Tooling:** Ghidra processor module ([`ghidra-jieli`](https://github.com/kagaimiq/ghidra-jieli)) and official Pi32v2 toolchain notes.
* **Firmware Security & BadUSB Threat Modeling:** Theoretical risks of unsigned firmware execution (e.g. re-enumerating USB descriptors to standard HID keyboard to inject keystroke payloads) and host security mitigation considerations.

**Read the full documentation:** **[REVERSE_ENGINEERING.md](REVERSE_ENGINEERING.md)**

---

## 3. External References & Resources

Useful open-source tools, documentation, and SDK repositories:

### 3.1. Hardware Recovery, Bootloaders & Firmware Flashers

 1. **[jl-uboot-tool Repository](https://github.com/kagaimiq/jl-uboot-tool):**
    Utility for interacting with JieLi UBOOT bootloaders over USB Mass Storage / SCSI pass-through.

 2. **[Unbricking a Soft-Bricked FM-1 over Plain USB (Reddit Guide by acrawf1)](https://www.reddit.com/r/MVaveFM1/comments/1wz48t7/guide_unbricking_a_softbricked_fm1_black_screen/):**
    Detailed community guide for recovering devices stuck on a black screen in `WL82 UBOOT1.00` mode (`VID_4C4A:PID_8057`) via plain USB cable and `jl-uboot-tool` without extra hardware. Includes the [`fm1_extract_app.py` helper script](https://gist.github.com/Acrawf1/ae2b9930b49231db397568cfc2abc2a8).

 3. **[FM-1 Transporter by Leo Kuroshita (kurogedelic)](https://github.com/kurogedelic/FM-1-transporter) ([Hard Brick Recovery Guide](https://www.reddit.com/r/MVaveFM1/comments/1x5lifu/mvave_fm1_unbricking_after_a_hard_brick_using_a/)):**
    Hardware RP2040-based USB dongle firmware that pulses the JieLi `USB_KEY` pattern (`0x16EF`) to force unresponsive FM-1 devices into mask-ROM USB download mode for emergency flash recovery. See the practical community walkthrough for wiring a Seeed XIAO RP2040 or Raspberry Pi Pico (Green to D6, White to D7, Black to GND) and recovering via `jl-uboot-tool`: [Reddit: Unbricking after a hard brick using a RP2040 and the FM-1 Transporter](https://www.reddit.com/r/MVaveFM1/comments/1x5lifu/mvave_fm1_unbricking_after_a_hard_brick_using_a/).

 4. **[MvaveFM1Unbricker by Quixotic7](https://github.com/Quixotic7/MvaveFM1Unbricker) ([Troubleshooting Guide](https://github.com/Quixotic7/MvaveFM1Unbricker#troubleshooting)):**
    Python-based unbricking toolkit and comprehensive troubleshooting reference for M-VAVE FM-1 recovery. Automates safe backup and restoring via `jl-uboot-tool` (strictly protects the `< 0x4000` boot head, prevents `erasechip`, and verifies flash SHA-256), while providing procedures for forcing unresponsive units into ROM boot (watchdog timeouts, OCT-/OCT+ holds, quick power cycles) and RP2040 Transporter hardware recovery.

 5. **[flipper-fm1-recovery by merthsoft](https://github.com/merthsoft/flipper-fm1-recovery):**
    Firmware flasher and unbricker utility utilizing a **Flipper Zero** to pulse the hardware ROM recovery sequence on the FM-1's USB data pins without requiring an RP2040 dongle or wiring.

 6. **[fm-static by seajaysec](https://github.com/seajaysec/fm-static) ([Web App](https://seajaysec.github.io/fm-static/)):**
    WebMIDI flasher solving the issue where an FM-1's USB-MIDI port identifies under an unusual/renamed descriptor, which causes official updaters to report the synthesizer as missing.

 7. **[fm1-linux-update by fuleo](https://github.com/fuleo/fm1-linux-update):**
    Linux CLI updater tool for flashing and verifying stock V14 to V15 firmware binaries over USB-MIDI.

 8. **[JieLi USB Boot Key Activation (jielie docs)](https://kagaimiq.github.io/jielie/isp/usb/usb-key.html):**
    Documentation on triggering JieLi hardware USB boot loader mode via D+/D- signal patterns and ISP keys.

 9. **[ip2k/mvave-fm1-open-firmware Repository](https://github.com/ip2k/mvave-fm1-open-firmware):**
    Research project towards an open-source firmware for the M-VAVE FM-1. Includes specification, reference implementation, and simulation testbench for an **RP2040-based `USB_KEY` hardware recovery dongle** (`dongle/` directory) that forces the JieLi AC791N SoC into mask-ROM USB download mode (`UBOOT1.00`) via the external USB-C port, enabling low-level flash backup and unbricking.

10. **[Custom Bootloader & Full Flash Backup/Restore Flasher by mobiliakas1](https://www.reddit.com/r/MVaveFM1/comments/1x6xtz1/testers_for_custom_bootloader_needed/):**
    Under-development custom recovery bootloader and cross-platform flasher utility (Windows/macOS/Linux) for FM-1 and SMK-37. Enables full 1 MB SPI flash backup/restore over plain USB and provides standalone recovery without requiring external hardware dongles (RP2040/Transporter) if a bad firmware flash occurs.

11. **[Slipway by Discodave-Glitch](https://github.com/Discodave-Glitch/slipway) ([Releases](https://github.com/Discodave-Glitch/slipway/releases) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1x8ec69/slipway_free_fm1_firmware_manager_with_a/)):**
    Windows desktop application that catalogues community FM-1 firmwares, validates downloaded packages against published cryptographic hashes, and installs them through Felucca's flasher engine with a stock-first upgrade safety rule and USB recovery guide.

12. **[FM-SWITCH by Drew Robinson (ocean)](https://github.com/ocean/FM-SWITCH):**
    Native iOS companion app that installs and swaps FM-1 firmwares directly from an iPhone/iPad over USB-C using CoreMIDI, featuring an offline catalogue of community firmwares saved locally on the device for on-the-go flashing without a laptop.

13. **[TransitFM1 by Quixotic7](https://github.com/Quixotic7/TransitFM1) ([Web Installer](https://quixotic7.github.io/TransitFM1/)):**
    * **License:** Open Source (GPL-3.0-only). Built upon Dinghy (zvenson), Felucca's platform as carried by SLOOP, and ChoralRoot FM-1's boot stub. Concept proposed by Melodee author Kerem Kilic.
    * **Concept & Role:** Lightweight intermediate "stopover" bridge firmware for the M-VAVE FM-1 designed to safely transition between different community custom firmwares.
    * **Features & Safety Mechanisms:**
      * **V15 Protocol Identity:** Answers the USB-MIDI update protocol disguised as official stock V15 so that third-party web updaters and installers accept it without version conflicts or compatibility rejections.
      * **Crash-Guarded Write Cycle:** Employs a commit-last write strategy where the first sector of the application area is programmed last, protecting the flash from being left in an unbootable state during an incomplete write.
      * **Power Interruption Recovery:** If a cable is unplugged or battery dies mid-flash, cycling power automatically enters update mode (signaled by 3 short key LED flashes and a black screen). Re-running the installer completes the flashing process without requiring emergency hardware recovery. Holding `OCT-` on power-on manually triggers update mode at any time.
      * **Built-in Safety Checks:** Blocks direct flashing over incompatible older firmwares (such as SLOOP or early Felucca betas) and disallows firmware packages that exceed the standard application partition size (such as Baud Girl, which requires returning to true stock V15 first).
      * **Direct Package Flashing:** Includes browser functionality to inspect the currently installed firmware or upload and flash any raw `.fwsc` package directly (including official stock `FM-1.fwsc`).

14. **[M-Flasher by Julius Vitkauskas (jvitkauskas)](https://github.com/jvitkauskas/m-flasher):**
    * **License:** Open Source (GPL-3.0). Cross-platform desktop utility (Windows, macOS, Linux).
    * **Concept:** Low-level hardware backup, restore, and unbricking flashing tool for the M-VAVE FM-1 (and SMK-37). Communicates directly with the JieLi AC791N SoC's built-in USB download mode (`MASKROM` / recovery loader), enabling complete flash extraction, recovery, and re-flashing even when installed firmware is corrupted or unbootable. Automatically creates full flash backups before every write and installs `m-bootloader`.

15. **[m-bootloader by Julius Vitkauskas (jvitkauskas)](https://github.com/jvitkauskas/m-bootloader):**
    * **License:** Open Source (MIT).
    * **Concept:** Open-source replacement bootloader for the JieLi AC791N SoC on the M-VAVE FM-1 and SMK-37.
    * **Features:** Introduces hardware-key triggered USB download mode (holding **REC** on power-up) and an interactive on-device recovery menu, allowing bricked or unresponsive devices to re-enter flashing mode without disassembling hardware or opening cases. Fully compatible with stock firmware, Baud Girl, and custom open firmwares.

16. **[FM-1 Swap by HyruleanHero1988](https://github.com/HyruleanHero1988/FM-1-Swap):**
    * **Platform:** Native Android Application (Kotlin / Jetpack Compose).
    * **Concept:** Portable USB-MIDI firmware manager and offline installer for Android smartphones and tablets. Bundles community firmware catalogues (The Firmware Hub, fm1-editor.com, RedtailWorks) with cached offline `.fwsc` packages (and official stock V15) for swapping firmwares on the go without computers. Automatically performs safety backups before flashing.

17. **[FM-1 Pico Recovery Guide by codeine4563-netizen](https://github.com/codeine4563-netizen/fm1-pico-recovery-guia-en-espa-ol-para-uso-de-raspberry-pi-pico-rp2040-):**
   * **License:** Open Source.
   * **Concept:** Illustrated step-by-step recovery guide (PDF) for reviving soft-bricked or hard-bricked M-VAVE FM-1 units using a Raspberry Pi Pico (RP2040) as an SWD hardware programmer on Windows.

18. **[fm1-flipper-recovery by highdrone](https://github.com/highdrone/fm1-flipper-recovery):**
    * **License:** Open Source.
    * **Concept:** Flipper Zero boot-key recovery utility and illustrated macOS / Windows connection manual for triggering JieLi mask-ROM USB download mode without disassembling hardware.

19. **[FM-1 Backup & Restore for Android by workeffortwaste](https://github.com/workeffortwaste/fm1-backup-restore) ([Releases / APK](https://github.com/workeffortwaste/fm1-backup-restore/releases)):**
    * **Platform:** Native Android Application (Material 3 Expressive & Material You design).
    * **Concept:** Standalone mobile backup and full-flash snapshot utility for the M-VAVE FM-1.
    * **Features:** Takes complete byte-for-byte snapshots of device flash (firmware, settings, projects, songs) straight from an Android phone over USB-C (safely leaving the protected bootloader untouched) to enable instant factory rollback, disaster recovery, and seamless on-the-go firmware hopping without data contamination. Includes custom FM-1 styled themes.

20. **[Sloop Pocket by tar_anton](https://testflight.apple.com/join/2TTUuEGd) ([Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1xh3c2f/i_made_an_iphone_companion_app_for_the_fm1/)):**
    * **Platform:** Native iOS Application (iPhone, iOS 17+, available via Apple TestFlight).
    * **Concept:** Standalone iPhone companion and librarian app for the M-VAVE FM-1 running SLOOP firmware, offering project management, offline song previewing, DAW stem export, and a live performance mixer.
    * **Features:**
      * **Project Backup & Library:** Full project save and restore over USB-C/Lightning (including current loop, sections A–D, user sounds, and drum samples), with project sharing and clean project initiation.
      * **Offline Project Previewer:** Audio and 4-track visual note/drum roll playback with mute controls without needing hardware connected.
      * **Multi-Track DAW Stem Export:** Exports projects to standard MIDI files, master stereo WAV, or individual 4-track isolated audio WAV stems directly into GarageBand and other mobile/desktop DAWs.
      * **Live Assistant Screen (v0.13.1):** 4-track mixer with vertical faders, mute/solo, track filters, effect sends, master Duck and Dust controls, momentary FX latching, scene memory with smooth transitions, bidirectional knob feedback, and full Undo/Redo.
      * **OTA Firmware Updates:** Checks for and flashes SLOOP firmware updates directly to the FM-1 over USB.

### 3.2. Reverse Engineering, Disassembly & Decompilation


 1. **[M-VAVE FM1 Hardware Architecture & Protocol Reference (Local)](REVERSE_ENGINEERING.md):**
    In-depth local technical reverse-engineering documentation: JieLi AC791N hardware overview, UBOOT memory map, Qt container analysis, verified two-step device-pull SysEx OTA protocol, and flasher implementation.

 2. **[AL-255/FM-1-RE Repository](https://github.com/AL-255/FM-1-RE):**
    Reverse-engineering repository for M-VAVE FM-1 firmware. It reveals that the stock FM-1 firmware itself utilizes a Dexed/msfa-derived 6-operator FM synthesis engine, and contains V13/V14 disassembly function maps, XIP flash offset analyses, as well as an experimental custom firmware build.

 3. **[ghidra-jieli Repository](https://github.com/kagaimiq/ghidra-jieli):**
    Ghidra processor extension for disassembling and decompiling JieLi `pi32`, `pi32v2`, and `q32s` CPU binaries.

 4. **[fm1-bootloader by jvitkauskas](https://github.com/jvitkauskas/fm1-bootloader):**
    Readable C source implementation of the stock FM-1 bootloader, reverse-engineered and reconstructed byte-identically from the hardware image.

 5. **[MVAVE-M-UPGRADE-decompiled by entitymar](https://github.com/entitymar/MVAVE-M-UPGRADE-decompiled):**
    Full decompilation and resource extraction of the official M-VAVE M-UPGRADE macOS and Windows updater applications.

 6. **[jl-misctools Repository](https://github.com/kagaimiq/jl-misctools):**
    Utilities for inspecting and converting JieLi firmware containers, key files, and UI resources.

 7. **[M-VAVE SMK-37 PRO Reverse Engineering Gist (by probonopd)](https://gist.github.com/probonopd/18b3ed65a69d0229eb630c47d7e316dc):**
    Research notes on unpacking `.fwsc` firmware files for the M-VAVE SMK-37 PRO (DX7 FM MIDI keyboard) and identifying the underlying JieLi AC791N platform structure using `jl-misctools`.

### 3.3. Vendor SDKs, Architecture & JieLi Community Research

 1. **[JieLi AC79 AIoT SDK (Gitee Repository)](https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK):**
    Official C SDK codebase for AC79 series (WL82 / AC791N) microcontrollers, containing board support packages (BSP), linker scripts, and hardware register headers.

 2. **[JieLi AC79 Official Peripheral Documentation](https://doc.zh-jieli.com/AC79/zh-cn/release_v1.0.3/module_example/peripherals/sd.html):**
    Official documentation covering AC79xx series peripheral hardware modules (SD controller, GPIO, UART, SPI, I2S).

 3. **[JieLi SoC Forum Thread (esp8266.ru)](https://esp8266.ru/forum/threads/jl-soc.5500/):**
    Community research thread discussing JieLi SoCs, SDKs, toolchains, flash recovery, and hardware boot modes.

### 3.4. Emulators, Simulators & Virtual Instruments

 1. **[fm1-emulator by Simon Johansson](https://github.com/simonjohansson/fm1-emulator):**
    Rust-based desktop emulator for the M-VAVE FM-1. Executes firmware binaries (`.fwsc`, `.elf`, `.bin`) on desktop operating systems, emulating the JieLi dual-core CPU and peripheral state.

 2. **[m-wave-fm1-browser-emulator by shcherbakov7](https://github.com/shcherbakov7/m-wave-fm1-browser-emulator):**
    Rust/WebAssembly in-browser emulation of the AC791N SoC's two `pi32v2` cores and the FM-1's color display.

 3. **[SLOOP FM-1 Simulator by Chance Roth](https://github.com/chancethemaker/sloop-fm1-sim) ([Web Simulator](https://chancethemaker.github.io/sloop-fm1-sim)):**
    Self-contained in-browser interactive simulator of the SLOOP / Felucca firmware for the FM-1, allowing testing controls, sound engines, and workflow directly in the browser without physical hardware.

 4. **[FM-1 Mobile by hb3p8](https://github.com/hb3p8/fm1-mobile-emu) ([Web App & Mobile Emulator](https://hb3p8.github.io/fm1-mobile-emu/)):**
    * **Platform:** Mobile-first progressive web app (PWA) with full offline support (Add to Home Screen on iOS/Android).
    * **Concept:** Seven real FM-1 C firmware engines compiled to WebAssembly running inside an accurate hardware-simulated touch panel matching the physical FM-1 instrument layout.
    * **Switchable Firmwares:** On-the-fly switching between **X0X** 1.0.6 (acid/TR-style drums & 303), **Felucca** 1.6 (multi-engine synth & 64-step sequencer), **SLOOP** 2.6 (live groovebox), **FiMba-1** 0.6.1 (physical modeling kalimba), **Melodee** 1.4.0-rc.1 (CZ-1, FM6, Prophet-5 & microtonal), **AMB-1** 1.1 (generative ambient), and **MAKU** 0.1 (generative intermission soundscapes).
    * **Features & Architecture:**
      * **AudioWorklet Hardware Clock:** Accurate timing loop where rendering audio advances the device's clock, driving firmware audio interrupts and main loops exactly as on physical hardware.
      * **Display & Graphics:** Real-time 240 × 240 display output drawn via WebGL with optional retro xBR smoothing filter.
      * **Responsive Ergonomics:** Adaptive portrait and landscape touch layouts, multi-touch keys with glides, encoder drag controls, button latching ("Hold" mode for SEL combos), and computer keyboard shortcuts.
      * **Persistent Storage:** Browser local storage isolates and preserves patterns, projects, and custom loops separately across each firmware switch.

 5. **[Virtual-FM-1 by Bockage (jbschooley)](https://github.com/jbschooley/Virtual-FM-1) ([Releases](https://github.com/jbschooley/Virtual-FM-1/releases) | [Video Demo](https://www.youtube.com/watch?v=HEgBhuk4VSM) | [Reddit Discussion](https://www.reddit.com/r/MVaveFM1/comments/1xga9x0/vibe_fm_plugin/)):**
    * **Formats:** Standalone application, VST3, AU, LV2, and AUv3 audio plugin for macOS (Apple Silicon / Intel), Windows (10/11 64-bit), Linux (x86-64), and iOS/iPadOS.
    * **Concept:** Comprehensive software replica and DAW plugin host for the M-VAVE FM-1 (often referred to in community videos as the "Vibe FM Plugin"). Functions as an Expanded Softsynth Plugin (ESP) that runs real FM-1 firmware engines compiled directly from source, renders the physical device's 240 × 240 screen and front panel, and bidirectionally synchronizes presets, sequences, and live knob tweaks with physical hardware.
    * **Multi-Firmware Engine Support:**
      * **Felucca 1.6.1:** 13 synthesis engines (ANALOG, FM6, PHASE, LOFI, SAMPLE, VOICE, TRIO, WHEEL, GRAIN, PHYS, NOISE, SLICE, DRUM), 4 parts, step conditions (1:2–4:4, FILL), 292 DAW automation parameters, Device front panel tab, and Pull/Send/Live sync.
      * **SLOOP 2.7:** 4-track groovebox with 15 arp modes, 3 synth tracks + 1 programmable drum kit, live punch-in FX, themes, Section A–D, and Live synchronization.
      * **Melodee 1.4.1:** Prophet-5, Casio CZ-1, 6-op FM6, and Commodore 64 SID synthesis engines, SID drum kits, shared U001–U384 preset library, and Live sync.
      * **ChoralRoot 0.23:** Quixotic7's Monome/Orchid chord engine, DX7/CZ-1 SysEx import/export, and complete backup synchronization.
      * **FM1 Open V12:** M-VAVE's official open firmware built from source, featuring 8 tracks, 6 sound engines, 16 demo projects, and direct sample bank / project transfers.
      * **baud girl FM-1+VA 101:** Virtual Analog + FM synthesis, 128-preset library editing, and pattern transfers.
      * **Stock V15:** Authentic Yamaha DX7-compatible FM engine editing and preset playback.
    * **Key Features & Hardware Integration:**
      * **Hardware Character Aliasing:** When running in DAW projects at sample rates other than 44.1 kHz, the engine runs internally at the FM-1's native 44.1 kHz rate with downsampling to reproduce authentic hardware DAC aliasing and grit (with sub-millisecond host latency reporting).
      * **Device Tab Screen & Panel:** Faithful on-screen reproduction of the 240 × 240 display, encoders, buttons, and piano keys for all supported firmwares.
      * **Bidirectional Hardware Sync:** Pull presets/projects from physical hardware, Send edits to hardware without saving, or engage `Live` mode for instant two-way knob and step editing over USB-C or Bluetooth MIDI.
      * **Modern Library Management:** Stores shared presets as human-readable JSON files in `Documents/Virtual FM-1/Banks`, with `.trash` recovery and DAW project-isolated sound states.

 6. **[FM1VST by Quixotic7](https://github.com/Quixotic7/FM1VST):**
    DAW plugin host (VST3, AU, and standalone) running Felucca-family firmwares (ChoralRoot, Felucca, Melodee) compiled directly from source and switchable on the fly.

 7. **[fm1-emu by Joakim Eriksson](https://github.com/joakimeriksson/fm1-emu) ([Web Emulator](https://joakimeriksson.github.io/fm1-emu/)):**
    Full hardware emulator for the M-VAVE FM-1 running unmodified firmwares natively and directly in the browser via WebAssembly:
    * **Hardware & CPU Emulation:** Full WebAssembly virtual machine emulating the JieLi AC791N SoC (dual-core 32-bit `pi32v2` CPU), 240 × 240 display, tactile buttons, knobs, and audio synthesis.
    * **Firmware Loading:** Runs community firmwares (Felucca, X0X, FM1 Quest, AMB-1, FM-1 SID, ORBIT, FiMba-1, stock M-VAVE) downloaded on the fly, with support for uploading custom `.fwsc` update packages.
    * **Features:** Configurable emulated clock speed, Web MIDI input routing with channel selection, support for loading Yamaha DX7 32-voice `.syx` banks for stock firmware, and computer keyboard / touch panel controls. Also includes an experimental SMK-37 emulator.

 8. **[FM-1 Studio by thingsapart](https://github.com/thingsapart/fm1-studio):**
    * **License:** Open Source (GPL-3.0).
    * **Platform:** Native Android Application (Java / WebAssembly runtime).
    * **Concept:** Multi-firmware companion environment and touch synthesizer for Android smartphones and tablets.
    * **Features:**
      * Hosts real FM-1 C firmware engines (SLOOP, FM1 MOVE, Felucca, sloopDX) compiled to WebAssembly running directly on Android.
      * Full touch panel simulating the FM-1's 240 × 240 color display, keys, and rotary encoders.
      * Integrated touch piano roll, sound editors, preset management, and USB-MIDI integration to synchronize projects with physical FM-1 hardware.

 9. **[PIGEON WebAssembly Emulator](https://theshrimpblimp.github.io/pigeon-website/webapp/emu/) ([Project Page](https://theshrimpblimp.com/pigeon/)):**
    Firmware-based WebAssembly emulator with the 240 × 240 interface, user sample loading, chopping, sequencing, audio playback, screen-reader support and WAV/MP3 output recording. It runs in the browser without hardware; it does not emulate the physical USB sampling peripheral.

 10. **[FM-1 Grid by jasonbot](https://github.com/jasonbot/fm1-grid):**
     * **License:** Open Source (GPL-3.0). Built in Rust with `gpui-kit`.
     * **Platform:** Native desktop application (macOS / Linux / Windows).
     * **Concept:** Multi-instance emulator running four virtual M-VAVE FM-1 units simultaneously in a 2×2 grid, each with its own independent firmware and screen.
     * **Features:**
       * **Four Independent Firmware Panes:** Ships loading SLOOP, Felucca, FM1 Open, and ChoralRoot out of the box; any pane can load arbitrary community `.fwsc` firmware binaries.
       * **Interactive Front Panel:** Large mirrored FM-1 front panel mirroring the active unit's 240 × 240 display (with NTSC filter, hqx upscaling up to 4x, and dynamic dominant color palette backdrop), responsive keys, buttons, rotary encoders, and LEDs.
       * **Hardware & MIDI Routing:** Devices tab with live USB hardware management and inter-unit MIDI node graph routing.
       * **Resource Efficiency:** Inactive or unselected panes power down to zero CPU cost.

 11. **[Harbor by markterm](https://github.com/markterm/harbor):**
     * **License:** Open Source (GPL-3.0).
     * **Platform:** Native Android Application (phones and tablets).
     * **Concept:** Android runner and emulator host that plays community M-VAVE FM-1 firmwares unchanged via the [fm1-emu](https://github.com/joakimeriksson/fm1-emu) engine.
     * **Features:** Full touch UI mirroring the FM-1 panel; plays via USB-MIDI, Bluetooth LE MIDI, inter-app audio, and connected computers; acts as a standard system MIDI device for other music apps.

12. **[FM-1 Emulator Desktop (hdavid fork) by hdavid](https://github.com/hdavid/fm1-emulator):**
    * **Platform:** Native desktop application for macOS, Windows, and Linux.
    * **Concept:** High-performance Rust port of simonjohansson's FM-1 emulator featuring low-latency audio rendering and direct bi-directional USB-MIDI support.

13. **[Felucca for tuttidaw by weavejam](https://github.com/weavejam/Felucca):**
    * **Platform:** Browser-based tuttidaw audio plugin.
    * **Concept:** Adapts Felucca's browser emulator into a DAW audio plugin, rendering Felucca song projects or live MIDI offline into a polished master mix and 4 discrete audio stems.

### 3.5. Web Editors, Patch Librarians & Companion Utilities

 1. **[FM-1 Utility](https://fm1-utility.pages.dev/):**
    Lightweight, dependency-free WebMIDI parameter editor and diagnostic tool for the FM-1.

 2. **[FM-1 Workbench by thegiantsnail](https://github.com/thegiantsnail/fm1-workbench-public) ([Web App](https://fm1-workbench.web.app)):**
    Multi-platform utility suite (Web app, Android app, VST3/CLAP plugin, and Model Context Protocol MCP server) featuring a DX7 preset library, voice randomizer/mutator, drum sequencer, and MIDI file player.

 3. **[fm1-read-voice by Christian Zietz](https://github.com/czietz/fm1-read-voice):**
    Python utility to request and read the currently active sound patch back from the FM-1 hardware over USB-MIDI SysEx.

 4. **[OpenPatch.es (Yamaha DX7 Patch Utility)](https://openpatch.es/):**
    Web utility for DX7 FM patches allowing WAV upload to recover/match patches, live auditioning, sequencing, modifying, mutating, and exporting patch sets as `.syx` files.

 5. **[DXcompanion](https://dxcompanion.uk/):**
    Browser-based patch and parameter editor for the Yamaha DX synth family featuring experimental M-VAVE FM-1 support.

 6. **[Dexed by asb2m10](https://asb2m10.github.io/dexed/):**
    Open-source DX7 plugin and editor. The FM-1 hardware natively responds to Dexed real-time parameter-change SysEx messages for live DAW sound design.

 7. **[FM-1 Pulses by mene311](https://github.com/mene311/fm1-pulses) ([Web App](https://mene311.github.io/fm1-pulses/)):**
    Browser-based generative MIDI sequencer and pattern generator for the M-VAVE FM-1 (Web MIDI API / PWA, runs on desktop/mobile). Generates reproducible 64-step banks with parameter drift and can freeze them directly into the hardware pattern slots over SysEx (supported on Baud Girl / FM-1+VA firmware), or broadcast live MIDI notes in real time.

 8. **[sloop-fm1-go by jahlib](https://github.com/jahlib/sloop-fm1-go) ([Releases / APK](https://github.com/jahlib/sloop-fm1-go/releases)):**
    * **License:** Open Source (GPL-3.0).
    * Android-native touchscreen companion and project editor for SLOOP custom firmware (based on the SLOOP web editor). Allows editing tracks, synth parameters, samples, and sequence patterns directly from an Android smartphone or tablet over USB-MIDI.

 9. **[SLOOP 8-Track Web Workstation by smhulme](https://github.com/smhulme/sloop-web-8trk):**
    Hybrid production environment driving SLOOP's four hardware tracks over WebMIDI while adding four synchronized browser audio tracks alongside them.

10. **[Choppa Lite by WaveLoop](https://waveloop.app/toys/choppa):**
    In-browser, installable sampler web application for the FM-1. Allows recording up to 12 seconds of audio, chopping it into 16 pads, and transferring the sample bank directly to the FM-1 over USB-MIDI. Built for Felucca and SLOOP firmware families (also available for iOS, with Android version planned).

11. **[take-taker by groundstation1](https://github.com/groundstation1/take-taker) ([Releases / APK](https://github.com/groundstation1/take-taker/releases)):**
    * **License:** Open Source (MIT).
    * Android multitrack audio & video recorder designed specifically for USB audio devices.
    * When paired with the **Melodee** firmware on FM-1 (which exposes all 4 audio outputs as discrete USB audio streams), it bypasses Android's default stereo downmixing via raw USB mode to record each channel as an independent track.
    * Exports individual lossless FLAC stems, normalized MP3 mixdowns, or synced video takes (using phone camera footage or rendered live scrolling waveform overlays).

12. **[FM-1 Patch Bank Utility (Soundspirate) by klonecom](https://github.com/klonecom/M-VAVE-FM1-LOADER---):**
    * Single-file, client-side browser Web MIDI tool for transmitting `.syx` patch bank files to the FM-1 with auto-detection and SysEx framing validation.

13. **[FM1 Bank Sender by Leo Maimoni](https://github.com/leomaimoni/fm1-bank-sender):**
    * Android utility app to transmit DX7 sound bank files (`.syx`, 32-voice banks or single patches) to the M-VAVE FM-1 via USB-OTG without entering special receive modes.

14. **[Felucca Editor Skill by hunterxiong2026](https://github.com/hunterxiong2026/fm1-felucca-editor-2026):**
    * **License:** Open Source (MIT).
    * Natural language LLM / Agent skill integration for controlling the M-VAVE FM-1 (running Felucca firmware) over MIDI SysEx for tone design, multi-track arranging, and song playback.

15. **[Oscuro Companion Protocol & File Bridge by kartun83](https://github.com/kartun83/oscuro-companion-protocol):**
    * **License:** Open Source (Apache-2.0).
    * **Concept:** High-speed phone ↔ hardware file bridge and companion communication service over USB (smartphone acts as USB host, device runs as USB peripheral).
    * **Architecture & Features:**
      * Native Android USB-Host app (Kotlin) paired with a lightweight RAM firmware payload (`usbfiles.c` + `usbven.c`) executed on the JieLi AC791N SoC.
      * Fast bidirectional file listing, patch browsing, sample transfer, and remote UI state synchronization on 240 × 240 displays without requiring flash wear.
      * Developed for M-VAVE SMK-37 (under the Oscuro project) and architecturally adaptable to the M-VAVE FM-1 given their shared AC791N SoC and USB stack. Includes desktop Python host mock (`pyusb`) and wire protocol documentation.

16. **[AMÉTRA-001 by Sopozcreations](https://ametra-liard.vercel.app/) ([Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1x89ias/am%C3%A9tra001_a_free_polymetric_sequencer_in_the/)):**
    * **Concept:** Free browser-based polymetric MIDI sequencer and groove generator designed for the M-VAVE FM-1 (and compatible with external MIDI gear and DAWs via Web MIDI).
    * **Features:**
      * **4 Polymetric Loop Lanes:** Four polyrhythmic lanes running completely independent step counts (e.g. 16 vs 7 steps vs triplets) that drift continuously out of phase and realign over time.
      * **Generative Chance & Mutation:** Per-track hit stutter, drift, and random dice-roll probability parameters.
      * **Audio & MIDI Integration:** Supports internal sample playback or live microphone recording alongside Web MIDI transmission, plus direct WAV audio capture and standard MIDI file export.
      * **User Interface:** Clean bilingual (English / French) responsive UI with built-in interactive help tooltips.

17. **[PIGEON Web Sample Tool & Studio](https://theshrimpblimp.github.io/pigeon-website/webapp/pigeon/) ([Documentation](https://theshrimpblimp.com/pigeon/)):**
    * In-browser sample preparation, slicing, and backup workstation for the PIGEON sampler firmware.
    * Allows importing custom audio files into Song 1 / Song 2 slots and a 16-pad drum kit, previewing waveforms, automatic transient slicing (up to 32 chops per song), trimming boundaries, offline MP3/ADPCM encoding, and transmitting complete banks with up to 500 KiB usable sample storage to the FM-1 over Web MIDI. The 0.5 tool adds reusable chop collections, selected-chop trimming, playback controls and normalization. Complete session archives preserve samples and patterns before firmware updates.

18. **[Eight Bells V3 by Discodave-Glitch](https://discodave-glitch.github.io/eight-bells/) ([Desktop Releases](https://github.com/Discodave-Glitch/eight-bells/releases)):**
    * Multi-engine pattern generator and live MIDI performance workstation for the FM-1 and its custom firmwares.
    * Features 28 rhythm/melody generation engines (Euclidean rhythms, Markov chains, chaos math), 8 tracks (up to 64 steps each), live screen view (Now & Next, side-by-side Generate/Play/Record, bar queue buttons, per-track Mute/Solo/Lock, track zoom editing, 10 dice generators, and 16 punch FX), recent takes recorder, and cross-platform desktop releases (Windows/macOS) with responsive mobile/tablet layout support.

19. **[VIZZ by kloti](https://vizz.netwove.com/):**
    * **Concept:** Interactive 3D and 2D real-time browser visualizer and live performance stage for the M-VAVE FM-1 (and external MIDI/audio devices).
    * **Features:**
      * Over 20 live 3D visual scenes driven by note events, steps, bars, velocities, and audio spectrum (bass/mids/highs analysis via USB audio or mic).
      * Custom 2D/3D Studio for building personal visual scenes with custom shaders, textures, GIFs, moving heads, and cameras.
      * Includes an optional dedicated FM-1 companion firmware build (derived from Skiff with `SEQ MIDI OUT`) allowing the FM-1 to transmit live sequencer steps, mutes, and transport state over USB to dynamically modulate visual elements.
      * Built-in software demo sequencer, computer keyboard piano controller, and video recording export.

20. **[FIZZ by Quixotic7](https://github.com/Quixotic7/FIZZ) ([Web Emulator & Preview](https://quixotic7.github.io/FIZZ/)):**
    * **License:** Open Source (MPL-2.0). C99 deterministic audio/sequencer core.
    * **Concept:** Advanced parameter-locking step sequencer for FM TONE (ChoralRoot's 6-op FM synth engine) running as an FM1VST module and standalone web simulator, designed for live panel integration with physical FM-1 hardware via RemoteFM1.
    * **Features:** 8 tracks sharing 16 polyphonic FM voices, 128 sound patch pool, deep parameter locks (p-locks), microtiming, condition gates, probability/chance trigs, ratchets, and up to 6-note polyphonic chords per step.
    * **Hardware Panel Bridge:** Phase 1 uses physical FM-1 hardware as an active panel controller and screen display via RemoteFM1 while rendering DSP on host; Phase 2 standalone `.fwsc` firmware target in development.

21. **[Forge Remote by Khantipol Kasemsant](https://forge.kktp.net/) ([Reddit Teaser](https://www.reddit.com/r/MVaveFM1/comments/1xfviiw/teaser_forge_remote_an_ipad_companion_app_for_the/)):**
    * **Platform:** Native iPad / iOS companion application.
    * **Target Firmware:** [FORGE ONE](https://forge.kktp.net/one/) (4-track groovebox firmware).
    * **Features:** Full-screen touch control over FORGE ONE via USB-C: 4-track step pattern grid with touch-editing for notes, ties, accents, slides, ratchets, nudge, and drum lanes; sound design page with oversized virtual encoders for synth engines and presets; per-track mixer with delay/reverb/chorus sends; and real-time bidirectional synchronization with physical FM-1 knobs and keys.

22. **[M-VAVE FM1 Editor & Librarian by Benny Sparra (benny-sparra)](https://github.com/benny-sparra/fm1-dx7-patch-importer) ([Web App](https://benny-sparra.github.io/fm1-dx7-patch-importer/)):**
    * **Concept:** In-browser DX7 voice editor and patch librarian running entirely client-side via Web MIDI.
    * **Features:** Full visual editing of every standard Yamaha DX7 voice parameter and internal FM-1 DSP effects (reverb, delay, chorus). Starts with the FM-1's four factory preset banks; allows building, reordering, and importing custom banks, with one-click single-patch or complete 32-voice bank transmission to hardware over SysEx.

23. **[M-Wave FM-1 SysEx Patch Curator Pro by Grandsummoner](https://github.com/Grandsummoner/fm-1-helper) ([Web App](https://grandsummoner.github.io/fm-1-helper/FM-1%20Helper.html)):**
    * **Concept:** Web-based DX7-compatible SysEx bank curator and compiler designed specifically for the M-VAVE FM-1.
    * **Features:** Streamlines ingesting arbitrary DX7 `.syx` patch data, auditioning and managing voices, and compiling clean, stable, bank-ready SysEx packages for flawless transmission to FM-1 hardware.

24. **[FM-1 Pulses (Felucca) by mene311](https://github.com/mene311/fm1-pulses-felucca) ([Web App](https://mene311.github.io/fm1-pulses-felucca/)):**
    * **Concept:** Dedicated Felucca-adapted version of the browser-based generative 64-step sequencer and pattern matrix for the FM-1.
    * **Features:** Tailored to the Felucca editor protocol and a 4×4 track/project matrix, featuring an interactive piano roll, real-time MIDI playback, and direct SysEx pattern freezing into hardware memory.

25. **[Consort by zisonzishen0415-stack](https://github.com/zisonzishen0415-stack/sloop-consort) ([Web App](https://zisonzishen0415-stack.github.io/sloop-consort/)):**
    * **Platform:** Web application and Android companion utility.
    * **Target Firmware:** SLOOP 2.7+.
    * **Features:** Live sample recording and direct upload to hardware flash, responsive touch punch-in FX performance pads, complete project backup/restore, and custom UI themes.

26. **[SLOOP Editor Desktop by Catnip233](https://github.com/Catnip233/sloop-editor-desktop):**
    * **Platform:** Cross-platform desktop application (Electron for Windows and macOS).
    * **Concept:** Standalone offline desktop client package for the SLOOP 2.5 web editor, allowing offline parameter sculpting and project management without relying on internet access or browser WebMIDI quirks.

27. **[dx7toFM1 by s0fx2](https://github.com/s0fx2/YamahaDX7_to_FM-1):**
    * **License:** Open Source.
    * **Concept:** Python CLI utility that parses standard 32-voice Yamaha DX7 SysEx banks (`.syx`) and splits them into clean individual patch files formatted for import into FM-1 firmware libraries.

28. **[Falua by ehn96](https://github.com/ehn96/Falua):**
    * **Platform:** VST3 / AU audio plugin and standalone desktop application for DAW integration.
    * **Concept:** Compiles and runs JIANT's synthesis algorithms natively on host computers, allowing producers to compose in DAWs with identical sound engines.

29. **[Pocket Six by NOKILL Pedal Co.](https://github.com/nokill-pedal-co/pocket-six) ([Play Web App](https://nokill-pedal-co.github.io/pocket-six/)):**
    * **Concept:** Browser-based 6-operator FM synthesizer and DX7 sound design workstation inspired by the M-VAVE FM-1 pocket synthesizer and the Yamaha DX7. Runs with zero install on phones, tablets, or computers (`index.html` + `ps-dsp.js`).
    * **Sound Engine & Library:** 6 operators, all 32 DX7 algorithms with feedback, 4-rate/4-level envelopes, pitch envelope, keyboard scaling, 6-wave LFO, and optional amp ADSR. Includes a built-in searchable DX7 library of 607 banks (10,494 distinct sounds, including original Yamaha factory ROMs) with support for loading custom `.syx` patch banks.
    * **Performance Features:** Multi-touch keybed with glides, pitch bend/mod touch strips, laptop QWERTY/Z-row input, Web MIDI USB controller support, 16-step polyphonic chord sequencer (16 patterns with keyboard transposition), arpeggiator, and a 6-effect DSP chain (filter, distortion, phaser, chorus, delay, reverb).

30. **[fm1-manager by bratta](https://github.com/bratta/fm1-manager):**
    * **License:** Open Source (MIT).
    * **Concept:** Standalone desktop and web preset manager, bank editor, and firmware restoration tool for the M-VAVE FM-1.

31. **[Felucca Tutor by wochende](https://github.com/wochende/FM-1-Felucca-Tutor):**
    * **License:** Open Source.
    * **Concept:** Interactive educational firmware that teaches the principles of FM synthesis, sound design, sequencer chaining, and groove creation directly on the FM-1 screen.

32. **[SLOOP & Felucca SysEx Editors by hunterxiong2026](https://github.com/hunterxiong2026/fm1-sloop-editor-2026):**
    * **License:** Open Source.
    * **Concept:** DeepSeek Harness skills and specialized SysEx parameter control scripts for SLOOP 2.3 and Felucca firmware builds over Web MIDI.

33. **[fm1-midi-converter by balancechiang](https://github.com/balancechiang/fm1-midi-converter):**
    * **License:** Open Source.
    * **Concept:** Single-page offline Web MIDI project converter that translates and parses sequence arrangements between standard Standard MIDI Files (`.mid`) and FM-1 project data structures.

34. **[mwave-fm1-linux-vst by SpeakingColors](https://github.com/SpeakingColors/mwave-fm1-linux-vst):**
    * **License:** Open Source.
    * **Concept:** Native Linux VST controller plugin providing live parameter automation, patch librarianship, and bidirectional MIDI communication with physical FM-1 hardware.

35. **[Jexed (JSFX Port of Dexed)](https://www.reddit.com/r/MVaveFM1/comments/1xgre3k/jexed_a_jsfx_port_of_dexed/):**
    * **Platform:** Cockos REAPER JSFX script / instrument plugin.
    * **Concept:** Modern JSFX port of the Dexed Yamaha DX7 synthesizer engine for Cockos REAPER, featuring a modernized UI, clear functional visualizations of 8-stage rate and level envelope behaviors, and built-in preset collections for sound design.

### 3.6. Developer Frameworks, UI Designers & Curated Collections


 1. **[MvaveFM1-Designer by Quixotic7](https://github.com/Quixotic7/MvaveFM1-Designer) ([Web App](https://quixotic7.github.io/MvaveFM1-Designer/)):**
    Visual UI and panel state designer for FM-1 custom developers (mapping key/button LED states, knob functions, and OLED/TFT screen layouts).

 2. **[foma by konsumer](https://github.com/konsumer/foma) ([Web Companion](http://konsumer.js.org/foma/)):**
    * **License:** Open Source.
    * **Concept:** *Fm-One Makers' Assistant* — streamlined zero-install Docker development environment for the M-VAVE FM-1.
    * **Features:** Allows developers to write FM-1 firmware in C with nothing installed locally except Docker (`konsumer/foma-toolchain`). Editing a single C file triggers live hot-reloading in the browser WebAssembly emulator upon saving, with one-click direct WebMIDI hardware flashing from the same interface (`./fm1 dev`).

 3. **[Schwung by Charles Vestal](https://github.com/charlesvestal/schwung):**
    Open-source music architecture framework for standalone devices. Core synthesis code and models (TR-909, TR-808, TB-303, PSX Verb) are shared with the X0X and Lunar Modulator FM-1 firmwares.

 4. **[FM1Kit by ocean](https://github.com/ocean/FM1Kit):**
    * **License:** Open Source (MIT).
    * **Concept:** Swift toolkit and CoreMIDI framework for communicating with, configuring, and flashing the M-VAVE FM-1 synthesizer from native macOS and iOS applications.

 5. **[setup-fm1-emulator by DimmKirr](https://github.com/DimmKirr/setup-fm1-emulator):**
    * **License:** Open Source (MIT).
    * **Concept:** GitHub Actions workflow action that automatically provisions and configures the `fm1-emu` headless WebAssembly emulator in CI/CD pipelines to run automated UI and regression tests via Playwright.

 6. **[awesome-fm-1 by cicloid](https://github.com/cicloid/awesome-fm-1):**
    A curated awesome-list of resources, custom firmwares, tools, and open-source projects for the M-VAVE FM-1 pocket synthesizer.

 7. **[Fluyt by rgrvmusic](https://www.reddit.com/r/LogueSDK/comments/1x3upww/fluyt_felucca_synth_engines_for_drumlogue/):**
    Community port and adaptation of the open-source **Felucca** synthesizer engines from the M-VAVE FM-1 to the **Korg drumlogue** (LogueSDK user synth unit), demonstrating cross-platform portability of Felucca DSP algorithms.

 8. **[M-VAVE FM-1 Firmware Ports to M5Stack Tab5 by zircothc](https://github.com/zircothc/x0x-tab5):**
    Cross-platform ports of popular M-VAVE FM-1 open-source firmwares to the **M5Stack Tab5** (ESP32-P4) with full touchscreen control, USB-MIDI host mode, MIDI learn, and ready-to-flash binary releases:
    * **[x0x-tab5](https://github.com/zircothc/x0x-tab5):** Port of the X0X groovebox (TR-909, TR-808, two TB-303s, break player).
    * **[sloop-tab5](https://github.com/zircothc/sloop-tab5):** Port of the SLOOP 4-track live groovebox firmware.
    * **[jiant-tab5](https://github.com/zircothc/jiant-tab5):** Port of the JIANT bio-synthetic performance synthesizer OS.

 9. **[FM-1 Learning Web by itoyohane](https://github.com/itoyohane/fm1-learning-web):**
    * **Concept:** Interactive web documentation and reference manual for exploring, learning, and comparing different M-VAVE FM-1 community firmwares, control layouts, and cheat sheets.

10. **[fm1-dev-wiki by sbegueria](https://github.com/sbegueria/fm1-dev-wiki):**
    * **Concept:** Comprehensive community developer wiki and technical reference documenting memory maps, register definitions, peripheral clocks, and compiler flags for the JieLi AC791N SoC on FM-1 and SMK-37.

11. **[fm1-firmware-collection by 2bbb](https://github.com/2bbb/fm1-firmware-collection):**
    * **Concept:** Automated aggregation repository linking all open-source community M-VAVE FM-1 firmwares as Git submodules with continuous integration matrix compilation.

12. **[mvave-fm1 Claude Skills & Podman Build Container by Max Fridbe (maxfridbe)](https://github.com/maxfridbe/mvave-fm1):**
    * **License:** Open Source.
    * **Concept:** Ready-to-use AI agent skills for Claude Code alongside an automated Podman/Docker build environment for the M-VAVE FM-1.
    * **Features:** Bundles two modular Claude skills (`mvave-fm1-firmware` for backing up, flashing, restoring, and recovery; `mvave-fm1-software-development` for writing firmware with JieLi AC791N hardware APIs, memory maps, and safety rules), complemented by a hash-pinned Podman container image compiling Dinghy, Felucca, and ORBIT in headless CI without local toolchain pollution.

### 3.7. Custom Soundbanks & Preset Collections


Dedicated sound banks, commercial patches, and SysEx preset packs tailored for the M-VAVE FM-1:

 1. **[Ambient & Dreams by NatLife Sounds](https://natlifesounds.com/product/ambient-dreams-for-m-vave-fm-1-fm-synthesizers/):**
    * **Format & Compatibility:** Standard 32-preset SysEx bank (`.syx`) with FM-1 USB installation instructions (cross-compatible with Yamaha DX7/DX7 II, Korg Opsix 2.0, Korg Volca FM/FM2, Dexed, Arturia DX7 V, and NI FM8).
    * **Sound Design:** 32 tailored ambient FM presets designed to showcase soft, harmonic FM textures without harsh digital dissonance — includes 1 AAH vocal preset, 5 bass patches, 2 FX textures, 2 leads, 5 ambient pads, 10 plucks, and 8 melodic synth sounds. Includes video demo walkthroughs and tutorials.

 2. **[FM-1 Banks by mene311](https://github.com/mene311/fm1-banks):**
    * **Format:** 26 curated, themed banks of 32 DX7 voices (832 patches total) formatted specifically for the M-VAVE FM-1.
    * **Sound Categories:** Includes Synthwave, Acid, Techno, Vintage Drums, Ambient, Industrial, and Classic FM collections, bundled with a Python SysEx batch transmission tool for rapid flashing.

 3. **[Aquanode Soundscapes by aquanodemusic](https://github.com/aquanodemusic/aquanode-soundscapes):**
    * **Format:** Free sound design collections and DX7 SysEx banks tailored for the FM-1.
    * **Sound Design:** Atmospheric soundscapes, custom FM timbres, and recreations of Ekhozone's Infinite Cycles patches, optimized for transmission via FM1 Editor & Librarian.

### 3.8. Firmware Hubs, Web Directories & Online Installers

Community hubs, live directory dashboards, web-based flashers, and metadata registries tracking and installing M-VAVE FM-1 custom firmwares:

 1. **[The FM-1 Firmware Hub (Make Firmware, Not War)](https://thefirmwarehub.com/) ([List View](https://thefirmwarehub.com/?view=list)):**
    Web-based firmware manager and one-click WebMIDI installer created by Sven Trogus (zvenson). Allows previewing, installing, and switching between 50+ open-source community firmwares for the M-VAVE FM-1 directly from Chrome/Edge with automatic nightly updates from author repositories and instant rollback to official stock V15 firmware.

 2. **[FM-1 Online Editor & Firmware Directory](https://fm1-editor.com/) ([Firmware Catalog](https://fm1-editor.com/firmware/)):**
    Web-based configuration and patch editor / librarian for the M-VAVE FM1 synthesizer, along with a curated directory and status tracker for community firmwares.

 3. **[FMDB: FM-1 & SMK-37 Firmware Database / Relay by Stanley Gurvich (EmeraldMoonLabs)](https://stanleygurvich.github.io/FMDB_FM1_FirmwareDatabase/) ([Source & Tools](https://github.com/stanleygurvich/fm1-firmware-database) | [Reddit Announcement](https://www.reddit.com/r/MVaveFM1/comments/1x6gg0h/relay_fm1_editor_firmware_database_emulator/)):**
    * **Concept:** Comprehensive FM-1 and SMK-37 firmware database, emulator host, ability matrix, and automated release crawler.
    * **Automated Firmware Feed & Abilities:** Crawls the community ecosystem and upstream GitHub repositories, publishing `feed.json`, `fwinfo.json`, `abilities.json`, and `genes.json`. Tracks over 300 firmwares, mods, and tools across FM-1 and SMK-37 hardware targets with verified `.fwsc` SHA-256 signatures, star metrics, and install routes.
    * **Companion Tools & Editor:** Includes interactive card filters, the Galaxy & Genome lineage visualizers, companion [UplinkFeluccaEditor-WebApp](https://github.com/stanleygurvich/UplinkFeluccaEditor-WebApp) with WebMIDI SysEx control, and in-browser testing harnesses.

 4. **[Octo-Vave by amacias (Artificial Music)](https://github.com/amacias/octo-vave) ([Web App & Directory](https://amacias.github.io/octo-vave/) | [Reddit Announcement](https://www.reddit.com/r/synthdiy/comments/1x9ptdn/octovave_taming_the_mvave_fm1_firmware_explosion/)):**
    * **License:** Open Source (MIT).
    * **Concept:** Local web application and firmware catalog dashboard designed to organize, track, and test-verify the expanding universe of community FM-1 custom firmwares.
    * **Features:**
      * **Automatic Ranking & Catalog:** Live top-firmware tracking sorted by stars and downloads, directory of 30+ firmwares with install routes, open/closed-source tags, and revert-path indicators.
      * **"Octo-Seal" Hardware Verification:** Badging system signifying firmwares that have been physically installed, auditioned, and successfully reverted to stock on real FM-1 hardware, pinned by SHA256 checksums.
      * **DX7-Style Voice Editor & Sound Checks:** Built-in 6-operator patch library and editor with MIDI/SysEx transfer, post-flash sound check routines, and real-time MIDI monitoring.
      * **Local & Privacy-Focused:** Runs locally via standard-library Python (`127.0.0.1:8765`) or directly in the browser with no required accounts or cloud dependencies.

 5. **[FM-1 Firmware Atlas by wero1414](https://wero1414.github.io/atlas-fm-1):**
    Visual map, purpose matrix, and lineage directory for all known M-VAVE FM-1 community custom firmwares, complete with safety guides and recovery pathways.

 6. **[altstrument: M-VAVE FM-1 Directory](https://altstrument.org/devices/m-vave-fm-1):**
    Open-source device registry and custom firmware catalog for the M-VAVE FM-1 tracking 90+ firmwares, companion tools, licenses, release histories, and brick-risk flags.

---

## 4. Documentation, Protocols & Guides

Comprehensive technical references and community guides:

1. **[M-VAVE FM1 Hardware Architecture & Protocol Reference (Local)](REVERSE_ENGINEERING.md):**
   In-depth local technical documentation covering JieLi AC791N hardware architecture, pinout maps, OTA MIDI SysEx protocol specifications, and external protocol references ([AL-255](https://github.com/AL-255/FM-1-RE/blob/main/docs/io/11-ota-protocol.md) and [KingParamount](https://github.com/KingParamount/fm1-factory-presets/blob/main/docs/protocol-and-provenance.md)).
2. **[FM-1 Easy Guide (by pingywon)](https://pingywon.github.io/fm1-easy-guide/) ([Source](https://github.com/pingywon/fm1-easy-guide)):**
   Beginner-friendly rewrite of the official manual with an interactive step-by-step browser walkthrough.
3. **[fm1-guide (by fuleo)](https://fuleo.github.io/fm1-guide/):**
   Practical operational notes covering sequencer workflows, the V15 reverb bugfix, and Linux flashing procedures.
4. **[FM-1 on Tao of Mac (by Rui Carmo)](https://taoofmac.com/space/com/m-vave/fm-1):**
   Architectural notes, teardown observations, and hackability insights.

---

## 5. Hardware Add-ons & DIY Enhancements

Community hardware companion projects and accessories:

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
   * **Concept:** Standalone hardware companion and portable host for the M-VAVE FM-1 built with inexpensive microcontroller hardware.
   * **Features:**
     * **On-the-Fly Firmware Swapping:** Switches FM-1 firmwares without a computer or smartphone by flashing images directly from a microSD card or downloading live over Wi-Fi from [The Firmware Hub](https://thefirmwarehub.com/).
     * **USB & Bluetooth MIDI Hub:** Hosts up to 4 USB-MIDI devices simultaneously (via USB hub) alongside Bluetooth LE MIDI controllers, bridging them directly to the FM-1 even when running firmwares that only support USB.
     * **Touchscreen Interface:** Color touchscreen displaying firmware selector, battery diagnostics, and customizable UI themes.

6. **[Display SPI Bus MicroSD Card Mod by mobiliakas1](https://www.reddit.com/r/MVaveFM1/comments/1xhiryu/loading_firmware_from_sd_card/):**
   * **Concept:** Hardware modification tapping directly into the AC7911B's hardware SPI1 display bus (`PC10` MOSI, `PC9` SCK) with an inverted chip-select line (`/CS`) to interface a microSD card reader without requiring free dedicated microcontroller pins.
   * **Applications:** Allows loading and swapping `.fwsc` firmware binaries on the go directly from a memory card without computer connection, opening future architectural possibilities for streaming offline sample banks and sound libraries into device RAM.

### 5.1. 3D-Printed Accessories, Enclosures & Desktop Mounts


3D-printable cases, faceplates, and stands designed specifically for the FM-1 form factor:

1. **[M-VAVE FM-1 Protective Snap Case (Printables #1819065)](https://www.printables.com/model/1819065-m-vave-fm-1-case):**
   Form-fitting travel case and protective shell designed for the M-VAVE FM-1 pocket synthesizer, keeping rotary encoders and capacitive keys safe in bags.
2. **[M-VAVE / Cuvave FM-1 Synth Stand 18° Desk Mount (MakerWorld #3487782)](https://makerworld.com/ru/models/3487782-m-vave-cuvave-fm-1-synth-stand-18deg-desk-mount):**
   Ergonomic 18-degree tilted desktop stand providing optimal viewing angles for the 240 × 240 screen and comfortable finger access to the capacitive keyboard and rotary knobs.
3. **[M-VAVE FM-1 3D CAD Chassis Reference Model by Zande Creates](https://grabcad.com/library/m-vave-fm-1-1):**
   High-precision dimensional CAD model (accurate to ~0.1 mm) for modeling custom faceplates, cases, desktop angled stands, and hardware attachments.
4. **[M-Vave FM-1 Comfort Grip/Handle - 34g/70 minutes](https://makerworld.com/en/models/3490222-m-vave-fm-1-comfort-grip-handle-34g-70-minutes)**
   Ergonomic, game controller-style grip, tight snap-fit thanks to Zande Creates's CAD model (5.1.3 above). Good for noodling on the couch or using game emulators.
5. **[Triple-Screen Cyberdeck Folding Laptop Enclosure by fantasmoslam](https://www.reddit.com/r/MVaveFM1/comments/1xgp82y/triple_screen_cyberdeck_fm1_running_ny_custom/):**
   Cassette-futurism folding laptop enclosure holding an M-VAVE FM-1 alongside an external smartphone (Galaxy S22 Ultra / Pixel 5) as a secondary display running Paleotone's USB second-screen companion app.

---

## 6. Articles, Reviews & Community Analyses

Articles and press coverage detailing community custom firmwares and feature overhauls:

* **[Synth Anatomy: Baud Girl FM-1+VA](https://synthanatomy.com/2026/09/baud-girl-fm-1-va-custom-m-vave-fm-1-firmware.html):** Detailed review of the first community firmware adding Virtual Analog synthesis and 64-step sequencing.
* **[Synth Anatomy: Felucca 1.0 Release](https://synthanatomy.com/2026/10/hugelton-instruments-felucca-custom-m-vave-fm-1-firmware-turns-it-into-a-multi-engine-synth.html):** Coverage of Hügelton Instruments' multi-engine open-source platform.
* **[Synth Anatomy: SLOOP Groovebox](https://synthanatomy.com/2026/10/3dsam-sloop-custom-firmware-turns-m-vave-fm-1-into-a-4-track-groovebox.html):** Feature breakdown of SLOOP 4-track groovebox with USB audio.
* **[Synth Anatomy: X0X Techno Firmware](https://synthanatomy.com/2026/10/charles-vestal-x0x-custom-firmware-turns-the-m-vave-fm-1-into-a-rebirth-like-groovebox.html):** Examination of Charles Vestal's ReBirth-inspired 303/808/909 firmware.
* **[Synth Anatomy: Groove OS](https://synthanatomy.com/2026/10/groove-os-turns-the-m-vave-fm-1-into-an-8-track-groovebox.html):** Coverage of the commercial 8-track groovebox firmware.
* **[Piano & Synth Magazine: Custom Firmware Collection](https://pianoandsynth.com/m-vave-fm-1-custom-firmware-collection/):** Side-by-side comparison matrix of major FM-1 custom firmwares.
* **[Sonicstate: Free Custom Firmware for M-VAVE FM-1](https://sonicstate.com/news/2026/09/29/free-custom-firmware-for-mvave-fm-1-/):** News coverage of third-party firmware development.
* **[Synth Anatomy: Xfer Records Shrub (Serum for FM-1)](https://synthanatomy.com/2026/10/xfer-records-shrub-serum-for-m-vave-fm-1-before-gta-6.html):** Coverage of Steve Duda / Xfer Records' upcoming free wavetable synthesizer firmware *Shrub* (a stripped-down "mini Serum" port tailored for the M-VAVE FM-1).
* **[Ars Technica: From impulse purchase to pocket studio: The M-Vave FM-1](https://arstechnica.com/gadgets/2026/10/from-impulse-purchase-to-pocket-studio-the-m-vave-fm-1/) ([Reddit Discussion](https://www.reddit.com/r/MVaveFM1/comments/1xh2c3z/arstechnica_from_impulse_purchase_to_pocket/)):** In-depth feature article by Nick Indge exploring how M-VAVE's $60 FM synth evolved into a vibrant hacker playground. Covers the official FM1 Open workbench, safe flashing tips (citing this repository's TransitFM1 advice), running *Doom*, and field testing Melodee, Felucca, and SLOOP for standalone beatmaking and DAW recording.

---

## 7. Community Hubs & Discussions

Where the M-VAVE FM-1 community discusses reverse engineering, troubleshooting, and new releases:

* **[M-VAVE Official Forum (Topic #4: FM1 Open Firmware Announcement)](https://forum.m-vave.com/topic/4):** The official manufacturer forum and announcement hub (announcement topic #4 was subsequently removed by manufacturer).
* **[Reddit: r/MVaveFM1](https://www.reddit.com/r/MVaveFM1/):** The primary community hub for custom firmware releases, unbricking help, and hardware hacks.
* **[KVR Audio: M-VAVE FM-1 Thread](https://www.kvraudio.com/forum/viewtopic.php?t=632127):** Technical thread where factory preset recovery and early tools were first shared.
* **[Hacker News: FM-1 Reverse-Engineering Discussion](https://news.ycombinator.com/item?id=49994065):** Discussion on the FM-1-RE architecture and JieLi SoC discoveries.
* **[Elektronauts: M-VAVE FM-1 Thread](https://www.elektronauts.com/t/m-vave-fm-1/252170):** Groovebox workflow discussions, firmware releases, and audio demos.
* **[Gearspace: M-VAVE FM-1 Owners Thread](https://gearspace.com/threads/m-vave-fm-1.1465371/):** Hardware impressions, comparison with Yamaha DX-series hardware, and tips.
