from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

class TransatictionTypeEnum(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class CategoryCreate(BaseModel):
    name:str

class CategoryOut(CategoryCreate):
    id:int
    class Config:
        from_attributes = True

class TransactionCreate(BaseModel):
    amount:float = Field(..., gt=0, description="O valor deve ser positivo")
    description:Optional[str] = None
    date:datetime = Field(default_factory=datetime.now)
    type:TransatictionTypeEnum
    category_id:int

class TransactionOut(TransactionCreate):
    id:int
    class Config:
        from_attributes = True

class DashboardStats(BaseModel):
    total_balance:float
    total_income:float
    total_expense:float
    expense_by_category:list[dict]
