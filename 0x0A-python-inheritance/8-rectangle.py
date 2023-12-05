#!/usr/bin/python3
"""Dfining a class Rectangle that inherits
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
        self.__width = width
        self.__height = height
        super().integer_validator("width",width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
