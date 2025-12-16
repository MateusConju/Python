from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base
import enum

class TransactionType(str, enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"

class Category(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="categories")
    transactions = relationship("Transaction", back_populates="category")

class Transaction(Base):
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    descrition = Column(String)
    date = Column(DateTime(timezone=True), server_default=func.now())
    type = Column(String, nullable=False) # >> TransactionType[income, expense]

    category_id = Column(Integer, ForeignKey("category.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    category = relationship("Category", back_populates="transactions")
    owner = relationship("User", back_populates="transactions")
