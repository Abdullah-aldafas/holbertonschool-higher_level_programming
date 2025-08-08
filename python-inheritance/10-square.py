#!/usr/bin/python3
"""This module defines the BaseGeometry class with basic validation methods."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("Size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
