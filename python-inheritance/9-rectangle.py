#!/usr/bin/python3
"""This module defines the BaseGeometry class with basic validation methods."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
