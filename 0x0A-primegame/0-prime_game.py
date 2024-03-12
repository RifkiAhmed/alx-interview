#!/usr/bin/python3
""" Prime Game winner
"""


def is_prime(n):
    """ Checks if n is a prime number
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(n):
    """ Counts the number of prime numbers up to n inclusive
    """
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count


def isWinner(x, nums):
    """ Returns prime game winner, else returns None
    """
    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        total_primes = count_primes(n)
        if total_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return "Maria" if ben_wins < maria_wins else "Ben"
