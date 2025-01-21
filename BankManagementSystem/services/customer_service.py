from models.customer import Customer
from models import db

def create_customer(name):
    new_customer = Customer(name=name)
    db.session.add(new_customer)
    db.session.commit()
    return new_customer