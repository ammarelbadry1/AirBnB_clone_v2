#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', back_populates='cities')

# Creating the database engine
engine = create_engine('sqlite:///:memory:')

# Creating tables
Base.metadata.create_all(engine)

# Creating a session
session = Session(engine)

# Creating a state and associated cities
california = State(name='California', cities=[City(name='Los Angeles'), City(name='San Francisco')])
session.add(california)
session.commit()

# Querying data
california = session.query(State).filter_by(name='California').first()
print(california.name, [city.name for city in california.cities])

# Deleting the state (and associated cities due to cascade)
session.delete(california)
session.commit()

# Verifying that the state and cities are deleted
california = session.query(State).filter_by(name='California').first()
print(california)  # Should be None

