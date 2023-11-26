#!/usr/bin/python3

"""
A module that defines a square by private instance attributes: size
And a Public instance method: def area(self):
that returns the current are of a square
Methods Getter and Setter properties for size
property def size(self): to retrieve it
property setter def size(self, value): to set it:
Method my_print prints the square using "#".
"""


class Square:
    """
    instantiating variable self and size.
    Raising errors if conditions are not met.
    printing using '#'
    """
    def __init__(self, size=0):
        """Initializng private variable
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if `size` is not integer
            ValueError: if `size` is < 0
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
