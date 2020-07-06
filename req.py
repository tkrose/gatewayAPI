from datetime import datetime
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Nook": {
        "fname": "Nook",
        "lname": "Tom",
        "timestamp": get_timestamp(),
    },
    "Clark": {
        "fname": "Kent",
        "lname": "Clark",
        "timestamp": get_timestamp(),
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp(),
    },
}


# Responds to a request for /api/peoplevwith the complete lists of people (json string of list of people)
def read_all():
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


# Responds to a request for /api/people/{lname} with one matching person from people
def read_one(lname):

    # Does the person exist in people?
    if lname in PEOPLE:
        person = PEOPLE.get(lname)

    # otherwise, not found
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))
    return person


# Creates a new person in the people structure based on the passed in person data
def create(person):
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response("{lname} successfully created".format(lname=lname), 201)

    # Otherwise, they exist, that's an error
    else:
        abort(406,"Person with last name {lname} already exists".format(lname=lname),)


# Updates an existing person in the people structure
def update(lname, person):

    # Does the person exist in people?
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()

        return PEOPLE[lname]

    # otherwise, nope, that's an error
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))


# Deletes a person from the people structure
def delete(lname):

    # Does the person to delete exist?
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response("{lname} successfully deleted".format(lname=lname), 200)

    # Otherwise, person to delete not found
    else:
        abort(404, "Person with last name {lname} not found".format(lname=lname))