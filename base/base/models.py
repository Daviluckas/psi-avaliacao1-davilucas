class Produto:
    def __init__(self, id, nome, preco, categoria, unidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.unidade = unidade


usuarios = [
    {"id": 1, "nome": "admin", "senha": "1234"}
]

produtos = [
    Produto(1, "Banana", 5.50, "Fruta", "kg"),
    Produto(2, "Maçã", 7.90, "Fruta", "kg"),
    Produto(3, "Alface", 2.80, "Verdura", "un"),
    Produto(4, "Cenoura", 3.40, "Legume", "kg"),
    Produto(5, "Tomate", 6.20, "Legume", "kg")
]


def buscar_produto(produto_id):
    for p in produtos:
        if p.id == produto_id:
            return p
    return None


def buscar_por_categoria(categoria):
    return [p for p in produtos if p.categoria == categoria]


def buscar_por_nome(nome):
    return [p for p in produtos if nome in p.nome]
