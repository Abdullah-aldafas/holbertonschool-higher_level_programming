#!/usr/bin/python3

"""
Script that adds all command-line arguments to a list,
and saves it to add_item.json in JSON format.

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
