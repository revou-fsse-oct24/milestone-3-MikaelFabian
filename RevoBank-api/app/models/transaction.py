from app import db, ma
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from marshmallow import fields
import enum

class TransactionType(enum.Enum):
    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'
    TRANSFER = 'transfer'

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    account_id = Column(String(36), ForeignKey('accounts.id'), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    description = Column(String(255))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    account = relationship('Account', back_populates='transactions')

    def __repr__(self):
        return f'<Transaction {self.id}>'

class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction
        load_instance = True

    id = fields.Str(dump_only=True)
    account_id = fields.Str(required=True)
    transaction_type = fields.Enum(TransactionType)
    timestamp = fields.DateTime(dump_only=True)