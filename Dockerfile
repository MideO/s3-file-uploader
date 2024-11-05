# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.11-slim AS builder

RUN apt update \
 && apt -y install bash curl\
 && apt clean


COPY requirements.txt /requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt

COPY s3fileuploader/src /s3fileuploader/src
USER nobody

