#!/usr/bin/python3
"""This module defines a Square class."""

class Square:
    """Represents a square with a given size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square with the given size."""
        self.__size = size
        self.__position

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get postion attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter of position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print("")
        for i in range(self.size):
            for j in range(size):
                print('#', end = "")
            print("")

    def my_print(self):
            """Prints the square using the character '#'."""
            if self.__size == 0:
                print()
            else:
                for i in range(self.__size):
                    print(" " * self.__position[0] + "#" * self.__size)
