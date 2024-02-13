#!/usr/bin/python3
"""
modules: square
resources: class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """creates a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes square with its attributes inherited from rectangle"""
        super().__init__(height=size, width=size, x=x, y=y, id=id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """gets the value of size"""
        return self.width

    @size.setter
    def size(self, size):
        """sets the value of width and height to size"""
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size
