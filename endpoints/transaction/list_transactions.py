from flask import jsonify
from models.transaction import Transaction


def get():
    json_transaction_list = Transaction.objects.all().to_json()
    return jsonify(json_transaction_list)