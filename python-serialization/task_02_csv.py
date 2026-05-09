#!/usr/bin/python3
"""Module to convert CSV data into JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV file data into JSON format and saves it as data.json.

    Args:
        csv_filename (str): Name of the input CSV file

    Returns:
        bool: True if conversion succeeds, False otherwise
    """
    try:
        # Read CSV data
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Write JSON data
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
