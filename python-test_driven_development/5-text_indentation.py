#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines
after each '.', '?', or ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', or ':'.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""

        if buffer.strip():
            print(buffer.strip())
