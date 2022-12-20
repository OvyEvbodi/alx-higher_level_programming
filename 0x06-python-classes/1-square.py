#!/usr/bin/python3
'''Defines a Square class'''


class Square:
    '''Defines a Square
    Attributes:
    __size (int): the size of 1 side of a square
    '''
    def __init__(self, size):
        ''' Initializes an instnce of the Square class
        Args:
            size (int): the size of 1 side of a square
        Returns: None
        '''
        self.__size = size
