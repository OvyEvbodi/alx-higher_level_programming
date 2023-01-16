#!/usr/bin/python3

"""This module defines a square
It inherits from the ``Rectangle`` class in rectangle.py
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """updates the string representation of a square

        Returns:
            the string representation of a square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """returns a dictionary representation of a square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    @property
    def size(self):
        """gets the size attribute of a sqquare"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size attribute of a sqquare"""
        self.validate_attr(value, "width", 1)
        self.width = value
