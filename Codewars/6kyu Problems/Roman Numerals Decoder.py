roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def solution(string):
    total = 0
    for i in range(len(string)):
        if i + 1 < len(string) and roman_dict[string[i]] < roman_dict[string[i + 1]]:
            total -= roman_dict[string[i]]
        else:
            total += roman_dict[string[i]]

    return total