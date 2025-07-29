#!/usr/bin/python3
"""
This module defines a Square class that validates its size and can compute its area.
"""

class Square:
    """
    Represents a square. The size attribute is private and validated.
    """
    def __init__(self, size=0):
        """
        Initialize the square with an optional size.
        Size must be an integer and greater than or equal to zero.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current area of the square.
        """
        return self.__size * self.__size