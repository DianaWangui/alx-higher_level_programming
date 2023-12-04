#!/usr/bin/python3
"""Containing Mylist class """

def Mylist(list):
    """a list subclass """
    def __init__(self):
        """initilize the object """
        super().__init__()

    def print_sorted(self):
        """printing the list in ascending order"""
        print(sorted(self))
