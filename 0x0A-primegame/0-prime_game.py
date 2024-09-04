#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """ Returns the winner in the game"""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    ben = 0
    maria = 0
    prime_list = [1 for _ in range(sorted(nums)[-1] + 1)]
    prime_list[0], prime_list[1] = 0, 0
    # Use Sieve of Eratosthenes algorithm to generate array of prime numbers
    for i in range(2, len(prime_list)):
        remove_multiples(prime_list, i)

    for i in nums:
        # If the sum of prime numbers in the set is even, Ben wins
        if sum(prime_list[0: i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # Determine the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def remove_multiples(ls, x):
    """
    sets multiples of a prime number from an array to zero
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
