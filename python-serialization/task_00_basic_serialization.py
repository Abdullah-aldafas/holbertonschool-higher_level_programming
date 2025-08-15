#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it as a JSON file.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a
    Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)

    if not isinstance(obj, dict):
        raise TypeError("JSON content is not a dictionary")

    return obj
