from fastapi import APIRouter
from .endpoints.users import user_router

# Declarando o Router
api_router = APIRouter()

# Definido o Router filho
api_router.include_router(user_router, prefix='/users')
