from flask import jsonify
from flask import request
from models.customer import Customer


def post():
   # POST to create customer
    # return: JSON object

    data = request.get_json()
    post_customer = Customer(**data)
    post_customer.save()
    output = {'id': str(post_customer.id)}
    return jsonify({'result': output})
