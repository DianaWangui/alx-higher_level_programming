#!/usr/bin/python3
"""a function that returns json rep of an obj string"""
import json


def to_json_string(my_obj):
    """ Returns a json rep of a tring object """
    my_json = json.dumps(my_obj)
    return my_json
