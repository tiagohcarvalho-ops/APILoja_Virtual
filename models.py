
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

    roupas = relationship(
        "Roupa",
        back_populates="produto",
        cascade="all, delete"
    )


class Roupa(Base):
    __tablename__ = "roupas"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    tamanho = Column(String, nullable=False)
    cor = Column(String, nullable=False)

    produto_id = Column(
        Integer,
        ForeignKey("produtos.id")
    )

    produto = relationship(
        "Produto",
        back_populates="roupas"
    )