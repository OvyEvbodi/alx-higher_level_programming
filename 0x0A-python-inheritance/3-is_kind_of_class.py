#!/usr/bin/python3

"""This module returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class, otherwise False.
It contains 1 function ``is_kind_of_class``
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class, otherwise False.

    Args:
        obj: the object whose type is to be checked
        a_class: the class to check the object type against

    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class, otherwise False
    """

    return isinstance(obj, a_class)
