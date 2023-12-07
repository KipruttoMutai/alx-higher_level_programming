#!/usr/bin/python3
"""a function that writes an Object to a text using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file
    Args:
    my_obj: the text to write
    filename: name of file to write the text to
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
