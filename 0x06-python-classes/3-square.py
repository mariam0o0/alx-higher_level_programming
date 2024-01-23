#!/usr/bin/python3
"""This module defines Square class."""


class Square:
    """Represents a square with a given size"""
    def __init__(self, size=0):
        """Initializes a new square with the given size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            """Returns current square area"""
            return self.__size ** 2
