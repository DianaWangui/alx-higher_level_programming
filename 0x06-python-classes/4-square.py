#!/usr/bin/python3

""" a square class that defines a square """


class Square:
    """instantiation of the attributes of the methods """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        area = self.__size * self.__size
        return area
