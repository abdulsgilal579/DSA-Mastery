import math

number = int(input("Number: "))
primeNumbers = []


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


primeNumbers = [n for n in range(1, number + 1) if is_prime(n)]
print(primeNumbers)
