from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api import deps
from app.core import security
# Suponha que temos um Fake DB para simplificar o login no exercício base
from app.db.session import FAKE_USERS_DB 

router = APIRouter()

@router.post("/token")
def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = FAKE_USERS_DB.get(form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário ou senha incorretos."
        )

    if not security.verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário ou senha incorretos."
        )

    token = security.create_access_token(
        {"sub": user["username"], "role": user["role"]}
    )

    return {"access_token": token, "token_type": "bearer"}
    """
    TODO
    ----
    Implementar o fluxo de login (Password Flow).
    1. Buscar usuário no FAKE_USERS_DB pelo username.
    2. Validar senha com security.verify_password.
    3. Gerar token com security.create_access_token (incluindo a role).
    4. Retornar {"access_token": token, "token_type": "bearer"}.
    """
    pass

