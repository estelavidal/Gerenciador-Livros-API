from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

DATABASE_URL = "sqlite:///./livros.db"

database = Database(DATABASE_URL)
metadata = MetaData()

livros = Table(
    "livros",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("titulo", String),
    Column("autor", String),
    Column("ano", Integer),
)

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
