#!/usr/bin/python3
"""
This module implements a Rectangle object
"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The class init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
