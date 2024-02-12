#!/usr/bin/python3
"""
This module implements `base` class of all other classes in this project.
"""
import json
import os.path
import csv
import turtle


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
        """Dictionary to instance"""
        if cls.__name__ == "Rectangle":
            ins = cls(1, 1)
        if cls.__name__ == "Square":
            ins = cls(1)
        ins.update(**dictionary)
        return ins

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file"""
        filename = cls.__name__ + ".json"
        text = []
        if list_objs is not None:
            for item in list_objs:
                text.append(item.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as file:
            return file.write(Base.to_json_string(text))

    @classmethod
    def load_from_file(cls):
        """file to instances"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as file:
            data = cls.from_json_string(file.read())
        return [cls.create(**i) for i in data]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to CSV file"""
        filename = cls.__name__ + ".csv"
        fieldnames = []
        rows = []
        if list_objs is not None and len(list_objs) > 0:
            fieldnames = list(list_objs[0].to_dictionary().keys())
            rows.append(fieldnames)
            for obj in list_objs:
                rows.append(list(obj.to_dictionary().values()))
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        return filename

    @classmethod
    def draw(cls, rectangles, squares):
        """Draws all the Rectangles and Squares"""
        screen = turtle.Screen()
        pen = turtle.Pen()
        figures = rectangles + squares

        for figure in figures:
            pen.up()
            pen.goto(figure.x, figure.y)
            pen.down()
            pen.forward(figure.width)
            pen.right(90)
            pen.forward(figure.height)
            pen.right(90)
            pen.forward(figure.width)
            pen.right(90)
            pen.forward(figure.height)
            pen.right(90)

        screen.exitonclick()
