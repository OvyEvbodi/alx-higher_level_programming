#!/usr/bin/python3

"""Defines the ``City`` class"""

from sqlalchemy import Column, Integer, String, Sequence, Foreign_key
from model_state import Base


class City(Base):
    """Defines a ``City``

    Attributes:
        id(int): the unique id of a city instance
        name(str): the name of a city instance
    """

    __table__ = 'cities'
    id = Column(Integer, Sequence('user_id_seq'),
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreign_key('states.id'), nullable=False)

    def __repr__(self):
        """Returns a string representation of the ``City`` class"""

        return f"<City(name='{self.name}'>"
