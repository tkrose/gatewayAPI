from flask import Flask, render_template, make_response, abort
import connexion
import requests
import json

@app.route('/', methods=["GET","POST"])
def send_all(reqList):
    if request.method == "POST":
        reqObj = json.loads(reqList.text) #or should this be dict() since I'm sending strings?
        for key in reqObj["requirements"]:
            if key == "baremetal":
                #turn it to a string
                reqOne = str(reqObj["requirements"][key])
                #post reqObj["requirements"][key] to baremetal
                requests.post('https://URLforBaremetal/requirements', data=reqOne)
            if key == "virtual-machine":
                #turn it to a string
                reqOne = str(reqObj["requirements"][key])
                #post reqObj["requirements"][key] to vm
                requests.post('https://URLforVM/requirements', data=reqOne)
    return render_template('home.html') #WILL THIS BE NEEDED?



# Responds to a request for /api/people/{lname} with one matching person from people
#def read_one(container):

    # Does the person exist in people?
    #if container in requirements:
        #info = requirements.get(container)

    # otherwise, not found
    #else:
        #abort(404, "{container} not found".format(container=container))
    #return info


# Responds to a request for /api/people/{lname} with one matching person from people
#def send_one(container):

    # Does the person exist in people?
    #if container in requirements:
        #info = requirements.get(container)

    # otherwise, not found
    #else:
        #abort(404, "{container} not found".format(container=container))
    #return info