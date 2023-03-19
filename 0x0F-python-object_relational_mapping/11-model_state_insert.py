#!/usr/bin/python3

"""This module adds a new state to the database ``hbtn_0e_6_usa``
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_states():
    """Lists adds a new state to the ``hbtn_0e_6_usa`` database"""
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

    new_state_obj = State(name="Louisiana")
    session.add(new_state_obj)
    session.commit()
    new_state = session.query(State.id).filter(State.name == "Louisiana")\
        .first()
    print(State.id)


if __name__ == '__main__':
    list_states()
