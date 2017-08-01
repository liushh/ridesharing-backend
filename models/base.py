from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class Base:
    @declared_attr
    def __tablename__(self, cls):
        return cls.__name__.lower()

    created_time = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_time = Column(DateTime(timezone=True),
                          default=datetime.utcnow,
                          onupdate=datetime.utcnow)


Base = declarative_base(cls=Base)
