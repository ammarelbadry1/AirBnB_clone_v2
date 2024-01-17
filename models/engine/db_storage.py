#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiates model for database storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ['HBNB_MYSQL_USER'],
            os.environ['HBNB_MYSQL_PWD'],
            os.environ['HBNB_MYSQL_HOST'],
            os.environ['HBNB_MYSQL_DB']), pool_pre_ping=True, echo=False)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
        if os.environ['HBNB_ENV'] == 'test':
            metadata = MetaData(bind=self.__engine)
            metadata.drop_all()

    def all(self, cls=None):
        """query on the current database session and return a dictionary"""
        from models import storage
        dic = {}
        if cls is None:
            result = self.__session.query(
                State, User, City, Amenity, Place, Review).all()
            for r in result:
                dic[f"{r.__class__.__name__}.{r.id}"] = r
            return (dic)
        else:
            if (isinstance(cls, str)):
                result = self.__session.query(eval(cls)).all()
            else:
                result = self.__session.query(cls).all()

            for r in result:
                dic[f"{r.__class__.__name__}.{r.id}"] = r
            return (dic)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
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
        Base.metadata.create_all(self.__engine)
