from flask import Blueprint
from app.controllers import user_controller
from app.utils.auth import token_required
from flask_jwt_extended import jwt_required

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['POST'])
def register():
    return user_controller.register_user()

@user_bp.route('/users/me', methods=['GET'])
@jwt_required()
def get_profile():
    return user_controller.get_user_profile()

@user_bp.route('/users/me', methods=['PUT'])
@jwt_required()
def update_profile():
    return user_controller.update_user_profile()