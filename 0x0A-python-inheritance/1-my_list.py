#!/usr/bin/python3

"""This module defines a class ``MyList``
that inherits from the class ``list``
"""


class MyList(list):
    """Defines a class ``MyList`` that inherits from ``list``"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
