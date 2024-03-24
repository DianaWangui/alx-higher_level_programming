#!/usr/bin/python3

""" script that lists all State objects that contain the letter a."""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def add_state(u_name, p_word, db_name):
    a_query = f"mysql://{u_name}:{p_word}@localhost:3306/{db_name}"

    engine = create_engine(a_query, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)

    session.commit()
    name = 'Louisiana'
    new_state_id = session.query(State).filter(State.name == name).first()

    print(f'{new_state_id.id}')
    session.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Error')
        sys.exit(1)

    u_name, p_word, db_name = sys.argv[1:]
    add_state(u_name, p_word, db_name)
