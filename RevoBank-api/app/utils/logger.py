import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(app):
    # Ensure logs directory exists
    if not os.path.exists('logs'):
        os.mkdir('logs')
    
    # Configure file handler
    file_handler = RotatingFileHandler(
        'logs/revobank.log', 
        maxBytes=10240, 
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)

def log_transaction(user_id, action, details):
    logging.info(f"User {user_id}: {action} - {details}")