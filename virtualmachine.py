from flask import Flask, render_template, make_response, abort
import connexion
import requests


def vm_post(vmReq):
    print(vmReq)
    return "200"