
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import auth
import models
import schemas

from database import get_db

router = APIRouter()

# =====================================================
# LOGIN
# =====================================================

@router.post("/login")
def login(login: schemas.Login, db: Session = Depends(get_db)):

    cliente = db.query(models.Cliente).filter(
        models.Cliente.email == login.email
    ).first()

    if cliente is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos."
        )

    if not auth.verificar_senha(
        login.senha,
        cliente.senha
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos."
        )

    token = auth.criar_token(
        {
            "sub": cliente.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# =====================================================
# CLIENTES
# =====================================================

@router.post("/clientes")
def cadastrar_cliente(
    cliente: schemas.ClienteCreate,
    db: Session = Depends(get_db)
):

    existe = db.query(models.Cliente).filter(
        models.Cliente.email == cliente.email
    ).first()

    if existe:
        raise HTTPException(
            status_code=400,
            detail="Este email já está cadastrado."
        )

    novo_cliente = models.Cliente(
        nome=cliente.nome,
        email=cliente.email,
        senha=auth.hash_senha(cliente.senha)
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return {
        "mensagem": "Cliente cadastrado com sucesso!",
        "cliente": novo_cliente
    }


@router.get("/clientes")
def listar_clientes(db: Session = Depends(get_db)):

    clientes = db.query(models.Cliente).all()

    return clientes


@router.get("/clientes/{cliente_id}")
def buscar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):

    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    return cliente


@router.put("/clientes/{cliente_id}")
def atualizar_cliente(
    cliente_id: int,
    dados: schemas.ClienteUpdate,
    db: Session = Depends(get_db)
):

    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    cliente.nome = dados.nome
    cliente.email = dados.email
    cliente.senha = auth.hash_senha(dados.senha)

    db.commit()
    db.refresh(cliente)

    return {
        "mensagem": "Cliente atualizado com sucesso!",
        "cliente": cliente
    }


@router.delete("/clientes/{cliente_id}")
def excluir_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):

    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id
    ).first()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    db.delete(cliente)
    db.commit()

    return {
        "mensagem": "Cliente excluído com sucesso!"
    }


@router.post("/produtos")
def cadastrar_produto(
    produto: schemas.ProdutoCreate,
    db: Session = Depends(get_db)
):

    novo_produto = models.Produto(
        nome=produto.nome,
        preco=produto.preco
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return {
        "mensagem": "Produto cadastrado com sucesso!",
        "produto": novo_produto
    }


@router.get("/produtos")
def listar_produtos(
    db: Session = Depends(get_db)
):

    produtos = db.query(models.Produto).all()

    return produtos


@router.get("/produtos/{produto_id}")
def buscar_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):

    produto = db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    return produto


@router.put("/produtos/{produto_id}")
def atualizar_produto(
    produto_id: int,
    dados: schemas.ProdutoUpdate,
    db: Session = Depends(get_db)
):

    produto = db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    produto.nome = dados.nome
    produto.preco = dados.preco

    db.commit()
    db.refresh(produto)

    return {
        "mensagem": "Produto atualizado com sucesso!",
        "produto": produto
    }


@router.delete("/produtos/{produto_id}")
def excluir_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):

    produto = db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    db.delete(produto)
    db.commit()

    return {
        "mensagem": "Produto excluído com sucesso!"
    }


@router.post("/roupas")
def cadastrar_roupa(
    roupa: schemas.RoupaCreate,
    db: Session = Depends(get_db)
):

    # Verifica se o produto existe
    produto = db.query(models.Produto).filter(
        models.Produto.id == roupa.produto_id
    ).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado."
        )

    nova_roupa = models.Roupa(
        tipo=roupa.tipo,
        tamanho=roupa.tamanho,
        cor=roupa.cor,
        produto_id=roupa.produto_id
    )

    db.add(nova_roupa)
    db.commit()
    db.refresh(nova_roupa)

    return {
        "mensagem": "Roupa cadastrada com sucesso!",
        "roupa": nova_roupa
    }


@router.get("/roupas")
def listar_roupas(
    db: Session = Depends(get_db)
):

    roupas = db.query(models.Roupa).all()

    return roupas


@router.get("/roupas/{roupa_id}")
def buscar_roupa(
    roupa_id: int,
    db: Session = Depends(get_db)
):

    roupa = db.query(models.Roupa).filter(
        models.Roupa.id == roupa_id
    ).first()

    if roupa is None:
        raise HTTPException(
            status_code=404,
            detail="Roupa não encontrada."
        )

    return roupa


@router.put("/roupas/{roupa_id}")
def atualizar_roupa(
    roupa_id: int,
    dados: schemas.RoupaUpdate,
    db: Session = Depends(get_db)
):

    roupa = db.query(models.Roupa).filter(
        models.Roupa.id == roupa_id
    ).first()

    if roupa is None:
        raise HTTPException(
            status_code=404,
            detail="Roupa não encontrada."
        )

    produto = db.query(models.Produto).filter(
        models.Produto.id == dados.produto_id
    ).first()

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto informado não existe."
        )

    roupa.tipo = dados.tipo
    roupa.tamanho = dados.tamanho
    roupa.cor = dados.cor
    roupa.produto_id = dados.produto_id

    db.commit()
    db.refresh(roupa)

    return {
        "mensagem": "Roupa atualizada com sucesso!",
        "roupa": roupa
    }


@router.delete("/roupas/{roupa_id}")
def excluir_roupa(
    roupa_id: int,
    db: Session = Depends(get_db)
):

    roupa = db.query(models.Roupa).filter(
        models.Roupa.id == roupa_id
    ).first()

    if roupa is None:
        raise HTTPException(
            status_code=404,
            detail="Roupa não encontrada."
        )

    db.delete(roupa)
    db.commit()

    return {
        "mensagem": "Roupa excluída com sucesso!"
    }

