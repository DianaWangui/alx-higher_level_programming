#!/usr/bin/python3
"""
A module that defines an inherited list class MyList.
"""


class MyList(list):
    """Inherits from list."""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
