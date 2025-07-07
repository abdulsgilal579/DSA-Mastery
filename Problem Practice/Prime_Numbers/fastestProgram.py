"""
✅ 2. Sieve of Eratosthenes (FASTEST for many primes)
✅ Very efficient — O(n log log n)
✅ Best for finding lots of primes quickly

Concepts: https://chatgpt.com/share/686b90d8-77c8-8012-b0d1-ee5d6f84c9a3

"""


def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0:2] = [False, False]  # 0 and 1 are not prime

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    for i in range(2, limit + 1):
        if primes[i]:
            print(i, end=" ")


number = int(input("Number: "))
sieve(number)
