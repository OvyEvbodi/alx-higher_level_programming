#!/usr/bin/python3
'''Defines a Square class'''


class Square:
    '''Defines a Square
    Attributes:
    __size (int): the size of 1 side of a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        ''' Initializes an instance of the Square class
        Args:
            size (int): the size of 1 side of a square
        Returns:
            None
        '''
        self.__size = size
        self.__position = position

    def area(self):
        ''' Calculates the area of a Square instance
        Returns:
            the area of the square
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''Gets the size attribute of a class instance
        Returns:
            the size of a square instance
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets the size attribute of a square instance
        Args:
            value: the value to set size to
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2 \
            and type(value[0]) is int and type(value[1]) is int \
                and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        count = self.__size
        pos = self.__position
        if count > 0:
            for i in range(pos[1]):
                print()
            for i in range(count):
                for i in range(pos[0]):
                    print(" ", end="")
                for i in range(count):
                    print("#", end="")
                print()
        else:
            print()
