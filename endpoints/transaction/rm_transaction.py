from flask import jsonify, request
from models.transaction import Transaction

def rmtran(transactionId):
    transaction = None
    try:
        transaction = Transaction.objects.get(id=transactionId)
        transaction.delete()
        return jsonify("Successful operation"), 200
    except :
        if len(transactionId) != 24:
            return jsonify("Invalid input"), 400
        elif transaction == None:
            return jsonify("Transaction not found"), 404


