import os
from datetime import timedelta

class Config:
    # Security Configurations
    SECRET_KEY = os.environ.get('SECRET_KEY', 'development_secret')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', SECRET_KEY)
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 
        'postgresql://username:password@localhost/revobank'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API Configurations
    API_VERSION = 'v1'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max payload
    
    # Security Limits
    MAX_LOGIN_ATTEMPTS = 5
    TRANSACTION_LIMIT = 10000.00

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Additional production-specific settings

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class AdvancedConfig:
    # Security Settings
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_SALT')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
    
    # Transaction Limits
    MAX_DAILY_TRANSACTION_AMOUNT = 10000
    MAX_SINGLE_TRANSACTION_AMOUNT = 5000
    
    # Feature Flags
    ENABLE_2FA = True
    ENABLE_TRANSACTION_VERIFICATION = True

# Implement feature flags
def is_feature_enabled(feature_name):
    return getattr(AdvancedConfig, feature_name, False)