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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
