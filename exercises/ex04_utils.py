"""Checks to see if all the numbers in a list equal a single int."""

__author__ = "730563276"


def all(all_numbers: list[int], checking_value: int) -> bool:
    """Checks to see if all the numbers in a list equal a certain int."""
    i = 0
    while len(all_numbers) > i:
        if all_numbers[i] != checking_value:
            return False
        else:
            i += 1
    if len(all_numbers) == 0:
        return False
    return True


def max(input: list[int]) -> int:
    """Picks out the largest value in a list."""
    i = 0
    saved_number = input[i]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(input) - 1:
        if saved_number >= input[i + 1]:
            i += 1
        else:
            saved_number = input[i + 1]
            i += 1

    return saved_number


def is_equal(first_string: list[int], second_string: list[int]) -> bool:
    """Checks to see if two lists are equal."""
    i = 0
    if len(first_string) != len(second_string):
        return False
    while i < len(first_string):
        if first_string[i] == second_string[i]:
            i += 1
        else:
            return False
    return True