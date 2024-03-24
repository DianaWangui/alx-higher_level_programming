#!/usr/bin/python3

""" script that lists all State objects that contain the letter a."""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def find_state(u_name, p_word, db_name, s_name):
    """Found method that prints the State object."""
    s_query = f"mysql://{u_name}:{p_word}@localhost:3306/{db_name}"

    engine = create_engine(s_query, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == s_name).first()

    if not state:
        print('Not found')
    else:
        print(state.id)

    session.close()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Error')
        sys.exit(1)

u_name, p_word, db_name, s_name = sys.argv[1:]
find_state(u_name, p_word, db_name, s_name)
