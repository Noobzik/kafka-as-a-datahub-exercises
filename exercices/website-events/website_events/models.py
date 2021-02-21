from datetime import datetime
from faust import Record
import random
import uuid

_RANDOM_URLS = [
    "/home",
    "/me",
    "/store",
    "/store/books",
    "/store/tech",
    "/store/tech/phones",
    "/store/tech/home-automation",
    "/store/tech/home-automation/heating",
    "/store/tech/home-automation/lamps",
    "/store/tech/home-automation/alarms",
    "/store/tech/home-automation/coffee",
    "/store/tech/home-automation/42",
    "/store/tech/health",
    "/store/tech/computers",
    "/store/tech/tv",
    "/store/photo",
    "/store/photo/reflex",
    "/store/photo/bridge",
    "/store/photo/camera",
    "/store/books",
]


class Visit(Record, coerce=True, serializer="json"):
    _id: str
    timestamp: datetime
    sourceIp: str
    url: str

    @classmethod
    def generate(cls):
        index = random.randint(0, len(_RANDOM_URLS) - 1)
        s_ip = f"{random.randint(0, 224)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        return Visit(
            _id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            sourceIp=s_ip,
            url=_RANDOM_URLS[index],
        )


class Metric(Record, coerce=True, serializer="json"):
    _id: str
    timestamp: datetime
    latency: int

    @classmethod
    def generate(cls):
        return Metric(
            _id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            latency=random.randint(0, 600),
        )