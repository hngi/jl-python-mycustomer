import datetime
from flask_login import UserMixin
from flask import current_app
from config import db, login_manager

from config import db


class User(db.Document):
    # adding auth username for auth
    username = db.Column(db.String(20), unique=True, nullable=False)
    phone_number = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    is_active = db.BooleanField(default=0)
    password = db.StringField(required=True)
    api_token = db.StringField()
    user_role = db.StringField(default="store_admin")
    reg_date = db.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return "<User: {}>".format(self.first_name)

