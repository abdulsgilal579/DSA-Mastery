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


for num in range(1, number + 1):
    if is_prime(num):
        primeNumbers.append(num)

print(primeNumbers)
