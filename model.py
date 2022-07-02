from distutils.command import check
import email
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    email = Column(String(255))
    adminoruser = Column(Integer)

# class Student(Base):
#     __tablename__ ="student"
#     name = Column(String(255))
#     number = Column(Integer, primary_key = True)
  