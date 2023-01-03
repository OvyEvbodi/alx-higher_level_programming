#!/usr/bin/python3
'''This module adds two integers.
It contains 1 function ``add_integer``'''


def add_integer(a, b=98):
    '''
    Adds two integers

    ARGS:
    a - the first number
    b - the second number

    Returns: the result of the addition of a and b

    Try it with 2 integers
    >>> add_integer(2, 5)
    7

    It also works with floating point numbers, but the result is always an integer.
    For example:
    >>> add_integer(7.0, 2.67)
    9

    Raises:
        A TypeError for non int or non float datatypes
    '''
 
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
