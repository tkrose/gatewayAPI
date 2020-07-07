import json
import requests
from flask import make_response, abort

# Data to serve with our API
requirements= {
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


# Responds to a request for /api/peoplevwith the complete lists of people (json string of list of people)
def send_all():
    #read in the json and turn json into a string
    requirements = str(json.loads("requirements.json"))

    #post to gateway
    return requests.post('https://URLforGW/requirements', data=requirements)