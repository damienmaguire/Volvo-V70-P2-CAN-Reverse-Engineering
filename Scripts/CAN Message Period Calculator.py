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
import sys
import statistics
from collections import defaultdict

# === Read file path from command line argument ===
if len(sys.argv) < 2:
    print("Usage: python can_analysis.py <path_to_can_log.csv>")
    sys.exit(1)

csv_file = sys.argv[1]

# === Data structure to hold timestamps per message ID ===
timestamps_by_id = defaultdict(list)

# === Read CSV file ===
with open(csv_file, 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            timestamp = int(row['Time Stamp']) / 1000
            message_id = row['ID']
            timestamps_by_id[message_id].append(timestamp)
        except (ValueError, KeyError):
            continue  # Skip rows with missing or invalid data

# === Analyze periods ===
results = []

for message_id, timestamps in timestamps_by_id.items():
    if len(timestamps) < 2:
        continue  # Not enough data to compute periods

    # Sort timestamps to ensure correct period calculation
    timestamps.sort()
    
    # Compute periods (differences between timestamps)
    periods = [t2 - t1 for t1, t2 in zip(timestamps, timestamps[1:])]

    # Compute statistics
    count = len(timestamps)
    mean_period = statistics.mean(periods)
    stdev_period = statistics.stdev(periods) if len(periods) > 1 else 0
    min_period = min(periods)
    max_period = max(periods)
    jitter_percent = (stdev_period / mean_period) * 100 if mean_period > 0 else 0

    results.append({
        'ID': message_id,
        'Count': count,
        'Mean Period [ms]': mean_period,
        'Std Dev [ms]': stdev_period,
        'Min [ms]': min_period,
        'Max [ms]': max_period,
        'Jitter [%]': jitter_percent
    })

# === Sort results by mean period ===
results.sort(key=lambda x: x['ID'])

# === Print results ===
print("")
header = ['       ID ', 'Count', ' Mean [ms]', 'StdDev [ms]', 'Min [ms]', 'Max [ms]', 'Jitter [%]']
headerStr = f"{' | '.join(header)}"
print(headerStr)
print('-' * len(headerStr))
for entry in results:
    print(f"{entry['ID']:>10} | {entry['Count']:>5} | "
          f"{entry['Mean Period [ms]']:>10.2f} | {entry['Std Dev [ms]']:>11.2f} | "
          f"{entry['Min [ms]']:>8.2f} | {entry['Max [ms]']:>8.2f} | {entry['Jitter [%]']:>10.2f}")
          
# === Summary footer ===
total_ids = len(results)
total_messages = sum(len(timestamps) for timestamps in timestamps_by_id.values())

print('-' * len(headerStr))
print(f"  {total_ids} CAN IDs analyzed, {total_messages} total messages")