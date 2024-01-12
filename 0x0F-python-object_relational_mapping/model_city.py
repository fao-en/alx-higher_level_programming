#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, text, ForeignKey
from relationship_state import Base
"""
python script that performs creates a States class based off of Base.
"""
Base = declarative_base()


class City(Base):
    """
The "City" class which inherits from "Base" class.
Attributes:
id (str): The city's id.
name (sqlalchemy.Integer): The city's name.
state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
