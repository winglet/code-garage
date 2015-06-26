#!/usr/bin/python
#example usage: ./closePorts.py 445 8856 80 --allowed_ips 192.168.0.0/24 10.20.30.40
import argparse
from subprocess import call

def closePort(port):
    print 'closing port: ' + port
    call(["iptables -A INPUT -p tcp --dport " + port + " -j DROP" ], shell=True)
    return

def openPort(port, IP):
    call(["iptables -A INPUT -p tcp --dport " +  port + " -s " + IP + " -j ACCEPT"], shell=True)
    return



parser = argparse.ArgumentParser(description='Set up IPTables rules to block certain ports for all but certain IPs')
parser.add_argument("ports", help='list of ports', nargs='+')
parser.add_argument("--allowed_ips", help='list of allowed IPs', nargs='*')


args = parser.parse_args()

print args

for port in args.ports:
    closePort(port)
    if args.allowed_ips:
        for ip in args.allowed_ips:
            openPort(port, ip)
