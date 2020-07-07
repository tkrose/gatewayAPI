#accept post
from flask import Flask, render_template, make_response, abort
import connexion
import requests
import json


def bm_post(bmReq):
    return reqObj = json.loads(reqList.text)