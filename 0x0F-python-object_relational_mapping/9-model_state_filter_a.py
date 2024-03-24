#!/usr/bin/python3

""" script that lists all State objects that contain the letter a."""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_of_a(u_name, p_word, db_name):
    a_query = f"mysql://{u_name}:{p_word}@localhost:3306/{db_name}"

    engine = create_engine(a_query, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    if not states:
        print('Nothing')
    else:
        for state in states:
            print(f'{state.id}: {state.name}')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Error')
        sys.exit(1)

    u_name, p_word, db_name = sys.argv[1:]
    list_of_a(u_name, p_word, db_name)
