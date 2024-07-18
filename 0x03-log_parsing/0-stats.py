#!/usr/bin/python3
"""Log parsing"""

import sys
import re
import signal

pattern = r'(\d{3}) (\d+)$'
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0


def print_metrics():
    print(f"File size: {total_file_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def handle_interrupt(sig, frame):
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

for line in sys.stdin:
    match = re.search(pattern, line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        status_counts[status_code] = status_counts.get(status_code, 0) + 1
        total_file_size += file_size
        line_count += 1
        if line_count % 10 == 0:
            print_metrics()

# Print metrics if the input ends before 10 lines are processed
print_metrics()
