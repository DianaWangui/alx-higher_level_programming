#!/usr/bin/python3

"""Magic class that works as python bytecode."""

import math


class MagicClass:
    """Initialize the radius of the circle."""
    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Get the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Get the circumference of circle."""
        return 2 * math.pi * self.__radius
