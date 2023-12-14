#!/usr/bin/python3
"""Base class with a public attribute and a class constructor."""
import json


class Base:
    """private class attribute."""
    __nb_objects = 0
    """instantiating a class constructor."""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string rep of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string rep of list_dictionary.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Write the JSON string rep of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        # Get the class name
        class_name = cls.__name__

        # Generate filename
        filename = f"{class_name}.json"

        # Convert list_objs to list dict
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        #Get JSON str representation
        json_string = cls.to_json_string(list_dicts)

        # Write JSON str to file
        with opne(filename, 'w', encoding="utf-8") as file:
            file.write(json_string)
