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

    def validation(self, name, value, condition=True):
        """validate the value and type of attributes"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if condition and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not condition and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """The width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter"""
        self.validation('width', value)
        self.__width = value

    @property
    def height(self):
        """The height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter"""
        self.validation('height', value)
        self.__height = value

    @property
    def x(self):
        """The x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """The x setter"""
        self.validation('x', value, False)
        self.__x = value

    @property
    def y(self):
        """The y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """The y setter"""
        self.validation('y', value, False)
        self.__y = value
