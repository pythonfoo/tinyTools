#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For Atari-Frosh to Get Whois into Wiki
# make it executable and execute with ip address like '192.168.1.10'

# IMPORTS

import os
import sys
IP = sys.argv[1]

command = 'whois ' + IP

f = os.popen(command)

text = []

text.append("{|")

for line in f:
    if line[:1] == "%":
        newline = "| ||"
        data = line.split()
        data.pop(0)
        for element in data:
            newline += " " + element
        newline += "\n|-"
        text.append(newline)
    
    elif len(line) < 2:
        pass
        
    else:
        newline = "|"
        
        data = line.split()
        if len(data) >0:
            newline += data.pop(0) + "||"
        
        for element in data:
            newline += " " + element
        newline += "\n|-"
        text.append(newline)

text.append("|}")

for line in text:
    print line
