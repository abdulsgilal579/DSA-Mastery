def high(x):
    score = 0
    h_word = "highest"
    words = x.split()
    for word in words:
        new_score = 0
        for char in word:
            new_score += ord(char.lower()) - ord('a') + 1
            if new_score > score:
                score = new_score
                h_word = word
    return h_word


string = input("Type anything")
print(high(string))