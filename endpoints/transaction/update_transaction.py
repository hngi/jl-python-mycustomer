from datetime import datetime
from flask import jsonify, request
from models.transaction import Transaction
from flask_mongoengine import mongoengine


def update(transactionId):
    try:
        if len(transactionId) != 24 or Transaction.objects.\
                with_id(transactionId) is None:
            return jsonify("Invalid ID supplied"), 400
        data = request.get_json(cache=False)
        value = {
            "amount": data["amount"],
            "description": data["description"],
            "interest": data["interest"],
            "total_amount": data["total_amount"],
            "transaction_name": data["transaction_name"],
            "transaction_role": data["transaction_role"],
            "updated_at": datetime.utcnow()
        }
        if Transaction.objects(id=transactionId).update_one(**value) == 0:
            return jsonify("Transaction not found"), 404
        return jsonify("Successful operation"), 200
    except KeyError as q:
        return jsonify("Missing required field: "+str(q)[1:-1]), 403
    except mongoengine.errors.ValidationError as e:
        return jsonify("Validation exception"), 405
