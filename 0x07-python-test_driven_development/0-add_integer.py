#!/usr/bin/python3
def add_integer(a, b=98):

    """Return integer addition of a and b

    if float a and b must first be casted to integer

    if not integer or non-float :TypeEror.
    """

    if ((not isinstance (a, int) and not isinstance (b, float))):
        raise TypeError ("a must be an integer")
    if ((not isinstance (b, int) and not isinstance (b, float))):
        raise TypeError ("b must be an integer")
    return (int(a) + int(b))