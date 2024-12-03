# eLabFTW Chemistry plugin

## Description

This image contains two services:

1. Ketcher molecule editor service
2. Fingerprinting service with OpenBabel

## Build

~~~
docker build -t elabftw/chem-plugin .
~~~

## Usage

Deploy it on the same network as eLabFTW and configure eLabFTW to use this service.

### With HTTPS

Use `TLS_KEYFILE` and `TLS_CERTFILE` env vars pointing to the key/cert files.
