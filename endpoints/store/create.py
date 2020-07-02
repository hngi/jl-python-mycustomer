from flask import jsonify, request
from mongoengine import NotUniqueError
from models.store import Store


def post(data):
    store = {
        'shop_address': data['address'],
        'store_name': data['name'],
        'tagline': data['tagline'],
        'phone_number': data['phone'],
        'email': data['email'],  # the user object may not need an email
    }
    try:
        new_store = Store(**store).save()
    except NotUniqueError as e:
        return jsonify({'status': 'fail',
                        'message': 'Store already exists', }), 403
    except Exception as e:
        return jsonify({'message': str(e)}), 400

    return jsonify({'result': new_store}), 201


