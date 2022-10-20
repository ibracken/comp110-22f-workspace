"""A series of functions involving lists."""

__author__ = 730563276


def only_evens(number_list: list[int]) -> list[int]:
    """Creates new list of all the integers in the list that are even."""
    i = 0
    final_list = []
    while len(number_list) > i:
        if number_list[i] % 2 == 0:
            final_list.append(number_list[i])
            i += 1
        else: 
            i += 1
    return final_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """The function takes two lists and puts them together into a final list."""
    i = 0
    last_list = []
    while len(list_1) > i:
        last_list.append(list_1[i])
        i += 1
    i = 0
    while len(list_2) > i:
        last_list.append(list_2[i])
        i += 1
    return last_list
    

def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Creates a new list from a section of another list."""
    i = 0
    final_list = []
    while len(a_list) > i:
        if i >= start_index and i <= end_index - 1:
            final_list.append(a_list[i])
            i += 1
        else:
            i += 1
    return final_list