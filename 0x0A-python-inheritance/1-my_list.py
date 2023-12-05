#!/usr/bin/python3
"""Defining an inherited list class MyList """


class MyList(list):
    """public instance method for printing sorted list """

    def print_sorted(self):
        """printing the list in ascending order"""
        print(sorted(self))
