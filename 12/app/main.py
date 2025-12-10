from fastapi import FastAPI, Depends, APIRouter
from app.api.auth import router as auth_router
from app.api.deps import get_current_user

app = FastAPI()

app.include_router(auth_router)
router = APIRouter()

@router.get(" /users/me")
async def read_users_me(user:str = Depends(get_current_user)):
    return {"usuario_logado":user, "mensagem":"Área restrita (AuthN OK)"}

#@router.post("/content")

app.include_router(router)