#!/usr/bin/python
# Tool to change the Hostname in Ubuntu 11.10

import sys
import socket
import os

#print sys.argv[1]
newhostname = sys.argv[1]

hostname = socket.gethostname()

def replaceText(filename, text, newtext):
    inputFile = open(filename, 'r')     #Open file in read mode
    hostsfiledata = inputFile.read()
    inputFile.close()

    hostsfiledata = hostsfiledata.replace(text, newtext)

    outputFile = open(filename, 'w')
    outputFile.write(hostsfiledata)
    outputFile.close()
    
replaceText('/etc/hosts',  hostname,  newhostname)
replaceText('/etc/hostname', hostname, newhostname)
os.system('hostname -F /etc/hostname')

# voller Hostname mit nachfolgendem code
#host2 = socket.gethostbyaddr(socket.gethostname()) 
#print str(host2) + " :Hostname by gethostbyaddr"



