#!/usr/bin/python3
"""Module for XML serialization and deserialization."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format.

    Args:
        dictionary (dict): Dictionary to serialize
        filename (str): Output XML filename
    """
    # Create root element
    root = ET.Element("data")

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): Input XML filename

    Returns:
        dict: Reconstructed dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for child in root:
        value = child.text

        # Try converting numbers back to int
        if value.isdigit():
            value = int(value)

        # Convert boolean strings back to bool
        elif value == "True":
            value = True
        elif value == "False":
            value = False

        result[child.tag] = value

    return result
