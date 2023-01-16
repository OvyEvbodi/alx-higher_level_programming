#!/usr/bin/python3

"""This module defins a base class"""

import json


class Base:
    """Defines a base object"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a base object

        Attribute:
            id(int): the id of the object 
        """

        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries(dict): is a list of dictionaries

        Returns:
            the JSON string representation of list_dictionaries,
            otherwise, ``[]`` if the list is None or empty
        """

        json_list = []
        if not list_dictionaries:
            return []
        for dict_item in list_dictionaries:
            json_list.append(dict_item)
        return json.dumps(json_list)
