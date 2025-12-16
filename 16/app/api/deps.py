from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError, ExpiredSignatureError, decode as jwt_decode
from colorama import Fore
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.core.config import settings
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/login")

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user(
        db:Session = Depends(get_db), token:str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        payload = jwt_decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM], options={"veriry_exp":False}) # 
        email:str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except ExpiredSignatureError:
        print(f"{Fore.RED}[ERROR]{Fore.RESET} A assinatura expirou")
        raise credentials_exception
    except PyJWTError as e:
        print(f"{Fore.RED}[ERROR]{Fore.RESET} Um erro ocorreu: {Fore.LIGHTBLACK_EX}{e}{Fore.RESET}")
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first
    if user is None:
        raise credentials_exception
    return user