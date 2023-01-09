#!/usr/bin/python3

"""This module returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class,
otherwise False.
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class,
    otherwise False

    Args:
        obj: the object whose type is to be checked
        a_class: the class to check the object type against

    Returns:
        True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class,
        otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
