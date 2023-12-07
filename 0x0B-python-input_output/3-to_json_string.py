#!/usr/bin/python3
import json
"""a function that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """returns the JSON representation of an object """
    data = json.dumps(my_obj)
    return data
