# API de Gerenciamento de Livros

Uma API REST feita com **FastAPI** e **SQLite** para cadastro, consulta, atualização e remoção de livros.

---

## Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

4. Acesse a documentação interativa:
   - Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoints principais

### POST `/livros/`
Cria um novo livro.

**Exemplo de JSON:**
```json
{
  "titulo": "1984",
  "autor": "George Orwell",
  "ano": 1949
}
```

### GET `/livros/`
Lista todos os livros.

### GET `/livros/{id}`
Busca um livro por ID.

### PUT `/livros/{id}`
Atualiza os dados de um livro.

### DELETE `/livros/{id}`
Remove um livro pelo ID.

---

## Validações aplicadas

- `titulo`: não pode estar vazio
- `ano`: deve ser um número positivo
- Duplicidade de título e autor não é permitida

---

## Testes rápidos

Execute o script de testes automáticos com:

```bash
python test_api.py
```

---

## Requisitos (requirements.txt)

```txt
fastapi
uvicorn
databases[sqlite]
sqlalchemy
pydantic
requests
```

---

Este projeto foi desenvolvido como exemplo de uma API RESTful com FastAPI e SQLite.
