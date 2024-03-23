#!/usr/bin/python3

import MySQLdb
import sys

def states_list(username, password, state_name):
    db = MySQLdb.connect(
        username=username,
        passwd=password,
        port=3306,
        database=database
    )

    cur = db.cursor()
    sql_query = """SELECT cities.id, cities.name, states.name
                       FROM cities
                       INNER JOIN states ON cities.state_id = states.id
                       ORDER BY cities.id ASC"""
    cur.execute(sql_query)
 