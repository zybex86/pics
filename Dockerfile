FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers zlib-dev gcc musl-dev
RUN apk add --update --no-cache jpeg-dev python3-dev postgresql-dev
RUN pip install -U pip
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir -p /app
WORKDIR /app
COPY ./app /app/

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
