#!/usr/bin/python3
ef weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        d_num = 0
        for tup in my_list:
            number += (tup[0] * tup[1])
            d_num += (tup[1])
        return (number/d_num)
    return 0
