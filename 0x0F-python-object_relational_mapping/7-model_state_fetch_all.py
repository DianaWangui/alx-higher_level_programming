#!/usr/bin/python3

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def list_class(u_name, p_word, db_name):
    engine = create_engine(f'mysql://{u_name}\
    :{p_word} @localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Erro")
        exit(1)

    username, password, db_name = sys.argv[1:]
    list_class(u_name, p_ward, db_name)
