from flask import Blueprint, request, jsonify
from services.transaction_service import create_transaction

bp = Blueprint('transaction', __name__, url_prefix='/transactions')

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    transaction = create_transaction(data['amount'], data['account_id'], data['timestamp'])
    return jsonify(transaction), 201