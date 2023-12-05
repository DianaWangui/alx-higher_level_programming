#!/usr/bin/python3
"""Containing Mylist class """


class MyList(list):
    """public instance method for printing sorted list """

    def print_sorted(self):
        """printing the list in ascending order"""
        print(sorted(self))
