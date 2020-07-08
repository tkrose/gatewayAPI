import json
import requests
from flask import make_response, abort
from constants import headers

# Data to serve with our API
requirements = {
    "baremetal": {
        "name": "baremetal-node",
        "role": "node",
        "provider": {
           "name": "baremetal",
           "credential": "baremetal-creds",
           "image": "rhel-7.5-server-x86_64-released",
           "networks": [
              "{{ network }}"
           ]
        }
     },
    "virtual-machine": {
        "name": "virtual-machine-node",
        "role": "node",
        "provider": {
           "name": "virtual-machine",
           "credential": "virtual-machine-creds",
           "image": "rhel-7.5-server-x86_64-released",
           "networks": [
              "{{ network }}"
           ]
        }
    }
  }

# Read in the json
with open('requirements.json') as f:
   fileData = open('requirements.json', 'rb')
print(type(fileData))

# Post to gateway API
requests.post('http://localhost:8080/api/requirements', headers=headers, data=fileData)