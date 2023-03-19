#!/usr/bin/python3
# Defines a State model.
# Inherits from SQLAlchemy Base and links to the MySQL table states.

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
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

class State(Base):
    """Represents a state for a MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
