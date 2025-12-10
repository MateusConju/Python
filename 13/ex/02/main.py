from fastapi import FastAPI, APIRouter, status
from fastapi.exceptions import RequestValidationError
from ex.app.core.handlers import validation_exception_handler
from ex.app.schemas.item import ItemSchema

app = FastAPI()

# Handler Global
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Rota de teste
router = APIRouter()

@router.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemSchema):
    return item

app.include_router(router, prefix="/api/test")