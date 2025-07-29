#!/usr/bin/python3
"""
this module is an emptiy class
"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        """ initilize function"""
        self.size = size

    @property
    def size(self):
        """a getter function for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """a setter function for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """a function that returns the area of square"""
        return self.__size * self.__size
