#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    HBNB_TYPE_STORAGE = os.getenv('db')

    if HBNB_TYPE_STORAGE == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', backref='user',
                              cascade=('all, delete_orphan'))
        reviews = relationship('Review', backref='user',
                               cascade=('all, delete_orphan'))
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
