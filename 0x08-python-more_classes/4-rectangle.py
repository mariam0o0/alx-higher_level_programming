#!/usr/bin/python3

"""
Module for a class Rectangle
"""


class Rectangle:
    """Class of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """String representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ['#' * self.__width for _ in range(self.__height)]
        return '\n'.join(rect)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
