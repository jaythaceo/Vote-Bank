#!/usr/bin/env python

import requests
#import facebook # pip install facebook-sdk
import json

access_token = ''

base_url = 'https://graph.facebook.com/me'

# A helper function to pretty-print Python objects as JSON
def pp(o):
    print json.dumps(o, indent=1)

# Create a connection to the graph

#g = facebook.GraphAPI(access_token)

# Execute a few sample queries

# Get 10 likes for 10 friends
fields = 'id,name,friends.limit(100).fields(likes.limit(100))'

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
pp(content)
