# app/models.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BadgeCounter(Base):
    __tablename__ = "badge_counter"
    id = Column(String, primary_key=True, index=True)
    counter = Column(Integer, default=0)
