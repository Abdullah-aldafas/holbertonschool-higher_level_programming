#!/usr/bin/python3
"""Module that defines the MyList class."""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance"""
    if type(obj) is a_class:  # return type(obj) is a_class
        return True
    else:
        return False
