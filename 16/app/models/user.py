from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)   
    hashed_password = Column(String, nullable=False)

    transactions = relationship("Transaction", back_populates="owner")
    categories = relationship("Category", back_populates="owner")
