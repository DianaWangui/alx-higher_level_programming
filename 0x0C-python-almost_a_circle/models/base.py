#!/usr/bin/python3
"""Base class with a public attribute and a class constructor."""


class Base:
    """private class attribute."""
    __nb_objects = 0
    """instantiating a class constructor."""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
            Base.__nb_objects += 1
        else:
            id - __nb_objects

