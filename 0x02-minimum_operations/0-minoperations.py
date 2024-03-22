#!/usr/bin/python3
"""
Script that computes a minimum operations
needed in a CopyAll - Paste task
"""


def minOperations(n):
    if n <= 1:
        return 0
    divisorList = []
    divisor = 1
    while n > 1:
        divisor += 1
        if n % divisor == 0:
            while n % divisor == 0:
                n /= divisor
                divisorList.append(divisor)
    return sum(divisorList)
