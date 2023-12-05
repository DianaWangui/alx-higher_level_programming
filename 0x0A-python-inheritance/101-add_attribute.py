#!/usr/bin/python3
"""A module that adds attributes to objects if possible"""


def add_attribute(obj, att, value):
    """A function that adds a new attribute to an object if possible.

    Args:
        obj
        att
        value
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
