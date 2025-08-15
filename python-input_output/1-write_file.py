#!/usr/bin/python3

"""
Module that provides a helper to write text into a file.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return
    the number of characters written.
    """

    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
