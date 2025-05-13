from flask import Blueprint
from app.controllers import transaction_controller
from flask_jwt_extended import jwt_required

transaction_bp = Blueprint('transactions', __name__)

@transaction_bp.route('/transactions', methods=['POST'])
@jwt_required()
def create_transaction():
    return transaction_controller.create_transaction()

@transaction_bp.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    return transaction_controller.get_user_transactions()

@transaction_bp.route('/transactions/<transaction_id>', methods=['GET'])
@jwt_required()
def get_transaction(transaction_id):
    return transaction_controller.get_transaction_details(transaction_id)