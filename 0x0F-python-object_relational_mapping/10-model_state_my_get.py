#!/usr/bin/python3

"""This module lists all State objects from the database ``hbtn_0e_6_usa``
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_states():
    """Lists all the states in the ``hbtn_0e_6_usa`` database"""
    if len(argv) < 5:
        ('Usage: argv[0] <username> <password> <database>')
    user, password = argv[1], argv[2]
    database, state = argv[3], argv[4]
    url = f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    engine = create_engine(url)

    Base.metadata.create_engine_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_info = session.query(State).filter(State.name == state).first()
    if state_info:
        print(State.id)
    else:
        print("Not found")


if __name__ == '__main__':
    list_states()
