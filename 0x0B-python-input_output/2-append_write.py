#!/usr/bin/python3
"""
Module to append to file
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file
    returns the number of characters added """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return file.tell()
