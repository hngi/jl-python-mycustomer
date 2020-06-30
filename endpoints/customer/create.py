from flask import jsonify, request
from models.customer import Customer

def post():
    try:
        data = request.get_json()
        new_customer = Customer(**data).save()
    except Exception as e:
        return jsonify({'error_msg':str(e)}), 405
    return jsonify({'result': new_customer}), 201
