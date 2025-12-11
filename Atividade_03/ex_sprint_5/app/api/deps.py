from typing import Generator, Annotated
from fastapi import Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer
import jwt
from app.core import security
from app.db.session import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- Token Validation ---
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    TODO
    1. Decodificar o token com PyJWT.
    2. Validar expiração e assinatura.
    3. Retornar um dicionário com sub e role.
    """

    try:
        payload = jwt.decode(
            token,
            security.settings.SECRET_KEY,
            algorithms=[security.settings.ALGORITHM],
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    username = payload.get("sub")
    role = payload.get("role")

    if username is None or role is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido: dados incompletos.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"username": username, "role": role}

class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: Annotated[dict, Depends(get_current_user)]):
        """
        TODO
        1. Verificar se user['role'] está permitido.
        2. Senão → 403 Forbidden.
        """

        if user["role"] not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Acesso negado: role não autorizada.",
            )
        
        return True
    
idempotency_store = {}

def check_idempotency(idempotency_key: str = Header(None)):
    """
    TODO
    1. Se chave ausente → permitir.
    2. Se já existir → lançar 409 Conflict.
    """

    if idempotency_key is None:
        return

    if idempotency_key in idempotency_store:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Chave de idempotência já utilizada.",
        )

    idempotency_store[idempotency_key] = True
