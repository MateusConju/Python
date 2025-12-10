from fastapi import FastAPI
from app_02.api.v1.router import api_router as v1_api_router
from app_02.api.v2.router import api_router as v2_api_router

app = FastAPI()

app.include_router(v1_api_router, prefix='/v1')

app.include_router(v2_api_router, prefix='/v2')

