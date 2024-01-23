#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square with a given size."""
    def __init__(self, size=0):
        """Initializes a new square with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end = "")
            print("")
