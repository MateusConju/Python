from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.core.database import Base

class Category(Base):
    __tablename__ = 'categories'

    id:Mapped[int] = mapped_column(primary_key=True, init=False)
    name:Mapped[str] = mapped_column(String(50), unique=True, index=True)
    slug:Mapped[str] = mapped_column(String(50), unique=True)