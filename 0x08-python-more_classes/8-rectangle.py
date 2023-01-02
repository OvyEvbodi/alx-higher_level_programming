#!/usr/bin/python3

'''Defines an empty rectangle.
It contains one class ``Rectangle``.'''


class Rectangle:
    '''Defines a rectangle
        Attributes:
        __width (int): the width of the rectangle
        __height (int): the height of the rectangle
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initializes an instance of a rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        Rturns:
            None
        '''
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''Calculates the area of a rectangle instance
        Returns:
            The calculated area
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculates the area of a rectangle instance
        Returns:
            The calculated area
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        '''Returns the canonical string representation of the object
        Returns:
            The canonical string representation of the object
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __str__(self):
        '''Creates a new string object from the given object
        Returns:
            A string representation of the object
        '''
        rect_str = ""
        if self.__height == 0 or self.__width == 0:
            return rect_str
        rect_print = [str(self.print_symbol) * self.width
                      for i in range(self.height)]
        rect_str = '\n'.join(rect_print)
        return rect_str

    def __del__(self):
        '''Deletes an instance of a rectangle'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Finds the bigger of 2 rectangles

        Args:
        rect_1: the first rectanngle
        rect_2: the second rectangle

        Returns:
        rect_2, if it's bigger than rect_1,
        otherwise, rect_1
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
