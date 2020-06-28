from config import db
import datetime


class (db.Document):
	store_id = db.Integer(primary_key=True)
	store_name = db.StringField(required=True)
	ph_no = db.StringField(required=True)
	tagline = db.StringField(required=True)
	shop_addr = db.stringField(required=True)
	email_addr = db.StringField(required=True)
	ts = db.DateTime(nullable=False, default=datetime.utcnow)



    def __repr__(self, store_id, store_name, ts):
        self.store_id = store_id
        self.store_name = store_name
        self.ts = ts
        return "<Store name: {}; ID: {} updated at {}>".format(self.store_name, self.store_id, self.ts)

	
	
	
