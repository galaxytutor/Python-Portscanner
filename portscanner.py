#!/bin/python3

import sys
import socket
from datetime import datetime

#define the target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 portscanner.py <ip>")

#add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("This scanner is garbo btw")
print("Coded by L1GHTNER in Python")
print("Version 1.0 PORTSCANNER")
print("-" * 50)

try: 
	for port in range(1,150):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(.001)
		result = s.connect_ex((target,port)) #returns an error indicator
		#print("Checking port {}".format(port)) #commented out for a clean interface
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
