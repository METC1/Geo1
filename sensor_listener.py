#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *
from socket import *
from datetime import datetime
# from models.amenity import Amenity
from models.base_model import BaseModel
from models.sensor_data import Sensor_data
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State
# from models.user import User


s = socket(AF_INET, SOCK_STREAM)
s.bind(('0.0.0.0', 5222))
s.listen()
clientsocket, adress = s.accept()
# sensor_1 = Sensor_data()
while True:
#   clientsocket, adress = s.accept()
    sensor_1 = Sensor_data()
    print ("\n\nclient socket: " + str(clientsocket))
    print ("adress: " + str(adress))
    data = clientsocket.recv(1024)
    print ("data: " + str(data))
    data2 = data.decode().split(",")
    imei = data2[1]
    dattim = data2[5]
    dtyy = "20" + dattim[0:2]
    dtmm = dattim[2:4]
    dtdd = dattim[4:6]
    dtHH = dattim[6:8]
    dtmin = dattim[8:10]
    dtss = dattim[10:12]
    datetimeformatted = datetime(int(dtyy), int(dtmm), int(dtdd), int(dtHH), int(dtmin), int(dtss))
    gpsstatus = data2[6]
    if gpsstatus == "A":
        sensor_status = "valid"
    if gpsstatus == "V":
        sensor_status = "invalid"
    latitude = data2[7]
    longitude = data2[8]
    inputs = data2[18]
    machine_st = "OFF"
    if inputs == "02":
        machine_st = "ON"

    moredata = data2[20]
    moredata = moredata.split("|")
    fuelvolt = int(moredata[2], base=16)
    fuel_level = (fuelvolt/500) * 100
    print ("\nsensor_id: " + imei)
    print ("created_at: " + str(datetimeformatted))
    print ("sensor_status: " + gpsstatus)
    print ("latitude: " + latitude)
    print ("longitude: " + longitude)
    print ("fuel_level: " + str(fuel_level) + "%")
    print ("aux volt input: " + str(inputs))
    print ("Machine status: " + str(machine_st))
    data_dictionary = { 'sensor_id'  : imei, 'created_at' : str(datetimeformatted), 'longitude' : longitude , 'latitude' : latitude, 'sensor_status' : sensor_status , 'machine_status' : machine_st , 'fuel_level' : fuel_level}
    print ("\ndata_dictionary: " + str(data_dictionary))
    
    sensor_1.sensor_name = imei
    sensor_1.sensor_status = gpsstatus
    sensor_1.latitude = latitude
    sensor_1.longitude = longitude
    sensor_1.machine_status = machine_st
    sensor_1.fuel_level = fuel_level
    sensor_1.sensor_time = datetimeformatted
    print("saving..........")
    storage.new(sensor_1)
    storage.save()
    print("OK")

