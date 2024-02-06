#!/usr/bin/python3
"""
Module that adds args to JSON file
"""

import sys
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file


def add_to_list_and_save(arguments):
    """adds all arguments to a Python list and save them to a file"""
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []
    existing_list.extend(arguments)
    save_to_json_file(existing_list, "add_item.json")
