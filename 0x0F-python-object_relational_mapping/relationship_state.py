#!/usr/bin/python3
"""
class of state
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymeta = MetaData()
Base = declarative_base(metadata=mymeta)


class State(Base):
    """Represents a state"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
