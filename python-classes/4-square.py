#!/usr/bin/python3
"""
This module defines a Square class with size validation.
"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        self.size = size

    @property
    def size(self):
        """a getter function for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size
