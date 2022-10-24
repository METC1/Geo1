#!/usr/bin/python3
""" holds class Sensor"""
from datetime import datetime
import models
from models.base_model import BaseModel, Base
# from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Sensor_data(BaseModel, Base):
    """Representation of sensor data """
    if models.storage_t == "db":
        __tablename__ = 'sensors_data'
        sensor_name = Column(String(128), nullable=False)
        sensor_status = Column(String(10), nullable=False)
        latitude = Column(String(20), nullable=False)
        longitude = Column(String(20), nullable=False)
        machine_status = Column(String(3), nullable=False)
        fuel_level = Column(String(10), nullable=False)
        sensor_time = Column(DateTime, nullable=False)
#        machine = relationship("Machine",
#                              backref="Sensor_data",
#                              cascade="all, delete, delete-orphan")
    else:
        sensor_name = ""
        sensor_status = ""
        latitude = ""
        longitude = ""
        machine_status = ""
        fuel_level = ""
        sensor_time = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

#    if models.storage_t != "db":
#        @property
#        def cities(self):
#            """getter for list of city instances related to the state"""
#            city_list = []
#            all_cities = models.storage.all(City)
#            for city in all_cities.values():
#                if city.state_id == self.id:
#                    city_list.append(city)
#            return city_list
