import datetime
import jwt
from config import db, bcrypt


class User(db.Document):
    phone_number = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    is_active = db.BooleanField(default=False)
    password = db.StringField(required=True)
    api_token = db.StringField()
    user_role = db.StringField(default="store_admin")
    reg_date = db.DateTimeField(default=datetime.datetime.utcnow)

    #hash password and return
    def hash_password(self):
        self.password = bcrypt.generate_password_hash(self.password).decode('utf-8')
        return self.password


    def __str__(self):
        return "<User: {}>".format(self.first_name)

