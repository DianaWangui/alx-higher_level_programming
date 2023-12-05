#!/usr/bin/python3
"""Defining an inherited list class MyList """


class MyList(list):
    """Inherits from list uisng
    Methods: print_sorted(self)
    """
    def __init__(self):
        """initializes the object """
        super().__init__()

    def print_sorted(self):
        """printing the list in ascending order"""
        print(sorted(self))


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
