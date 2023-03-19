#!/usr/bin/python3

"""This module updates a state in the database ``hbtn_0e_6_usa``
that contain the letter a
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def list_states():
    """Updates a state in the ``hbtn_0e_6_usa`` database"""
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

    state_obj = session.query(State).filter(id == 2).first()
    state_obj.name = "New Mexico"
    session.commit()


if __name__ == '__main__':
    list_states()
