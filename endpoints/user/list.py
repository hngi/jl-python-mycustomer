from flask import jsonify
from models.user import User


def get():
    # json_user_list = User.objects.all().to_json()
    users = User.objects.all()
    return jsonify(users)
