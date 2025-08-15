#!/usr/bin/python3

"""
Module that provides a function to convert Python objects to JSON strings.
"""
import json as j


def to_json_string(my_obj):
    """
    Return the JSON string representation of a Python object.
    """
    ra = j.dumps(my_obj)
    return ra  # return j.dumps(my_obj)   the same solv
