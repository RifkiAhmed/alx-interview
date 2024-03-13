#!/usr/bin/python3
""" Prime Game winner
"""


def prime_sieve(n):
    """ Returns a list of prime numbers up to n
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def count_primes_up_to_n(n, primes):
    """ Counts the number of prime numbers up to n
    """
    return sum(primes[:n + 1])


def isWinner(x, nums):
    """ Returns prime game winner, else returns None
    """
    if x <= 0 or not nums or x != len(nums):
        return None

    max_num = max(nums)
    primes = prime_sieve(max_num)
    maria_wins = sum(
        1 for n in nums if count_primes_up_to_n(
            n, primes) %
        2 != 0)
    ben_wins = x - maria_wins

    if maria_wins == ben_wins:
        return None
    return "Maria" if ben_wins < maria_wins else "Ben"
