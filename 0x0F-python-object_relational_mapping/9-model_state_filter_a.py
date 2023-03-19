#!/usr/bin/python3

"""This module lists all states from the database ``hbtn_0e_6_usa``
that contain the letter a
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_states():
    """Lists all the states in the ``hbtn_0e_6_usa`` database"""
    if len(argv) < 4:
        print(f"Usage: {argv[0]} <username> <password> <database>")
        return
    user = argv[1]
    password = argv[2]
    database = argv[3]
    url = f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    engine = create_engine(url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.match("%a%"))\
            .order_by(State.id).all():
        print(f"{state.id}: {state.name})


if __name__ == '__main__':
    list_states()
