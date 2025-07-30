#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


env = getenv("HBNB_TYPE_STORAGE")


if env == "db":
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = "cities"
        id = BaseModel.id
        created_at = BaseModel.created_at
        updated_at = BaseModel.updated_at
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities")
else:
    class City(BaseModel):
        """ The city class, contains state Id and name"""
        name = ""
        state_id = ""
