from flask import make_response, abort

# Data to serve with our API
PEOPLE = {
    "Nook": {
        "fname": "Nook",
        "lname": "Tom",
    },
    "Clark": {
        "fname": "Kent",
        "lname": "Clark",
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
    },
}