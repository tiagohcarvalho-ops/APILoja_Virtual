
from pydantic import BaseModel



class ClienteCreate(BaseModel):
    nome: str
    email: str
    senha: str


class ClienteUpdate(BaseModel):
    nome: str
    email: str
    senha: str


class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True


class Login(BaseModel):
    email: str
    senha: str


class ProdutoCreate(BaseModel):
    nome: str
    preco: float


class ProdutoUpdate(BaseModel):
    nome: str
    preco: float


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float

    class Config:
        from_attributes = True


class RoupaCreate(BaseModel):
    tipo: str
    tamanho: str
    cor: str
    produto_id: int


class RoupaUpdate(BaseModel):
    tipo: str
    tamanho: str
    cor: str
    produto_id: int


class RoupaResponse(BaseModel):
    id: int
    tipo: str
    tamanho: str
    cor: str
    produto_id: int

    class Config:
        from_attributes = True