#!/usr/bin/python3

"""
module:3-to_json_string
resource:to_json_string()function
"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)"""
    json_string = json.dumps(my_obj)
    return json_string
