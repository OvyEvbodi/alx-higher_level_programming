#!/usr/bin/python3

"""This module gets the list of available attributes and methods of an object.
It has 1 function ``lookup``.
"""


def lookup(obj):
    """returns the list of available attributes
    and methods of an object

    Args:
        obj: the object

    Returns:
        list object
    """
    return dir(obj)
