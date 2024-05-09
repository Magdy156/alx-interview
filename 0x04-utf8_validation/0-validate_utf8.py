#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """ validate a list of integers"""
    try:
        eight_bits_numbers = [num & 255 for num in data]
        bytes(eight_bits_numbers).decode("UTF-8")
        return True
    except Exception:
        return False
