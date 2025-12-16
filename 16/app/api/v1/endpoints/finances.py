from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from datetime import datetime
from app.api import deps
from app.models.finance import Transaction, Category, TransactionType
from app.models.user import User
from app.schemas.finance import TransactionCreate, TransactionOut, CategoryOut, CategoryCreate, DashboardStats

router = APIRouter()

@router.post("/categories/", response_model=CategoryOut)
def create_category(
    cat_in:CategoryCreate,
    db:Session = Depends(deps.get_db),
    current_user:User = Depends(deps.get_current_user)
):
    category = Category(**cat_in.model.dump(), user_id=current_user.id)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

@router.post("/transactions/", response_model=TransactionOut)
def create_transaction(
    trans_in:TransactionCreate,
    db:Session = Depends(deps.get_db),
    current_user:User = Depends(deps.get_current_user)
):
    cat = db.query(Category).filter(Category.id == trans_in.category_id, Category.user_id == current_user.id).first()
    if not cat:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada!"
        )
    transaction = Transaction(**trans_in.model_dump(), user_id=current_user.id)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

@router.get("/dashboard/", response_model=DashboardStats)
def get_dashboard(
    month:int = datetime.now().month,
    year:int = datetime.now().year,
    db:Session = Depends(deps.get_db),
    current_user:User = Depends(deps.get_current_user)
):
    base_query = db.query(Transaction).filter(
        Transaction.user_id == current_user.id,
        func.extract('month', Transaction.date) == month,
        func.extract('year', Transaction.date) == year
    )

    income_total = base_query.filter(Transaction.type == TransactionType.INCOME).with_entities(func.sum(Transaction.amount)).scalar() or 0.0
    expense_total = base_query.filter(Transaction.type == TransactionType.EXPENSE).with_entities(func.sum(Transaction.amount)).scalar() or 0.0

    # Enviar a versão em sql no documento de apoio
    expenses_by_cat = (
        db.query(Category.name, func.sum(Transaction.amount).label("total"))
        .join(Category)
        .filter(
            Transaction.user_id == current_user.id,
            Transaction.type == TransactionType.EXPENSE,
            func.extract('month', Transaction.date) == month,
            func.extract('year', Transaction.date) == year
        )
        .group_by(Category.name)
        .all()
    )

    return {
        "balanço_total": income_total - expense_total,
        "ganhos_totais": income_total,
        "despesas_totais": expense_total,
        "despesas_por_categoria": [{"category":name, "amount": total} for name, total in expenses_by_cat]
    }