#!/usr/bin/python3
"""
module:rectangle
resources:class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """creates a rectangle"""
    @property
    def width(self):
        """
        The width getter method returns the size
        of the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The corresponding setter method is used to
        set the size of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        The height getter method is used to return the size
        of the rectangle's height to the user.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        While the corresponding height setter method is used
        to the the size of the rectangle's height.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        The x getter method is used to set the x coordinate
        position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Its corresponding setter method is used to set x
        coordinate of the rectangle
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        The y getter method return the y coordinate
        position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        The corresponding setter method is used to
        set the y coordinate position.
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """calls the super classs with id
        and assigns each argument with the right attribute
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character "#" """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """overrides the __str__method"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute using args
        **kwargs) that assigns a key/value argument to attributes
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
