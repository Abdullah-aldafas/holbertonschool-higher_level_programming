#!/usr/bin/python3
"""
This module defines an abstract Shape class and two subclasses: Circle and Rectangle.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


def shape_info(shape):
    """Prints area and perimeter of any shape passed in."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
