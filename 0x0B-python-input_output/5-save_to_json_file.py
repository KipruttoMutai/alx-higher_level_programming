#!/usr/bin/python3

"""
module:5-save_to_json_file
resource:save_to_json_file(function)
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as file:
        file = json.dumps(my_obj)
        return file
