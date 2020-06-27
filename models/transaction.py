import datetime
from config import db

class Transaction(db.Document):
    """
    A class used to represent the transaction model
    ...

    Attributes
    ----------
    date : str
        a datetime string for the time of transaction
    _from : str
        the name of the person/businees/store who initiated the transaction
    _to : str
        the name of the person/business/store recieving the payment
    description: str
        the description of the transaction
    payment_method : str
        the method of payment e.g cash, card (default Cash)
    isCleared: str
        boolean for whether the transaction was successful or not (default False)
 
    """

    date = db.DateTimeField(default=datetime.datetime.utcnow)
    _from = db.StringField(required=True)
    _to = db.StringField(required=True)
    description = db.StringField(required=True)
    payment_method = db.StringField(default="Cash")
    isCleared = db.Boolean(default=False)

    def __str__(self):
        return "<Transaction: {} to {}\n{}>".format(self._from, self._to, self.isCleared)
