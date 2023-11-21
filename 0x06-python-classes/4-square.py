#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes square
        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square
           Args:
               self: the instance
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves a private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets a new value to the attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
