#!/usr/bin/python3
""" Creates class Square """

from numbers import Number

class Square:
    """ Square class"""

    def __init__(self, size=0):
        self.__validate_size(size)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__validate_size(value)
        self.__size = value

    def __validate_size(self, value):
        if not isinstance(value, Number):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        """check if equal to another square"""
        return self.area() == other.area()

    def __lt__(self, other):
        """check if less than other square"""
        return self.area() < other.area()

    def __le__(self, other):
        """check if less than or equal to other square"""
        return self.area() <= other.area()

    def __ne__(self, other):
        """check if not equal to another suqare"""
        return self.area() != other.area()

    def __gt__(self, other):
        """check if greater than another square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """check if greater than or equal to another square"""
        return self.area() >= other.area()
