#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            nb_print += 1
    except IndexError:
        pass
    finally:
        print()
    return nb_print
