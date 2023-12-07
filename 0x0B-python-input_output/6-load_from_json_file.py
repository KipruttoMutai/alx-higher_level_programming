#!/usr/bin/python3
""" a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Opens the Json file"""
    with open(filename, 'r') as file:
        json.load(file)
