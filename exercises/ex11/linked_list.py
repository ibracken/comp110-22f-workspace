"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730563276"

"""globals"""
i = 0
max_value = 0
nodes = 0


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is not None:
            return last(head.next)
        else:
            return head.data

def value_at(head: Optional[Node], index: int) -> int:
    """Retruns the value of a data of a Node at a given index"""
    global i
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.data
    elif i is not index:
        i += 1
        return value_at(head.next, index)
    else:
        i = 0
        return head.data

def max(head: Optional[Node]) -> int:
    """Finds the max data value in a series of Nodes"""
    global max_value
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is not None:
        if head.data > max_value:
            max_value = head.data
        return max(head.next)
    if head.next is None:
        if head.data > max_value:
            max_value = head.data
        return max_value


def linkify(items: list[int]) -> Optional[Node]:
    """Turns a list of items into connected Nodes"""
    global nodes
    if len(items) == 0 or len(items) == nodes:
        return None
    nodes += 1
    a_node: Node = Node(items[nodes - 1], linkify(items))
    nodes = 0
    return a_node


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    return None