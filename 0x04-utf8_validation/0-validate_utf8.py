#!/usr/bin/python3
"""
determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    num_bytes = 0
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        byte = byte & 0xFF
        if num_bytes == 0:
            mask = 1 << 7
            while (byte & mask):
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
