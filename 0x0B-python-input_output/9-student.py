#!/usr/bin/python3
"""
Module for class Student.
"""


class Student:
    """the Student class"""

    def __init__(self, first_name, last_name, age):
        """class initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of an instance"""
        return self.__dict__
