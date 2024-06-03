from sqlalchemy import Column, Float, Integer, String

from db import Base


class User(Base):
    __tablename__ = "users"

    __table_args__ = {
        "keep_existing": True,
        # "extend_existing": True
    }
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
