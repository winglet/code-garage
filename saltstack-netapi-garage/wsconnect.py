#!/usr/bin/python
import websocket
import requests
import ssl

import sys

token=sys.argv[1];

ws = websocket.WebSocket()
ws = websocket.create_connection("ws://localhost:8001/formatted_events/" + token)
ws.send('websocket client ready')

# Look at https://pypi.python.org/pypi/websocket-client/ for more
# examples.
while True:
    print ws.recv()

ws.close()
