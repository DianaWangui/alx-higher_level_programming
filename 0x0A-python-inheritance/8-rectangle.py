#!/usr/bin/python3
"""Defining a class Rectangle that inherits
from another class called BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle by using BaseGeometry class
    """
    def __init__(self, width, height):
        """ Initializing a new rectangle
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height


r = Rectangle(3, 5)
print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
