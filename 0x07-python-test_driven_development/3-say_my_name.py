#!/usr/bin/python3

'''This module prints "My name is <first name> <last name>"
It contains 1 function ``say_my_name``
'''


def say_my_name(first_name, last_name=""):
    '''prints "My name is <first name> <last name>"
    Args:
        first_name: the first name
        last_name: the last name
    Returns:
        None
    Raises:
        TypeError: When either first_name or last_name is not of type str
    Examples:
        >>>
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name:s} {last_name:s}")
