#!/usr/bin/python3

"""
module for Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initalize"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
