from flask import Flask, render_template, make_response, abort
import connexion
import requests

# Receives requirements stanza from gateway.py and prints to terminal
def bm_post(bmReq):
    print(str(bmReq))
    return "200"
