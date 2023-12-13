#!/usr/bin/python3

"""Rectangle Class module that inherits from Base."""
from models.base import Base



class Rectangle(Base):
    """instantiating attributes of rectangle.
    Inherits attribute of: id
    from Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # setting of getter and setter of each attribute
    # width setter and getter
    @property
    def width(self):
        """Getter for width
        Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__width = value

    # height getter and setter
    @property
    def height(self):
        """Getter for height
        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        self.height = value

    # getter and setter for x
    @property
    def x(self):
        """Getter for x
        Return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # Getter and Setter for y
    @property
    def y(self):
        """Getter for y
        Return: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.__y = value
