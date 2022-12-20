"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify

__author__ = "730563276"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3

def test_value_at_empty() -> None:
    """Value_at of an empty Linked List should raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 1)

def test_value_at_non_empty() -> None:
    """Value_at of a non-empty list should return the data value at the index."""
    Nodes = Node(1, Node(2, Node(3, None)))
    assert value_at(Nodes, 2) == 3

def test_value_at_index_zero() -> None:
    """Value_at of a non-empty list should return the data value at the index of 0."""
    Nodes = Node(5, Node(2, Node(3, None)))
    assert value_at(Nodes, 0) == 5

def test_max_empty() -> None:
    """Value_at of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)

def test_max_last_max() -> None:
    """Max of a non-empty list should return its greatest data value(at the end)."""
    Nodes = Node(1, Node(2, Node(3, None)))
    assert max(Nodes) == 3

def test_max_middle_max() -> None:
    """Last of a non-empty list should return its greatest data value(in the middle)."""
    Nodes = Node(1, Node(5, Node(3, None)))
    assert max(Nodes) == 5

def test_linkify_empty() -> None:
    """Value_at of an empty List should return nothing."""
    a_list = list()
    assert linkify(a_list) == None 

def test_linkify_small_list() -> None:
    """Value_at of an empty List should return nothing."""
    a_list = list([1, 2, 3])
    assert str(linkify(a_list)) == "1 -> 2 -> 3 -> None"


def test_linkify_other_list() -> None:
    """Value_at of an empty List should return nothing."""
    a_list = list([5, 2, 18])
    assert str(linkify(a_list)) == "5 -> 2 -> 18 -> None"