#!/usr/bin/env python3
"""Module for basic JSON serialization"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a dictionary and save it to a JSON file

    Args:
        data: Python dictionary
        filename: output file name
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it

    Args:
        filename: input file name

    Returns:
        Python dictionary
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
