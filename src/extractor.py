import csv
import datetime
import os
from typing import List, Generator, Callable

from config import CONFIG as CFG
from event import RadonMeasurementEvent, RadonMeasurementPayload

_CSV_LOCATION = CFG.csv_location if os.path.isdir(CFG.csv_location) else os.path.join(os.getcwd(), CFG.csv_location)


def if_not_null(value: str, function: Callable):
    if value == 'null':
        return None
    return function(value)


def _extract_event(row: List[str], station: str) -> RadonMeasurementEvent:
    # 2019-09-07T17:20:00+01:00
    timestamp = if_not_null(row[0], lambda v: int(datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S%z").timestamp()))
    radon = if_not_null(row[1], float)
    pressure = if_not_null(row[2], float)
    payload = RadonMeasurementPayload(station, radon, pressure, timestamp)
    return RadonMeasurementEvent(payload)


def extract_events() -> Generator[RadonMeasurementEvent, None, None]:
    for file in os.listdir(_CSV_LOCATION):
        station = file.replace('.csv', '')
        with open(os.path.join(_CSV_LOCATION, file), 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader)  # skip sep=;
            next(reader)  # skip headers
            for row in reader:
                yield _extract_event(row, station)
