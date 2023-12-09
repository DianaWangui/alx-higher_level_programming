#!/usr/bin/python3
""" a function that wtites an obj to a txt file using json rep"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    obj_str = json.dumps(my_obj)

    with open(filename, "w") as file:
        file.write(obj_str)
