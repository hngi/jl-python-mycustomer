from config import db


class Role(db.Document):
    _id = db.StringField(default="store_admin")
    name = db.StringField(required=True)
   
    def __str__(self):
        return "<Role: {} {}>".format(self.name, self._id)