from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token, get_password

mock_db = {
    "alberto":{
        "username":"alberto",
        "hashed_password": get_password('bertinho@1999'),
        "role":"editor"
        },
    "betina":{
        "username":"betina",
        "hashed_password": get_password('superadmin'),
        "role":"admin"
        },
    "carlos":{
        "username":"carlos",
        "hashed_password": get_password('minhasenha123'),
        "role":"user"
        }
}

router = APIRouter()

@router.post('/token')
async def login_access_token(form_data:OAuth2PasswordRequestForm = Depends()):
    user = mock_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user['hashed_password']):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = 'Usuário ou senha incorretos!',
            headers={'WWW-Authenticate':'Bearer'}
        )
    
    role = user.get("role","user")
    access_token = create_access_token(data={"sub":user['username'], "role":role})
    return {'access_token':access_token, 'token_type':'bearer'}