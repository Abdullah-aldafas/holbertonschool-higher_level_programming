#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """Custom list class that can print its elements sorted."""

    def print_sorted(self):
        """that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
