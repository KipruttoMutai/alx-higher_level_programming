#!/usr/bin/python3

"""function to convert class to json"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    for JSON serialization of an object
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("Object is not an instance of a class")
    json_dict = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
        json_dict[attr_name] = attr_value
    return json_dict
