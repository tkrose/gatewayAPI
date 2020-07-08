import json
import requests
from flask import make_response, abort
from constants import headers

# Read in the json
with open('requirements.json') as f:
   fileData = open('requirements.json', 'rb')
print(type(fileData))

# Post to gateway API
requests.post('http://localhost:8080/api/requirements', headers=headers, data=fileData)