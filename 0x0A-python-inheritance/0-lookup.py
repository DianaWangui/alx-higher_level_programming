#!/usr/bin/python3

"""Define an object attribute lookuo function """


def lookup(obj):
    """Return a list of an objects available attribute """
    return [attr for attr in dir(obj)]
