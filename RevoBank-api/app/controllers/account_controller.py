from flask import request, jsonify
from app.models.account import Account, AccountSchema
from app.models.user import User
from app import db
from app.utils.auth import token_required
from marshmallow import ValidationError
import random
import string

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)

def generate_account_number():
    """Generate a unique account number"""
    while True:
        account_number = ''.join(random.choices(string.digits, k=12))
        existing = Account.query.filter_by(account_number=account_number).first()
        if not existing:
            return account_number

def create_account(current_user_id):
    try:
        # Validate input
        account_data = account_schema.load(request.json)
        
        # Verify user exists
        user = User.query.get_or_404(current_user_id)
        
        # Set user_id and generate account number
        account_data.user_id = current_user_id
        account_data.account_number = generate_account_number()
        
        # Set default balance if not provided
        account_data.balance = request.json.get('balance', 0.00)
        
        # Save account
        db.session.add(account_data)
        db.session.commit()
        
        return jsonify(account_schema.dump(account_data)), 201
    
    except ValidationError as err:
        return jsonify(err.messages), 400

def get_user_accounts(current_user_id):
    accounts = Account.query.filter_by(user_id=current_user_id).all()
    return jsonify(accounts_schema.dump(accounts)), 200

def get_account_details(current_user_id, account_id):
    account = Account.query.filter_by(id=account_id, user_id=current_user_id).first_or_404()
    return jsonify(account_schema.dump(account)), 200

def update_account(current_user_id, account_id):
    account = Account.query.filter_by(id=account_id, user_id=current_user_id).first_or_404()
    
    try:
        # Partial update
        account_data = account_schema.load(
            request.json, 
            instance=account, 
            partial=True
        )
        
        db.session.commit()
        
        return jsonify(account_schema.dump(account_data)), 200
    
    except ValidationError as err:
        return jsonify(err.messages), 400

def delete_account(current_user_id, account_id):
    account = Account.query.filter_by(id=account_id, user_id=current_user_id).first_or_404()
    
    try:
        db.session.delete(account)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Could not delete account'}), 500