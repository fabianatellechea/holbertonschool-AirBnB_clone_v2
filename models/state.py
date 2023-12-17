#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            """ returns the list of City instances with
            state_id equals to the current State.id """
            from models import storage
            new_list = []

            for key, value in storage._FileStorage__objects.items():
                if value.__class__.__name__ == 'City':
                    if value.state_id == self.id:
                        new_list.append(value)
            return new_list
