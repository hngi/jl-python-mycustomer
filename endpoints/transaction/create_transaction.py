from flask import jsonify, request
from models.transaction import Transaction

def post():
    try:
        data = request.get_json()
        new_transaction = Transaction(**data).save()
    except Exception as e:
        return jsonify({'error_msg':str(e)}), 405
    return jsonify({'result': new_transaction}), 201
