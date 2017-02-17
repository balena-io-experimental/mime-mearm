FROM resin/raspberrypi3-python:2.7

ENV INITSYSTEM on

RUN apt-get update && apt-get install -yq --no-install-recommends \
    python-smbus \
    python-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN pip install flask picamera
RUN curl -SLOJ http://4tronix.co.uk/piconzero/piconzero.py

COPY . ./

CMD modprobe i2c-dev && python arm.py
