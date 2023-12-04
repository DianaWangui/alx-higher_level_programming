#!/usr/bin/python3
"""function that defines an inherited class-checked function """


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True
        Otherwise - False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
