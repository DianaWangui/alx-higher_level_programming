#!/usr/bin/python3
"""Defining an inherited list class MyList """


class MyList(list):
    """Inherits from list uisng
    Methods: print_sorted(self)
    """
    def __init__(self):
        """initializes the object """
        super().__init__(self):

    def print_sorted(self):
        """printing the list in ascending order"""
        print(sorted(self))
