#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    # name = ""
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    if os.environ['HBNB_ENV'] != 'db':
        @property
        def cities(self):
            from models import storage
            dic = storage.all('City')
            return [].append(v for k, v in dic.items()
                             if self.id == v['state_id'])
