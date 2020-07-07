#accept post
from flask import Flask, render_template, make_response, abort
import connexion
import requests
import json


def vm_post(vmReq):
    return reqObj = json.loads(vmReq.text)