#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    d_num = 0
    for tup in my_list:
        number += (tup[0] * tup[1])
        d_num += (tup[1])
    return (number/d_num)
