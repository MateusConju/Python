from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME:str = "PycketMoney API"
    API_V1_STR:str = "/api/v1"
    SECRET_KEY:str = "chave_super_secreta" # Usar .env em produção
    ALGORITHM:str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 30
    SQLALCHEMY_DATABASE_URI:str = "sqlite:///./pycket_database.db"

    class Config:
        case_sentive = True

settings = Settings()