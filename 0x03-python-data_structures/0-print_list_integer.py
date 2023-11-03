#!/usr/bin/python3
my_list = [1,2,3]
def print_list_integer(my_list=[]):
    list_len = len(my_list)
    list1 = my_list[0:]
    for i in list1:
        print("{}".format(i))
print_list_integer(my_list)
