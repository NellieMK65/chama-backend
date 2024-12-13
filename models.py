from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, Integer, VARCHAR, DateTime, ForeignKey
from datetime import datetime

# create a base model
Base = declarative_base()

# create our model
"""
1. We must provide the table name via the __tablename__ attribute
2. It must have at least one column defined
"""
class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    email = Column(VARCHAR(), nullable=True, unique=True)
    phone = Column(VARCHAR(), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

class Saving(Base):
    __tablename__ = "savings"

    id = Column(Integer(), primary_key=True)
    amount = Column(Integer(), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'))
    created_at = Column(DateTime(), default=datetime.now())
