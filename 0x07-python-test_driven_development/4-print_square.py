#!/usr/bin/python3

'''This module prints a square with the character #
It contains one function ``print_square``
'''


def print_square(size):
    '''prints a square with the character #
    Args:
        size: the size of the square

    Returns:
        None

    Raises:
        TypeError: if size is an instance of float,
            and is less than 0;
            if size is not an instance of int
        ValueError: if size is less than zero

    Examples:
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####
    '''
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        print("#" * size)
