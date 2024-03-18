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

    #executing the cursor in order to sort all states starting with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cursor.fetchall()

    #printing th states
    for state in states:
        print(state)

    #closing the db and cursor
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)