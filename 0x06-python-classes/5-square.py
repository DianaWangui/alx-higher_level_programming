#!/usr/bin/python3


"""
class Square that defines a square
The class takes one private instance: self.__size
uses getter and setter properties
check condition of the value and raises error
"""


class Square:

    """ instantiating private attribute size using __"""
    def __init__(self, size=0):
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
        return (self.__size ** 2)

    def print(self):
        if self.__size = 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
