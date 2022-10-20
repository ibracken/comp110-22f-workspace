"""Making use of dictionaries."""

__author__ = "730563276"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and flips the key with the value."""
    # Creates a new dictionary that will have the flipped values.
    inverted: dict[str, str] = {}
    # Creates a loop that modifies each value in a dictionary
    for key in old_dict:
        for inverted_key in inverted:
            if old_dict[key] == inverted_key:
                raise KeyError("You can't invert a list that has the same values!")
        # For each key in the new dictionary, the new key is the value of the original dictionary while each new value is the key from the old dictionary.
        inverted[old_dict[key]] = key
    return inverted


def favorite_color(color_names: dict[str, str]) -> str:
    """Takes a dictionary of colors with names as keys and returns the most common color."""
    # Creates a new list of str
    color_list: list[str] = []
    # Creates a dictionary that will track the # of colors
    color_tracker: dict[str, int] = {}
    # Creates str that will be returned
    fav_color = ""
    # Creates int that will be changed to the max value in the final_dict
    color_max = 0
    # loops through color_dict to gather the colors
    for name in color_names:
        # Adds the color_names value to color_list
        color_list.append(color_names[name])
    # loops through color list
    for color in color_list:
        # Checks if the color is in color list
        if color in color_tracker:
            # If the color is in the list, the # in color tracker goes up by one
            color_tracker[color] += 1
        else:
            # If the color is not in the color tracker, it is added and given a value of 1
            color_tracker[color] = 1
    # Creates a loop where each color(key) in the color_tracker dictionary is gone through
    for color in color_tracker:
        # if color_tracker index is greater or equal than the index before it...
        if color_tracker[color] > color_max:
            # Then favorite color is equal to that color
            fav_color = color
            color_max = color_tracker[color]
    return fav_color


def count(words: list[str]) -> dict[str, int]:
    """Takes a list of strings and returns how often each string is repeated."""
    # Creates the dictionary where key is a str and the value is an int
    tracker: dict[str, int] = {}
    # loops through the list of strings
    for item in words:
        # Checks if the str is in tracker already
        if item in tracker:
            tracker[item] += 1
        else:
            tracker[item] = 1
    return tracker