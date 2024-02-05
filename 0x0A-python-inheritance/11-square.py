#!/usr/bin/python3

"""
Square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size):
        """Initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of Square"""
        return self.__size ** 2

    def __str__(self):
        """Return the square description string"""
        return f"[Square] {self.__size}/{self.__size}"
