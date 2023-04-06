#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """
    A function that determines the winner of the game
    based on the rule which is that the player who doesn't
    get to play fails and any number chosen must be prime
    to be valid
    """
    def get_primes(n):
        """
        Function to get a prime number using the
         Sieve of Eratosthenes algorithm
         """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(n + 1) if primes[i]]

    def play_game(n):
        """ Function to get player to play the game"""
        primes = get_primes(n)
        player = 1
        while primes:
            removed = False
            for p in primes:
                if n % p == 0:
                    primes = [x for x in primes if x % p != 0]
                    n = max(x for x in range(1, n) if x not in primes)
                    removed = True
                    break
            if not removed:
                break
            player = 3 - player
        return player

    scores = [play_game(n) for n in nums]
    if scores.count(1) > scores.count(2):
        return "Maria"
    elif scores.count(1) < scores.count(2):
        return "Ben"
    else:
        return None
