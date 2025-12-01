from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncAttrs
)
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

DATABASE_URL = "sqlite+aiosqlite:///./shopflow.db"

async_engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

class Base(AsyncAttrs, DeclarativeBase, MappedAsDataclass):
    pass

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    autoflush=False
)

@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = AsyncSessionLocal()

    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
