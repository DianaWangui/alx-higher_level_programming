#!/usr/bin/python3

"""
class square
private instance attribute: size
property def size(self): getter
property def size(self, value): setter
private instance attribute: position
property def position(self): getter
property def position(self, value): setter
public method: def area(self):
returns area of square
method def my_print(self): prints square using '#'
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        square instance initialization
        Args:
            size: the size of square
            position: position used to intend the square
         """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setting position value"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 3 positive integer")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1]:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Finding area"""
        return (self.__size ** 2)

    def my_print(self):
        """printing square using symbol '#'."""
        if self.size == 0:
            print()
        for i in range(self.__Position[1]):
            print('')
        for i in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], '#' * self.__size))

    def __str__(self):
        """
        prints a square offsetting it by position with symbol #
        """
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.__position[1]
        space = ' ' * self.__position[0]hash = '#' * self.__size
        return new_lines + '\n'.join(space + hash for e in range(self.size))
