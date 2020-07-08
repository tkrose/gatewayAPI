from flask import Flask, render_template, make_response, abort
import connexion
import requests
import json
from constants import headers

# Iterates through the requirements list to split by provider and make individual POST requests
def gw_post(reqList):
    for key in reqList["requirements"]:
        if key == "baremetal":
            # Turn requirements list to a string
            reqOne = reqList["requirements"][key]
            # Post baremetal stanza to baremetal API
            send_one('http://localhost:8080/api/baremetal', data=reqOne)
        if key == "virtual-machine":
            # Turn requirements list to a string
            reqOne = reqList["requirements"][key]
            # Post vm stanza to vm API
            send_one('http://localhost:8080/api/virtualmachine', data=reqOne)
    return "200"


def gw_get():
    return "hello, world"


# Turn data into json string and POST request to the given URL
def send_one(url, data):
    dataString = json.dumps(data)
    requests.post(url, headers=headers, data=dataString)
