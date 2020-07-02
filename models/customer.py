import datetime
from config import db
from mongoengine import signals
from models import user_store,store

class Customer(db.Document):
    """
    A class used to represent the customer model
    ...

    Attributes
    ----------
    store_ref_id: reference
        store reference ID
    name : str
        the name of the customer
    phone_number: str
        the phone number of the customer
    created_at: datetime str
        time when customer is created
    updated_at: datetime str
        time when customer is modified

    Methods
    -------
    pre_save(cls, sender, customer, *kw)
        handles time attribute(updated_at) ONLY when customer detail is modified
    """

    # store_ref_id = db.ReferenceField(store.Store, dbref=True, required=True)
    name = db.StringField(required=True)
    phone_number = db.StringField(required=True, unique=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)


    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.datetime.utcnow()

    def __str__(self):
        return "<Customer: {}; {} at {}>".format(self.name, self.store_ref_id, self.created_at)


signals.pre_save.connect(Customer.pre_save, sender=Customer)
