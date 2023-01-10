#!/usr/bin/python3

"""This module writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: the object
        filename: the file to be written to

    Returns: None
    """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
