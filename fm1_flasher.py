#!/usr/bin/env python3
"""
FM-1 Synthesizer OTA Firmware Flasher & Extraction Utility
Reverse-engineering research tool for FM-1 synthesizers.

NOTE ON FLASHING:
    The direct flash streaming implementation in this script is experimental/non-functional
    due to wire-framing differences (device-pull vs host-push). For proven, hardware-verified
    firmware flashing on physical hardware, use AL-255's `tools/fm1_ota.py` from AL-255/FM-1-RE.
    Firmware extraction (--extract) is fully functional and carves byte-exact .fwsc packages.

Usage:
    python3 fm1_flasher.py --list                 # List available MIDI ports
    python3 fm1_flasher.py --extract out.fwsc     # Extract embedded .fwsc firmware package
    python3 fm1_flasher.py --file my_firmware.ufw # Experimental flash (at own risk)
"""

import sys
import os
import time
import argparse
import mido
from tqdm import tqdm

SYSEX_HEADER = bytes([0xF0, 0x00, 0x32, 0x45])  # Arturia / FM-1 SysEx Prefix
SYSEX_END = 0xF7

DEFAULT_APP_PATH = '/Users/aroum/Documents/fm1/M-UPGRADE-FM1.app/Contents/MacOS/M-UPGRADE-FM1'
EMBEDDED_FW_OFFSET = 0xF3BB8  # @JMUA container offset inside M-UPGRADE-FM1 executable


def pack_8bit_to_7bit(data: bytes) -> bytes:
    """
    Packs an 8-bit byte array into 7-bit MIDI bytes (MSB packing).
    Groups of 7 bytes are encoded into 8 bytes (first byte contains MSB flags).
    """
    res = bytearray()
    i = 0
    while i < len(data):
        chunk = data[i:i+7]
        msb = 0
        payload = bytearray()
        for idx, b in enumerate(chunk):
            if b & 0x80:
                msb |= (1 << (6 - idx))
            payload.append(b & 0x7F)
        res.append(msb & 0x7F)
        res.extend(payload)
        i += 7
    return bytes(res)


def calculate_checksum(data: bytes) -> int:
    """Calculates a simple 7-bit checksum for SysEx frames."""
    return sum(data) & 0x7F


def extract_embedded_firmware(app_binary_path: str) -> bytes:
    """
    Extracts the embedded .fwsc firmware package from the native M-UPGRADE-FM1 binary.
    The package is stored as a Qt resource ending at JLUFW + 16, preceded by a
    4-byte big-endian length prefix, with 'AC791N' identifier near offset 0x424.
    """
    import struct
    if not os.path.exists(app_binary_path):
        raise FileNotFoundError(f"App binary not found: {app_binary_path}")

    with open(app_binary_path, 'rb') as f:
        binary_data = f.read()

    idx = 0
    while True:
        idx = binary_data.find(b'JLUFW', idx)
        if idx == -1:
            break
        end_pos = idx + 16
        # Scan backward for Qt 4-byte big-endian length word matching end_pos
        for p in range(end_pos - 1000000, end_pos - 100000, 4):
            if p >= 4:
                length = struct.unpack('>I', binary_data[p-4:p])[0]
                if p + length == end_pos:
                    if b'AC791N' in binary_data[p:p + 0x1000]:
                        fw_data = binary_data[p:end_pos]
                        print(f"[+] Successfully carved embedded firmware package:")
                        print(f"    Offset range: 0x{p:X} - 0x{end_pos:X} (size: {len(fw_data)} bytes)")
                        return fw_data
        idx += 5

    raise ValueError("Valid firmware package (.fwsc) not found in binary executable!")


def find_fm1_ports():
    """Auto-detects matching MIDI In/Out ports for FM-1."""
    in_ports = mido.get_input_names()
    out_ports = mido.get_output_names()

    # 1. Look for explicit fm1 or fm-1 names
    for i_name in in_ports:
        if 'fm1' in i_name.lower() or 'fm-1' in i_name.lower():
            for o_name in out_ports:
                if 'fm1' in o_name.lower() or 'fm-1' in o_name.lower():
                    return i_name, o_name

    # 2. Look for matching USB Composite Device ports
    if 'USB Composite Device' in in_ports and 'USB Composite Device' in out_ports:
        return 'USB Composite Device', 'USB Composite Device'

    # 3. Look for common port names excluding third-party controllers
    common = set(in_ports).intersection(set(out_ports))
    for name in common:
        if not any(ex in name.lower() for ex in ['minilab', 'iac', 'monitor']):
            return name, name

    return None, None


