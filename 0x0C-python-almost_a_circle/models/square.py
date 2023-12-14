#!/usr/bin/python3
"""A class Square that inherits from class Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """instantiating the class attribute of the square
    inheriting some attributes from base class Reactangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for size
        Return: size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """a method to return the string"""
        return ("[{:s}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width))
