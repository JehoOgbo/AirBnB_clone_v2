#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


env = getenv('HBNB_TYPE_STORAGE')


if env == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state')
else:
    class State(BaseModel):
        """State class """
        name = ""

        @property
        def cities(self):
            """ returns the list of City instances with
            state_id equals to the current State.id"""
            from models.city import City
            from models import storage

            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
