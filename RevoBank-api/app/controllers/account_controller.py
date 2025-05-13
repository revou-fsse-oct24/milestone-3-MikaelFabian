from flask import request, jsonify, abort
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
        account_data = account_schema.load(request.json)
        user = User.query.get_or_404(current_user_id)
        account_data.user_id = current_user_id
        account_data.account_number = generate_account_number()
        account_data.balance = request.json.get('balance', 0.00)
        
        db.session.add(account_data)
        db.session.commit()
        
        return jsonify(account_schema.dump(account_data)), 201
    
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as ex:
        db.session.rollback()
        return jsonify({'error': str(ex)}), 500

def delete_account(current_user_id, account_id):
    account = Account.query.filter_by(id=account_id, user_id=current_user_id).first_or_404()
    try:
        db.session.delete(account)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Could not delete account', 'message': str(e)}), 500