from flask import jsonify
from models.customer import Customer



def call(customerId):
    customer = Customer.objects.get(phone_number=customerId)
    if customer:
        return jsonify(customer), 200

    return jsonify({'message': 'Custer  number not found.'}), 404


