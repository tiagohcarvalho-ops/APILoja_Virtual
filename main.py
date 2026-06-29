
from fastapi import FastAPI

from database import Base, engine
from routes import router

# Cria a aplicação
app = FastAPI(
    title="API Loja Virtual",
    description="Projeto ADS - Loja Virtual",
    version="1.0"
)

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Adiciona todas as rotas
app.include_router(router)


@app.get("/")
def home():
    return {
        "mensagem": "API Loja Virtual funcionando!"
    }