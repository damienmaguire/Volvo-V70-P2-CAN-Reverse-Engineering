#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CAN Extended ID Analyzer
#
# Copyright (C) 2025  crasbe <crasbe@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
#
# Created with the help of AI tools.

import csv
import sys

def format_binary_grouped(value, bits=29, group_size=4):
    """
    Converts an integer to a right-aligned grouped binary string with 29 bits,
    where the first group may have fewer bits (e.g. 1 to 3 bits).
    """
    binary = bin(value)[2:].zfill(bits)
    groups = []

    first_group_len = bits % group_size or group_size
    groups.append(binary[:first_group_len])
    for i in range(first_group_len, bits, group_size):
        groups.append(binary[i:i+group_size])

    return ' '.join(groups)

def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_can_log.py <path_to_csv>")
        sys.exit(1)

    filepath = sys.argv[1]
    seen_ids = {0: {}, 1: {}}  # bus_id: {can_id: entry_dict}

    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row['Extended'].lower() != "true":
                continue

            try:
                bus = int(row['Bus'])
                if bus not in (0, 1):
                    continue

                can_id_hex = row['ID']
                can_id_int = int(can_id_hex, 16)

                if can_id_hex not in seen_ids[bus]:
                    seen_ids[bus][can_id_hex] = {
                        'hex': can_id_hex.upper(),
                        'int': can_id_int,
                        'bin': format_binary_grouped(can_id_int)
                    }

            except Exception as e:
                print(f"Error parsing row: {e}", file=sys.stderr)

    for bus_id in (0, 1):
        entries = list(seen_ids[bus_id].values())
        entries.sort(key=lambda x: x['int'])  # sort by numeric ID

        print(f"\n=== Bus {bus_id} ===")
        header = [' ID (hex) ', 'ID (binary)                         ']
        headerStr = ' | '.join(header)
        print(headerStr)
        print('-' * len(headerStr))

        for entry in entries:
            print(f"{entry['hex']:>10} | {entry['bin']}")

        print('-' * len(headerStr))
        print(f"  {len(entries):>3} unique extended CAN IDs found on Bus {bus_id}\n")

if __name__ == "__main__":
    main()
