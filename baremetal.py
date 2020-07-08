from flask import Flask, render_template, make_response, abort
import connexion
import requests
import json


def bm_post(bmReq):
    json_object = json.loads(bmReq)
    #print(str(bmReq))
    return "200"
