#!/usr/bin/python3

"""
Module: custom_object
This module defines the CustomObject class with attributes and methods
for displaying data, and serializing/deserializing objects using pickle.
"""

import pickle
import json


class CustomObject:
    """
    A custom class that represents an
    object with a name, age, and student status.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initialize a CustomObject instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object instance and save
        it to a file using pickle.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a
        file and return the CustomObject instance.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
