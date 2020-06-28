from flask import jsonify, request
from models.store import Store

def post():
    try:
        data = request.get_json()
        new_store = Store(**data).save()
    except Exception as e:
        return jsonify({'error_msg':str(e)})
    return jsonify({'result': new_store}), 201
