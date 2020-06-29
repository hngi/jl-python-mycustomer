from flask import jsonify
from flask import request
from models.customer import Customer


def post():
   # POST to create customer
    # return: JSON object

    data = request.get_json()
    if data:
      post_customer = Customer(**data)
      post_customer.save()
      output = {'id': str(post_customer.id)}
      return jsonify({'result': output}), 201
    return jsonify({'error_msg':"No valid data"}), 400 
