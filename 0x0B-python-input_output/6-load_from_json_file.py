#!/usr/bin/python3
""" a function that creates an obj from json file"""
import json


def load_from_json_file(filename):
    """creates a python obj from json file"""
    with open(filename, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    return json_data
