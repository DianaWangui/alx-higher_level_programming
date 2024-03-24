#!/usr/bin/python3

""" script that prints the first State object from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

def list_first_state(u_name, p_word, db_name):
    state_query = f"mysql://{u_name}:{p_word}@localhost:3306/{db_name}"
    engine = create_engine(state_query, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if not first_state:
        print('Nothing\n')

    print(f'{first_state.id}: {first_state.name}')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Error')
        sys.exit(1)

    u_name, p_word, db_name = sys.argv[1:]
    list_first_state(u_name, p_word, db_name)
