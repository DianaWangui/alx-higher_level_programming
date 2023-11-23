#!/usr/bin/python3
"""
    a class square that defines a square
    with private instances of size and raisng
    error incase certain conditions are not met

"""


class Square:
    """instatiating object attribute size"""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size  must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        sArea = self.__size * self.__size
        return sArea
