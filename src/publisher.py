from kafka import KafkaProducer

from config import CONFIG
from event import RadonMeasurementEvent


# class _KafkaPublisher:
#     kafka_producer = KafkaProducer(
#         bootstrap_servers=CONFIG.kafka_server,
#         value_serializer=str.encode,
#         key_serializer=str.encode
#     )
#
#     @staticmethod
#     def publish(event: RadonMeasurementEvent):
#         _KafkaPublisher.kafka_producer.send(CONFIG.topic, key=event.key(), value=event.serialize())


def _printer_publisher(event: RadonMeasurementEvent):
    print(f"Key: {event.key()}, event: {event.serialize()}")


# publish = _KafkaPublisher.publish
publish = _printer_publisher
