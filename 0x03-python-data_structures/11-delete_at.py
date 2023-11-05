#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_list = len(my_list)
    new_list = []
    if idx < 0 or idx >= len_list:
        return my_list
    else:
        new_list = my_list[:idx] + my_list[idx + 1:]
        return new_list
