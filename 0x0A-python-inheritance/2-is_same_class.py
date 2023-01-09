#!usr/bin/python3

"""This module returns True if the object is
exactly an instance of the specified class.
It contains 1 function ``is_same_class``
"""


def is_same_class(obj, a_class):
    return type(obj) == a_class
