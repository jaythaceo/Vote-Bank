#!/usr/bin/env python

import requests
import facebook
import json

access_token = ''
base_url = 'https://graph.facebook.com/me'

# A helper function to pretty-print Python objects as JSON
def pp(o):
    print json.dumps(o, indent=1)

# Create a connection to the graph
g = facebook.GraphAPI(access_token)

url = '%s?fields=%s&access_token=%s' % \
    (base_url, fields, access_token,)

# This API is HTTP-based and could be requested in the browser,
# with a command line utlity like curl, or using just about
# any programming language by making a request to the URL.
# Click the hyperlink that appears in your notebook output
# when you execute this code cell to see for yourself...
print url

# Interpret the response as JSON and convert back
# to Python data structures
content = requests.get(url).json()

# Pretty-print the JSON and display it
pp(g.get_connections('me', 'friends'))

# Find Pepsi and Coke in search results
pp(g.request('search', {'q' : 'pepsi', 'type' : 'page', 'limit' : 5}))
pp(g.request('search', {'q' : 'coke', 'type' : 'page', 'limit' : 5}))

# Use the ids to query for likes
pepsi_id = '56381779049' # Could also use 'PepsiUS'
coke_id = '40796308305'  # Could also use 'CocaCola'

# A quick way to format integers with commas every 3 digits
def int_format(n): return "{:,}".format(n)

print "Pepsi likes:", int_format(g.get_object(pepsi_id)['likes'])
print "Coke likes:", int_format(g.get_object(coke_id)['likes'])

