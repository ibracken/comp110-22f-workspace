"""The model classes maintain the state and logic of the simulation."""


from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730563276"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x 
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> int:
        """Calculates the distance between two points by using square roots."""
        distance_x = abs(self.x - other.x)
        distance_y = abs(self.y - other.y)
        final_distance_total = sqrt(distance_x ** 2 + distance_y ** 2)
        return final_distance_total


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def contract_disease(self) -> None:
        """Makes the cell infected."""
        self.sickness = constants.INFECTED
    
    def immunize(self) -> None:
        """Makes the cell immune to infection."""
        self.sickness = constants.IMMUNE
    
    def is_vulnerable(self) -> bool:
        """Checks to see if the cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Checks to see if the cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        return False

    def is_immune(self) -> bool:
        """Checks to see if the cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "pink"
        if self.is_immune():
            return "orange"

    def tick(self) -> None:
        """Moves the cell."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness == 90:
            self.immunize()

    def contact_with(self, other_cell: Cell) -> None:
        """Checks to see if an infected cell is in contact with vulnerable one."""
        if (self.is_vulnerable() and other_cell.is_infected()):
            self.contract_disease()
        if (self.is_infected() and other_cell.is_vulnerable()):
            other_cell.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []

        if infected_cells <= 0 or cells <= infected_cells:
            raise ValueError("Some Cells must be infected.")

        if immune_cells > cells or immune_cells < 0:
            raise ValueError("The cells aren't adding up.")
        
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)

        for i in range(infected_cells):
            self.population[i].contract_disease()

        for i in range(immune_cells):
            self.population[i].immunize()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < - constants.MAX_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        counter = 0
        for cell in self.population:
            if cell.is_vulnerable() or cell.is_immune():
                counter += 1
            if counter == len(self.population):
                return True
        return False

    def check_contacts(self) -> None:
        """Checks to see if any two cells are touching."""
        for cell in self.population:
            for other_cell in self.population:
                if cell != other_cell and cell.location.distance(other_cell.location) <= constants.CELL_RADIUS:
                    cell.contact_with(other_cell)