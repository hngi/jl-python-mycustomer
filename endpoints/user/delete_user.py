from flask import jsonify, request
from models.user import User

def delete(userId):
    user = None
    try:
        user = User.objects.get(id=userId)
        user.delete()
        return jsonify("Successful operation"), 200
    except :
        if len(userId) != 24:
            return jsonify("Invalid input"), 400
        elif user == None:
            return jsonify("User not found"), 404


