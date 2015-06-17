#!/usr/bin/python
#example run: ./consumeWSevts.py localhost:8000
import websocket
import requests
import ssl

import sys

import urllib2, urllib
import json

mydata=[('username','saltuser'),('password','saltuser'),('eauth','pam')]   
mydata=urllib.urlencode(mydata)
myjsondata={
'username':'saltuser',
'password':'saltuser',
'eauth':'pam'
}

serverFQDN=sys.argv[1];
loginURL="http://"+serverFQDN + "/login"
print("Logging in: "+ loginURL)


req=urllib2.Request(loginURL, json.dumps(myjsondata))
req.add_header("Content-type", "application/json")
#req=urllib2.Request(loginURL, mydata)
#req.add_header("Content-type", "application/x-www-form-urlencoded")

req.add_header("Accept", "application/json")
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
