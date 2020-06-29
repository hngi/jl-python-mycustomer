from flask import jsonify
from models.customer import Customer


def get(customerId):

    # get to retrieve customer
    # return: JSON object

    customer = Customer.objects.get(id=customerId)
    if customer:
        return jsonify({"Customer": customer}), 200
    return jsonify({"msg":"Customer not found"}), 404


