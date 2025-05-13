from flask import jsonify
from werkzeug.exceptions import HTTPException
import traceback

class CustomError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

def handle_error(error):
    if isinstance(error, HTTPException):
        return jsonify({
            'error': error.description,
            'status_code': error.code
        }), error.code
    
    if isinstance(error, CustomError):
        return jsonify({
            'error': error.message,
            'status_code': error.status_code
        }), error.status_code
    
    # Unexpected errors
    traceback.print_exc()
    return jsonify({
        'error': 'Internal Server Error',
        'message': str(error),
        'status_code': 500
    }), 500

def register_error_handlers(app):
    app.register_error_handler(Exception, handle_error)