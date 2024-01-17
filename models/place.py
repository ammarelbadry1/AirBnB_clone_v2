#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models import storage

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """
    HBNB_TYPE_STORAGE = os.getenv('db')

    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship('Review', backref='place',
                               cascade=('all, delete_orphan'))
    else:
        city_id = ""
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
            method that returns the list of Review instances with
            place_id equals to the current Place.id.
            """
            newlist = []
            review_dict = storage.all('Review')
            for value in review_dict.values():
                if self.id == value['place_id']:
                    newlist.append(value)
            return newlist

        @property
        def amenities(self):
            """Getter method to retrieve related Amenity instances"""
            newlist = []
            amenity_dict = storage.all('Amenity')
            for value in amenity_dict.values():
                if self.id == value['amenity_ids']:
                    newlist.append(value)
            return newlist

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
