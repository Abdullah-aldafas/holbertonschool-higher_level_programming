#!/usr/bin/python3


"""
This module defines a function that adds two integers
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    """  
    if type(a) is not int and type(a) is not float:  #  if not isinstance(a, (int, float)):
        raise TypeError("a and b must be integers")
    if type(b) is not int and type(b) is not float:  # if not isinstance(b, (int, float)):
        raise TypeError("a and b must be integers")
    return int(a) + int(b)
