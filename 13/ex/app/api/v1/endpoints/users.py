from fastapi import APIRouter
from ex.app.schemas.response import PaginatedResponse

router = APIRouter()

@router.get('/{page_id}', response_model=PaginatedResponse)
def get_product(page_id:int):
    show_user_data = {'page':page_id, 'per_page':50, 'total':80}

    return PaginatedResponse(data=show_user_data)