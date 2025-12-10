from fastapi import APIRouter, status, Response

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product():
    # >Lógica de criação de produto<
    pass

@router.get('/{product_id}', status_code=status.HTTP_200_OK)
def get_product(product_id:int):
    # >Lógica de busca de produto<
    return {'id':product_id, 'name':'Produto - Exemplo'}

@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id:int):
    # Lógica de Delete
    return Response(status_code=status.HTTP_204_NO_CONTENT)