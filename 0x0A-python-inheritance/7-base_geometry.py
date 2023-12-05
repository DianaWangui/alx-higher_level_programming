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
        """unimplemented area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
