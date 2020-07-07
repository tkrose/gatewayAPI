#accept post
@app.route('/baremetal', methods=["GET","POST"])
def send_one(container):
    if request.method == "POST":
        reqObj = json.loads(reqList.text)