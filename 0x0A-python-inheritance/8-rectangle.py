#!/usr/bin/python3
"""
BaseGeometry/Rectangle. module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class"""
    def __init__(self, width, height):
        "initialization""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
