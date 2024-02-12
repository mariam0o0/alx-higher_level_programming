#!/usr/bin/python3
"""
This module implements a Square object
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ the class init"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self) -> str:
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.__size)
