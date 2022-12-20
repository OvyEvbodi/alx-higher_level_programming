#!/usr/bin/python3
'''Defines a Square class'''


class Square:
    '''Defines a Square
    Attributes:
    __size (int): the size of 1 side of a square
    '''
    def __init__(self, size=0):
        ''' Initializes an instance of the Square class
        Args:
            size (int): the size of 1 side of a square
        Returns: None
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ''' Calculates the area of a Square instance
                Returns: the area of the square
        '''
        return self.__size * self.__size
