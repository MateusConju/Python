from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import async_engine, Base, get_session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryResponse

@asynccontextmanager
async def lifespan(app:FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="ShopFlow - API",
    lifespan=lifespan
)

@app.post(
    "/categories",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED)
async def create_category(
    category_data:CategoryCreate,
    db:AsyncSession = Depends(get_session)
):
    new_category = Category(**category_data.model_dump())
    db.add(new_category)
    await db.flush()
    await db.refresh(new_category)

    return new_category

@app.get(
    "/categories",
    response_model=List[CategoryResponse]
)
async def list_categories(db:AsyncSession = Depends(get_session)):
    #return (await db.execute(select(Category).order_by(Category.id))).scalars().all()
    query = select(Category).order_by(Category.id)
    result = await db.execute(query)
    categories = result.scalars().all()
    return categories