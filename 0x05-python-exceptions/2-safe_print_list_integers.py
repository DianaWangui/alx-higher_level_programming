#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        nb_print = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                nb_print += 1
                print("{:d}".format(my_list[i]), end="")
    except TypeError:
        print("This is not an int")
    else:
        print("")
        return nb_print


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
