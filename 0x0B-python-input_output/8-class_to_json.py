#!/usr/bin/python3
"""a function that returns the dict description with simple data structure"""


def class_to_json(obj):
    """the function"""
    if not hasattr(obj, '__dict__'):
        return obj
    data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            data[key] = value
        elif hasattr(value, '__dict__'):
            data[key] = class_to_join(value)
    return data
