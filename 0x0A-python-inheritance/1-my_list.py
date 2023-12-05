#!/usr/bin/python3
"""Defining an inherited list class MyList """


class MyList(list):
    """instantiating the MyList attributes"""
    def __init__(self):
        """Calling the parent class list """
        list.__init__(self):

    """public instance method for printing sorted list """

    def print_sorted(self):
        """printing the list in ascending order"""
        print(sorted(self))
