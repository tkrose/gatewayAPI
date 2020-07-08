from flask import Flask, render_template, make_response, abort
import connexion
import requests


def gw_post(reqList):
    for key in reqList["requirements"]:
        if key == "baremetal":
            #turn it to a string
            reqOne = str(reqList["requirements"][key])
            #post reqObj["requirements"][key] to baremetal
            #requests.post('https://URLforBaremetal/requirements', data=reqOne)
            send_one('https://localhost:8080/api/baremetal', data=reqOne)
        if key == "virtual-machine":
            #turn it to a string
            reqOne = str(reqList["requirements"][key])
            #post reqObj["requirements"][key] to vm
            #requests.post('https://URLforVM/requirements', data=reqOne)
            send_one('https://localhost:8080/api/virtualmachine', data=reqOne)
    return "200"


def gw_get():
    return "hello, world"


def send_one(url, data):
    print(data)
    json_object = json.loads(data)
    #requests.post(url, data)
    