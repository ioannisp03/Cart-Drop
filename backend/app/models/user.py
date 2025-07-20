from .product import Product
from sqlalchemy import Column, Integer, String, Datetime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True)
