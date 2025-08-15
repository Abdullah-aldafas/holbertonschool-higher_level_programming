#!/usr/bin/python3
"""Return a dictionary of simple-typed attributes of an object for JSON."""


def class_to_json(obj):
    """Return the dictionary description of an
     object for JSON serialization."""
    return obj.__dict__.copy()
