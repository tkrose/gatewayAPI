from flask import Flask, render_template, make_response, abort
import connexion
import requests

# Receives requirements stanza from gateway.py and prints to terminal
def vm_post(vmReq):
    print(vmReq)
    return "200"