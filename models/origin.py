from models.location import Location
from models.base import Base


class Origin(Location, Base):
    __tablename__ = 'origin'
