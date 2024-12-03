# Dockerfile for eLabFTW chemistry tools
# Fingerprinter + indigo ketcher service

# This must match the version used in the app
ARG INDIGO_VERSION=1.25.0
FROM epmlsop/indigo-service:$INDIGO_VERSION
# on top of it, we add openbabel so we can do some fingerprinting
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    openbabel \
    python3-openbabel \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*
RUN pip install openbabel-wheel uvicorn
WORKDIR /app
RUN mkdir fingerprinter
COPY src/main.py fingerprinter/main.py
COPY fingerprinter.auto.conf /etc/supervisor/conf.d/