#!/usr/bin/python3
my_list = [1,2,3]
def print_list_integer(my_list=[]):
    list_len = len(my_list)
    for i in my_list:
        print("{}".format(i))
print_list_integer(my_list)
