from fastapi import FastAPI
from app_01.api.v1.endpoints.products import router as ProductTouter

app = FastAPI()

app.include_router(ProductTouter, prefix='/product')

# Dada a lista de endpoints:
# POST /updateUser
# GET /deleteOrder?id=5
# GET /addUser?name=john&surname=doe
# POST /returnUser/{uid}

# Escreva uma versão RESTful correta (Verbo + URL + Status Sucesso + Status Erro)
