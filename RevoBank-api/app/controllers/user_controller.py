from flask import request, jsonify
from app.models.user import User, UserSchema
from app.utils.auth import hash_password, check_password, generate_token
from app import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def register_user():
    try:
        # Validate input
        user_data = user_schema.load(request.json)
        
        # Check if user already exists
        existing_user = User.query.filter(
            (User.username == user_data.username) | 
            (User.email == user_data.email)
        ).first()
        
        if existing_user:
            return jsonify({
                'message': 'User already exists',
                'error': 'Duplicate user'
            }), 400
        
        # Hash password
        user_data.password = hash_password(user_data.password)
        
        # Save user
        db.session.add(user_data)
        db.session.commit()
        
        # Generate token
        token = generate_token(user_data)
        
        return jsonify({
            'user': user_schema.dump(user_data),
            'token': token
        }), 201
    
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            'message': 'Registration failed',
            'error': 'Database error'
        }), 500

def get_user_profile(current_user_id):
    user = User.query.get_or_404(current_user_id)
    return jsonify(user_schema.dump(user)), 200

def update_user_profile(current_user_id):
    user = User.query.get_or_404(current_user_id)
    
    try:
        # Partial update
        user_data = user_schema.load(
            request.json, 
            instance=user, 
            partial=True
        )
        
        # Update password if provided
        if 'password' in request.json:
            user_data.password = hash_password(request.json['password'])
        
        db.session.commit()
        
        return jsonify(user_schema.dump(user_data)), 200
    
    except ValidationError as err:
        return jsonify(err.messages), 400