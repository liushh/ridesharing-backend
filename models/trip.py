from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class Trip(Base):
    __tablename__ = 'trip'

    id = Column(Integer, primary_key=True)
    drive_or_ride = Column(String, nullable=False)
    time = Column(DateTime, nullable=False)
    origin = relationship('Location', ForeignKey('location.id'), back_populates='trip')
    destination = relationship('Location', ForeignKey('location.id'), back_populates='trip')

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='trip')
