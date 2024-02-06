#!/usr/bin/python3
"""
Module to add arguments to a Python list and save them to a file
"""

import sys
import os

arguments = sys.argv[1:]

savej = __import__('5-save_to_json_file').save_to_json_file
loadj = __import__('6-load_from_json_file').load_from_json_file

listj = []
if os.path.exists('add_item.json'):
    listj = loadj('add_item.json')

savej(listj + arguments, "add_item.json")
