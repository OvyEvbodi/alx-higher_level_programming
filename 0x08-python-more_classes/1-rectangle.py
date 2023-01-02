#!/usr/bin/python3

'''This module defines an empty rectangle.
It contains one class ``Rectangle``.'''


class Rectangle:
    '''Defines a rectangle
        Attributes:
        __width (int): the width of the rectangle
        __height (int): the height of the rectangle
    '''
    def __init__(self, width=0, height=0):
        '''Initializes an instance of a rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        Rturns:
            None
        '''
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        '''Gets the width attribute of a rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width attribute of a rectangle'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Gets the height attribute of a rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height attribute of a rectangle'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
