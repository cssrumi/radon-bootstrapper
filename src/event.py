import datetime
import json

import attr


@attr.s(frozen=True, slots=True)
class RadonMeasurementPayload:
    station = attr.ib(type=str)
    value = attr.ib(type=float)
    pressure = attr.ib(type=float)
    timestamp = attr.ib(type=int)

    def as_dict(self) -> dict:
        return attr.asdict(self)


@attr.s(frozen=True, slots=True)
class RadonMeasurementEvent:
    payload = attr.ib(type=RadonMeasurementPayload)
    timestamp = attr.ib(type=int, factory=lambda: int(datetime.datetime.utcnow().timestamp()))

    def as_dict(self) -> dict:
        return {
            'type': self.__class__.__name__,
            'payload': self.payload.as_dict(),
            'timestamp': self.timestamp
        }

    def serialize(self) -> str:
        return json.dumps(self.as_dict())

    def key(self):
        return self.payload.station
