#!/usr/bin/env python

import requests
import facebook
import json

access_token = 'CAACEdEose0cBALZCz9lH9XqceleRDRO3KXzvCh0H8Pnoyc62upJXVZB8yoLYU426ku31UhDb3BanC7ha77iALZCKqNdoW8IokzztkuBRBGJ63CGh0yfQwXfftygZBpeRoIcnofoer5oXNpzsP37uAZAWIFETzN8ZChi8kPAsu3nnkfq0NW4BujqZBaVGoJ9ziyjD8aFRZCbhlQZDZD'

base_url = 'https://graph.facebook.com/me'

g = facebook(access_token)

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
pp(g.get_connections('me', 'friends'))
