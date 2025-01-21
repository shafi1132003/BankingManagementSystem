from flask import Blueprint, request, jsonify
from services.customer_service import create_customer

bp = Blueprint('customer', __name__, url_prefix='/customers')

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    customer = create_customer(data['name'])
    return jsonify(customer), 201