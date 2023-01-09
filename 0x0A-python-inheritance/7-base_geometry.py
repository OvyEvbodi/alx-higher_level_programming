#!/usr/bin/python3

"""This module creates an empty class ``BaseGeometry``"""


class BaseGeometry:
    """Defines an empty BaseGeometry"""
    def area(self):
        """Gets the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates a value

        Args:
            name: the name
            value: the value to validate

        Returns:
            None
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
