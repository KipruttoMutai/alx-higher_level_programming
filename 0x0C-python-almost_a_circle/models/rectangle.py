#!/bin/usr/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """A class representing a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y
