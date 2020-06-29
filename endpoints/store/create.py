from flask import jsonify, request
from mongoengine import NotUniqueError
from models.store import Store


def post(data):
    if data:
        store = {
            'shop_address': data['address'],
            'store_name': data['name'],
            'tagline': data['tagline'],
            'Phone_number': data['phone'],
            'email': data['email'],     # todo: we might have to take this from the shop-creator's account
        }
        try:
            new_store = Store(**store).save()
        except NotUniqueError:
            return jsonify({'status': 'fail',
                            'message': 'Store already exists', }), 403
        except Exception as e:
            return jsonify({'message': "No valid data"}), 400

        return jsonify({'result': new_store}), 201

    else:
        return jsonify({'message': "No valid data"}), 400

