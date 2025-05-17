from sqlalchemy import Table, Column, Integer, String
from database import metadata
from pydantic import BaseModel, validator

livros = Table(
    "livros",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("titulo", String, index=True),
    Column("autor", String, index=True),
    Column("ano", Integer),
    extend_existing=True
)

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