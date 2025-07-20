def open_or_senior(data):
    new_list = ["Open"] * len(data)
    for idx, box in enumerate(data):
        if box[0] >= 55 and box[1] > 7:
            new_list[idx] = "Senior"
        else:
            new_list[idx] = "Open"
    return new_list


