#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpd import MPDClient, CommandError
from socket import error as SocketError
from sys import exit

### SETTINGS ###
HOST = 'localhost'
PORT = '6600'
PASSWORD = False

unwantedStrings = ['heino', 'quack']


client = MPDClient()

try:
    client.connect(host=HOST, port=PORT)
except SocketError as ex:
    print ex
    exit(1)

if PASSWORD:
    try:
        client.password(PASSWORD)
    except CommandError as ex:
        print ex
        exit(1)

print client.status()


removeItems = []
for itm in client.playlistinfo():
    foundBad = False
    for unwanted in unwantedStrings:
        for val in itm.itervalues():
            if unwanted in val.lower():
                removeItems.append(itm['id'])
                print unwanted,'=>',val,'IN:', itm
                foundBad = True
                break
                
        if foundBad == True:
            break
            
        #if unwanted in itm['name'].lower() or unwanted in itm['file'].lower() or unwanted in itm['title'].lower():
        #removeItems.append(itm['id'])

for itmId in removeItems:
    client.deleteid(itmId)

if len(removeItems) > 0:
    print '*********************'
    print 'Removed',len(removeItems),'HEINOS'
    print '*********************'
else:
    print 'theres no HEINO'

client.disconnect()

