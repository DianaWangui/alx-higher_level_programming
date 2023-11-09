#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    dic_dup = a_dictionary.copy()
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
    else:
        return dic_dup
