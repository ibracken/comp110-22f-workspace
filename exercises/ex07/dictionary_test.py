"""A place to test dictionary."""

__author__ = 730563276

from dictionary import invert
from dictionary import favorite_color
from dictionary import count
import pytest


# invert
def test_invert_key_error() -> None:
    """Raises a key error."""
    with pytest.raises(KeyError):
        dictionary: dict[str, str] = {'a': 'lists', 'c': 'lists', 'b': 'lists'}
        invert(dictionary)


def test_invert_one_entry() -> None:
    """Tests the invert function when the dictionary has one value."""
    dictionary: dict[str, str] = {"Elsa": "Anna"}
    assert invert(dictionary) == {"Anna": "Elsa"}


def test_invert_many_entries() -> None:
    """Tests the invert function when the dictionary has two values."""
    dictionary: dict[str, str] = {"MJ": "Scottie", "Lebron": "Kyrie", "Magic": "Kareem"}
    assert invert(dictionary) == {"Scottie": "MJ", "Kyrie": "Lebron", "Kareem": "Magic"}


# favorite_color
def test_favorite_color_empty() -> None:
    """Tests the favorite_color function when it is empty."""
    dictionary: dict[str, str] = {}
    assert favorite_color(dictionary) == ""


def test_favorite_color_one_entry() -> None:
    """Tests the favorite_color function when the dictionary has one value."""
    dictionary: dict[str, str] = {"Elsa": "Blue"}
    assert favorite_color(dictionary) == "Blue"


def test_favorite_color_many_entries() -> None:
    """Tests the favorite_color function when the dictionary has two values."""
    dictionary: dict[str, str] = {"MJ": "Blue", "Lebron": "Red", "Magic": "Red"}
    assert favorite_color(dictionary) == "Red"


# count
def test_count_empty() -> None:
    """Tests the count function when it is empty."""
    count_list: list[str] = {}
    assert count(count_list) == {}


def test_count_one_entry() -> None:
    """Tests the count function when the dictionary has one value."""
    count_list: list[str] = ["Elsa"]
    assert count(count_list) == {"Elsa": 1}


def test_count_many_entries() -> None:
    """Tests the count function when the dictionary has two values."""
    count_list: list[str] = ["MJ", "Scottie", "Lebron", "Lebron", "MJ", "MJ"]
    assert count(count_list) == {"MJ": 3, "Scottie": 1, "Lebron": 2}