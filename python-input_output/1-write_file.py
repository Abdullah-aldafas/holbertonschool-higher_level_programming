#!/usr/bin/python3

"""
Module for reading and printing the content of a text file.
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number of characters written.
    """

    with open(filename, "w", encoding="UTF8") as f:
        print(f.write(text), end="")
