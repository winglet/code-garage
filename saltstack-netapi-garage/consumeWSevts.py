#!/usr/bin/python
#example run: ./consumeWSevts.py localhost:8000 saltuser saltuser
import websocket
import requests
import ssl
import sys
import urllib2, urllib
import json
import argparse

parser = argparse.ArgumentParser(description='Connect to a salt server Websocket endpoint')
parser.add_argument("serverFQDN", help='Server URL e.g. localhost:8000')
parser.add_argument("username",   help='salt user name')
parser.add_argument("userpwd",    help='salt user password')

args = parser.parse_args()


mydata=[('username',args.username),('password',args.userpwd),('eauth','pam')]   
mydata=urllib.urlencode(mydata)
myjsondata={
'username':args.username,
'password':args.userpwd,
'eauth':'pam'
}

loginURL="http://"+args.serverFQDN + "/login"
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

wsuri="ws://"+args.serverFQDN+"/ws/"
ws = websocket.WebSocket()
print("Will try creating connection to: " + wsuri+token);
ws = websocket.create_connection( wsuri + token)
ws.send('websocket client ready')

# Look at https://pypi.python.org/pypi/websocket-client/ for more
# examples.
while True:
    print ws.recv()

ws.close()
