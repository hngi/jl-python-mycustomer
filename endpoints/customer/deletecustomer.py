from flask import jsonify
from models.customer import Customer

def delete(customerId):
    if len(customerId) != 24 or Customer.objects.\
            with_id(customerId) is None:
        return jsonify("Invalid ID supplied")
    if  Customer.objects(id=customerId).delete() == 0:
        return jsonify("Customer not found"), 404
    return jsonify("Successful operation"), 200

