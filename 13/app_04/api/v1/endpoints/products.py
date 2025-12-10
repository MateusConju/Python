from fastapi import APIRouter
from app_04.schemas.product import ProductSchema
from app_04.schemas.response import ResponseEnvelope

router = APIRouter()

@router.get('/{id}', response_model=ResponseEnvelope[ProductSchema])
def get_product(id:int):
    product_data = ProductSchema(id=id, name=f'Product {id}', price=42.42)

    return ResponseEnvelope(data=product_data)