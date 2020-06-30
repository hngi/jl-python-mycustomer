from flask import jsonify
from flask import request
from models.user import User


def post():
    """
    POST response method for creating user.
    :return: JSON object
    """
    data = request.get_json()
    post_user = User(**data)
    post_user.save()
    output = {'id': str(post_user.id)}
    return jsonify({'result': output})
