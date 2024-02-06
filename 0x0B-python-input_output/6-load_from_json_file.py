#!/usr/bin/python3

"""
mode:6-load_from_json_file
resource:load_from_json_file(filename)function
"""
import json


def load_from_json_file(filename):
    """
    Deserialize strings from specified file
    """
    with open(filename) as file:
        py_obj = json.load(file)
    return py_obj
