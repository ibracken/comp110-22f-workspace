def average_grades(dict_1: dict[str, list[int]]) -> dict[str, float]:
    new_dict: dict[str, float] = {}
    # Goes through all the keys in dict_1
    for item in dict_1:
        # Does nothing, just establishes the total variable
        total = 0
        # Goes through each item in each value(list)
        for grade in dict_1[item]:
            total += grade
        new_dict[item] = total/len(dict_1[item])
    return new_dict

print(average_grades({'Ian': [67, 84, 99], }))
