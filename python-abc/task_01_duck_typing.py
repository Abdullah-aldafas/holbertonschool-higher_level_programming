#!/usr/bin/python3
"""
This module defines an abstract Shape class and two subclasses: Circle and Rectangle.
"""

from abc import ABC, abstractmethod
import math as m


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
        return m.pi * (self.radius**2)

    def perimeter(self):
        return 2 * m.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter of any shape passed in."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


c = Circle(5)
r = Rectangle(3, 7)

print("[Circle Info]")
shape_info(c)

print("\n[Rectangle Info]")
shape_info(r)
