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

    def update(self, *args, **kwargs):
        """
        *args is the list of arguments - no-keyworded arguments
        **kwargs can be thought of as a double pointer to a dictionary:
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
