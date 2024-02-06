#!/usr/bin/python3
"""
Module for class Student.
"""


class Student:
    """The Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initialize The Class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            dict = {}
            for i, j in self.__dict__.items():
                if i in attrs:
                    dict[i] = j
            return dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """eplaces all attributes of the Student"""
        for i, j in json.items():
            self.__dict__[i] = j
