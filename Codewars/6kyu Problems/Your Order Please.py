import re

def order(sentence):
    str_split = sentence.split()
    items_list = [0 for x in range(len(str_split))]
    print(items_list)
    for i in str_split:
        number_list = re.findall(r'\d+', i)
        number = int(number_list[0])
        items_list[number-1] = i
    joined_list = ' '.join(items_list)
    return joined_list

order("Hello2 how1 are4 you3 ")