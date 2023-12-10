#!/usr/bin/python3

"""a script that adds all args to a python list and save to file """
import sys
import json

save_to_json_file = __import__('5-save_to_json_file')
load_from_json_file = __import__('6-load_from_json_file')

filename = "add_item.json"
args = sys.argv

with open(filename, "a+", encoding="utf-8") as file:
    my_list = []
    my_list.extend(args[1:])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
