from flask import request, jsonify
from app.models.transaction import Transaction, TransactionSchema, TransactionType
from app.models.account import Account
from app import db
from app.utils.auth import token_required
from marshmallow import ValidationError
from sqlalchemy import or_

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)

def create_transaction(current_user_id):
    try:
        # Validate input
        transaction_data = transaction_schema.load(request.json)
        
        # Verify account belongs to user
        account = Account.query.filter_by(
            id=transaction_data.account_id, 
            user_id=current_user_id
        ).first_or_404()
        
        # Handle different transaction types
        if transaction_data.transaction_type == TransactionType.DEPOSIT:
            account.balance += transaction_data.amount
        elif transaction_data.transaction_type == TransactionType.WITHDRAWAL:
            if account.balance < transaction_data.amount:
                return jsonify({'error': 'Insufficient funds'}), 400
            account.balance -= transaction_data.amount
        
        # Save transaction
        db.session.add(transaction_data)
        db.session.commit()
        
        return jsonify(transaction_schema.dump(transaction_data)), 201
    
    except ValidationError as err:
        return jsonify(err.messages), 400

def get_user_transactions(current_user_id):
    # Get accounts for the user
    user_accounts = Account.query.filter_by(user_id=current_user_id).all()
    account_ids = [account.id for account in user_accounts]
    
    # Filter transactions
    query = Transaction.query.filter(Transaction.account_id.in_(account_ids))
    
    # Optional filtering
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    transaction_type = request.args.get('type')
    
    if start_date:
        query = query.filter(Transaction.timestamp >= start_date)
    if end_date:
        query = query.filter(Transaction.timestamp <= end_date)
    if transaction_type:
        query = query.filter(Transaction.transaction_type == transaction_type)
    
    transactions = query.all()
    return jsonify(transactions_schema.dump(transactions)), 200

def get_transaction_details(current_user_id, transaction_id):
    # Find transaction for user's accounts
    user_accounts = Account.query.filter_by(user_id=current_user_id).all()
    account_ids = [account.id for account in user_accounts]
    
    transaction = Transaction.query.filter(
        Transaction.id == transaction_id,
        Transaction.account_id.in_(account_ids)
    ).first_or_404()
    
    return jsonify(transaction_schema.dump(transaction)), 200