#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity


env = getenv('HBNB_TYPE_STORAGE')


if env == 'db':
    place_amenity = Table(
            "place_amenity", Base.metadata,
            Column('place_id', String(60), ForeignKey("places.id")),
            Column('amenity_id', String(60), ForeignKey("amenities.id"))
            )

    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship(
                "Amenity",
                secondary=place_amenity,
                backref="place",
                viewonly=False
                )
else:
    class Place(BaseModel):
        """ A place to stay """
        city_id = ''
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            returns the list of Review instances with
            place_id equals to the current Place.id
            """
            from models import storage
            from models.review import Review
            review_list = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """
            returns a list of Amenity instances that contains
            all Amenity.id linked to the Place
            """
            return amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """
            add an amenity.id to the attribute amenity_ids
            """
            if obj.to_dict()['__class__'] != "Amenity":
                return
            self.amenity_ids.append(obj.id)
