#!/usr/bin/python3
"""A function that checks instance of class"""


def is_same_class(obj, a_class):
    """ Returns True if object is instance of class and Flase otherwise"""
    return type(obj) is a_class
