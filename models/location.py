from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.base import Base


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer(), primary_key=True)
    street = Column(String, nullable=True)
    streetNumber = Column(String, nullable=True)
    colonyOrDistrict = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    zipcode = Column(String, nullable=True)

    trip_id = Column(Integer, ForeignKey('trip.id'))
    trip = relationship('Trip')
