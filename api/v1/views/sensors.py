#!/usr/bin/python3
""" objects that handle all default RestFul API actions for States """
from models.machine import machine
from models.sensor_data import Sensor_data
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/all_sensors', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_state.yml', methods=['GET'])
def get_states():
    """
    Retrieves the list of all Sensor objects
    """
    print("estoy en all_sensors!!")
    all_sensors = storage.all(Sensor_data).values()
    list_sensors = []
    for sensor in all_sensors:
        list_sensors.append(sensor.to_dict())
    return jsonify(list_sensors)


@app_views.route('/sensor/<sensor_name>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_id_state.yml', methods=['get'])
def get_sensor(sensor_name):
    """ Retrieves a specific Sensor """
    print("Sensor Name -------")
    sensor = storage.get(Sensor_data, sensor_name)
    if not Sensor_data:
        abort(404)

    return jsonify(sensor.to_dict())

