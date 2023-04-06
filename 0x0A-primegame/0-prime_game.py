#!/usr/bin/python3
def isWinner(x, nums):
    def get_primes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(n + 1) if primes[i]]

    def play_game(n):
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
