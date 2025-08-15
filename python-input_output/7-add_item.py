#!/usr/bin/python3

"""
Module that provides a function to create a
Python object from a JSON file.

"""
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
import sys
import os

filename = "add_item.json"

if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
