#!/usr/bin/python3
""" A baseclass module that is used to define area
raises an error if area is not implemented
defines an integer validation method
if the value passed is not int it raises TypeError
if value is <= 0, it raised a ValueError
"""


class BaseGeometry:
    """method area that raises error if area is not
    implemented
    """
    def area(self):
        raise Exception('area() is not implemetend')
    """ second method for validating the value passed
    """
    def integer_validation(self, name, value):
        if is not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value  <= 0:
            raise ValueError("{} must be greater than 0".format(name))
