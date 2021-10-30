FROM python:3.7-alpine
MAINTAINER mansy

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev \
    && apk --no-cache add librdkafka librdkafka-dev




RUN python -m pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install --no-cache-dir confluent-kafka
RUN pip install mysqlclient

RUN apk del build-deps

RUN mkdir /task
WORKDIR /task
COPY ./task /task

RUN adduser -D user
USER user