from flask import jsonify, request
from models.customer import Customer


def getCustomerByID(customerId):
    customer = Customer.objects.get(id=customerId)
    if customer:
        return jsonify({'status': 'True',
                        'message': 'Customer was found',
                        'data': customer}), 200
    return jsonify({'status': 'FAILED',
                    'message':'Customer not found'}), 404