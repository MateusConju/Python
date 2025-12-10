from fastapi import FastAPI
from app_01.api.v1.endpoints.products import router as ProductRouter

app = FastAPI()

app.include_router(ProductRouter, prefix='/product')