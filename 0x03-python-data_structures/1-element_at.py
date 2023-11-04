#!/usr/bin/python3
my_list = [2, 4, 5, 7]
idx = 4


def element_at(my_list, idx):
    listlen = len(my_list)
    idx_len = listlen - 1
    if idx < 0:
        return None
    elif idx > idx_len:
        return None
    else:
        return my_list[idx]


result = element_at(my_list, idx)
if result is not None:
    print("Element at index {:d} is {}".format(idx, result))
