import datetime
from config import db
from models import transaction
from flask_mongoengine import signals


class DebtReminder:
    ts_ref_id = db.ReferenceField(transaction.Transaction, dbref=True, required=True)
    message = db.StringField(required=True)
    status = db.StringField(required=True)
    expected_pay_date = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)


    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.updated_at = datetime.datetime.utcnow()

    def __str__(self):
        return "<Debt Reminder: {}; {} at {}>".format(self.ts_ref_id, self.message, self.expected_pay_date)


signals.pre_save.connect(DebtReminder.pre_save, sender=DebtReminder)
