#!/usr/bin/python3
"""Python file similar to model_state.py named
model_city.py that contains the class definition of a City."""

import sys
from model_state import Base, State
from model_city import City
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
    for inst in session.query(State.name, City.id, City.name).filter(
        City.state_id == State.id
    ):
        print("{}: ({}) {}".format(inst[0], inst[1], inst[2]))
