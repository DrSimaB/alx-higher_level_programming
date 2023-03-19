#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.sql import select

if __name__ == "__main__":

    dialect = "mysql"
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"
    port = 3306
if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
     
                          .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
