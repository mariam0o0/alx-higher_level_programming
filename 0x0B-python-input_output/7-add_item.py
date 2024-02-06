#!/usr/bin/python3
'''
Module to add all arguments to a Python list save them to a file
'''

import sys
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file
import os

arg_list = sys.argv[1:]

lisst = []
if os.path.exists('add_item.json'):
    lisst = load_from_json_file('add_item.json')

save_to_json_file(lisst + arg_list, "add_item.json")
