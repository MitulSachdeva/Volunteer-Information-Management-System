from sqlalchemy import Column, Integer, String
from .database import Base

class Volunteer(Base):
    __tablename__ = "volunteers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    age = Column(Integer)
    skills = Column(String)
    availability = Column(String)
    address = Column(String)
    status = Column(String, default="Active")