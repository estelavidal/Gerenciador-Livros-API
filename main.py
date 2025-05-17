from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from typing import List

from database import database, engine, metadata
from models import livros

app = FastAPI()

metadata.create_all(engine)

class Livro(BaseModel):
    id: int | None = None
    titulo: str
    autor: str
    ano: int

    @validator('titulo')
    def titulo_nao_vazio(cls, v):
        if not v.strip():
            raise ValueError('O título não pode estar vazio')
        return v

    @validator('ano')
    def ano_valido(cls, v):
        if v < 0:
            raise ValueError('O ano deve ser positivo')
        return v

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/livros/", response_model=Livro)
async def criar_livro(livro: Livro):
    query_verificacao = livros.select().where(
        (livros.c.titulo.ilike(livro.titulo)) &
        (livros.c.autor.ilike(livro.autor))
    )
    resultado = await database.fetch_one(query_verificacao)

    if resultado:
        raise HTTPException(status_code=400, detail="Livro já cadastrado.")

    query = livros.insert().values(titulo=livro.titulo, autor=livro.autor, ano=livro.ano)
    last_record_id = await database.execute(query)
    return {**livro.dict(), "id": last_record_id}

@app.get("/livros/", response_model=List[Livro])
async def listar_livros():
    query = livros.select()
    resultados = await database.fetch_all(query)
    return [Livro(**livro) for livro in resultados]

@app.get("/livros/{livro_id}", response_model=Livro)
async def buscar_livro(livro_id: int):
    query = livros.select().where(livros.c.id == livro_id)
    livro = await database.fetch_one(query)
    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return Livro(**livro)

@app.put("/livros/{livro_id}", response_model=Livro)
async def atualizar_livro(livro_id: int, livro: Livro):
    # Checar duplicidade diferente do livro atual
    query_duplicado = livros.select().where(
        (livros.c.titulo.ilike(livro.titulo)) &
        (livros.c.autor.ilike(livro.autor)) &
        (livros.c.id != livro_id)
    )
    existe_duplicado = await database.fetch_one(query_duplicado)
    if existe_duplicado:
        raise HTTPException(status_code=400, detail="Já existe outro livro com mesmo título e autor.")

    query = livros.update().where(livros.c.id == livro_id).values(
        titulo=livro.titulo, autor=livro.autor, ano=livro.ano
    )
    await database.execute(query)
    return {**livro.dict(), "id": livro_id}

@app.delete("/livros/{livro_id}")
async def deletar_livro(livro_id: int):
    query = livros.delete().where(livros.c.id == livro_id)
    await database.execute(query)
    return {"detail": "Livro deletado"}