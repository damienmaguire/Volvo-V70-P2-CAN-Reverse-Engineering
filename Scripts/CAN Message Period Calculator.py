#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# CAN Log Period Analyzer
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
import statistics
import sys
from collections import defaultdict

# === Read file path from command line argument ===
if len(sys.argv) < 2:
    print("Usage: python can_analysis.py <path_to_can_log.csv>")
    sys.exit(1)

csv_file = sys.argv[1]

# === Group timestamps by (Bus, ID) ===
timestamps_by_bus_and_id = defaultdict(list)
total_messages = 0

try:
    with open(csv_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                timestamp = int(row['Time Stamp']) / 1000
                message_id = row['ID']
                bus = row['Bus']
                key = (bus, message_id)
                timestamps_by_bus_and_id[key].append(timestamp)
                total_messages += 1
            except (ValueError, KeyError):
                continue  # Skip invalid rows
except FileNotFoundError:
    print(f"Error: File '{csv_file}' not found.")
    sys.exit(1)
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# === Analyze per bus ===
def analyze_and_print(bus_id):
    results = []

    for (bus, message_id), timestamps in timestamps_by_bus_and_id.items():
        if bus != bus_id:
            continue
        if len(timestamps) < 2:
            continue

        timestamps.sort()
        periods = [t2 - t1 for t1, t2 in zip(timestamps, timestamps[1:])]

        mean_period = statistics.mean(periods)
        stdev_period = statistics.stdev(periods) if len(periods) > 1 else 0
        min_period = min(periods)
        max_period = max(periods)
        jitter_percent = (stdev_period / mean_period) * 100 if mean_period > 0 else 0

        results.append({
            'ID': message_id,
            'Count': len(timestamps),
            'Mean Period [ms]': mean_period,
            'Std Dev [ms]': stdev_period,
            'Min [ms]': min_period,
            'Max [ms]': max_period,
            'Jitter [%]': jitter_percent
        })
       
    if (len(results) == 0):
        return

    results.sort(key=lambda x: x['Mean Period [ms]'])

    print(f"\n=== Bus {bus_id} ===")
    header = ['        ID', 'Count', 'Mean [ms]', 'StdDev [ms]', 'Min [ms]', 'Max [ms]', 'Jitter [%]']
    headerStr = f"{' | '.join(header)}"
    print(headerStr)
    print('-' * len(headerStr))
    for entry in results:
        print(f"{entry['ID']:>10} | {entry['Count']:>5} | "
              f"{entry['Mean Period [ms]']:>9.2f} | {entry['Std Dev [ms]']:>11.2f} | "
              f"{entry['Min [ms]']:>8.2f} | {entry['Max [ms]']:>8.2f} | {entry['Jitter [%]']:>8.2f}")

    print('-' * len(headerStr))
    print(f"  {len(results):>2} CAN IDs analyzed, {sum(entry['Count'] for entry in results)} total messages")
    print()

# === Print analysis for Bus 0 and Bus 1 ===
analyze_and_print('0')
analyze_and_print('1')