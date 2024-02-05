#!/usr/bin/python3
"""
My list module.
"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
    """prints the list, but sorted"""
        print(sorted(self))
