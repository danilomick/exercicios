#ex 25, 26 e 27 juntos

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        
p1 = Produto("Celular", 1000)
p1.mostrar()