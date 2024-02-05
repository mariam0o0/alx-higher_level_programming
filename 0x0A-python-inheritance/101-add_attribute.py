#!/usr/bin/python3

"""
add_attribute module
"""


def add_attribute(obj, key, value):
    """adds a new attribute to an object if possible"""
    if not hasattr(obj, "__dict__") and not hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")
    if not hasattr(obj, key) and hasattr(obj, "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
