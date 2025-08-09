#!/usr/bin/python3
"""
This module defines an abstract Shape class and two subclasses: Circle and Rectangle.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height

    def area(self) -> float:
        return self.__width * self.__height

    def perimeter(self) -> float:
        return 2 * self.__width + 2 * self.__height


def shape_info(shape) -> None:
    """Prints area and perimeter of any shape passed in."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
