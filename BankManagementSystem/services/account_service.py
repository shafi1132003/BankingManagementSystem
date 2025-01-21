from models.account import Account
from models import db

def create_account(account_number, balance, customer_id):
    new_account = Account(account_number=account_number, balance=balance, customer_id=customer_id)
    db.session.add(new_account)
    db.session.commit()
    return new_account