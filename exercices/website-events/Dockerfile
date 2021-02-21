FROM python:3.7

RUN mkdir -p /srv/app

WORKDIR /srv/app
ADD files /srv/app/files
ADD website_events /srv/app/website_events
ADD requirements.txt /srv/app/
RUN pip install -r requirements.txt

CMD ["faust", "-A", "website_events", "worker", "-l", "info"]