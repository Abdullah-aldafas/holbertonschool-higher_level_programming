#!/usr/bin/python3

"""
Module that provides a function to save a Python
object to a file in JSON format.
"""
import json as j


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a text file using its JSON representation.
    """
    with open(filename, "w", encoding="utf-8") as c:
        return j.dump(my_obj, c)
