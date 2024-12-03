#!/usr/bin/env python3
import sys
import json
import base64
from openbabel import pybel

async def app(scope, receive, send):
    assert scope['type'] == 'http'

    body = await read_body(receive)
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        response = {
            'error': 'Invalid JSON'
        }
        await send({
            'type': 'http.response.start',
            'status': 400,
            'headers': [(b'content-type', b'application/json')],
        })
        await send({
            'type': 'http.response.body',
            'body': json.dumps(response).encode('utf-8'),
        })
        return

    fmt = data.get('fmt')
    content = data.get('data')
    mol = pybel.readstring(fmt, content)
    fp = mol.calcfp()
    response_data = json.dumps({"data": list(fp.fp)}).encode('UTF-8')

    response_headers = [
        (b'content-type', b'application/javascript'),
        (b'content-length', str(len(response_data)).encode())
    ]
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': response_headers,
    })
    await send({
        'type': 'http.response.body',
        'body': response_data,
    })

async def read_body(receive):
    """
    Read and return the entire body from an incoming ASGI message.
    """
    body = b''
    more_body = True

    while more_body:
        message = await receive()
        body += message.get('body', b'')
        more_body = message.get('more_body', False)

    return body
