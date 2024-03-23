#!/usr/bin/python3

"""script that lists all State objects from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_class(u_name, p_word, db_name):
    engine = create_engine(f'mysql://{u_name}:{p_word}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Erro")
        sys.exit(1)

    u_name, p_word, db_name = sys.argv[1:]
    list_class(u_name, p_word, db_name)
