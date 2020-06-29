from flask import jsonify, request
from models.user import User
from helpers.serializers import json_serializer

def get(userId):
    user = None
    try:
        user = User.objects.get(id=userId)
        user = json_serializer(user)
        return jsonify({"User": user}), 200
    except:
        if len(userId) != 24:
           return jsonify("Invalid Id specified"), 400
        elif user == None:
           return jsonify("User not found"), 404
