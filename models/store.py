from config import db
import datetime


class Store(db.Document):
    store_name = db.StringField(required=True)
    phone_number = db.StringField(required=True)
    tagline = db.StringField(required=True)
    shop_address = db.StringField(required=True)
    email = db.StringField(required=True)
    ts = db.DateTimeField(nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Store name: {}; ID: {} updated at {}>".format(
            self.store_name, self.store_id, self.ts)
