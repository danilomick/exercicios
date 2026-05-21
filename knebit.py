class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def exibir_produto(self, indice):
        print(f"\níndice: {indice}")
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
 
produtos = []
 
def cadastrar_produto():
    print("\n---CADASTRAR PRODUTO---")
    while True:
        nome = input("Digite o nome do produto: ")
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco <= 0:
                print("Erro! O produto não deve ter preço 0 ou negativo.")
                continue
            else:
                p = Produto(nome, preco)
                produtos.append(p)
                print(f"O produto {p.nome}, de preço {p.preco} foi cadastrado!")
                break
        except:
            print("Valor inválido!")
            continue
 
def listar_produtos():
    
    if len(produtos) == 0:
        print("\nNenhum produto cadastrado!")
    else:
        print("\n---LISTA DE PRODUTOS---")
        for i, p in enumerate(produtos):
            p.exibir_produto(i)
 
def comprar_produto():
    print("\n---MENU DE COMPRA---")
    listar_produtos()
    
    while True:
        
        if len(produtos) == 0:
            break

        try:
            num = int(input("\nDigite o número do produto: "))
            if num < 0:
                raise ValueError
        except:
            print("Erro! Valor inválido.")
            continue
        
        while True:
            try:
                qtd = int(input("Digite a quantidade desejada: "))
                if qtd <= 0:
                    print("A quantidade não pode ser 0!")
                    continue
                else:
                    break
            except:
                print("Erro! Valor inválido.")
                continue
        
        try:
            preco = produtos[num].preco
            total = preco * qtd
            print("O total é", total)
            break
        except:
            print("O produto não existe.")
            continue
 
 
 
 
def menu():
 
    while True:
        print("\n---MENU---")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Comprar Produto")
        print("4 - Sair")
    
        try:
            escolha = int(input("\nEscolha uma opção acima: ").strip())
            if escolha not in (1, 2, 3, 4):
                raise ValueError
            else:
                pass
        except ValueError:
            print("Valor inválido!")
            continue
 
        if escolha == 1:
            cadastrar_produto()
            continue
        elif escolha == 2:
            listar_produtos()
            continue
        elif escolha == 3:
            comprar_produto()
            continue
        else:
            print("Saindo...")
            break
 
menu()