FROM python:3.9
LABEL maintainer="Ricardo Sousa"

ENV PORT=8000
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/system
COPY ./ ./
RUN pip install -r requirements.txt


EXPOSE $PORT