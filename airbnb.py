#!/usr/bin/python3
"""This is a command line clone of the airbnb website"""

import sys

while True:
	try:
		sys.stdout.write("(hbnb) ")
		val = input()
		if val == "exit()":
			break;
	except EOFError:
		print("")
		break
		
	

