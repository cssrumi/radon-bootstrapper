import datetime
import os
import random

from config import CONFIG as CFG
from event import RadonMeasurementPayload, RadonMeasurementEvent

_CSV_LOCATION = CFG.csv_location if os.path.isdir(CFG.csv_location) else os.path.join(os.getcwd(), CFG.csv_location)


def _get_stations():
    for file in os.listdir(_CSV_LOCATION):
        yield file.replace('.csv', '')


_stations = list(_get_stations())


def _timestamp():
    return datetime.datetime.utcnow().timestamp()


def _payload():
    station = random.choice(_stations)
    value = random.uniform(0, 400)
    pressure = random.uniform(99, 102)
    timestamp = _timestamp()
    return RadonMeasurementPayload(station, value, pressure, timestamp)


def generate_event():
    return RadonMeasurementEvent(_payload())
