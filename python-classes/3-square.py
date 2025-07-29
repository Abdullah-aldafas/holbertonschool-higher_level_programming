#!/usr/bin/python3
"""
This module defines a Square class with size validation.
"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """a function that returns the area of square"""
        return self.__size * self.__size
