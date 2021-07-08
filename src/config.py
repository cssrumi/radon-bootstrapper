import os

import attr

_KAFKA_SERVER = 'KAFKA_SERVER'
_TOPIC = 'TOPIC'
_CSV_LOCATION = 'CSV_LOCATION'
_DEFAULTS = {
    _KAFKA_SERVER: 'localhost:9092',
    _TOPIC: 'test.radon.measurements',
    _CSV_LOCATION: '../data'
}


@attr.s(slots=True, frozen=True)
class _Config:
    kafka_server = attr.ib(type=str)
    topic = attr.ib(type=str)
    csv_location = attr.ib(type=str)

    @staticmethod
    def create() -> '_Config':
        kafka_server = _Config._get_value(_KAFKA_SERVER)
        topic = _Config._get_value(_TOPIC)
        csv_location = _Config._get_value(_CSV_LOCATION)

        return _Config(kafka_server, topic, csv_location)

    @staticmethod
    def _get_value(key: str) -> str:
        value = os.getenv(key) if os.getenv(key) else _DEFAULTS.get(key)
        if not value:
            raise ValueError(f"Invalid configuration. Value for key: {key} not found.")
        return value


CONFIG = _Config.create()
