#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """instantiation with validated height and width
    Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
    """

    def __init__(self, width, height):
        """Instiation"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
