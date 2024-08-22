#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total
        using greedy approach
    """
    if total <= 0:
        return 0
    check = 0
    count = 0
    coins.sort(reverse=True)
    for coin in coins:
        while check < total:
            check += coin
            count += 1
        if check == total:
            return count
        check -= coin
        count -= 1
    return -1
