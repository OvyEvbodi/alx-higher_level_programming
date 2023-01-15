#!/usr/bin/python3

"""This module creates a rectangle
It inherits from the ``Base`` class in base.py
"""

#Base = __import__('models').base.Base
from models.base import Base

class Rectangle(Base):
    """defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of a rectangle

        Attributes:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x(int): the x axis of the rectangle
            y(int): the y axis of the rectangle
            id(int): the id of the rectangle
        """

        super().__init__(id)

        self.validate_attr(width, "width", 1)
        self.width = width

        self.validate_attr(height, "height", 1)
        self.height = height

        self.validate_attr(x, "x")
        self.x = x

        self.validate_attr(y, "y")
        self.y = y

    @staticmethod
    def validate_attr(value, name, dim=0):
        """validates an attribute,
        and raises the appropriate exception

        Args:
            value: the value to be validated
            name: the name of the attribute
            dim: whether the attribute height/width (non-zero value for yes)
        """

        if not dim:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
            if type(value) != int:
                raise TypeError(f"{name} must be an integer")


    @property
    def width(self):
        """gets the width attribute of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute of a rectangle"""
        self.validate_attr(value, "width", 1)
        self.__width = value

    @property
    def height(self):
        """gets the height attribute of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute of a rectangle"""
        self.validate_attr(value, "height", 1)
        self.__height = value

    @property
    def x(self):
        """gets the x attribute of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x attribute of a rectangle"""
        self.validate_attr(value, "x")
        self.__x = value

    @property
    def y(self):
        """gets the y attribute of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y attribute of a rectangle"""
        self.validate_attr(value, "y")
        self.__y = value

    def area(self):
        """calculates the area of a rectangle
        
        Returns:
            the area of the rectangle
        """
        return self.__width * self.__height
