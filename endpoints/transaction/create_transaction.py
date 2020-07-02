from flask import jsonify, request

from models.transaction import Transaction
from models.customer import Customer
from models.store import Store
from models.user import User


def post(body):
    try:
        tmp_store_object = Store.objects.get(store_name=body.pop('store_name'))  # hack, not for production
        body['store_ref_id'] = tmp_store_object.id
        body['customer_ref_id'] = Customer.objects.get(phone_number=body.pop('customer_phone_number')).id
        # body['user_ref_id'] = User.objects.get(email=request.user.email).id  todo: make this work with auth

        # hack, not for production
        body['user_ref_id'] = User.objects.get(email=tmp_store_object.email).id

        new_transaction = Transaction(**body).save()
    except Exception as e:
        return jsonify({'error_msg': str(e)}), 405
    return jsonify({'result': new_transaction}), 201
