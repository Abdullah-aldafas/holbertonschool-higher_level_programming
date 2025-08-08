#!/usr/bin/python3
"""This module defines an empty class."""


class BaseGeometry:
    """Represents an empty class."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError("<name> must be an integer")
        if vlaue <= 0:
            raise ValueError("<name> must be greater than 0")
