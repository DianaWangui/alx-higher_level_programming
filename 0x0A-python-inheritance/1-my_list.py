#!/usr/bin/python3
"""Defining an inherited list class MyList """


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object """
        super().__init__(self):

    def print_sorted(self):
        """printing the list in ascending order"""
        print(sorted(self))
