#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class DBStorage():
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiates model for database storage"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
            pool_pre_ping=True, echo=False)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

        if HBNB_MYSQL_DB == 'test':
            metadata = MetaData(bind=self.__engine)
            metadata.drop_all()

    def all(self, cls=None):
        """query on the current database session and return a dictionary"""
        newdict = {}
        if cls:
            output = self.__session.query(cls).all()
            for obj in output:
                newdict[f'{obj.__class__.__name__}.{obj.id}'] = obj
        else:
            for classname in classes:
                output = self.__session.query(classname).all()
                for obj in output:
                    newdict[f'{obj.__class__.__name__}.{obj.id}'] = obj
        return newdict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """method create all tables in the database"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
