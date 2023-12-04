#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """defines a base geometry with a public instance method area"""

    def area(self):
        """Raises an exception area not defined"""
        raise Exception("area() is not implemented")
