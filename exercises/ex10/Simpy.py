"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730563276"


class Simpy:
    """A Class that consists of a list of floats."""
    values: list[float]

    def __init__(self, input_list: list[float]):
        """Initializes the Simpy list."""
        self.values = []
        for item in input_list:
            self.values.append(item)

    def __repr__(self) -> str:
        """Represents Simpy as a string."""
        return f"Simpy({self.values})"

    def fill(self, repeated_value: float, repeated_count: int) -> None:
        """Adds a value to a list a certain number of times."""
        self.values = []
        i = 0
        while i < repeated_count:
            self.values.append(repeated_value)
            i += 1
        return None

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Adds numbers to the values list."""
        assert step != 0.0
        current_value: int = 0
        current_value = start
        while current_value != stop:
            self.values.append(current_value)
            current_value += step

    def sum(self) -> float:
        """Takes the sum of all the items in the values list."""
        sum_number: float = 0.0
        sum_number = sum(self.values)
        return sum_number

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds together all the values between the list and either another list or a value."""
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            result: Simpy = Simpy([])
            for item in range(len(self.values)):
                result.values.append(self.values[item] + rhs.values[item])
            return result
        else:
            result: Simpy = Simpy([])
            for item in range(len(self.values)):
                result.values.append(self.values[item] + rhs)
            return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raises the values list to the power of either a float or the equal index of a different value list."""
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            result: Simpy = Simpy([])
            for item in range(len(self.values)):
                result.values.append(self.values[item] ** rhs.values[item])
            return result
        else:
            result: Simpy = Simpy([])
            for item in range(len(self.values)):
                result.values.append(self.values[item] ** rhs)
            return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks to see if an item in values is equal to another value."""
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            result: list[bool] = []
            for item in range(len(self.values)):
                if self.values[item] == rhs.values[item]:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            result: list[bool] = []
            for item in range(len(self.values)):
                if self.values[item] == rhs:
                    result.append(True)
                else:
                    result.append(False)
            return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks to see if any item in values is greater than another value."""
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            result: list[bool] = []
            for item in range(len(self.values)):
                if self.values[item] > rhs.values[item]:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            result: list[bool] = []
            for item in range(len(self.values)):
                if self.values[item] > rhs:
                    result.append(True)
                else:
                    result.append(False)
            return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns an item at a certain index."""
        if isinstance(rhs, int):
            answer: float = self.values[rhs]
            return answer
        else:
            result: Simpy = Simpy([])
            for item in range(len(rhs)):
                if rhs[item] is True:
                    result.values.append(self.values[item])
            return result

        
