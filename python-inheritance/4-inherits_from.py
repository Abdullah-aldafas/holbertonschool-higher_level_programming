#!/usr/bin/python3
"""Module that defines the MyList class."""


def inherits_from(obj, a_class):
    """a function that returns True if the object of a class that inherited"""
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
