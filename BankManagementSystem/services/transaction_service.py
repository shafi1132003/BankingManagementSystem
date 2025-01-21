from models.transaction import Transaction
from models import db

def create_transaction(amount, account_id, timestamp):
    new_transaction = Transaction(amount=amount, account_id=account_id, timestamp=timestamp)
    db.session.add(new_transaction)
    db.session.commit()
    return new_transaction