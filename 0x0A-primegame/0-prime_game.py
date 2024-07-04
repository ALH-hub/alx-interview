#!/usr/bin/python3
"""prime number game"""


def is_winner(x, nums):
    """
    Determines the winner of the game based on prime number selection.

    Args:
        x: Number of rounds played.
        nums: List of integers representing the starting sets for each round.

    Returns:
        str: Name of the player who wins the most rounds ("Maria" or "Ben").
        None: If the winner cannot be determined (a tie).
    """

    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0

    for i in range(2, int(n**0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0

    primes = [i for i in range(n + 1) if sieve[i] == 1]
    primes_count = [0] * (n + 1)

    count = 0
    for i in range(1, n + 1):
        if i in primes:
            count += 1
        primes_count[i] = count

    ben_wins = 0
    for num in nums:
        ben_wins += primes_count[num] % 2 == 0

    if ben_wins * 2 == x:
        return None

    return "Ben" if ben_wins > x // 2 else "Maria"
