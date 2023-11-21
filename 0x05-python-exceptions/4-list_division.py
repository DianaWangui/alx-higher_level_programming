#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list1 = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            list1.append(div)
        except ZeroDivisionError:
            print("division by 0")
            list1.append(0)
        except TypeError:
            print("wrong type")
            list1.append(0)
        except IndexError:
            print("out of range")
            list1.append(0)
    return list1
