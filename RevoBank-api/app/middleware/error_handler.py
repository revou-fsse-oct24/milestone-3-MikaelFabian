# app/middleware/error_handler.py
from flask import jsonify
from werkzeug.exceptions import HTTPException

class APIError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code

def handle_error(error):
    if isinstance(error, APIError):
        return jsonify({
            'error': error.message,
            'status_code': error.status_code
        }), error.status_code
    
    if isinstance(error, HTTPException):
        return jsonify({
            'error': error.description,
            'status_code': error.code
        }), error.code
    
    # Unexpected errors
    return jsonify({
        'error': 'Internal Server Error',
        'status_code': 500
    }), 500