import requests

BASE_URL = "http://127.0.0.1:8000/livros/"

def criar_livro(livro):
    response = requests.post(BASE_URL, json=livro)
    print("Criar:", response.status_code, response.json())

def listar_livros():
    response = requests.get(BASE_URL)
    print("Listar:", response.status_code, response.json())

def buscar_livro(livro_id):
    response = requests.get(f"{BASE_URL}{livro_id}")
    print("Buscar:", response.status_code, response.json())

def atualizar_livro(livro_id, livro):
    response = requests.put(f"{BASE_URL}{livro_id}", json=livro)
    print("Atualizar:", response.status_code, response.json())

def deletar_livro(livro_id):
    response = requests.delete(f"{BASE_URL}{livro_id}")
    print("Deletar:", response.status_code, response.json())

if __name__ == "__main__":
    livro1 = {"id": 1, "titulo": "1984", "autor": "George Orwell", "ano": 1949}
    criar_livro(livro1)

    listar_livros()

    buscar_livro(1)

    livro_atualizado = {"id": 1, "titulo": "1984", "autor": "G. Orwell", "ano": 1949}
    atualizar_livro(1, livro_atualizado)

    deletar_livro(1)

    listar_livros()
