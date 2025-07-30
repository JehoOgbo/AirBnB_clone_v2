#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        """ Defines the attributes of an amenity """
        __tablename__ = "amenities"
        id = BaseModel.id
        created_at = BaseModel.created_at
        updated_at = BaseModel.updated_at
        name = Column(String(128), nullable=False)
else:
    class Amenity(BaseModel):
        """ Defines the attributes of an amenity """
        name = ""
