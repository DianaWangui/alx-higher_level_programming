#!/usr/bin/python3

"""script that takes in the name of a state as an argument and lists all cities."""


import MySQLdb
import sys

def states_list(username, password, database, state_name):
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        port=3306,
        database=database
    )

    cur = db.cursor()
    sql_query = """SELECT cities.name
                       FROM cities
                       JOIN states ON cities.state_id = states.id
                       WHERE states.name = %s
                       ORDER BY cities.id ASC"""
                       
    cur.execute(sql_query, (state_name,))

    states = cur.fetchall()

    print(', '.join([state[0] for state in states]))

    
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        print(len(args))
        print(args[4])
        print("error")
        exit(1)
    
    states_list(args[1], args[2], args[3], args[4])