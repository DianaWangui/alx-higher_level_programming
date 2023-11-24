#!/usr/bin/python3

"""
class Square that defines a square
The class takes one private instance size
used getter to retrieve the value 
uses setter to set the value
check condition of the value and raises error

"""

class Square:
    """ instantiating private attribute size using __"""
    def __init__(self, size=0):
        self.__size = size

    # getting the size using property decorater
    @property
    def size(self):
        return self.__size

    # setting the value and raising error on some conditions
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # a function to find area of the square
    def area(self):
        return (self.__size **2)

    # a function to print to stdout the square using #
    def print(self):
        if self.__size = 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
