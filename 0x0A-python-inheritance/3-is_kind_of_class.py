#!/usr/bin/python3
"""unction that returns True if the object is an instance
otherwise returns false
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object to check.
         a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        otherwise - False
    """
    return isinstance(obj, a_class)
