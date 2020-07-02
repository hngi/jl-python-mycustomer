from flask import jsonify
from models.transaction import Transaction


def getTransaction(transactionId):

    try:
        transaction = Transaction.objects.get(id=transactionId)
        if transaction:
            return jsonify({"Success": transaction}), 200

    except:
        
        return jsonify({"Error":"Transaction not found"}), 404


