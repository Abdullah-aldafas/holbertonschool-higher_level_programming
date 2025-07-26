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

    current_line = ""
    for char in text:
        current_line += char
        if char in ".?:":
            print(current_line.strip())
            print()
            current_line = ""
    if current_line.strip():
        print(current_line.strip())