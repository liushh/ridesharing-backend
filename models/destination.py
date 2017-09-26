from models.location import Location
from models.base import Base


class Destination(Location, Base):
    __tablename__ = 'destination'
