from datetime import datetime, timedelta, timezone
from typing import Any, Union
import jwt
from passlib.context import CryptContext

# Configuração simulada
SECRET_KEY = "segredo_super_secreto_da_nasa"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto de hashing
pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")


def create_access_token(subject: Union[str, Any], role: str) -> str:
    """
    TODO
    -----------------
    1. Criar 'exp'.
    2. Incluir 'sub' e 'role'.
    3. Gerar JWT assinado.
    """

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": subject,
        "role": role,
        "exp": expire
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    TODO
    -----------------
    Verifica senha usando Passlib.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    TODO
    -----------------
    Gera hash da senha.
    """
    return pwd_context.hash(password)
