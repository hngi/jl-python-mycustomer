from flask import jsonify
from models.transaction import Transaction
from mongoengine.errors import DoesNotExist, ValidationError

def by_id(transactionId):
    try:
        tran_id = Transaction.objects(id=transactionId).get()
    except DoesNotExist:
        return jsonify({"error_msg": "Transaction not found"}), 404
    except ValidationError:
        return jsonify({"error_msg": "Invalid Id supplied"}), 400
    return jsonify({"result": tran_id}), 200

