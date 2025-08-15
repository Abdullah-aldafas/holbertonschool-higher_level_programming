#!/usr/bin/python3

"""
Module that provides a helper to write text into a file.
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number of characters written.
    """

    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
