from flask import jsonify, request
from models.store import Store

def post():
    data = request.get_json()
    if data:
        new_store = Store(**data).save()
        return jsonify({'result': new_store}), 201
    return jsonify({'error_msg':"No valid data"}), 400