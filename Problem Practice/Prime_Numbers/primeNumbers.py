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

"""
🔢 We’re checking which numbers multiply to give 36
These are called factor pairs.
We start from 1 and go up:

✅ Working pairs:
	•	1 × 36 → 1 and 36 are both factors of 36
	•	2 × 18 → 2 and 18 are factors
	•	3 × 12 → 3 and 12 are factors
	•	4 × 9 → 4 and 9 are factors
	•	5 × ? → 5 does not divide 36 evenly (36 ÷ 5 = 7.2), so ❌
	•	6 × 6 → 6 × 6 = 36 ✔️ — this is exactly the square root (√36 = 6)

🛑 Now stop here!
After this point:
	•	7 × ? → would give 7 × 5.14 = 36 (not an integer) ❌
	•	8, 9, 12… — we’ve already seen these numbers on the other side of the earlier pairs.

🧠 So what’s the point?
After √36 = 6, the factor pairs just reverse (like 9 × 4, 12 × 3, 18 × 2, 36 × 1).
So you don’t need to keep checking.

✅ That’s why we only check up to √n
	•	It saves time
	•	If no factor is found before or at √n → the number is prime

"""
