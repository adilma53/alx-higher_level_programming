#!/usr/bin/python3
"""Python script that connects to a MySQL database and retrieves a State
object based on a name passed as an argument"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(state[0].id)
    except IndexError:
        print("Not found")
