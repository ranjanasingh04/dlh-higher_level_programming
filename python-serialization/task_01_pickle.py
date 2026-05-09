#!/usr/bin/python3
"""Module for serializing and deserializing custom objects using pickle."""

import pickle


class CustomObject:
    """A custom object with serialization support."""

    def __init__(self, name, age, is_student):
        """Initialize object attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes in required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object instance to a file.

        Args:
            filename (str): File where object will be saved.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object instance from a file.

        Args:
            filename (str): File to load object from.

        Returns:
            CustomObject instance or None if error occurs.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
