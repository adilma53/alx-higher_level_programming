#!/usr/bin/python3
"""
a model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.
"""

from os import path
import json


class Base:
    """
    base class to manage unique IDs for objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes a Base instance with a unique ID.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_data):
        """
        converts a list of dictionaries to a JSON string.
        """
        if list_data is None or len(list_data) == 0:
            return '[]'
        return json.dumps(list_data)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves a list of objects to a JSON file.
        """
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                return file.write(cls.to_json_string(None))

            json_attrs = [obj.to_dictionary() for obj in list_objs]
            return file.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        """
        converts a JSON string to a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates a new instance of the class using the provided dictionary.
        """
        if cls.__name__ == 'Square':
            dummy = cls(3)
        elif cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        loads objects from a JSON file and returns a list of instances.
        """
        filename = cls.__name__ + '.json'

        if not path.exists(filename):
            return []

        with open(filename, mode='r', encoding='utf-8') as file:
            objs = cls.from_json_string(file.read())
            instances = [cls.create(**elem) for elem in objs]
            return instances
