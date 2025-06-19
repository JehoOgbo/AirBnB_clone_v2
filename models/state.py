#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


env = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if env == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        state = relationship("City", backref='State')

        @property
        def cities(self):
            """ returns the list of City instances with
            state_id equals to the current State.id"""
            from models.city import City
            return len(storage.all(City))
    else:
        name = ""
