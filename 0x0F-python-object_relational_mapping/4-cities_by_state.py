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
        port=3306,
    )

    cur = db.cursor()
    sql_query = """SELECT cities.id, cities.name, states.name
                       FROM cities
                       INNER JOIN states ON cities.state_id = states.id
                       ORDER BY cities.id ASC"""
    cur.execute(sql_query)

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> \
        <password> <database> <argument1>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
