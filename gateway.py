from flask import Flask, render_template, make_response, abort
import connexion
import requests
import json


def gw_post(reqList):
    reqObj = json.loads(reqList.text) #or should this be dict() since I'm sending strings?
    for key in reqObj["requirements"]:
        if key == "baremetal":
            #turn it to a string
            reqOne = str(reqObj["requirements"][key])
            #post reqObj["requirements"][key] to baremetal
            #requests.post('https://URLforBaremetal/requirements', data=reqOne)
            send_one('https://localhost:8080/baremetal', data=reqOne)
        if key == "virtual-machine":
            #turn it to a string
            reqOne = str(reqObj["requirements"][key])
            #post reqObj["requirements"][key] to vm
            #requests.post('https://URLforVM/requirements', data=reqOne)
            send_one('https://localhost:8080/virtualmachine', data=reqOne)
    return render_template('home.html') #WILL THIS BE NEEDED?


def send_one(url, data):
    requests.post(url, data)
    