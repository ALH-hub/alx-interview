#!/usr/bin/python3
"""validate utf8 data module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    continuation_bytes = 0

    for byte in data:
        if byte & 0b11000000 == 0b10000000:
            continuation_bytes -= 1
        else:
            if byte & 0b10000000 == 0:
                continue
            elif byte & 0b11100000 == 0b11000000:
                continuation_bytes = 1
            elif byte & 0b11110000 == 0b11100000:
                continuation_bytes = 2
            elif byte & 0b11111000 == 0b11110000:
                continuation_bytes = 3
            else:
                return False

        if continuation_bytes < 0:
            return False

    return continuation_bytes == 0
