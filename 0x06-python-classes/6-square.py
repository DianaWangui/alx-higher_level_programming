#!/usr/bin/python3

"""
class Square that defines a square
Private instance attribute: size
property def size(self): to retrieve it
property setter def size(self, value): to set it:

Private instance attribute: position
which takes a default (0, 0) tuple.
property def position(self): to retrieve it
property setter def position(self, value): to set it:

And a Public instance method: def area(self):
that returns the current square area
Method my_print prints the square using "#".
"""


class Square:
    """
    Instantiating variables size and position.
    Raising errors if conditions are not met
    printing sqaure using '#'
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size setter to ser size of sqaure.
        Args:
            value (int): size of Square
        Raises:
            TypeError: If value is not int.
            ValueError: if value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter that sets position of Square.
        Args:
            value (tuple): tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple of two integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of a square
        Returns: area
        """
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
