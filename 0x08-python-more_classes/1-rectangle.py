#!/usr/bin/python3
"""Defines class rectangle"""


class Rectangle:
    """represents rectangle"""
    def __init__(self, width=0, height=0):
        """initializes rectangle"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """property getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """property getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
