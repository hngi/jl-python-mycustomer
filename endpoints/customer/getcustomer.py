from flask import jsonify, request
from mongoengine import DoesNotExist
from models.customer import Customer


def getCustomerByID(customerId):
    try:
        customer = Customer.objects.get(id=customerId)
        return jsonify({'status': 'True',
                        'message': 'Customer was found',
                        'data': customer}), 200
    except DoesNotExist as e:
        return jsonify({'status': 'failure',
                        'message': 'Customer not found'}), 404
    except Exception as e:
        return jsonify({'status': 'failure',
                        'message': 'Something went wrong'}), 500

