#!/usr/bin/python3
"""Containing Mylist class """


def MyList(list):
    """a list subclass """
    def __init__(self):
        """initilize the object """
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
