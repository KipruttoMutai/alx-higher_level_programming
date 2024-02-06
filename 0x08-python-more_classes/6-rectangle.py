#!/usr/bin/python3
"""Defines class rectangle"""


class Rectangle:
    """represents rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializes rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * self.width + 2 * self.height

    def __str__(self):
        """Represents rectangle using #"""
        if self.height == 0 or self.width == 0:
            return ""
        else:
            rectangle = ""
            for _ in range(self.height):
                rectangle += '#' * self.width + '\n'
            return rectangle[:-1]

    def __repr__(self):
        """Returns string representation of rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when a class instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
