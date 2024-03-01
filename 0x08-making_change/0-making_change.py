#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """Returns minimum number of coins needed to meet amount total
    """
    if total <= 0:
        return 0

    memo = {}

    def method(remaining_total):
        if remaining_total in memo:
            return memo[remaining_total]
        if remaining_total < 0:
            return -1
        if remaining_total == 0:
            return 0

        min_coins = float('inf')
        for coin in coins:
            result = method(remaining_total - coin)
            if result >= 0 and result < min_coins:
                min_coins = result + 1

        memo[remaining_total] = min_coins if min_coins != float('inf') else -1
        return memo[remaining_total]

    return method(total)
