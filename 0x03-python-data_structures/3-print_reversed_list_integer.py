#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversedlist = my_list[::-1]
    for i in reversedlist:
        print("{:d}".format(i))
