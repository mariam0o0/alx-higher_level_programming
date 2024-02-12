#!/usr/bin/python3
"""
This module implements `base` class of all other classes in this project.
"""
import json


class Base:
    """
    implementation of Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization

        Args:
            id (int, optional): object id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: dict):
        """json reprsentation of list"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create instance with all attributes already set"""
        if cls.__name__ == "Rectangle" or cls.__name__ == "Square":
            new = cls(5, 5)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        f_name = f"{cls.__name__}.json"
        obj = []
        with open(f_name, 'r') as file:
            file_string = file.read().replace('\n', '')
            data = cls.from_json_string(file_string)
            for i in data:
                obj.append(cls.create(**i))
        return obj

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list"""
        if list_objs is None:
            list_objs = []
        f_name = f"{cls.__name__}.json"
        json_string = cls.to_json_string
        ([obj.to_dictionary() for obj in list_objs])
        with open(f_name, 'w') as file:
            return file.write(json_string)
