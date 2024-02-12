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
        """string reprsentation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.validation('size', value)
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

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        return {'id' : self.id, 'x' : self.x, 'size' : self.__size, 'y' : self.y}
