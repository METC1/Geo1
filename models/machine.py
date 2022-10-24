#!/usr/bin/python
""" holds class machine"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class machine(BaseModel, Base):
    """Representation of machine """
    if models.storage_t == "db":
        __tablename__ = 'machine'
#        sensor_id = Column(String(60), ForeignKey('sensor.id'), nullable=False)
        name = Column(String(128), nullable=False)
        model = Column(String(128), nullable=False)
#        places = relationship("Place",
#                              backref="cities",
#                              cascade="all, delete, delete-orphan")
    else:
#        sensor_id = ""
        name = ""
        model = ""


    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
