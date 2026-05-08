#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Student to JSON with filter"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        """Return dictionary representation of Student"""
        if type(attrs) is list and all(type(i) is str for i in attrs):
            new_dict = {}

            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]

            return new_dict

        return self.__dict__
