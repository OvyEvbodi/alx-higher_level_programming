#!/usr/bin/python3

"""This module contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Defines a state

    Attributes:
        id(int): the unique id of a state
        name(str): the name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, Sequence('states_id'))
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """Returns a string representation of the ``State`` class"""

        return f"<State(name='{self.name}'"
