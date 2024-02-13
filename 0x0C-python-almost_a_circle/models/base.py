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
