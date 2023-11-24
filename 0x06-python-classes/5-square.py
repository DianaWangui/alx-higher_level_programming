#!/usr/bin/python3

"""A module that defines a square"""


class Square:
    """A class that represents a square"""
    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not int
            ValueError: if size is < 0
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns: area
        """
        return (self.__size ** 2)

    def print(self):
        """print the square in #"""
        if self.__size = 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
