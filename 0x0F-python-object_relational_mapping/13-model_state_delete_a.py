#!/usr/bin/python3

"""This module updates a state in the database ``hbtn_0e_6_usa``
that contain the letter a
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def delete_states():
    """Updates a state in the ``hbtn_0e_6_usa`` database"""
    if len(argv) < 4:
        print(f"Usage: {argv[0]} <username> <password> <database>")
        return
    user = argv[1]
    password = argv[2]
    database = argv[3]
    url = f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.contains('a')).all():
        session.delete(state)
    session.commit()
    session.close()


if __name__ == '__main__':
    delete_states()
