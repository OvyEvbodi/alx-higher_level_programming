#!/usr/bin/python3

"""This module lists the first state from the database ``hbtn_0e_6_usa``
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_state():
    """Lists the first state in the ``hbtn_0e_6_usa`` database"""
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

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")


if __name__ == '__main__':
    list_state()
