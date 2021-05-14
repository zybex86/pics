FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --update --no-cache zlib-dev jpeg-dev gcc musl-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir -p /app
WORKDIR /app
COPY ./app /app/

RUN adduser -D user
USER user
