#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    HBNB_TYPE_STORAGE = os.getenv('db')

    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade=('all, delete-orphan'))
    else:
        name = ""

    if HBNB_TYPE_STORAGE != 'db':
        @property
        def cities(self):
            """
            method returns the list of City instances with state_id
            equals to the current State.id.
            """
            from models import storage
            city_dict = storage.all('City')
            cityList = []
            for value in city_dict.values():
                if self.id == value['state_id']:
                    cityList.append(value)
            return cityList
