#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.sql import select

if __name__ == "__main__":
    db_conf = {
        'host':     'localhost',
        'user':     sys.argv[1],
        'passwd':   sys.argv[2],
        'db':       sys.argv[3],
        'port':     3306
    }
    db = MySQLdb.connect(**db_conf)
    cursor = db.cursor()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
