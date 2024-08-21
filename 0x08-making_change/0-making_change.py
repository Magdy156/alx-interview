#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total
        using using bottom to up approach
    """
    if total <= 0:
        return 0
    arr = [float('inf')] * (total + 1)
    arr[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                arr[i] = min(arr[i], arr[i - coin] + 1)

    return arr[total] if arr[total] != float('inf') else -1
