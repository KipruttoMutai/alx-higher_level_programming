#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the Perimeter of Rectangle"""
        perimeter = 0
        if self.__height == 0 or self.__width == 0:
            return perimeter
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Prints the rectangle with # symbol"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = []
        for _ in range(self.__height):
            [rect.append('#') for _ in range(self.__width)]
            if _ != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """"Rerurns string representation of a rectangle"""
        rectangle = "Rectangle("+str(self.__width)
        rectangle += ","+str(self.__height)+")"
        return rectangle
