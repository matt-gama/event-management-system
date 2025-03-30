import os

from fastapi import HTTPException, Depends, status

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from passlib.context import CryptContext
from dotenv import load_dotenv



load_dotenv()

API_KEY = os.getenv('API_KEY', "myapikey")


# Cria um esquema para autenticação do tipo Bearer
auth_scheme = HTTPBearer()

# Define o contexto de criptografia
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Retorna a senha criptografada (hash).
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica se a senha enviada confere com o hash salvo.
    """
    return pwd_context.verify(plain_password, hashed_password)

# Função para validar o Bearer Token
def verify_bearer_token(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Credenciais de autenticação não fornecidas"
        )
    
    token = credentials.credentials  
    if token != API_KEY: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou não autorizado"
        )
    
    return token