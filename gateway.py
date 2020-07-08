from flask import Flask, render_template, make_response, abort
import connexion
import requests


# Iterates through the requirements list to split by provider and make individual POST requests
def gw_post(reqList):
    for key in reqList["requirements"]:
        if key == "baremetal":
            # Turn requirements list to a string
            reqOne = str(reqList["requirements"][key])
            # Post baremetal stanza to baremetal API
            #requests.post('https://URLforBaremetal/requirements', data=reqOne)
            send_one('https://localhost:8080/api/baremetal', data=reqOne)
        if key == "virtual-machine":
            # Turn requirements list to a string
            reqOne = str(reqList["requirements"][key])
            # Post vm stanza to vm API
            #requests.post('https://URLforVM/requirements', data=reqOne)
            send_one('https://localhost:8080/api/virtualmachine', data=reqOne)
    return "200"


def gw_get():
    return "hello, world"


# Makes POST request to the given URL
def send_one(url, data):
    print(data)
    json_object = json.loads(data)
    #requests.post(url, data)
    