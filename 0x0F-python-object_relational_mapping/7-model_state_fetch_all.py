#!/usr/bin/python3

"""This module lists all State objects from the database ``hbtn_0e_6_usa``
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_states():
    """Lists all the states in the ``hbtn_0e_6_usa`` database"""
    if len(argv) < 4:
        ('Usage: argv[0] <username> <password> <database>')
    user = argv[1]
    password = argv[2]
    database = argv[3]
    url = f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    engine = create_engine(url)

    Base.metadata.create_engine_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print(State.id, State.name)


if __name__ == '__main__':
    list_states()
