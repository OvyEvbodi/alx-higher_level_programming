#!/usr/bin/python3

"""This module defins a base class"""

import json
import csv


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

        if not list_dictionaries:
            return []
        if not type(list_dictionaries) == list or not all(
                type(item) == dict for item in list_dictionaries):
            raise TypeError

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs(list): a list of instances who inherits of Base

        Returns:
            None
        """

        filename = cls.__name__ + ".json"
        if not list_objs:
            return []
            if not all(type(item, cls) for item in list_objs):
                raise TypeError(
                       "list_obj must contain instance(s) of the Base class")
            json_str = cls.to_json_string(
                        [item.to_dictionary for item in list_objs])
            with open(filename, 'w') as f:
                json.load(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        pass
