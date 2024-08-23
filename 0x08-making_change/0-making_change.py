#!/usr/bin/python3
"""
Makechange module
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    it determine the fewest number of coins needed
    to meet a given total total.
    solution 1:(but not efficient)
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[total] if dp[total] != float('inf') else - 1
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total >= coin:
            num_coins += total // coin
            total %= coin

        if total == 0:
            break
    return num_coins if total == 0 else -1
