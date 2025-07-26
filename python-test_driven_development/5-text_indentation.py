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
    text = text.strip()
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print()
            print()
            while i + 1 < len(text) and text[i + 1] in " \t":
                i += 1
        i += 1
