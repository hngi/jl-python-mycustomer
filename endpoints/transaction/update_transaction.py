from datetime import datetime
from flask import jsonify, request
from models.transaction import Transaction
from flask_mongoengine import mongoengine


def update(transactionId):
    if len(transactionId) != 24:
        return jsonify("Invalid ID supplied"), 400
    try:
        tran = Transaction.objects.get(id=transactionId)["created_at"]
        data = request.get_json(cache=False)
        value = {
            "amount": data["amount"],
            "description": data["description"],
            "interest": data["interest"],
            "total_amount": data["total_amount"],
            "transaction_name": data["transaction_name"],
            "transaction_role": data["transaction_role"],
            "created_at": tran,
            "updated_at": datetime.utcnow()
        }
        val = Transaction.objects(id=transactionId).update_one(**value)
        return jsonify("Successful operation"), 200
    except KeyError as q:
        return jsonify("Missing required field: "+str(q)[1:-1] ), 403
    except mongoengine.errors.DoesNotExist as e:
        return jsonify("Transaction not found"), 404
    except mongoengine.errors.ValidationError as e:
        print(e)
        return jsonify("Validation exception"), 405
