#!/usr/bin/python3
"""Module for converting object to JSON string"""

import json


def to_json_string(my_obj):
    """ return JSON representation"""
    return json.dumps(my_obj)
