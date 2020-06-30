
from flask import jsonify

from models.user import User

from helpers.serializers import json_serializer


def get():
    users = User.objects.all()
    # convert to python dictionary
    json_user_list = json_serializer(users)

    return jsonify(json_user_list)
