#!/usr/bin/env python3
"""
FM-1 Safe SysEx Parameter Scanner (Read-Only Query)
Безопасный сканер SysEx параметров синтезатора M-VAVE FM1.
Отправляет только чтение (Get Value = 0x7F) и не затрагивает Flash-память.
"""

import sys
import time
import argparse
import mido

SYSEX_HEADER = bytes([0xF0, 0x00, 0x32, 0x45])
SYSEX_END = 0xF7


def find_matching_ports():
    in_ports = mido.get_input_names()
    out_ports = mido.get_output_names()

    # 1. Приоритет: порты содержащие fm1 или fm-1
    for i_name in in_ports:
        if 'fm1' in i_name.lower() or 'fm-1' in i_name.lower():
            for o_name in out_ports:
                if 'fm1' in o_name.lower() or 'fm-1' in o_name.lower():
                    return i_name, o_name

    # 2. Ищем совпадение по 'USB Composite Device' для обоих портов (вход и выход)
    if 'USB Composite Device' in in_ports and 'USB Composite Device' in out_ports:
        return 'USB Composite Device', 'USB Composite Device'

    # 3. Ищем порт, который есть и во входе, и в выходе (исключая сторонние клавиатуры)
    common = set(in_ports).intersection(set(out_ports))
    for name in common:
        if not any(ex in name.lower() for ex in ['minilab', 'iac', 'monitor']):
            return name, name

    return None, None


def scan_parameters(in_port_name: str, out_port_name: str, start_id: int = 0, end_id: int = 127):
    print("====================================================")
    print("    БЕЗОПАСНОЕ СКАНИРОВАНИЕ СТАТУСОВ M-VAVE FM1     ")
    print("====================================================")
    print(f"[*] MIDI In:  '{in_port_name}'")
    print(f"[*] MIDI Out: '{out_port_name}'")
    print(f"[*] Сканирование Parameter ID с {start_id} по {end_id} (только чтение 0x7F)...")
    print("----------------------------------------------------\n")

    inport = mido.open_input(in_port_name)
    outport = mido.open_output(out_port_name)

    found_responses = 0

    try:
        for param_id in range(start_id, end_id + 1):
            # Формируем безопасный запрос чтения: F0 00 32 45 00 00 00 <PARAM_ID> 7F F7
            frame = bytearray(SYSEX_HEADER)
            frame.extend([0x00, 0x00, 0x00]) # Address / Channel
            frame.append(param_id & 0x7F)    # Parameter ID
            frame.append(0x7F)               # 0x7F = Get Value (Чтение)
            frame.append(SYSEX_END)

            msg = mido.Message('sysex', data=frame[1:-1])
            outport.send(msg)

            # Ожидаем ответ 100 мс
            start_time = time.time()
            got_response = False

            while time.time() - start_time < 0.1:
                for resp in inport.iter_pending():
                    if resp.type == 'sysex' and len(resp.data) > 3:
                        raw_hex = ' '.join(f'{b:02X}' for b in resp.data)
                        ascii_str = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in resp.data)
                        print(f"[+] ОБНАРУЖЕН ОТВЕТ на Param ID 0x{param_id:02X} ({param_id:3d}):")
                        print(f"    HEX:   F0 {raw_hex} F7")
                        print(f"    ASCII: {ascii_str}")
                        print("----------------------------------------------------")
                        found_responses += 1
                        got_response = True
                if got_response:
                    break
                time.sleep(0.005)

    finally:
        inport.close()
        outport.close()

    print(f"\n[+] Сканирование завершено. Найдено ответов: {found_responses}")


def main():
    parser = argparse.ArgumentParser(description="M-VAVE FM1 Safe SysEx Parameter Scanner")
    parser.add_argument("--in-port", type=str, help="Имя MIDI In порта")
    parser.add_argument("--out-port", type=str, help="Имя MIDI Out порта")
    parser.add_argument("--start", type=int, default=0, help="Начальный ID (0-127)")
    parser.add_argument("--end", type=int, default=127, help="Конечный ID (0-127)")
    args = parser.parse_args()

    in_name = args.in_port
    out_name = args.out_port

    if not in_name or not out_name:
        auto_in, auto_out = find_matching_ports()
        in_name = in_name or auto_in
        out_name = out_name or auto_out

    if not in_name or not out_name:
        print("[!] Не удалось определить MIDI-порты FM1.")
        print("[!] Доступные входы:", mido.get_input_names())
        print("[!] Доступные выходы:", mido.get_output_names())
        sys.exit(1)

    scan_parameters(in_name, out_name, args.start, args.end)


if __name__ == "__main__":
    main()
