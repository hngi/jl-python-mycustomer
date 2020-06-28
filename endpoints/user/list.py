from flask import jsonify
from models.user import User


def get():
    json_user_list = User.objects.all().to_json()
    return jsonify(json_user_list)
