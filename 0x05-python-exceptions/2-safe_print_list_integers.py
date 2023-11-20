#!/usr/bin/python3

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    try:
        for i in range(x):
            if not is_int(my_list[i]):
                continue
            print("{:d}".format(my_list[i]), end="")
            nb_print += 1
    finally:
        print()
    return nb_print


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
