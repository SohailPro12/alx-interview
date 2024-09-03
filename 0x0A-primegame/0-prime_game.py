#!/usr/bin/python3
"""
Prime Game
"""


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p] is True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers


def moves_for_each_round(n, primes):
    moves = 0
    is_prime = [False] * (n + 1)
    for prime in primes:
        if prime > n:
            break
        if is_prime[prime] is False:
            moves += 1
            for multiple in range(prime, n + 1, prime):
                is_prime[multiple] = True
    return moves


def isWinner(x, nums):
    if x < 1 or nums is None or len(nums) < 1:
        return None

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = eratosthenes(n)
        moves = moves_for_each_round(n, primes)
        if moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
