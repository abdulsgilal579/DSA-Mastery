import math

number = int(input("Type number to check: "))
sqrt_number = int(math.sqrt(number))


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            return False
    return f"{number} is a prime number!"


print(is_prime(number))
