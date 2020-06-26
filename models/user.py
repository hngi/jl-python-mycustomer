import datetime

import mongoengine as db


class User(db.DynamicDocument):
    phone_number = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    is_active = db.Boolean(default=0)
    password = db.StringField(required=True)
    api_token = db.StringField()
    user_role = db.StringField(default="store_admin")
    reg_date = db.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return "<User: {}>".format(self.first_name)

