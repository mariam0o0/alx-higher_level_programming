#!/usr/bin/python3
"""
Module to append text to file
"""


def append_write(filename="", text=""):
    """ Appends text to file
    and returns the number of characters added"""
    with open(filename, 'a') file:
        file.write(text)
        return len(text)
