from flask import Blueprint, request, jsonify
from services.account_service import create_account

bp = Blueprint('account', __name__, url_prefix='/accounts')

@bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    account = create_account(data['account_number'], data['balance'], data['customer_id'])
    return jsonify(account), 201