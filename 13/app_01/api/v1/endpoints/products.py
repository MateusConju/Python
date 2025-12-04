from fastapi import APIRouter, status, Response

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product():
    pass

@router.get("/{product_id}", status_code=status.HTTP_200_OK)
def get_product(product_id:int):
    return {'id':product_id, 'name':'Produto - Exemplo'}

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id:int):
    return Response(status_code=status.HTTP_204_NO_CONTENT)
