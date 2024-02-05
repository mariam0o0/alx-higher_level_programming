#!/usr/bin/python3

"""
module for add_attribute
"""


def add_attribute(obj, key, value):
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
