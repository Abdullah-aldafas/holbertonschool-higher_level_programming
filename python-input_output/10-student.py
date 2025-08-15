#!/usr/bin/python3

"""Module that defines a Student class with JSON serialization capability."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance."""
        if isinstance(attrs, list):
            return {
                key: self.__dict__[key]
                for key in attrs if key in self.__dict__
            }
        else:
            return self.__dict__.copy()
