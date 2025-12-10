from fastapi import APIRouter
from fastapi.responses import JSONResponse

user_router = APIRouter()

@user_router.get('/{uid}')
def get_user(uid:int):
    data = {'user-id':uid, 'version':'v1'}
    return JSONResponse(data)