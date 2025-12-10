from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "minha_secret_key" # Em prod, use .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    encodar = data.copy() # Copiando os dados
    data_expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # Setando a data de expiração
    encodar.update({"exp":data_expiracao})
    encoded_jwt = jwt.encode(encodar, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def decode_acess_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        print('Erro: Token expirado!')
        return None
    except jwt.InvalidTokenError:
        print('Erro: Token inválido!')
        return None


contexto_senha = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_password(password:str) -> str:
    return contexto_senha.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return contexto_senha.verify(plain_password, hashed_password)

if __name__ == '__main__':
    '''
    print('Testing...')
    print('[!] Warning: This should not be used on production!')
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RlIiwicGFzc3dvcmQiOiJ0ZXN0ZSIsImV4cCI6MTc2NDU5NTg5N30.M1VFluLbJXGu45W7yjFODa5RW4BZyQefnVTUx5v6ec0'
    payload = decode_acess_token(token)
    print(payload)
    
    username = input('Digite o usuário:\n> ')
    password = input('Digite a senha:\n> ')
    payload = {'username': username, 'password':password}
    token = create_access_token(payload)
    print(token)
    '''
    '''
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RlIiwicGFzc3dvcmQiOiJ0ZXN0ZSIsImV4cCI6MTc2NDU5NTg5N30.M1VFluLbJXGu45W7yjFODa5RW4BZyQefnVTUx5v6ec0
    
    SENHA_ADMIN = '123456@admin'

    senha = input('Digite sua senha:\n> ')

    hashed_one = get_password(senha)
    hashed_two = get_password(senha)

    print(f'Senha: {hashed_one} ({verify_password(SENHA_ADMIN, hashed_one)})')
    print(f'Senha: {hashed_two} ({verify_password(SENHA_ADMIN,hashed_two)})')
    '''
    senha_plain = input('Digite uma senha:\n> ')
    senha_hashed = get_password(senha_plain)

    print(senha_hashed)