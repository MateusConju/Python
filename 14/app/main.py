from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from app.auth import get_current_user
from app.core.errors import StatusCodeNotFound

app = FastAPI()

from app.core.handlers import resource_not_found_handler, status_not_found_handler
app.add_exception_handler(404, resource_not_found_handler)
app.add_exception_handler(StatusCodeNotFound, status_not_found_handler)

@app.get('/')
def home():
    return {"status":200,"msg":"O app está funcionando!"}

@app.get('/health')
def health():
    return {"status":"ok"}

@app.get('/users/me')
def read_users_me(user:dict = Depends(get_current_user)):
    return user

@app.get('/test/{http_code}')
def test_error(http_code:int):
    http_codes = {200:status.HTTP_200_OK, 404:status.HTTP_404_NOT_FOUND, 401:status.HTTP_401_UNAUTHORIZED, 502:status.HTTP_502_BAD_GATEWAY}
    try: meu_status = http_codes[http_code]
    except KeyError: raise StatusCodeNotFound(detail=f'Não foi cadastrado o status_code \'{http_code}\'!')
    return JSONResponse(
        status_code=meu_status,
        content={'status':meu_status, 'msg':'ok'})
