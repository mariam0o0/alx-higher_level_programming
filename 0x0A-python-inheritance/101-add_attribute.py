#!/usr/bin/python3

"""
module for add_attribute
"""


def add_attribute(obj, key, value):
    if not hasattr(obj, '__dict__') and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
