# Loja API

## Descrição

Este projeto consiste em uma API desenvolvida com **FastAPI** para o gerenciamento de uma loja virtual.

A API permite o cadastro e gerenciamento de clientes, produtos e roupas, além de realizar autenticação utilizando **JWT (JSON Web Token)**.

---

## Tecnologias Utilizadas

* Python
* FastAPI
* SQLite
* SQLAlchemy
* JWT
* Uvicorn

---

## Funcionalidades

* Cadastro de clientes
* Login de clientes
* Autenticação com Token JWT
* Cadastro de produtos
* Cadastro de roupas
* Relacionamento entre produtos e roupas
* Consulta de registros
* Atualização de registros
* Exclusão de registros

---

## Estrutura do Projeto

```text
Loja_API/
│
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── routes.py
├── main.py
├── requirements.txt
└── loja.db
```

---

## Instalação

Clone o projeto ou faça o download dos arquivos.

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Executando a API

No terminal, execute:

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

---

## Documentação

O FastAPI gera automaticamente a documentação da API.

Swagger:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Endpoints

### Clientes

* POST /clientes
* GET /clientes
* GET /clientes/{id}
* PUT /clientes/{id}
* DELETE /clientes/{id}

### Login

* POST /login

### Produtos

* POST /produtos
* GET /produtos
* GET /produtos/{id}
* PUT /produtos/{id}
* DELETE /produtos/{id}

### Roupas

* POST /roupas
* GET /roupas
* GET /roupas/{id}
* PUT /roupas/{id}
* DELETE /roupas/{id}

---


