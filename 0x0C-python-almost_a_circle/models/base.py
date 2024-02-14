#!/usr/bin/python3
"""
modules:base.py
resources:class base
"""
import json


class Base:
    """creates a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
         assigns the public instance attribute id with this argument value
         if id is not none otherwise  assigns the new value to
         the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string representation of a dictionary"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        new_list_objs = []
        if type(list_objs) is list:
            for item in list_objs:
                new_list_objs.append(item.to_dictionary())
        class_name = cls.__name__
        filename = f"{class_name}.json"
        json_string = Base.to_json_string(new_list_objs)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return "[]"
        else:
            return json.loads(json_string)
