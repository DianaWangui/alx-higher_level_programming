#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_list = len(my_list)
    if idx < 0 or idx >= len_list:
        return my_list
    else:
        del my_list[idx]
    return my_list
