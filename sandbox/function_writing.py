def reverse_multiply(a_list: list[int]) ->list[int]:
    final_list: list[int] = list()
    a_num = int
    i = len(a_list) - 1
    while i >= 0:
        a_num = a_list[i]
        a_num *= 2
        final_list.append(a_num)
        i -= 1
    return final_list

#print(reverse_multiply([1, 2, 3]))

def free_biscuits(game: dict[str, list[int]]) -> dict[str, list[bool]]:
    final_dict: dict[str, list[bool]] = {}
    for item in game:
        added_value = 0
        for number in game[item]:
            added_value += number
        if added_value >= 100:
            final_dict[item] = True
        else:
            final_dict[item] = False
    return final_dict

print(free_biscuits({"UNC": [1, 2 ,3], "NC": [100, 1, 100]}))

def dictionary_numbers(game: dict[str, list[int]]) -> list[int]:
    final_list: list[int] = list()
    for item in game:
        for point in game[item]:
            final_list.append(point)
    return final_list

print(dictionary_numbers({"UNC": [1, 2 ,3], "NC": [100, 1, 100]}))


def merge_lists(fruit: list[str], fruit_num: list[int]) -> dict[str, int]:
    final_dict: dict[str, int] = {}
    i = 0
    if len(fruit) != len(fruit_num):
        return final_dict
    else:
        while i < len(fruit):
            final_dict[fruit[i]] = fruit_num[i]
            i += 1
        return final_dict

#print(merge_lists(["apple", "orange"], [5, 4]))

def reverse_string(input: str) -> str:
    i: int = len(input) - 1
    final_string: str = ""
    while i >= 0:
        final_string += input[i]
        i -= 1
    return final_string
print(reverse_string("cows"))


class HotCocoa:
    has_whip: bool
    flavor: str
    sweetness: int
    marshmallow_count: int
    
    def __init__(self, has_whip: bool, flavor: str, sweetness: int, marshmallow_count: int):
        self.has_whip = has_whip
        self.flavor = flavor
        self.sweetness = sweetness
        self.marshmallow_count = marshmallow_count

    def mallow_adder(self, mallows: int):
        self.marshamllow_count += mallows
        mallows *= 2
        self.sweetness += mallows

    def calorie_count(self) -> float:
        cals: float = 0
        if self.flavor == "vanilla" or "peppermint":
            cals += 30
        else:
            cals += 20
        if self.has_whip == True:
            cals += 100
        cals += (self.marshmallow_count/2)
        return cals