class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
P1 = Produto("borracha", 5, 3 )       
P2 = Produto("Caneta", 6.5, 8)


valortotal = P1.preco * P1.quantidade + P2.preco * P2.quantidade
print(valortotal)