#!usr/bin/python3

"""This module returns True if the object is
exactly an instance of the specified class.
It contains 1 function ``is_same_class``
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly
    an instance of the specified class

    Args:
        obj: the object whose type is to be checked
        a_class: the class to check the object type against

    Returns:
        True if obj is an instance of a_class,
        otherwise, False
    """
    return type(obj) is a_class
