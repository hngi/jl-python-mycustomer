import datetime
from config import db
from mongoengine import signals
from models import user, user_store, customer, store

class Transaction(db.Document):
    """
    A class used to represent the transaction model
    ...

    Attributes
    ----------
    customer_ref_id : reference
        a reference field to the customer
    amount : float
        the transaction amount
    interest : float
        the interest applied to the amount
    total_amount: float
        the total_amount
    description : str
        the description of the transaction
    transaction_name: str
        the name of transaction
    user_ref_id: reference
        user reference ID
    store_ref_id: reference
        store reference ID

    Methods
    -------
    pre_save(cls, sender, transaction, *kw)
        handles time attribute(updated_at) ONLY when transaction is modified
    """

    customer_ref_id = db.ReferenceField(customer.Customer, required=True, dbref=True)
    amount = db.FloatField(required=True)
    interest = db.FloatField(required=True)
    total_amount = db.FloatField(required=True)
    description = db.StringField(required=True)
    transaction_name= db.StringField(required=True)
    transaction_role = db.StringField(required=True)
    user_ref_id = db.ReferenceField(user.User, dbref=True, required=True)
    #store_ref_id = db.ReferenceField(user_store.Store, dbref=True, required=True)
    store_ref_id = db.ReferenceField(store.Store, dbref=True, required=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)


    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.datetime.utcnow()

    def __str__(self):
        return "<Transaction Details: {}-{} by {} at {}>".format(self.transaction_name, self.transaction_role, self.user_ref_id, self.created_at)


signals.pre_save.connect(Transaction.pre_save, sender=Transaction)
