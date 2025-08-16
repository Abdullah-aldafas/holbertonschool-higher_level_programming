#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.
    This function reads a CSV file, converts its content into
    a list of dictionaries, and saves it as 'data.json'.
    """
    try:
        row: List[Dict[str, str]] = []
        with open(csv_filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                row.append(dict(r))

        with open("data.json", "w", encoding="utf-8") as o:
            json.dump(row, o, indent=4)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
