#!/usr/bin/python3

"""
Module for reading and printing the content of a text file.
"""


def read_file(filename=""):
    """
    Read a text file (UTF8) and print its content to stdout.
    """

    with open(filename, "r", encoding="UTF8") as f:
        print(f.read(), end="")
