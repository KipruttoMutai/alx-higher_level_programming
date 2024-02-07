#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square
        Args:
            size (int): The size of the new square
            position (tuple): The position of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieves the current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets a new value to the attribute position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints out the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
