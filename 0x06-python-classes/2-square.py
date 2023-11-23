#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ initializing an isntance of a class"""
    def __init__(self, size=0):
        self.__size = 0
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
