from .models import Visit, Metric


def generate_visit():
    return Visit.generate()


def generate_metric():
    return Metric.generate()
