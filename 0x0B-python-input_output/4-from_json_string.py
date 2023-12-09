#!/usr/bin/python3
""" a function that returns an object rep of json str"""
import json


def from_json_string(my_str):
    """Returns the json object rep of json str"""
    my_obj_json = json.loads(my_str)
    return my_obj_json
