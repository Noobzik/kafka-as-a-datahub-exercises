import asyncio
import os
import ssl
import uuid

import faust

from .models import Metric, Visit
from .source import generate_metric, generate_visit

SSL_CONTEXT = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)

BROKER_HOST = os.environ.get("BROKER_HOST", "localhost")

app = faust.App(
    "website-events",
    broker=f"kafka://{BROKER_HOST}",
    broker_credentials=faust.SASLCredentials(
        username=os.environ["BROKER_USERNAME"],
        password=os.environ["BROKER_PASSWORD"],
        ssl_context=SSL_CONTEXT,
    ),
)

visit_topic = app.topic("visits", key_type=str, value_type=Visit)
metric_topic = app.topic("metrics", key_type=str, value_type=Metric)


@app.timer(interval=0.05)
async def sender(app):
    uuid_str = str(uuid.uuid4())
    visit = Visit.generate(id=uuid_str)
    metric = Metric.generate(id=uuid_str)
    await asyncio.gather(
        *[
            visit_topic.send(key=str(visit._id), value=visit),
            metric_topic.send(key=str(metric._id), value=metric),
        ]
    )
