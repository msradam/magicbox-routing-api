FROM ubuntu:latest
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apt-get -y update && apt-get -y install build-essential libxml2-dev zlib1g-dev python3-dev python3-pip pkg-config libffi-dev libcairo-dev libspatialindex-dev

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . . 

CMD gunicorn geo_routing.wsgi:application --bind 0.0.0.0:$PORT
