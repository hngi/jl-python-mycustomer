from flask import jsonify
from mongoengine import NotUniqueError
from models.customer import Customer


def post(body):
    try:
        body['phone_number'] = body.pop('phone')
        new_customer = Customer(**body).save()
    except NotUniqueError:
        return jsonify({'status': 'failure', 'message': 'Phone number already registered'}), 403
    except KeyError:
        return jsonify({'status': 'failure', 'message': 'Phone number not supplied'}), 405
    except Exception as e:
        return jsonify({'status': 'failure', 'message': 'Something went wrong while adding customer'}), 500
    return jsonify({'result': new_customer}), 201
