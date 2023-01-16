#!/usr/bin/python3

"""This module defins a base class"""


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
