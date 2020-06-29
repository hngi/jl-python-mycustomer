from flask import jsonify, request
from models.user import User


def update(userId):

    data = request.get_json()
    user = User.objects.get(id=userId)
    exists = userId in User
    user['id'] = userId
    if exists:
        User[data].update()

    else:
        User[userId] = user
    return jsonify({ "status": "OK" }), 200
