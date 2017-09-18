from sqlalchemy import Column, Integer, String
from models.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    username = Column(String(60), nullable=False)
    email = Column(String, index=True, nullable=False)
    auth0_id = Column(String, index=True, unique=True)
