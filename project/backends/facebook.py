#!/usr/bin/env python

import requests
import facebook # pip install facebook-sdk
import json

access_token = ' '

# A helper function to pretty-print Python objects as JSON
def pp(o):
    print json.dumps(o, indent=1)

# Create a connection to the graph

g = facebook.GraphAPI(access_token)

# Execute a few sample queries
