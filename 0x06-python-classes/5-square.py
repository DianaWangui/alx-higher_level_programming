#!/usr/bin/python3

"""
Create class Square that defines a square by private instance attribute: size
And a Public instance method: def area(self):
that returns the current square area
Methods Getter and Setter properties for size.
property def size(self): to retrieve it
property setter def size(self, value): to set it:
Method my_print prints the square using "#".
"""


class Square:
    """
    Instantiating the variables self and size.
    raising errors if conditions are not met.
    and print square using '#'.
    """
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
        """
        Calculates area of square
        Return: area
        """
        return (self.__size ** 2)

    def print(self):
        if self.__size = 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
