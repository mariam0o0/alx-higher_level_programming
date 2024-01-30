#!/usr/bin/python3
"""
Module print_square
"""


def print_square(size):

    """function that prints a square with the character #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return

    for _ in range(size):
        print('#' * size)
