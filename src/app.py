from time import sleep

from extractor import extract_events
from generate import generate_event
from publisher import publish


def boostrap():
    for event in extract_events():
        publish(event)


def mock_random_events():
    while True:
        event = generate_event()
        publish(event)
        sleep(1)


def main():
    boostrap()
    mock_random_events()


if __name__ == '__main__':
    main()
