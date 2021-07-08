import datetime
import random

from event import RadonMeasurementPayload, RadonMeasurementEvent
from extractor import extract_stations

_stations = list(extract_stations())


def _payload():
    station = random.choice(_stations)
    value = random.uniform(0, 400)
    pressure = random.uniform(99, 102)
    timestamp = datetime.datetime.utcnow().timestamp()
    return RadonMeasurementPayload(station, value, pressure, timestamp)


def generate_event():
    return RadonMeasurementEvent(_payload())
