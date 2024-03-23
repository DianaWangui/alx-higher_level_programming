#!/usr/bin/python3
"""python file that contains the class definition of a State."""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)


Base = declarative_base()


class State(Base):
    """A class to create db object."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
