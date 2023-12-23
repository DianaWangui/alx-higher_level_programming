#!/usr/bin/python3

"""class Square that defines a square."""


class Square:
    """initializing square, determines size, calculates area, prints"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes instance of square
        Args:
            size: the size of square
            position: position used to indent the square
         """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size"""
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
        """sets position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 3 positive integer")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1]:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        This functon determines the area of a square

        Returns: area
        """
        return (self.__size ** 2)

    def my_print(self):
        """printing square using symbol "#"."""
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print('')
        for i in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], '#' * self.__size))

    def __str__(self):
        """
        prints a square offsetting it by position with symbol "#"
        """
        if self.__size == 0:
            return ''
        n_lns = '\n' * self.__position[1]
        space = ' ' * self.__position[0]
        hashes = '#' * self.__size
        return n_lns + '\n'.join(space + hashes for e in range(self.__size))
