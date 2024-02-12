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

    def __str__(self):
        """string representation"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        self.validation('width', value)
        self.__size = value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        full = (self.id, self.size, self.x, self.y)
        if args != ():
            self.id, self.size, self.x, self.y = \
                args + full[len(args):len(full)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self) -> dict:
        """dictionary representation"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': size, 'y': y}
