from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr


class Location:

    @declared_attr
    def trip_id(cls):
        return Column(Integer, ForeignKey('trip.id'))

    @declared_attr
    def trip(cls):
        return relationship('Trip')

    id = Column(Integer, primary_key=True)
    street = Column(String, nullable=True)
    street_number = Column(String, nullable=True)
    colony_or_district = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    zipcode = Column(String, nullable=True)
