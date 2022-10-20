"""A place to test utils."""

__author__ = 730563276

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Tests when only_evens function consists of an empty string."""
    number_list: list[float] = []
    assert only_evens([number_list]) == []


def test_only_evens_single_item() -> None:
    """Tests when only_evens function consists of a single item."""
    number_list: list[float] = [110]
    assert only_evens(number_list) == [110]


def test_only_evens_many_items() -> None:
    """Tests when only_evens function consists of many items."""
    number_list: list[float] = [8, 2, 10]
    assert only_evens(number_list) == [8, 2, 10]


def test_concat_empty() -> None:
    """Tests when concat function consists of an empty string."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_single_item() -> None:
    """Tests when concat function consists of a single item."""
    list_1: list[int] = [1]
    list_2: list[int] = [3]
    assert concat(list_1, list_2) == [1, 3]


def test_concat_many_items() -> None:
    """Tests when concat function consists of many items."""
    list_1: list[int] = [1, 8, 100]
    list_2: list[int] = [2, 4, 3]
    assert concat(list_1, list_2) == [1, 8, 100, 2, 4, 3]


def test_sub_empty() -> None:
    """Tests when sub function consists of an empty string."""
    a_list: list[int] = []
    start_index: int = 0
    end_index: int = 1
    assert sub(a_list, start_index, end_index) == []


def test_sub_single_item() -> None:
    """Tests when sub function consists of a single item."""
    a_list: list[int] = [1]
    start_index: int = 0
    end_index: int = 1
    assert sub(a_list, start_index, end_index) == [1]


def test_sub_many_items() -> None:
    """Tests when sub function consists of many items."""
    a_list: list[int] = [0, 1, 2, 3, 4]
    start_index: int = 1
    end_index: int = 4
    assert sub(a_list, start_index, end_index) == [1, 2, 3]