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

    