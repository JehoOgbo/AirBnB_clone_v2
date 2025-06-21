#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import Relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        """ Defines the attributes of an amenity """
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
                "Place",
                secondary=association_table,
                back_populates="amenities")
else:
    class Amenity(BaseModel):
        """ Defines the attributes of an amenity """
        name = ""
