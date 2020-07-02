import datetime
from config import db


class Store(db.Document):
    store_name = db.StringField(required=True, unique=True)
    phone_number = db.StringField(required=True)
    tagline = db.StringField(required=True)
    shop_address = db.StringField(required=True)
    email = db.StringField(unique=True)
    created = db.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return "<Store: {}>".format(self.store_name)
