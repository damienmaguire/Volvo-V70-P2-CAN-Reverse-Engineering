#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CAN Log Counter Finder
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
from collections import defaultdict, Counter
import sys

# Read CSV and extract messages with timestamp, ID, bus, and data bytes
def read_csv(filename):
    messages = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_bytes = [int(row[f'D{i}'], 16) for i in range(1, 9)]
            messages.append({
                'timestamp': float(row['Time Stamp']),
                'id': row['ID'],
                'bus': row['Bus'],
                'data': data_bytes
            })
    return messages

# Group messages by (ID, Bus) and sort by timestamp
def group_by_id(messages):
    id_dict = defaultdict(list)
    for msg in messages:
        key = (msg['id'], msg['bus'])
        id_dict[key].append(msg)
    for key in id_dict:
        id_dict[key].sort(key=lambda x: x['timestamp'])
    return id_dict

# Find likely counter bytes based on consistent increment patterns
def find_counters(id_dict):
    counter_results = {}
    for (msg_id, bus), msgs in id_dict.items():
        byte_positions = len(msgs[0]['data'])
        for byte_index in range(byte_positions):
            values = [msg['data'][byte_index] for msg in msgs]
            diffs = [
                (values[i + 1] - values[i]) % 256
                for i in range(len(values) - 1)
            ]
            if diffs:
                most_common_diff, count = Counter(diffs).most_common(1)[0]
                match_rate = count / len(diffs)
                if most_common_diff != 0 and match_rate > 0.8:
                    key = ((msg_id, bus), byte_index)
                    counter_results[key] = {
                        'step': most_common_diff,
                        'rate': round(match_rate, 2),
                        'min': min(values),
                        'max': max(values)
                    }
    return counter_results

# Print formatted table
def print_table(header, rows):
    print()
    
    # Determine column widths based on header and row content
    col_widths = [len(h) for h in header]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Format header line
    header_line = " | ".join(f"{h:<{col_widths[i]}}" for i, h in enumerate(header))
    print(header_line)

    # Print separator line
    print("-" * len(header_line))

    # Format each row
    for row in rows:
        print(" | ".join(f"{str(cell):>{col_widths[i]}}" for i, cell in enumerate(row)))

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_can.py <filename.csv>")
        sys.exit(1)

    filename = sys.argv[1]
    messages = read_csv(filename)
    id_dict = group_by_id(messages)

    counters = find_counters(id_dict)
    def format_id_with_bus(msg_id, bus):
        return f"{msg_id} ({bus})"

    counter_rows = sorted(
        [
            (format_id_with_bus(msg_id, bus), byte_index, data['step'], data['min'], data['max'], data['rate'])
            for ((msg_id, bus), byte_index), data in counters.items()
        ],
        key=lambda x: (x[0], x[1])
    )
    print_table(["ID (Bus)", "Byte", "Step", "Start", "End", "Match Rate"], counter_rows)

if __name__ == "__main__":
    main()
