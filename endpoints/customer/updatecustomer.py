# Seems this is better 😏
from flask import request, jsonify
from datetime import datetime as dt
from models.customer import Customer
from flask_mongoengine import mongoengine as me
def update(customerId):

    if len(customerId) != 24:
        return jsonify("Invalid ID supplied"), 400
    data = request.get_json()
    value = {
        "name": data["name"],
        "phone_number": data["phone"],
        "updated_at": dt.utcnow()
    }
    try:
        if Customer.objects(id=customerId).update_one(**value) == 0:
            return jsonify("Customer not found"), 404
    except (me.errors.ValidationError, me.errors.NotUniqueError):
        return jsonify("Validation exception"), 405
    return jsonify("Successful operation"), 200

