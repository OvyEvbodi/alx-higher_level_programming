#!/usr/bin/python3

"""This module returns an object (Python data structure)
represented by a JSON string"""

import json


def from_json_string(my_str):
    """Deserialize a string to an object

    Args:
        my_str: the string

    Rzeturns: the deserialized python object
    """

    return json.loads(my_str)
