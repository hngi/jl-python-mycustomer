from flask import jsonify, request
from models.user import User
from flask_mongoengine import mongoengine


def update(userId):
    if len(userID)!=24:
        return jsonify("Invalid ID given"), 400
    try:
        data = request.get_json()
        value ={
            "user_role" : data["user_role"],
            "email" : data["email"],
            "first_name" : data["first_name"],
            "phone_number" : data["phone_number"],
            "last_name" : data["last_name"],
            "password" : data["password"],
        }
        val = User.objects(id=userId).update(**value)
        return jsonify({"Success":"User updated"}), 200
    except KeyError as q:
        return jsonify({"Error":"User not found"}), 404
    except mongoengine.errors.ValidationError as e:
        return jsonify("Server Error"), 500
