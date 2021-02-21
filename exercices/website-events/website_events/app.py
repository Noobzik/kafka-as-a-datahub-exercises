import os

import faust

from .models import Visit, Metric
from .source import generate_metric, generate_visit

BROKER_HOST = os.environ.get("BROKER_HOST", "localhost")

app = faust.App("website-events", broker=f"kafka://{BROKER_HOST}")

visit_topic = app.topic("visits", key_type=str, value_type=Visit)
metric_topic = app.topic("metrics", key_type=str, value_type=Metric)


@app.timer(interval=0.05)
async def visit_sender(app):
    visit = generate_visit()
    await visit_topic.send(key=str(visit._id), value=visit)


@app.timer(interval=0.05)
async def metric_sender(app):
    metric = generate_metric()
    await metric_topic.send(key=str(metric._id), value=metric)
