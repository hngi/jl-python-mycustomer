from datetime import datetime
from flask import jsonify, request
from models.user import User
from flask_mongoengine import mongoengine


def update(userId):
    try:
        if len(userId) != 24:
            return jsonify("Invalid ID supplied"), 400
        data = request.get_json(cache=False)
        value = {
            "phone_number": data["amount"],
            "first_name": data["description"],
            "last_name": data["interest"],
            "email": data["total_amount"],
            "password": data["transaction_role"],
            "updated_at": datetime.utcnow()
        }
        if User.objects(id=userId).update_one(**value) == 0:
            return jsonify("User not found"), 404
        return jsonify("Successful operation"), 200
    except KeyError as q:
        return jsonify("Missing required field: "+str(q)[1:-1]), 403
    except mongoengine.errors.ValidationError as e:
        return jsonify("Validation exception"), 405