class FM1Flasher:
    def __init__(self, port_in_name: str, port_out_name: str):
        self.port_in_name = port_in_name
        self.port_out_name = port_out_name
        self.inport = None
        self.outport = None

    def connect(self):
        print(f"[*] Opening MIDI In: '{self.port_in_name}'")
        self.inport = mido.open_input(self.port_in_name)
        print(f"[*] Opening MIDI Out: '{self.port_out_name}'")
        self.outport = mido.open_output(self.port_out_name)

    def close(self):
        if self.inport:
            self.inport.close()
        if self.outport:
            self.outport.close()

    def send_sysex_command(self, cmd_type: int, payload: bytes = b'', wait_response: bool = True, timeout: float = 2.0) -> bool:
        """Constructs and transmits an OtaFormat SysEx frame."""
        frame = bytearray(SYSEX_HEADER)
        frame.append(cmd_type & 0x7F)

        if payload:
            encoded = pack_8bit_to_7bit(payload)
            frame.extend(encoded)

        crc = calculate_checksum(frame[4:])
        frame.append(crc)
        frame.append(SYSEX_END)

        msg = mido.Message('sysex', data=frame[1:-1])
        self.outport.send(msg)

        if not wait_response:
            return True

        start_time = time.time()
        while time.time() - start_time < timeout:
            for resp in self.inport.iter_pending():
                if resp.type == 'sysex' and len(resp.data) > 3:
                    if bytes(resp.data[:3]) == SYSEX_HEADER[1:]:
                        return True
            time.sleep(0.01)

        return False

    def flash_firmware(self, fw_bytes: bytes, chunk_size: int = 128):
        """Executes the two-step firmware flashing process (Verification -> Upgrade -> Chunk Stream)."""
        print("\n====================================================")
        print("          STARTING FM-1 OTA FIRMWARE FLASHING        ")
        print("====================================================")

        # Step 1: Handshake and Verification
        print("[1/3] Step 1: Sending metadata and verifying payload...")
        meta_payload = len(fw_bytes).to_bytes(4, 'big') + b'FM1_FIRMWARE'

        if not self.send_sysex_command(cmd_type=0x01, payload=meta_payload, timeout=3.0):
            print("[!] Warning: No direct response received, continuing OTA mode initialization...")

        time.sleep(0.5)

        # Step 2: Start Upgrade Mode
        print("[2/3] Step 2: Requesting device transition to Flash overwrite mode...")
        self.send_sysex_command(cmd_type=0x02, wait_response=False)
        time.sleep(1.0)  # Delay for bootloader initialization

        # Step 3: Stream Firmware Data Chunks
        print("[3/3] Step 3: Streaming firmware chunks over MIDI SysEx...")

        num_chunks = (len(fw_bytes) + chunk_size - 1) // chunk_size

        with tqdm(total=num_chunks, desc="Flashing progress", unit="chunk") as pbar:
            for seq in range(num_chunks):
                chunk = fw_bytes[seq * chunk_size : (seq + 1) * chunk_size]

                # Payload: Sequence number (2 bytes) + Binary Chunk
                seq_bytes = seq.to_bytes(2, 'big')
                payload = seq_bytes + chunk

                # Send data chunk frame (Cmd 0x03)
                self.send_sysex_command(cmd_type=0x03, payload=payload, wait_response=False)

                # Delay to prevent MCU buffer overrun
                time.sleep(0.015)
                pbar.update(1)

        print("\n[+] Firmware transmission completed successfully!")
        print("[+] Waiting for device reboot...")

    def update_presets(self, preset_bytes: bytes):
        """Uploads preset bank data (Cmd 0x04)."""
        print("\n[*] Uploading preset bank to FM-1...")
        self.send_sysex_command(cmd_type=0x04, payload=preset_bytes, wait_response=False)
        print("[+] Presets transmitted.")


def main():
    parser = argparse.ArgumentParser(description="FM-1 MIDI SysEx Firmware Flasher & Extraction Utility")
    parser.add_argument("--list", action="store_true", help="List available MIDI ports")
    parser.add_argument("--extract", type=str, help="Extract embedded .fwsc firmware from app binary to output file")
    parser.add_argument("--app", type=str, default=DEFAULT_APP_PATH, help="Path to M-UPGRADE-FM1 macOS executable (for extraction)")
    parser.add_argument("--file", type=str, help="Path to custom firmware file (.fwsc / .ufw)")
    parser.add_argument("--preset", type=str, help="Path to preset bank file (.syx / .bin)")
    parser.add_argument("--in-port", type=str, help="MIDI In port name")
    parser.add_argument("--out-port", type=str, help="MIDI Out port name")
    args = parser.parse_args()

    if args.extract:
        try:
            fw = extract_embedded_firmware(args.app)
            with open(args.extract, 'wb') as f:
                f.write(fw)
            print(f"[+] Saved extracted firmware to {args.extract} ({len(fw)} bytes)")
        except Exception as e:
            print(f"[!] Extraction failed: {e}")
            sys.exit(1)
        return

    if args.list:
        print("=== AVAILABLE MIDI INPUTS ===")
        for p in mido.get_input_names():
            print(f"  • {p}")
        print("\n=== AVAILABLE MIDI OUTPUTS ===")
        for p in mido.get_output_names():
            print(f"  • {p}")
        return

    in_port = args.in_port
    out_port = args.out_port

    if not in_port or not out_port:
        auto_in, auto_out = find_fm1_ports()
        in_port = in_port or auto_in
        out_port = out_port or auto_out

    if not in_port or not out_port:
        print("[!] Error: Could not automatically detect FM-1 MIDI ports.")
        print("[!] Use --list to view available ports and specify them with --in-port and --out-port.")
        sys.exit(1)

    print(f"[+] Selected MIDI In port: {in_port}")
    print(f"[+] Selected MIDI Out port: {out_port}")

    flasher = FM1Flasher(in_port, out_port)

    try:
        flasher.connect()

        if args.preset:
            with open(args.preset, 'rb') as f:
                p_data = f.read()
            flasher.update_presets(p_data)
        else:
            if args.file:
                with open(args.file, 'rb') as f:
                    fw_data = f.read()
                print(f"[+] Loaded custom firmware file: {args.file} ({len(fw_data)} bytes)")
            else:
                fw_data = extract_embedded_firmware(DEFAULT_APP_PATH)

            flasher.flash_firmware(fw_data)

    except Exception as e:
        print(f"\n[!] Execution error: {e}")
        sys.exit(1)
    finally:
        flasher.close()


if __name__ == "__main__":
    main()
