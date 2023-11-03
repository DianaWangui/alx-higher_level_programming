#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list_len = len(my_list)
    idx_len = list_len - 1
    if idx < 0:
        return my_list
    elif idx > idx_len:
        return my_list
    else:
        my_list[idx] = element
        new_list = my_list
        return new_list

my_list = [2, 3, 4, 5, 6]
idx = 5
new_element = 7
new_list = replace_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)
