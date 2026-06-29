
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

# Chave secreta
SECRET_KEY = "loja_virtual_ads_2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Criptografia da senha
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

# SENHAS

def hash_senha(senha: str):
    return pwd_context.hash(senha)


def verificar_senha(senha, senha_hash):
    return pwd_context.verify(senha, senha_hash)


# TOKEN JWT


def criar_token(dados: dict):

    dados_token = dados.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    dados_token.update(
        {"exp": expire}
    )

    token = jwt.encode(
        dados_token,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def verificar_token(token: str = Depends(oauth2_scheme)):

    credenciais_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credenciais_exception

        return email

    except JWTError:
        raise credenciais_exception