from flask import Blueprint
from app.controllers import account_controller
from flask_jwt_extended import jwt_required, get_jwt_identity

account_bp = Blueprint('accounts', __name__)

@account_bp.route('/accounts', methods=['POST'])
@jwt_required()
def create_account():
    current_user_id = get_jwt_identity()
    return account_controller.create_account(current_user_id)

@account_bp.route('/accounts', methods=['GET'])
@jwt_required()
def get_accounts():
    current_user_id = get_jwt_identity()
    return account_controller.get_user_accounts(current_user_id)

@account_bp.route('/accounts/<account_id>', methods=['GET'])
@jwt_required()
def get_account(account_id):
    current_user_id = get_jwt_identity()
    return account_controller.get_account_details(current_user_id, account_id)

@account_bp.route('/accounts/<account_id>', methods=['PUT'])
@jwt_required()
def update_account(account_id):
    current_user_id = get_jwt_identity()
    return account_controller.update_account(current_user_id, account_id)

@account_bp.route('/accounts/<account_id>', methods=['DELETE'])
@jwt_required()
def delete_account(account_id):
    current_user_id = get_jwt_identity()
    return account_controller.delete_account(current_user_id, account_id)