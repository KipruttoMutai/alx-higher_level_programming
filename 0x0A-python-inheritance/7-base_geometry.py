#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """defines a base geometry with a public instance method area"""

    def area(self):
        """Raises an exception area not defined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """It validates value
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
