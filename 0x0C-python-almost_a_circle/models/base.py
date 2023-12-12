#!/usr/bin/python3
"""Creates a base Model"""


class Base:
    """Represents a Base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""

        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
