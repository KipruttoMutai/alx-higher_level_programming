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
            raise  TypeError ("exception must be an integer")
        elif size < 0:
            raise ValueError ("size must be >= 0")
        else:
            self.size = size
