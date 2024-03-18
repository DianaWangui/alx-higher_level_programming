#!/usr/bin/python3

"""Script that lists all states from the database."""

import MySQLdb
import sys


def list_states(username, password, database):
    """Establish a connection to the databse server."""
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database,
        port=3306
        )

    #Creating a cursor in order to give the connection a good use
    cursor = db.cursor()

    #executing the cursor in order to sort all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    #printing th states
    for state in states:
        print(state)

    #closing the db and cursor
    cursor.close()
    db.close()
