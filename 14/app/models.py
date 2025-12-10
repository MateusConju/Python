from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Item(Base):
    __tablename__ = "items"

    id:Column = Column(Integer, primary_key=True, index=True)
    name:Column = Column(String, index=True)
    description:Column = Column(String)