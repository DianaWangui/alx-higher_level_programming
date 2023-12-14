#!/usr/bin/python3
"""Base class with a public attribute and a class constructor."""
import json


class Base:
    """private class attribute."""

    __nb_objects = 0
    """instantiating a class constructor."""
    def __init__(self, id=None):
        """Instantiate the attributes.

        Args:
            id (int): class id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string rep of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string rep of list_dictionary.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string rep of list_objs to a file."""
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(cls.to_dictionary(obj))

        filename = "{}.json".format(cls.__name__)

        # Write JSON str to file
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

    @classmethod
    def from_json_string(json_string):
        """Return the JSON string rep of list."""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance using the provided dict."""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from JSON file."""
        filename = "{}.json".format(cls.__name__)
        instance_list = []

        try:
            with open(filename, 'r') as f:
                json_data = f.read()
                data_list = cls.from_json_string(json_data)
                for data in data_list:
                    instance = cls.create(**data)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass

        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list of instances to a CSV file."""
        filename = '{}.csv'.format(cls.__name__)
        with open(filename, 'w', newline='') as my_file:
            writer = csv.writer(my_file)
            for x in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([x.id, x.width, x.height, x.x, x.y])
                if cls.__name__ == "Square":
                    writer.writerow([x.id, x.size, x.x, x.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file.

        Returns:
            list: list of instances.
        """
        instance_list = []
        filename = '{}.csv'.format(cls.__name__)

        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    data = {"id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])}
                if cls.__name__ == "Square":
                    data = {"id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])}
                instance = cls.create(**data)
                instance_list.append(instance)
        return instance_list
