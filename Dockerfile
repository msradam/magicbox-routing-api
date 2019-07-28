FROM ubuntu:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /geo_api 
WORKDIR /geo_api
ADD . /geo_api/
RUN apt-get -y update && apt-get -y install build-essential libxml2-dev zlib1g-dev python3-dev python3-pip pkg-config libffi-dev libcairo-dev libspatialindex-dev
RUN pip3 install -r requirements.txt
