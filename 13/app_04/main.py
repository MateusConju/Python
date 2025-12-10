from fastapi import FastAPI
from app_04.api.v1.endpoints.products import router as product_router

app = FastAPI()

app.include_router(product_router, prefix='/products')