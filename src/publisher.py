from kafka import KafkaProducer

from config import CONFIG
from event import RadonMeasurementEvent


class _Publisher:
    def publish(self, event: RadonMeasurementEvent):
        raise NotImplementedError()


class _PrinterPublisher(_Publisher):
    def publish(self, event: RadonMeasurementEvent):
        print(f"Key: {event.key()}, event: {event.serialize()}")


class _KafkaPublisher(_Publisher):
    kafka_producer = KafkaProducer(
        bootstrap_servers=CONFIG.kafka_server,
        value_serializer=str.encode,
        key_serializer=str.encode
    )

    def publish(self, event: RadonMeasurementEvent):
        _KafkaPublisher.kafka_producer.send(CONFIG.topic, key=event.key(), value=event.serialize())


_publishers = [_PrinterPublisher(), _KafkaPublisher()]


def publish(event: RadonMeasurementEvent):
    [publisher.publish(event) for publisher in _publishers]
