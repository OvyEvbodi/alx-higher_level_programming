#!/usr/bin/python3

"""This module defines a base class"""

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
            return "[]"
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

        if list_objs and not all(type(item) == cls for item in list_objs):
            raise TypeError(
                   "list_obj must contain instance(s) of the Base class")
        json_str = cls.to_json_string(
                [item.to_dictionary() for item in list_objs])
        with open(filename, 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with all the attributes already set

            Args:
                dictionary(dict): a dictionary

            Returns:
                an instance
        """

        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
            loads dict representing an
            instance and from that creating instances
        """
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, 'r') as f:
                content = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return instances
