#!/usr/bin/python3
"""
Module that for json string
"""

import json


def from_json_string(my_str):
    """returns an object from JSON string"""
    return json.loads(my_str)
