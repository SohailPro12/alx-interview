#!/usr/bin/python3
"""
determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    for x in data:
        if x > 127 or x < 0:
            return False
    return True
