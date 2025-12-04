from fatAPI import APIRouter
from .endpoints.users import user_router

api_router = APIRouter()
api_router.include_router(user_router, prefix='/users')