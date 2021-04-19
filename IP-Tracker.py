#! / usr / bin / python3

import argparse
import requests
import json
import sys

if __name__ == "__main__":

	#Get ip address
	parser = argparse.ArgumentParser ()
	parser.add_argument ("-i", "--ip_address", help = "Location site or ip address requested")
	args = parser.parse_args ()


# If no ip or arguments are given, print a help message and exit
if len (sys.argv) <= 1:
		parser.print_help ()
		sys.exit (0)

#assign the argument to the variable ip and query it from the site with request
# json, xml, csv etc. formats (available from the site)
# change file_type for required format
ip = args.ip_address
file_type="json"
url = "http://ip-api.com/"+file_type+"/"+ip
res = requests.get (url) .content

# Results as json object.
result = json.loads (res)

# print the results to the screen
#print ("results for ip:" , result )
for i, j in enumerate (result):
	print (str (j.upper ()) + ":" + str (result [j]))
