#!/usr/bin/python3

"""This module class Student that defines a student"""


class Student:
    """Defines a Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student instance
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student

        Returns:
            None
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
