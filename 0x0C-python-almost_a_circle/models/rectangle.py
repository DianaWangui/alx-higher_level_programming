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
        # Validating width, height, x, y during instantiation
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

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
        if type(value) != int:
            raise TypeError('{} must be an integer'.format('width'))
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # getter and setter for x
    @property
    def x(self):
        """Getter for x
        Return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the Rectangle instance
        Returns: area"""
        area = self.__height * self.__width
        return area

    def display(self):
        """method to display rectangle using '#' characters"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Return a string presentation of Rectangle class."""
        return ("[{:s}] ({}) {}/{} -{}/{}".format(self.__class__.name__,
            self.id, self.__x, self.__y, self.__width, self.__height))
