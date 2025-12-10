from fastapi import FastAPI
from ex.app.api.v1.endpoints.users import router as users_router

app = FastAPI()

app.include_router(users_router, prefix='/users')