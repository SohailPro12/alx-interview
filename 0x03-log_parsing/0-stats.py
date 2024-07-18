#!/usr/bin/python3
"""Log parsing"""

import sys
import re
import signal

pattern = r'(\d{3}) (\d+)$'
status_counts = {}
total_file_size = 0
line_count = 0


def handle_interrupt(signal, frame):
    print(f"File size: {total_file_size}")
    # Do not exit after Ctrl+C
    # sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)


for line in sys.stdin:
    line_count += 1
    match = re.search(pattern, line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        status_counts[status_code] = status_counts.get(status_code, 0) + 1
        total_file_size += file_size
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            i = 0
        else:
            print(f"{status_code}: {status_counts[status_code]}")
