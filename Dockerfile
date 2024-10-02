# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.11-slim AS builder

RUN apt update \
 && apt -y install bash \
 && apt clean


COPY requirements.txt /requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt

COPY s3fileuploader /s3fileuploader
COPY app.py /app.py
USER nobody
ENV PYTHONPATH "/s3fileuploader"
CMD ["python3", "app.py"]

