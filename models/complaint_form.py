import datetime
from config import db
from models import user, user_store


class Complaint(db.Document):
    user_ref_id = db.ReferenceField(user.User, required=True)
    message = db.StringField(required=True)
    store_ref_code = db.ReferenceField(user_store.UserStore, required=True)
    status = db.StringField(default="open")
    timestamp = db.DateTimeField(default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Complaint: from: {}; opened: {}>".format(self.store_ref_code, self.timestamp)
