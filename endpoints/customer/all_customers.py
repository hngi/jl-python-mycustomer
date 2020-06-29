
from flask import jsonify

from models.customer import Customer

from helpers.serializers import json_serializer


def get():
    customers = Customer.objects.all()
    # convert to python dictionary
    customer_list = json_serializer(customers)

    return jsonify(customer_list)
