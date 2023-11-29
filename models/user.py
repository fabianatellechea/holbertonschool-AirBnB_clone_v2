#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(string(123), nullable=False)
    password = Column(string(123), nullable=False)
    first_name = Column(string(123), nullable=False)
    last_name = Column(string(123), nullable=False)
