import requests # pip install requests
import json
access_token = 'CAACEdEose0cBAPIvgMxIehEANDJsrnYtHyJmw12OnllbahS44ZAS9VHIRTMsNk5mYnRh0LKZBB7OG6N88YyDO4TMXgaJSTn9NR8fMkJTbH5CRXxLtvtImEHKKNbE3xem9WTbfheLz5eWW7go4YAqkoSgltsAU9jnisbgtFO63dE08pvcconiDmGFU7MUIZD'
base_url = 'https://graph.facebook.com/me'

# Get 10 likes for 10 friends
fields = 'id,name,me.limit(100).fields(likes.limit(100))'

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
print json.dumps(content, indent=1)