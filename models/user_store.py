from config import db
from models import user, store


class UserStore(db.Document):
    user_ref_id = db.ReferenceField(user.User, required=True)
    store_ref_id = db.ReferenceField(store.Store, required=True)

    def __repr__(self):
        return "<UserStore: {}; {}>".format(self.user_ref_id, self.store_ref_id)