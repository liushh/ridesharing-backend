from sqlalchemy import Column, Integer, String
from models.base import Base


class Space(Base):
    __tablename__ = 'space'

    id = Column(Integer(), primary_key=True)
    office_id = Column(String(60), nullable=False)
    basic_units = Column(String(), index=True, nullable=False)
    owner_name = Column(String(60), nullable=True)
    owner_id = Column(String(60), index=True, nullable=True)
    team = Column(String(60), index=True, nullable=True)
    space_type = Column(String(60), index=True, nullable=True)
