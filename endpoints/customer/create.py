from flask import jsonify, request
from models.customer import Customer

def post():
    data = request.get_json()
    if data:
        new_customer = {
            'name': data['name'],
            'phone_number': data['phone']
        }
    try:
        new_customer = Customer(**new_customer).save()
    except Exception as e:
        return jsonify({'error_msg':str(e)}), 405
    return jsonify({'result': new_customer}), 201
