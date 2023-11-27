#!/usr/bin/python3

"""Define an empty class Rectangle"""


class Rectangle:
    """"Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize a Rectangle
        Args:
            width(int): The width of the Rectangle
            height(int): The height of the Rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Retreives private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets a new value to the attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retreives private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets a new value to the attribute size"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
