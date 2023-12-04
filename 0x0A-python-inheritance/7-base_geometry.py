#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """defines a base geometry with a public instance method area"""

    def area(self):
        """Raises an exception area not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """It validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
