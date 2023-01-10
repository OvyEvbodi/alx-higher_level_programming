#!/usr/bin/python3

"""This module returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj: the object whose JSON representation is to be returned

        Returns:
        returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
