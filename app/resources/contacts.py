from flask_restful import Resource, marshal
from app.models import Contact
from app import requests, db
from app.schemas import contact_field

class Contacts(Resource):
    def get(self):
        contacts = Contact.query.all()
        return marshal(contacts,contact_field,"contacts")

    def post(self):
        payload = requests.only(["name", "cellphone"])
        name = payload["name"]
        cellphone = payload["cellphone"]

        contact  =  Contact(name, cellphone)

        db.session.add(contact)
        db.session.commit()

        return marshal(contact,contact_field,"contact")


    def put(self):
        pass

    def delete(self):
        payload  = requests.only(["id"])
        _id = payload["id"]

        contact = Contact.query.get(_id)

        if not contact:
            return { "message": "Contact not found"}

        db.session.delete(contact)
        db.session.commit()

        return marshal(contact, contact_field, "contact")

    