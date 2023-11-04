#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    idx_len = list_len - 1
    if idx < 0 or idx > idx_len:
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
