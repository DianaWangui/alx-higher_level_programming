#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City


def list_cities(u_name, p_word, db_name):
    c_query = f"mysql://{u_name}:{p_word}@localhost:3306/{db_name}"

    engine = create_engine(c_query, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).\
        join(State, State.id == City.state_id).all()

    if cities:
        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")
    session.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Error')
        sys.exit(1)

    u_name, p_word, db_name = sys.argv[1:]
    list_cities(u_name, p_word, db_name)
