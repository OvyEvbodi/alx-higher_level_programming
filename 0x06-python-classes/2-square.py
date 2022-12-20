#!/usr/bin/python3
'''Defines a Square class'''


class Square:
    '''Defines a Square
    Attributes:
    __size (int): the size of 1 side of a square
    '''
    def __init__(self, size=0):
        ''' Initializes an instnce of the Square class
        Args:
            size (int): the size of 1 side of a square
        Returns: None
        '''
        if type(size) is not int:
            print("size must be an integer")
            raise TypeError
        elif size < 0:
            print("size must be >= 0")
            raise ValueError
        self.__size = size
