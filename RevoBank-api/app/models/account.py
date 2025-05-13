from app import db, ma
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.sql import func
import uuid
from marshmallow import fields

class Account(db.Model):
    __tablename__ = 'accounts'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    account_number = Column(String(20), unique=True, nullable=False)
    account_type = Column(String(50), nullable=False)  # e.g., 'savings', 'checking'
    balance = Column(Numeric(10, 2), default=0.00)
    currency = Column(String(3), default='USD')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    user = db.relationship('User', back_populates='accounts')
    transactions = relationship('Transaction', back_populates='account')

    def __repr__(self):
        return f'<Account {self.account_number}>'

class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account
        load_instance = True

    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    transactions = fields.List(fields.Nested('TransactionSchema', exclude=('account',)), dump_only=True)