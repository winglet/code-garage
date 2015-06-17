#!/usr/bin/python
#example run: ./consumeWSevts.py localhost:8000
import websocket
import requests
import ssl

import sys

import urllib2, urllib
mydata=[('username','saltuser'),('password','saltuser'),('eauth','pam')]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
serverFQDN=sys.argv[1];
loginURL="http://"+serverFQDN + "/login"
print("Logging in: "+ loginURL)
req=urllib2.Request(loginURL, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
req.add_header("Accept", "application/x-yaml")
page=urllib2.urlopen(req).read()
print page

import yaml
doc = yaml.load(page)

token = doc.get('return')[0].get('token')

wsuri="ws://"+serverFQDN+"/ws/"
ws = websocket.WebSocket()
print("Will try creating connection to: " + wsuri+token);
ws = websocket.create_connection( wsuri + token)
ws.send('websocket client ready')

# Look at https://pypi.python.org/pypi/websocket-client/ for more
# examples.
while True:
    print ws.recv()

ws.close()
