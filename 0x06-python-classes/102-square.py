#!/usr/bin/python3

"""Class that checks if squares are equal."""


class Square:
    """Instantiate the size of square."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter for the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the value."""
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to find area of square."""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Compare the current area with next."""
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        """Compare the current and next."""
        if isinstance(other, Square):
            return self.area() != other.area()

    def __gt__(self, other):
        """Compare the current and next."""
        if isinstance(other, Square):
            return self.area() > other.area()

    def __ge__(self, other):
        """compare the current and next."""
        if isinstance(other, Square):
            return self.area() >= other.area()

    def __lt__(self, other):
        """compare current and next."""
        if isinstance(other, Square):
            return self.area() < other.area()

    def __le__(self, other):
        """compare the current and next."""
        if isinstance(other, Square):
            return self.area() <= other.area()
