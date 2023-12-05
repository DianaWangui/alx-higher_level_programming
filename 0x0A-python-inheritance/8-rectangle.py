#!/usr/bin/python3
"""Defining a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle by using BaseGeometry class
    """
    def __init__(self, width, height):
        """ Initializing a new rectangle
        Args:
            width (int): Width of the new Rectangle
            height (int): Height of the new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
